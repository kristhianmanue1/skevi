"""Tests para scripts/check_templates.py (drift de plantillas: #28 D3 + T09).

Runner: `python3 -m unittest`.
"""

from __future__ import annotations

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
    "check_templates", SCRIPTS_DIR / "check_templates.py"
)
check_templates = importlib.util.module_from_spec(_SPEC)
sys.modules["check_templates"] = check_templates
_SPEC.loader.exec_module(check_templates)


def write_json(path, data):
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def manifest_data(version="plantillas/v2", history=None, files=None):
    return {
        "schema": "skevi/template-manifest/v1",
        "version": version,
        "generated_at": "2026-09-08T00:00:00Z",
        "files": files or {"usage-guide.md": "sha256:" + "a" * 64},
        "history": history if history is not None else [],
    }


def installed_data(version="plantillas/v1", customized=None, files=None):
    return {
        "schema": "skevi/template-install/v1",
        "version": version,
        "files": files or {"usage-guide.md": "sha256:" + "b" * 64},
        "installed_at": "2026-09-01T00:00:00Z",
        "source": "skevi/templates/skevi@0a1b2c3",
        "customized": customized or [],
    }


TWO_FILES = ["usage-guide.md", "architecture-overview.md"]


def files_for(names):
    return {name: "sha256:" + "a" * 64 for name in names}


class DriftCheckTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.manifest_path = self.root / "MANIFEST.json"
        self.installed_path = self.root / "installed.json"

    def _scenario(self, manifest, installed):
        write_json(self.manifest_path, manifest)
        write_json(self.installed_path, installed)

    def _run(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = check_templates.main(
                [
                    "--manifest", str(self.manifest_path),
                    "--installed", str(self.installed_path),
                ]
            )
        return code, buf.getvalue()

    # --- sin drift -------------------------------------------------------

    def test_same_version_is_ok(self):
        self._scenario(
            manifest_data(version="plantillas/v1"),
            installed_data(version="plantillas/v1"),
        )
        code, out = self._run()
        self.assertEqual(code, 0)
        self.assertTrue(out.startswith("OK —"))
        self.assertIn("al día", out)

    # --- caso A: obsoleto pero compatible (T09 D2-A) ----------------------

    def test_nonbreaking_chain_is_ok_with_notice(self):
        history = [
            {"from": "plantillas/v1", "to": "plantillas/v1.1",
             "breaking": False, "changes": {"usage-guide.md": "redacción"}},
            {"from": "plantillas/v1.1", "to": "plantillas/v2",
             "breaking": False, "changes": {}},
        ]
        self._scenario(
            manifest_data(version="plantillas/v2", history=history,
                          files=files_for(TWO_FILES)),
            installed_data(version="plantillas/v1", files=files_for(TWO_FILES)),
        )
        code, out = self._run()
        self.assertEqual(code, 0)
        self.assertTrue(out.startswith("OK —"))
        self.assertIn("compatible", out)
        self.assertIn("usage-guide.md", out)

    # --- caso B: obsoleto incompatible (T09 D2-B, #28 D3.2 = fallo) -------

    def test_breaking_chain_blocks(self):
        history = [
            {"from": "plantillas/v1", "to": "plantillas/v2",
             "breaking": True, "changes": {"usage-guide.md": "reestructura"}},
        ]
        self._scenario(
            manifest_data(version="plantillas/v2", history=history),
            installed_data(version="plantillas/v1"),
        )
        code, out = self._run()
        self.assertEqual(code, 1)
        self.assertTrue(out.startswith("BLOQ"))
        self.assertIn("template_drift_version", out)
        self.assertIn("breaking", out)
        self.assertIn("usage-guide.md", out)

    def test_breaking_chain_with_customized_file_blocks_only_the_rest(self):
        history = [
            {"from": "plantillas/v1", "to": "plantillas/v2",
             "breaking": True, "changes": {"usage-guide.md": "x"}},
        ]
        self._scenario(
            manifest_data(version="plantillas/v2", history=history,
                          files=files_for(TWO_FILES)),
            installed_data(version="plantillas/v1", customized=["arch.md"],
                           files={"arch.md": "sha256:" + "b" * 64}),
        )
        code, out = self._run()
        self.assertEqual(code, 1)
        self.assertIn("template_drift_version", out)
        self.assertIn("usage-guide.md", out)
        self.assertIn("customized", out)

    # --- caso C: personalizado anula por archivo (T09 D2-C) ---------------

    def test_all_files_customized_is_ok_with_notices(self):
        history = [
            {"from": "plantillas/v1", "to": "plantillas/v2",
             "breaking": True, "changes": {"usage-guide.md": "x"}},
        ]
        self._scenario(
            manifest_data(version="plantillas/v2", history=history),
            installed_data(version="plantillas/v1",
                           customized=["usage-guide.md"]),
        )
        code, out = self._run()
        self.assertEqual(code, 0)
        self.assertTrue(out.startswith("OK —"))
        self.assertIn("customized", out)
        self.assertIn("usage-guide.md", out)

    # --- versión desconocida / cadena rota: fail-closed (T09 D2) ----------

    def test_unknown_version_blocks(self):
        self._scenario(
            manifest_data(version="plantillas/v2"),
            installed_data(version="plantillas/v0.9"),
        )
        code, out = self._run()
        self.assertEqual(code, 1)
        self.assertIn("template_drift_version", out)

    def test_chain_gap_blocks(self):
        history = [
            {"from": "plantillas/v2", "to": "plantillas/v3",
             "breaking": False, "changes": {}},
        ]
        self._scenario(
            manifest_data(version="plantillas/v3", history=history),
            installed_data(version="plantillas/v1"),
        )
        code, out = self._run()
        self.assertEqual(code, 1)
        self.assertIn("template_drift_version", out)

    def test_ambiguous_history_blocks(self):
        history = [
            {"from": "plantillas/v1", "to": "plantillas/v1.1",
             "breaking": False, "changes": {}},
            {"from": "plantillas/v1", "to": "plantillas/v1.2",
             "breaking": False, "changes": {}},
        ]
        self._scenario(
            manifest_data(version="plantillas/v2", history=history),
            installed_data(version="plantillas/v1"),
        )
        code, out = self._run()
        self.assertEqual(code, 1)
        self.assertIn("template_drift_version", out)

    def test_history_cycle_blocks(self):
        # El ciclo debe estar EN el camino recorrido: con vigente v3, el
        # paseo v1->v2 vuelve a pisar v1 y el guardián debe frenarlo.
        history = [
            {"from": "plantillas/v1", "to": "plantillas/v2",
             "breaking": False, "changes": {}},
            {"from": "plantillas/v2", "to": "plantillas/v1",
             "breaking": False, "changes": {}},
        ]
        self._scenario(
            manifest_data(version="plantillas/v3", history=history),
            installed_data(version="plantillas/v1"),
        )
        code, out = self._run()
        self.assertEqual(code, 1)
        self.assertIn("template_drift_version", out)

    # --- entradas inválidas: fallo controlado, sin traceback (ADR-007) ----

    def test_missing_installed_file_blocks(self):
        write_json(self.manifest_path, manifest_data())
        code, out = self._run()
        self.assertEqual(code, 1)
        self.assertTrue(out.startswith("BLOQ"))
        self.assertNotIn("Traceback", out)

    def test_invalid_json_blocks_sanitized(self):
        self.manifest_path.write_text("{", encoding="utf-8")
        write_json(self.installed_path, installed_data())
        code, out = self._run()
        self.assertEqual(code, 1)
        self.assertIn("JSON inválido", out)
        self.assertNotIn("Traceback", out)

    def test_unknown_install_schema_blocks(self):
        data = installed_data()
        data["schema"] = "skevi/template-install/v2"
        self._scenario(manifest_data(), data)
        code, out = self._run()
        self.assertEqual(code, 1)
        self.assertIn("schema", out)
        self.assertNotIn("Traceback", out)

    def test_unknown_field_blocks(self):
        data = installed_data()
        data["extra"] = 1
        self._scenario(manifest_data(), data)
        code, out = self._run()
        self.assertEqual(code, 1)
        self.assertIn("campo desconocido", out)

    def test_customized_outside_files_blocks(self):
        self._scenario(
            manifest_data(),
            installed_data(customized=["nope.md"]),
        )
        code, out = self._run()
        self.assertEqual(code, 1)
        self.assertIn("customized", out)

    def test_bad_digest_format_blocks(self):
        self._scenario(
            manifest_data(),
            installed_data(files={"usage-guide.md": "abc"}),
        )
        code, out = self._run()
        self.assertEqual(code, 1)
        self.assertIn("digest", out)

    def test_bad_manifest_version_format_blocks(self):
        self._scenario(
            manifest_data(version="v1"),
            installed_data(),
        )
        code, out = self._run()
        self.assertEqual(code, 1)
        self.assertNotIn("Traceback", out)

    def test_bad_history_entry_type_blocks(self):
        history = [
            {"from": "plantillas/v1", "to": "plantillas/v2",
             "breaking": "sí", "changes": {}},
        ]
        self._scenario(manifest_data(version="plantillas/v2", history=history),
                       installed_data())
        code, out = self._run()
        self.assertEqual(code, 1)
        self.assertNotIn("Traceback", out)

    # --- hallazgos de la ronda adversarial (contexto fresco) --------------

    def test_deep_nested_json_blocks_without_traceback(self):
        """JSON anidado por debajo del límite de recursión: BLOQ saneado."""
        self.manifest_path.write_text("[" * 60000 + "]" * 60000,
                                      encoding="utf-8")
        write_json(self.installed_path, installed_data())
        code, out = self._run()
        self.assertEqual(code, 1)
        self.assertTrue(out.startswith("BLOQ"))
        self.assertNotIn("Traceback", out)
        self.assertNotIn("RecursionError", out)

    def test_read_failure_does_not_leak_payload(self):
        target = self.installed_path
        original = Path.read_text

        def read_with_failure(path, *args, **kwargs):
            if path == target:
                raise OSError("/private/private-payload")
            return original(path, *args, **kwargs)

        write_json(self.manifest_path, manifest_data())
        with patch.object(Path, "read_text", read_with_failure):
            code, out = self._run()
        self.assertEqual(code, 1)
        self.assertTrue(out.startswith("BLOQ"))
        self.assertNotIn("private-payload", out)
        self.assertNotIn("Traceback", out)

    def test_empty_changes_chain_does_not_fabricate_file_list(self):
        """Cadena compatible sin registro de cambios: aviso genérico, no una
        lista fabricada de archivos «cambiados» (hallazgo LOW)."""
        history = [
            {"from": "plantillas/v1", "to": "plantillas/v2",
             "breaking": False, "changes": {}},
        ]
        self._scenario(
            manifest_data(version="plantillas/v2", history=history),
            installed_data(),
        )
        code, out = self._run()
        self.assertEqual(code, 0)
        self.assertIn("no registra cambios por archivo", out)
        self.assertNotIn("cambia en la cadena", out)



class ScriptManifestFamilyTests(unittest.TestCase):
    """Extensión de ADR-020 a scripts/ (ADR-028): el mecanismo de MANIFEST +
    installed es genérico — no depende de que el artefacto sea una plantilla.
    Se añade una segunda familia de esquema (`skevi/script-manifest/v1` +
    `skevi/script-install/v1`) sin tocar la primera."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.manifest_path = self.root / "MANIFEST.json"
        self.installed_path = self.root / "installed.json"

    def _run(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = check_templates.main(
                ["--manifest", str(self.manifest_path),
                 "--installed", str(self.installed_path)]
            )
        return code, buf.getvalue()

    def test_script_manifest_schema_is_accepted(self):
        write_json(self.manifest_path, {
            "schema": "skevi/script-manifest/v1",
            "version": "gate/v2",
            "generated_at": "2026-09-08T00:00:00Z",
            "files": files_for(["check_sizes.py"]),
            "history": [],
        })
        write_json(self.installed_path, {
            "schema": "skevi/script-install/v1",
            "version": "gate/v2",
            "files": files_for(["check_sizes.py"]),
            "installed_at": "2026-09-08T00:00:00Z",
            "source": "skevi/scripts@0a1b2c3",
            "customized": [],
        })
        code, output = self._run()
        self.assertEqual(code, 0, output)
        self.assertTrue(output.startswith("OK —"))

    def test_corpus_family_is_accepted(self):
        """Tercera familia (ADR-032): el manifiesto del canon y el registro
        del adoptante comparan por versión, como las familias previas."""
        write_json(self.manifest_path, {
            "schema": "skevi/corpus-manifest/v1",
            "version": "corpus/v1",
            "generated_at": "2026-09-13T00:00:00Z",
            "files": files_for(["estandar.md"]),
            "history": [],
        })
        write_json(self.installed_path, {
            "schema": "skevi/corpus-install/v1",
            "version": "corpus/v1",
            "files": files_for(["estandar.md"]),
            "installed_at": "2026-09-13T00:00:00Z",
            "source": "skevi@0a1b2c3",
            "customized": [],
        })
        code, output = self._run()
        self.assertEqual(code, 0, output)
        self.assertTrue(output.startswith("OK —"))

    def test_corpus_version_must_use_corpus_namespace(self):
        write_json(self.manifest_path, {
            "schema": "skevi/corpus-manifest/v1",
            "version": "gate/v2",
            "generated_at": "2026-09-13T00:00:00Z",
            "files": files_for(["estandar.md"]),
            "history": [],
        })
        write_json(self.installed_path, installed_data())
        code, output = self._run()
        self.assertEqual(code, 1)
        self.assertTrue(output.startswith("BLOQ"))

    def test_gate_version_format_is_accepted(self):
        """El formato de versión no queda anclado a «plantillas»: cualquier
        espacio de nombres en minúsculas con /vN es válido."""
        self.assertTrue(check_templates.VERSION_RE.match("gate/v2"))
        self.assertTrue(check_templates.VERSION_RE.match("plantillas/v1"))
        self.assertFalse(check_templates.VERSION_RE.match("Gate/v2"))
        self.assertFalse(check_templates.VERSION_RE.match("gate/2"))

    def test_unknown_schema_family_is_still_rejected(self):
        write_json(self.manifest_path, {
            "schema": "skevi/inventado/v1",
            "version": "gate/v2",
            "generated_at": "2026-09-08T00:00:00Z",
            "files": files_for(["x.py"]),
            "history": [],
        })
        write_json(self.installed_path, installed_data())
        code, output = self._run()
        self.assertEqual(code, 1)
        self.assertTrue(output.startswith("BLOQ"))

    def test_template_family_still_works_unchanged(self):
        """No regresión: la familia original sigue funcionando tal cual."""
        write_json(self.manifest_path, manifest_data(
            version="plantillas/v1", files=files_for(TWO_FILES)))
        write_json(self.installed_path, installed_data(
            version="plantillas/v1", files=files_for(TWO_FILES)))
        code, output = self._run()
        self.assertEqual(code, 0, output)

    def test_mismatched_families_fail_closed_via_missing_chain(self):
        """Comparar un manifiesto de scripts contra un registro de plantillas
        no encuentra cadena de versión y falla cerrado."""
        write_json(self.manifest_path, {
            "schema": "skevi/script-manifest/v1",
            "version": "gate/v2",
            "generated_at": "2026-09-08T00:00:00Z",
            "files": files_for(["check_sizes.py"]),
            "history": [],
        })
        write_json(self.installed_path, installed_data(version="plantillas/v1"))
        code, output = self._run()
        self.assertEqual(code, 1)
        self.assertIn("sin cadena hasta la vigente", output)

    def test_manifest_version_must_match_its_own_schema_namespace(self):
        """Hallazgo HIGH de la ronda 2026-09-08: sin esto, un manifiesto de
        scripts con version «plantillas/v2» comparado contra un registro de
        plantillas en «plantillas/v2» daba OK falso — coincidencia de
        namespace entre familias, no protección real."""
        write_json(self.manifest_path, {
            "schema": "skevi/script-manifest/v1",
            "version": "plantillas/v2",
            "generated_at": "2026-09-08T00:00:00Z",
            "files": files_for(["x.py"]),
            "history": [],
        })
        write_json(self.installed_path, {
            "schema": "skevi/template-install/v1",
            "version": "plantillas/v2",
            "files": files_for(["x.py"]),
            "installed_at": "2026-09-08T00:00:00Z",
            "source": "x@0a1b2c3",
            "customized": [],
        })
        code, output = self._run()
        self.assertEqual(code, 1, output)
        self.assertTrue(output.startswith("BLOQ"))

    def test_installed_version_must_match_its_own_schema_namespace(self):
        write_json(self.manifest_path, manifest_data(version="plantillas/v1"))
        write_json(self.installed_path, {
            "schema": "skevi/script-install/v1",
            "version": "plantillas/v1",
            "files": files_for(["usage-guide.md"]),
            "installed_at": "2026-09-08T00:00:00Z",
            "source": "x@0a1b2c3",
            "customized": [],
        })
        code, output = self._run()
        self.assertEqual(code, 1, output)
        self.assertTrue(output.startswith("BLOQ"))

    def test_history_jump_version_must_match_manifest_schema_namespace(self):
        write_json(self.manifest_path, {
            "schema": "skevi/script-manifest/v1",
            "version": "gate/v2",
            "generated_at": "2026-09-08T00:00:00Z",
            "files": files_for(["x.py"]),
            "history": [{"from": "plantillas/v1", "to": "gate/v2",
                        "breaking": False, "changes": {}}],
        })
        write_json(self.installed_path, {
            "schema": "skevi/script-install/v1",
            "version": "plantillas/v1",
            "files": files_for(["x.py"]),
            "installed_at": "2026-09-08T00:00:00Z",
            "source": "x@0a1b2c3",
            "customized": [],
        })
        code, output = self._run()
        self.assertEqual(code, 1, output)
        self.assertTrue(output.startswith("BLOQ"))


class SourceProvenanceTests(unittest.TestCase):
    """A-7 de PROP-002, aterrizada por ADR-031: `source` es procedencia
    cerrada <origen>@<revisión>, no texto libre — la evidencia que su
    decisión exigía («un agente responde qué versión sigue y qué dejó,
    leyendo un archivo») no la produce un campo sin ancla."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)

    def _regex_accepts(self, *values):
        for value in values:
            self.assertTrue(
                check_templates.SOURCE_RE.match(value),
                f"debería aceptar {value!r}",
            )

    def _regex_rejects(self, *values):
        for value in values:
            self.assertFalse(
                check_templates.SOURCE_RE.match(value),
                f"debería rechazar {value!r}",
            )

    def test_closed_format(self):
        self._regex_accepts(
            "https://github.com/org/repo@0a1b2c3",
            "https://github.com/org/repo@" + "a" * 40,
            "https://github.com/org/repo@" + "a" * 64,
            "../espejo-local/skevi@0a1b2c3d",
        )
        self._regex_rejects(
            "skevi/templates/skevi",
            "repo@ABCDEF0",
            "repo@0a1b2c",
            "repo@a@0a1b2c3",
            "repo@0a1b2c3 extra",
            "",
        )

    def test_free_text_source_blocks_end_to_end(self):
        write_json(self.root / "MANIFEST.json", manifest_data(
            version="plantillas/v1"))
        installed = installed_data(version="plantillas/v1")
        installed["source"] = "la copié de otro proyecto"
        write_json(self.root / "installed.json", installed)
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = check_templates.main(
                ["--manifest", str(self.root / "MANIFEST.json"),
                 "--installed", str(self.root / "installed.json")]
            )
        output = buf.getvalue()
        self.assertEqual(code, 1)
        self.assertTrue(output.startswith("BLOQ"))
        self.assertIn("<origen>@<revisión>", output)


class SchemaNamespaceCompletenessTests(unittest.TestCase):
    """Ancla que SCHEMA_NAMESPACE cubre exactamente los esquemas reconocidos
    —si alguien añade una familia a MANIFEST_SCHEMAS/INSTALL_SCHEMAS sin
    registrar su namespace, este test lo dice antes que un adoptante."""

    def test_every_recognized_schema_has_a_namespace(self):
        self.assertEqual(
            set(check_templates.SCHEMA_NAMESPACE),
            check_templates.MANIFEST_SCHEMAS | check_templates.INSTALL_SCHEMAS,
        )


class MainBlockIsAtTheEndTests(unittest.TestCase):
    """Este defecto reapareció tres veces en la misma sesión: cada clase
    anexada con `>>` aterriza después de `if __name__ == "__main__":`, y
    ejecutar el archivo suelto la omite en silencio. Guardia estructural
    para que la próxima vez lo atrape la suite, no una ronda adversarial."""

    def test_nothing_meaningful_follows_the_main_block(self):
        # Ancla en columna 0: así no se confunde con el propio literal de
        # este método, que aparece indentado en el código fuente.
        texto = Path(__file__).read_text(encoding="utf-8")
        patron = r'(?m)^if __name__ == "__main__":\n    unittest\.main\(\)\n'
        match = re.search(patron, texto)
        self.assertIsNotNone(match, "no se encontró el bloque __main__")
        self.assertEqual(texto[match.end():].strip(), "",
                         "hay código después del bloque __main__")

class SalidaDeLaCadenaTests(unittest.TestCase):
    """Conductas de `main()` que gate/v8 introdujo para el issue #57. Sin
    estos casos, las tres se podían revertir enteras con la suite en verde:
    el único fallo era el digest del manifiesto, que detecta «el archivo
    cambió», no «el gate dice la verdad»."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.manifest_path = self.root / "MANIFEST.json"
        self.installed_path = self.root / "installed.json"

    def _run(self, manifest, installed):
        write_json(self.manifest_path, manifest)
        write_json(self.installed_path, installed)
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = check_templates.main([
                "--manifest", str(self.manifest_path),
                "--installed", str(self.installed_path),
            ])
        return code, buf.getvalue()

    def test_breaking_jump_fully_customized_is_announced_without_failing(self):
        """Antes decía «sin saltos breaking aplicables» y salía 0: el mensaje
        era falso y el adoptante nunca veía su migración. Sigue saliendo 0
        —hacerlo fallar rompería a quien hoy pasa—, pero lo nombra."""
        code, out = self._run(
            manifest_data(version="plantillas/v2", history=[{
                "from": "plantillas/v1", "to": "plantillas/v2",
                "breaking": True,
                "changes": {"usage-guide.md": "mueve X antes de re-copiar"},
            }]),
            installed_data(version="plantillas/v1",
                           customized=["usage-guide.md"]),
        )
        self.assertEqual(code, 0)
        self.assertIn("cubiertos por customized", out)
        self.assertIn("salto breaking: plantillas/v1 -> plantillas/v2", out)
        self.assertIn("mueve X antes de re-copiar", out)
        self.assertNotIn("sin saltos breaking aplicables", out)

    def test_notice_separates_installed_from_merely_new(self):
        code, out = self._run(
            manifest_data(version="plantillas/v2", history=[{
                "from": "plantillas/v1", "to": "plantillas/v2",
                "breaking": False,
                "changes": {"usage-guide.md": "cambia",
                            "frozen-trees.md": "nueva"},
            }]),
            installed_data(version="plantillas/v1"),
        )
        self.assertEqual(code, 0)
        self.assertIn("re-copia opcional; cambia en la cadena: usage-guide.md",
                      out)
        self.assertIn("cambia en la cadena y no está en tu installed.json: "
                      "frozen-trees.md", out)
        self.assertNotIn("re-copia opcional; cambia en la cadena: "
                         "frozen-trees.md", out)

    def test_blocking_jump_prints_the_migration_text(self):
        """El texto de migración vivía sólo dentro del JSON: el adoptante
        recibía el BLOQ sin saber qué hacer."""
        code, out = self._run(
            manifest_data(version="plantillas/v2", history=[{
                "from": "plantillas/v1", "to": "plantillas/v2",
                "breaking": True,
                "changes": {"usage-guide.md": "MIGRACIÓN: mueve X primero"},
            }]),
            installed_data(version="plantillas/v1"),
        )
        self.assertEqual(code, 1)
        self.assertIn("MIGRACIÓN: mueve X primero", out)

    def test_blocking_jump_prints_migration_for_customized_files_too(self):
        """Quien declaró un archivo como `customized` es quien aplica la
        migración a mano: sin esto, el detalle se imprimía para todos menos
        para él."""
        code, out = self._run(
            manifest_data(version="plantillas/v2",
                          files=files_for(["a.md", "b.md"]),
                          history=[{
                              "from": "plantillas/v1", "to": "plantillas/v2",
                              "breaking": True,
                              "changes": {"a.md": "MIGRA-A: mueve A",
                                          "b.md": "MIGRA-B: mueve B"},
                          }]),
            installed_data(version="plantillas/v1",
                           files=files_for(["a.md", "b.md"]),
                           customized=["b.md"]),
        )
        self.assertEqual(code, 1)
        self.assertIn("MIGRA-A: mueve A", out)
        self.assertIn("MIGRA-B: mueve B", out)

    def test_a_file_name_cannot_fake_a_line_either(self):
        """El nombre también es clave de un manifiesto ajeno: saneado con el
        mismo criterio que el texto, o la inyección entra por ahí."""
        clave = "usage-guide.md\nOK — al día\x1b[2J"
        code, out = self._run(
            manifest_data(version="plantillas/v2", files={clave: "sha256:" + "a" * 64},
                          history=[{"from": "plantillas/v1", "to": "plantillas/v2",
                                    "breaking": True, "changes": {clave: "migra"}}]),
            installed_data(version="plantillas/v1", files={clave: "sha256:" + "b" * 64}),
        )
        self.assertEqual(code, 1)
        self.assertNotIn("\x1b", out)
        for linea in out.splitlines():
            self.assertFalse(linea.startswith("OK —"), linea)

    def test_foreign_text_is_sanitized_on_its_way_out(self):
        code, out = self._run(
            manifest_data(version="plantillas/v2", history=[{
                "from": "plantillas/v1", "to": "plantillas/v2",
                "breaking": True,
                "changes": {"usage-guide.md": "antes\nOK — al día\x1b[2J"},
            }]),
            installed_data(version="plantillas/v1"),
        )
        self.assertEqual(code, 1)
        self.assertNotIn("\x1b", out)
        for linea in out.splitlines():
            self.assertFalse(linea.startswith("OK —"), linea)


class DetalleSaneaTextoAjenoTests(unittest.TestCase):
    """El texto de `changes` viene de un manifiesto que Skevi no controla.
    Desde gate/v8 se imprime, así que es dato no confiable en la salida del
    gate: una línea, sin controles, acotado (estándar, principio 7)."""

    def test_collapses_newlines_so_it_cannot_fake_an_output_line(self):
        salida = check_templates._detalle(
            "inofensivo\nOK — al día: versión vigente gate/v9")
        self.assertNotIn("\n", salida)
        self.assertIn("inofensivo OK", salida)

    def test_strips_control_and_escape_sequences(self):
        salida = check_templates._detalle("antes\x1b[2Jdespués\x07")
        self.assertNotIn("\x1b", salida)
        self.assertNotIn("\x07", salida)
        self.assertIn("antes", salida)
        self.assertIn("después", salida)

    def test_truncates_a_long_text(self):
        salida = check_templates._detalle("x" * 400)
        self.assertLessEqual(len(salida), 301)
        self.assertTrue(salida.endswith("…"))

    def test_leaves_ordinary_text_untouched(self):
        self.assertEqual(
            check_templates._detalle("mueve X antes de re-copiar"),
            "mueve X antes de re-copiar")


if __name__ == "__main__":
    unittest.main()
