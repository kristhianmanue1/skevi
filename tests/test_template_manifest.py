"""Tests del gate de MANIFEST de plantillas en check_sizes (#28 D1 + T09).

Runner: `python3 -m unittest`.
"""

from __future__ import annotations

import hashlib
import importlib.util
import io
import json
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


if __name__ == "__main__":
    unittest.main()
