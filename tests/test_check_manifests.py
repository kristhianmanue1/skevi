"""Tests del dominio de manifiestos en su hogar desde gate/v9 (ADR-039):
estructura, digests contra disco y listado exacto. Vivió en
tests/test_check_sizes.py; se movió con el código que prueba.
Runner: `python3 -m unittest`."""

from __future__ import annotations

import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))
import check_sizes
import check_templates


class CorpusManifestTests(unittest.TestCase):
    """Familia corpus (ADR-032): docs/MANIFEST.json valida estructura y
    digests del canon declarado, sin listado de directorio — docs/ anida
    subdirectorios y el contrato de plantillas es plano por diseño."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self._orig_root = check_templates.ROOT
        check_templates.ROOT = self.root
        (self.root / "docs" / "ai-agent-guide").mkdir(parents=True)
        self.canon = self.root / "docs" / "estandar.md"
        self.canon.write_text("norma\n", encoding="utf-8")

    def tearDown(self):
        check_templates.ROOT = self._orig_root

    def _digest_of(self, path):
        return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()

    def _manifest(self, files=None, schema=None, version="corpus/v1"):
        data = {
            "schema": schema or check_templates.CORPUS_MANIFEST_SCHEMA,
            "version": version,
            "generated_at": "2026-09-13T00:00:00Z",
            "files": files if files is not None else {
                "estandar.md": self._digest_of(self.canon),
            },
            "history": [],
        }
        path = self.root / "docs" / "MANIFEST.json"
        path.write_text(json.dumps(data), encoding="utf-8")
        return path

    def test_valid_corpus_manifest_passes(self):
        self.assertEqual(
            check_templates.check_corpus_manifest(self._manifest()), [])

    def test_stale_digest_is_reported_per_file(self):
        path = self._manifest(files={"estandar.md": "sha256:" + "0" * 64})
        failures = check_templates.check_corpus_manifest(path)
        self.assertEqual(len(failures), 1)
        self.assertIn("estandar.md", failures[0])
        self.assertIn("digest desactualizado", failures[0])

    def test_wrong_schema_is_rejected_strictly(self):
        path = self._manifest(schema=check_templates.TEMPLATE_MANIFEST_SCHEMA)
        failures = check_templates.check_corpus_manifest(path)
        self.assertTrue(failures)

    def test_path_escaping_root_is_rejected(self):
        path = self._manifest(files={"../../fuera.md": "sha256:" + "0" * 64})
        failures = check_templates.check_corpus_manifest(path)
        self.assertTrue(any("escapa" in f for f in failures))

    def test_missing_file_is_a_failure_not_a_skip(self):
        path = self._manifest(files={"ai-agent-guide/00-INDICE.md":
                                     "sha256:" + "0" * 64})
        failures = check_templates.check_corpus_manifest(path)
        self.assertEqual(len(failures), 1)


class ListingIgnoresOsJunkButNotConfigTests(unittest.TestCase):
    """El listado exacto ignora la basura del SO por constante cerrada, y sólo
    eso. `exempt_names` es config del adoptante: si pudiera retirar archivos
    del cotejo, cualquiera ocultaría uno real del versionado — el agujero que
    esta clase defiende (issue #59). Desde gate/v9 el listado vive en
    check_templates pero sigue sin leer la config de check_sizes."""

    def setUp(self):
        self._orig_root = check_templates.ROOT
        self._orig_names = set(check_sizes.EXEMPT_NAMES)
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.addCleanup(self._restore)
        self.root = Path(self._tmp.name)
        check_templates.ROOT = self.root
        self.dir = self.root / "templates" / "skevi"
        self.dir.mkdir(parents=True)
        (self.dir / "usage-guide.md").write_text("# x\n", encoding="utf-8")
        self.manifest = self.dir / check_templates.TEMPLATE_MANIFEST_NAME
        self._write_manifest({"usage-guide.md": self._digest("usage-guide.md")})

    def _restore(self):
        check_templates.ROOT = self._orig_root
        check_sizes.EXEMPT_NAMES.clear()
        check_sizes.EXEMPT_NAMES.update(self._orig_names)

    def _digest(self, name):
        return "sha256:" + hashlib.sha256((self.dir / name).read_bytes()).hexdigest()

    def _write_manifest(self, files):
        self.manifest.write_text(json.dumps({
            "schema": check_templates.TEMPLATE_MANIFEST_SCHEMA,
            "version": "plantillas/v1",
            "generated_at": "2026-09-18T00:00:00Z",
            "files": files,
            "history": [],
        }), encoding="utf-8")

    def test_os_junk_is_ignored_without_any_configuration(self):
        (self.dir / ".DS_Store").write_bytes(b"\x00\x01")
        check_sizes.EXEMPT_NAMES.clear()
        self.assertEqual(
            check_templates.check_template_manifest(self.manifest, self.dir),
            [])

    def test_config_cannot_hide_a_real_file_from_the_listing(self):
        """El caso que motivó rehacer el arreglo: `exempt_names` exime del
        límite de tamaño, nunca del versionado."""
        (self.dir / "notas-internas.md").write_text("real\n", encoding="utf-8")
        check_sizes.EXEMPT_NAMES.add("notas-internas.md")
        fallos = check_templates.check_template_manifest(self.manifest, self.dir)
        self.assertTrue(
            any("notas-internas.md" in f for f in fallos), fallos)

    def test_junk_declared_in_the_manifest_is_still_checked(self):
        (self.dir / ".DS_Store").write_bytes(b"\x00\x01")
        self._write_manifest({
            "usage-guide.md": self._digest("usage-guide.md"),
            ".DS_Store": "sha256:" + "0" * 64,
        })
        fallos = check_templates.check_template_manifest(self.manifest, self.dir)
        self.assertTrue(any("digest desactualizado" in f for f in fallos), fallos)

    def test_other_extra_files_still_fail_the_listing(self):
        (self.dir / "suelto.md").write_text("x\n", encoding="utf-8")
        fallos = check_templates.check_template_manifest(self.manifest, self.dir)
        self.assertTrue(
            any("archivos sin entrada en el manifiesto" in f for f in fallos),
            fallos)


if __name__ == "__main__":
    unittest.main()
