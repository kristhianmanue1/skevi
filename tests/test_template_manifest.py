"""Tests del gate de MANIFEST de plantillas en check_sizes (#28 D1 + T09).

Runner: `python3 -m unittest`.
"""

from __future__ import annotations

import hashlib
import importlib.util
import io
import json
import re
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

SCRIPTS_DIR = Path(__file__).resolve().parent.parent / "scripts"
_SPEC = importlib.util.spec_from_file_location(
    "check_sizes_manifest_gate", SCRIPTS_DIR / "check_sizes.py"
)
check_sizes = importlib.util.module_from_spec(_SPEC)
sys.modules["check_sizes_manifest_gate"] = check_sizes
_SPEC.loader.exec_module(check_sizes)


def digest_of(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


class TemplateManifestGateTests(unittest.TestCase):
    """Unidad: check_template_manifest() sobre un directorio de plantillas."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.dir = Path(self.tmp.name) / "skevi"
        self.dir.mkdir(parents=True)
        self.manifest_path = self.dir / "MANIFEST.json"
        (self.dir / "usage-guide.md").write_text("guía\n", encoding="utf-8")
        (self.dir / "architecture-overview.md").write_text(
            "arquitectura\n", encoding="utf-8"
        )

    def _manifest(self, **overrides) -> dict:
        data = {
            "schema": check_sizes.TEMPLATE_MANIFEST_SCHEMA,
            "version": "plantillas/v1",
            "generated_at": "2026-09-08T00:00:00Z",
            "files": {
                name: digest_of(self.dir / name)
                for name in ("usage-guide.md", "architecture-overview.md")
            },
            "history": [],
        }
        data.update(overrides)
        self.manifest_path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        return data

    def _failures(self):
        return check_sizes.check_template_manifest(self.manifest_path, self.dir)

    def test_valid_manifest_passes(self):
        self._manifest()
        self.assertEqual(self._failures(), [])

    def test_tampered_template_without_bump_fails(self):
        self._manifest()
        (self.dir / "usage-guide.md").write_text(
            "cambió sin bump\n", encoding="utf-8"
        )
        failures = self._failures()
        self.assertEqual(len(failures), 1)
        self.assertIn("digest desactualizado", failures[0])
        self.assertIn("usage-guide.md", failures[0])

    def test_unlisted_file_fails(self):
        self._manifest()
        (self.dir / "installed.json").write_text("{}\n", encoding="utf-8")
        failures = self._failures()
        self.assertTrue(any("sin entrada en el manifiesto" in f for f in failures))

    def test_entry_without_real_file_fails(self):
        self._manifest()
        data = json.loads(self.manifest_path.read_text(encoding="utf-8"))
        data["files"]["fantasma.md"] = "sha256:" + "a" * 64
        self.manifest_path.write_text(json.dumps(data), encoding="utf-8")
        failures = self._failures()
        self.assertTrue(any("sin archivo real" in f for f in failures))

    def test_manifest_listing_itself_fails(self):
        self._manifest()
        data = json.loads(self.manifest_path.read_text(encoding="utf-8"))
        data["files"]["MANIFEST.json"] = "sha256:" + "a" * 64
        self.manifest_path.write_text(json.dumps(data), encoding="utf-8")
        failures = self._failures()
        self.assertTrue(any("sin archivo real" in f for f in failures))

    def test_invalid_json_fails_sanitized(self):
        self.manifest_path.write_text("{", encoding="utf-8")
        failures = self._failures()
        self.assertEqual(len(failures), 1)
        self.assertIn("JSON inválido", failures[0])
        self.assertNotIn("Traceback", str(failures))

    def test_unknown_top_level_field_fails(self):
        self._manifest(extra=1)
        failures = self._failures()
        self.assertTrue(any("campo desconocido" in f for f in failures))

    def test_unknown_schema_fails(self):
        self._manifest(schema="skevi/template-manifest/v2")
        failures = self._failures()
        self.assertTrue(any("schema" in f for f in failures))

    def test_bad_version_format_fails(self):
        self._manifest(version="v1")
        failures = self._failures()
        self.assertTrue(any("version" in f for f in failures))

    def test_bad_digest_format_fails(self):
        self._manifest(files={"usage-guide.md": "abc"})
        failures = self._failures()
        self.assertTrue(any("digest" in f for f in failures))

    def test_bad_history_entry_fails(self):
        self._manifest(history=[
            {"from": None, "to": "plantillas/v1",
             "breaking": "sí", "changes": {}},
        ])
        failures = self._failures()
        self.assertTrue(any("breaking" in f for f in failures))

    def test_unreadable_template_fails_sanitized(self):
        self._manifest()
        target = self.dir / "usage-guide.md"
        original = Path.read_bytes

        def read_with_failure(path, *args, **kwargs):
            if path == target:
                raise OSError("/private/private-payload")
            return original(path, *args, **kwargs)

        with patch.object(Path, "read_bytes", read_with_failure):
            failures = self._failures()
        self.assertTrue(any("no se pudo leer" in f for f in failures))
        self.assertTrue(all("private-payload" not in f for f in failures))

    def test_deep_nested_json_fails_sanitized(self):
        """JSON anidado por debajo del límite de recursión: fallo controlado
        sin excepción cruda (hallazgo BLOCKER de la ronda adversarial)."""
        self.manifest_path.write_text("[" * 60000 + "]" * 60000,
                                      encoding="utf-8")
        failures = self._failures()
        self.assertEqual(len(failures), 1)
        self.assertIn("JSON", failures[0])
        self.assertNotIn("Traceback", str(failures))

    def test_symlink_in_templates_dir_fails(self):
        """Un symlink en templates/skevi/ no se sigue ni se digiere: fallo
        (hallazgo LOW de la ronda adversarial: frontera de raíz)."""
        self._manifest()
        outside = Path(self.tmp.name) / "fuera.md"
        outside.write_text("private-payload\n", encoding="utf-8")
        (self.dir / "leak.md").symlink_to(outside)
        failures = self._failures()
        self.assertTrue(any("symlink" in f for f in failures))
        self.assertTrue(all("private-payload" not in f for f in failures))


class TemplateManifestIntegrationTests(unittest.TestCase):
    """Integración: main() valida el MANIFEST cuando existe (#28 D1)."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self._orig_root = check_sizes.ROOT
        check_sizes.ROOT = self.root

    def tearDown(self):
        check_sizes.ROOT = self._orig_root

    def _minimal_repo(self):
        for relative in sorted(check_sizes.REQUIRED):
            path = self.root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(f"# {relative}\n", encoding="utf-8")
        skevi_dir = self.root / "templates" / "skevi"
        data = {
            "schema": check_sizes.TEMPLATE_MANIFEST_SCHEMA,
            "version": "plantillas/v1",
            "generated_at": "2026-09-08T00:00:00Z",
            "files": {
                p.name: digest_of(p)
                for p in sorted(skevi_dir.iterdir())
                if p.is_file() and p.name != "MANIFEST.json"
            },
            "history": [],
        }
        (skevi_dir / "MANIFEST.json").write_text(
            json.dumps(data, indent=2) + "\n", encoding="utf-8"
        )

    def _run_main(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = check_sizes.main()
        return code, buf.getvalue()

    def test_valid_manifest_passes_gate(self):
        self._minimal_repo()
        code, out = self._run_main()
        self.assertEqual(code, 0)
        self.assertTrue(out.startswith("OK —"))

    def test_template_change_without_bump_breaks_gate(self):
        """Aceptación #28 D1: editar plantilla sin bump rompe el gate local."""
        self._minimal_repo()
        (self.root / "templates" / "skevi" / "usage-guide.md").write_text(
            "editada\n", encoding="utf-8"
        )
        code, out = self._run_main()
        self.assertEqual(code, 1)
        self.assertIn("digest desactualizado", out)
        self.assertIn("usage-guide.md", out)

    def test_adopter_with_templates_dir_but_no_manifest_passes(self):
        """Promesa de ADR-020: un adoptante con templates/skevi/ previo (sin
        MANIFEST) que actualiza el gate no se ve bloqueado. La exigencia
        canónica de Skevi vive en su propia skevi-gate.json, no en los
        valores por defecto del script."""
        self._minimal_repo()
        (self.root / "templates" / "skevi" / "MANIFEST.json").unlink()
        code, out = self._run_main()
        self.assertEqual(code, 0)
        self.assertTrue(out.startswith("OK —"))



class ScriptManifestGateTests(unittest.TestCase):
    """Extensión de ADR-020 a scripts/ (ADR-028): mismo comprobador, distinto
    esquema y directorio, con validación estricta por artefacto — un
    manifiesto de scripts no puede colarse con el esquema de plantillas."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.dir = Path(self.tmp.name) / "scripts"
        self.dir.mkdir(parents=True)
        self.manifest_path = self.dir / "MANIFEST.json"
        (self.dir / "check_sizes.py").write_text("# gate\n", encoding="utf-8")

    def _manifest(self, schema=None):
        data = {
            "schema": schema or check_sizes.SCRIPT_MANIFEST_SCHEMA,
            "version": "gate/v2",
            "generated_at": "2026-09-08T00:00:00Z",
            "files": {"check_sizes.py": digest_of(self.dir / "check_sizes.py")},
            "history": [],
        }
        self.manifest_path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    def test_accepts_script_schema_when_declared_explicitly(self):
        self._manifest()
        failures = check_sizes.check_template_manifest(
            self.manifest_path, self.dir,
            expected_schema=check_sizes.SCRIPT_MANIFEST_SCHEMA,
        )
        self.assertEqual(failures, [])

    def test_template_schema_is_rejected_for_a_script_manifest(self):
        """Validación estricta por artefacto: aceptar cualquier esquema
        reconocido por Skevi en cualquier directorio sería más laxo de lo
        necesario — cada manifiesto declara y se valida contra el suyo."""
        self._manifest(schema=check_sizes.TEMPLATE_MANIFEST_SCHEMA)
        failures = check_sizes.check_template_manifest(
            self.manifest_path, self.dir,
            expected_schema=check_sizes.SCRIPT_MANIFEST_SCHEMA,
        )
        self.assertTrue(failures)
        self.assertIn("schema desconocido", failures[0])

    def test_default_expected_schema_is_the_template_one(self):
        """Compatibilidad: llamadas existentes sin el parámetro nuevo siguen
        validando contra el esquema de plantillas, sin cambio de firma."""
        import inspect
        sig = inspect.signature(check_sizes.check_template_manifest)
        self.assertEqual(
            sig.parameters["expected_schema"].default,
            check_sizes.TEMPLATE_MANIFEST_SCHEMA,
        )

    def test_label_reflects_the_scripts_directory(self):
        """El mensaje de error generaliza más allá de "templates/skevi/"."""
        (self.dir / "extra.py").write_text("# no listado\n", encoding="utf-8")
        self._manifest()
        failures = check_sizes.check_template_manifest(
            self.manifest_path, self.dir,
            expected_schema=check_sizes.SCRIPT_MANIFEST_SCHEMA,
        )
        self.assertTrue(any("scripts/MANIFEST.json" in f for f in failures), failures)
        self.assertFalse(any("templates/skevi/" in f for f in failures), failures)


class MainRunsScriptsManifestTests(unittest.TestCase):
    """main() valida scripts/MANIFEST.json cuando existe, igual que ya hace
    con templates/skevi/MANIFEST.json."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self._orig_root = check_sizes.ROOT
        check_sizes.ROOT = self.root
        for relative in sorted(check_sizes.REQUIRED):
            path = self.root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(f"# {relative}\n", encoding="utf-8")
        skevi_dir = self.root / "templates" / "skevi"
        data = {
            "schema": check_sizes.TEMPLATE_MANIFEST_SCHEMA,
            "version": "plantillas/v1",
            "generated_at": "2026-09-08T00:00:00Z",
            "files": {
                p.name: digest_of(p)
                for p in sorted(skevi_dir.iterdir())
                if p.is_file() and p.name != "MANIFEST.json"
            },
            "history": [],
        }
        (skevi_dir / "MANIFEST.json").write_text(
            json.dumps(data, indent=2) + "\n", encoding="utf-8"
        )

    def tearDown(self):
        check_sizes.ROOT = self._orig_root

    def _run(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = check_sizes.main()
        return code, buf.getvalue()

    def test_absent_scripts_manifest_is_not_an_error(self):
        """Adopción progresiva: sin scripts/MANIFEST.json, nada se comprueba
        — mismo criterio que templates/skevi/MANIFEST.json."""
        exit_code, output = self._run()
        self.assertEqual(exit_code, 0, output)

    def test_scripts_manifest_out_of_sync_is_blocked(self):
        (self.root / "scripts" / "MANIFEST.json").write_text(
            json.dumps({
                "schema": check_sizes.SCRIPT_MANIFEST_SCHEMA,
                "version": "gate/v2",
                "generated_at": "2026-09-08T00:00:00Z",
                "files": {"check_sizes.py": "sha256:" + "0" * 64},
                "history": [],
            }) + "\n",
            encoding="utf-8",
        )
        exit_code, output = self._run()
        self.assertEqual(exit_code, 1)
        self.assertIn("scripts/MANIFEST.json", output)

    def test_scripts_manifest_in_sync_passes(self):
        real = digest_of(self.root / "scripts" / "check_sizes.py")
        (self.root / "scripts" / "MANIFEST.json").write_text(
            json.dumps({
                "schema": check_sizes.SCRIPT_MANIFEST_SCHEMA,
                "version": "gate/v2",
                "generated_at": "2026-09-08T00:00:00Z",
                "files": {"check_sizes.py": real},
                "history": [],
            }) + "\n",
            encoding="utf-8",
        )
        exit_code, output = self._run()
        self.assertEqual(exit_code, 0, output)


class ScriptManifestMatchesGateVersionTests(unittest.TestCase):
    """scripts/MANIFEST.json.version y check_sizes.GATE_VERSION (ADR-027) son
    el mismo número por convención, no por código compartido: si divergen,
    nada los detecta salvo este test. Subir GATE_VERSION sin regenerar el
    manifiesto —o al revés— debe romper aquí (ADR-028)."""

    def test_manifest_version_equals_gate_version_constant(self):
        root = Path(__file__).resolve().parent.parent
        data = json.loads((root / "scripts" / "MANIFEST.json").read_text(
            encoding="utf-8"))
        self.assertEqual(data["version"], check_sizes.GATE_VERSION)

    def test_manifest_digests_match_the_real_files_on_disk(self):
        root = Path(__file__).resolve().parent.parent
        data = json.loads((root / "scripts" / "MANIFEST.json").read_text(
            encoding="utf-8"))
        for name, digest in data["files"].items():
            self.assertEqual(digest_of(root / "scripts" / name), digest, name)


class ScriptsInstalledTemplateTests(unittest.TestCase):
    """La plantilla copiable de scripts-installed.json debe coincidir con la
    versión vigente del manifiesto fuente al momento de publicarse: si no,
    un adoptante nuevo que sólo llena los placeholders documentados recibe
    BLOQ en su primera ejecución (hallazgo BLOCKER de la ronda 2026-09-08)."""

    def test_template_version_matches_source_manifest(self):
        root = Path(__file__).resolve().parent.parent
        plantilla = json.loads(
            (root / "templates" / "skevi" / "scripts-installed.json")
            .read_text(encoding="utf-8"))
        fuente = json.loads(
            (root / "scripts" / "MANIFEST.json").read_text(encoding="utf-8"))
        self.assertEqual(plantilla["version"], fuente["version"])

    def test_a_freshly_filled_template_passes_the_gate(self):
        """Simula un adoptante que llena sólo los placeholders documentados
        —digests, installed_at, source— y corre el comparador tal cual."""
        root = Path(__file__).resolve().parent.parent
        plantilla = json.loads(
            (root / "templates" / "skevi" / "scripts-installed.json")
            .read_text(encoding="utf-8"))
        fuente = json.loads(
            (root / "scripts" / "MANIFEST.json").read_text(encoding="utf-8"))
        plantilla["files"] = dict(fuente["files"])
        plantilla["installed_at"] = "2026-09-08T00:00:00Z"
        plantilla["source"] = "skevi/scripts"
        with tempfile.TemporaryDirectory() as tmp:
            installed_path = Path(tmp) / "scripts-installed.json"
            installed_path.write_text(json.dumps(plantilla), encoding="utf-8")
            buf = io.StringIO()
            ct_spec = importlib.util.spec_from_file_location(
                "check_templates_from_manifest_test",
                SCRIPTS_DIR / "check_templates.py")
            check_templates = importlib.util.module_from_spec(ct_spec)
            ct_spec.loader.exec_module(check_templates)
            with redirect_stdout(buf):
                code = check_templates.main([
                    "--manifest", str(root / "scripts" / "MANIFEST.json"),
                    "--installed", str(installed_path),
                ])
        self.assertEqual(code, 0, buf.getvalue())


class CheckSizesEnforcesNamespaceTests(unittest.TestCase):
    """HIGH de la segunda ronda (2026-09-08): check_templates.py ataba
    version al namespace de su schema; check_sizes.py —la autoverificación
    de Skevi sobre sí misma— no. Un scripts/MANIFEST.json con schema de
    scripts pero version de plantillas pasaba la autoverificación de Skevi
    y luego el adoptante lo rechazaba: el defecto opuesto al BLOCKER
    original, detectable sólo por el gate equivocado."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.dir = Path(self.tmp.name) / "scripts"
        self.dir.mkdir(parents=True)
        (self.dir / "check_sizes.py").write_text("# gate\n", encoding="utf-8")

    def test_wrong_namespace_for_script_schema_is_rejected(self):
        manifest = {
            "schema": check_sizes.SCRIPT_MANIFEST_SCHEMA,
            "version": "plantillas/v2",
            "generated_at": "2026-09-08T00:00:00Z",
            "files": {"check_sizes.py": digest_of(self.dir / "check_sizes.py")},
            "history": [],
        }
        manifest_path = self.dir / "MANIFEST.json"
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
        failures = check_sizes.check_template_manifest(
            manifest_path, self.dir, expected_schema=check_sizes.SCRIPT_MANIFEST_SCHEMA
        )
        self.assertTrue(failures)
        self.assertIn("espacio de nombres", failures[0])

    def test_wrong_namespace_for_template_schema_is_rejected(self):
        (self.dir / "usage-guide.md").write_text("x\n", encoding="utf-8")
        (self.dir / "check_sizes.py").unlink()
        manifest = {
            "schema": check_sizes.TEMPLATE_MANIFEST_SCHEMA,
            "version": "gate/v2",
            "generated_at": "2026-09-08T00:00:00Z",
            "files": {"usage-guide.md": digest_of(self.dir / "usage-guide.md")},
            "history": [],
        }
        manifest_path = self.dir / "MANIFEST.json"
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
        failures = check_sizes.check_template_manifest(manifest_path, self.dir)
        self.assertTrue(failures)
        self.assertIn("espacio de nombres", failures[0])

    def test_history_jump_namespace_is_rejected(self):
        manifest = {
            "schema": check_sizes.SCRIPT_MANIFEST_SCHEMA,
            "version": "gate/v2",
            "generated_at": "2026-09-08T00:00:00Z",
            "files": {"check_sizes.py": digest_of(self.dir / "check_sizes.py")},
            "history": [{"from": "plantillas/v1", "to": "gate/v2",
                        "breaking": False, "changes": {}}],
        }
        manifest_path = self.dir / "MANIFEST.json"
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
        failures = check_sizes.check_template_manifest(
            manifest_path, self.dir, expected_schema=check_sizes.SCRIPT_MANIFEST_SCHEMA
        )
        self.assertTrue(failures)
        self.assertIn("espacio de nombres", failures[0])


class ManifestListingRespectsExemptionsTests(unittest.TestCase):
    """Un .DS_Store en el directorio del manifiesto no debe exigir entrada,
    pero la exención tiene que ser propia y estrecha —dotfiles—, nunca
    EXEMPT_PATHS/EXEMPT_SUFFIXES: esos significan "exento del límite de
    tamaño", y reusarlos aquí dejaba que una línea de skevi-gate.json
    sacara un archivo real de la exigencia de versionado, en verde y sin
    aviso (hallazgo HIGH de la tercera ronda, 2026-09-08)."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self._orig_root = check_sizes.ROOT
        check_sizes.ROOT = Path(self.tmp.name)
        self.dir = check_sizes.ROOT / "scripts"
        self.dir.mkdir()
        (self.dir / "check_sizes.py").write_text("# gate\n", encoding="utf-8")

    def tearDown(self):
        check_sizes.ROOT = self._orig_root

    def _manifest_failures(self):
        manifest = {
            "schema": check_sizes.SCRIPT_MANIFEST_SCHEMA,
            "version": "gate/v2",
            "generated_at": "2026-09-08T00:00:00Z",
            "files": {"check_sizes.py": digest_of(self.dir / "check_sizes.py")},
            "history": [],
        }
        manifest_path = self.dir / "MANIFEST.json"
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
        return check_sizes.check_template_manifest(
            manifest_path, self.dir, expected_schema=check_sizes.SCRIPT_MANIFEST_SCHEMA
        )

    def test_ds_store_dotfile_does_not_require_manifest_entry(self):
        (self.dir / ".DS_Store").write_bytes(b"\x00\x01binary")
        self.assertEqual(self._manifest_failures(), [])

    def test_exempt_paths_cannot_hide_a_real_file_from_the_manifest(self):
        """EXEMPT_PATHS es config del adoptante (skevi-gate.json); no debe
        poder silenciar la exigencia de versionado de un archivo real."""
        (self.dir / "notas.txt").write_text("no debería colarse\n",
                                             encoding="utf-8")
        check_sizes.EXEMPT_PATHS.add("scripts/notas.txt")
        self.addCleanup(check_sizes.EXEMPT_PATHS.discard, "scripts/notas.txt")
        failures = self._manifest_failures()
        self.assertTrue(
            any("notas.txt" in f for f in failures), failures)

    def test_exempt_suffix_cannot_hide_a_real_file_from_the_manifest(self):
        (self.dir / "notas.md").write_text("no debería colarse\n",
                                            encoding="utf-8")
        check_sizes.EXEMPT_SUFFIXES.add(".md")
        self.addCleanup(check_sizes.EXEMPT_SUFFIXES.discard, ".md")
        failures = self._manifest_failures()
        self.assertTrue(any("notas.md" in f for f in failures), failures)


class MainBlockIsAtTheEndTests(unittest.TestCase):
    """Ver test_check_templates.MainBlockIsAtTheEndTests: misma guardia,
    mismo defecto reaparecido tres veces en la misma sesión."""

    def test_nothing_meaningful_follows_the_main_block(self):
        # Ancla en columna 0: así no se confunde con el propio literal de
        # este método, que aparece indentado en el código fuente.
        texto = Path(__file__).read_text(encoding="utf-8")
        patron = r'(?m)^if __name__ == "__main__":\n    unittest\.main\(\)\n'
        match = re.search(patron, texto)
        self.assertIsNotNone(match, "no se encontró el bloque __main__")
        self.assertEqual(texto[match.end():].strip(), "",
                         "hay código después del bloque __main__")



class CheckSizesNamespaceFailsClosedTests(unittest.TestCase):
    """check_sizes._check_namespace portaba la comprobación pero no el
    fail-closed de check_templates.py: un esquema sin namespace registrado
    pasaba en silencio en vez de fallar (MED, tercera ronda 2026-09-08)."""

    def test_unregistered_schema_fails_closed(self):
        """_check_namespace devuelve un mensaje de fallo (no None) ante un
        esquema sin namespace registrado — el patrón del resto de
        _validate_template_manifest, que acumula strings, no excepciones.
        Un test que sólo comprobara "no revienta" habría sido vacuo: aquí
        se exige la señal positiva de fallo."""
        fallo = check_sizes._check_namespace(
            "cualquier/cosa", "skevi/tercera-familia/v1", "L")
        self.assertIsNotNone(fallo)
        self.assertIn("namespace", fallo)

    def test_every_expected_schema_has_a_namespace(self):
        self.assertEqual(
            set(check_sizes.SCHEMA_NAMESPACE),
            {check_sizes.TEMPLATE_MANIFEST_SCHEMA, check_sizes.SCRIPT_MANIFEST_SCHEMA},
        )
if __name__ == "__main__":
    unittest.main()
