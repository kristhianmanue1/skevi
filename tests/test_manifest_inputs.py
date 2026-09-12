"""ADR-007: campos ausentes y tipos inválidos fallan de forma controlada."""

import contextlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import check_sizes
import check_templates


def documents(family):
    namespace = "gate" if family == "script" else "plantillas"
    common = {"version": f"{namespace}/v1", "files": {"x": "sha256:" + "a" * 64}}
    return (
        dict(common, schema=f"skevi/{family}-manifest/v1",
             generated_at="2026-09-12T00:00:00Z", history=[]),
        dict(common, schema=f"skevi/{family}-install/v1",
             installed_at="2026-09-12T00:00:00Z", source="fixture", customized=[]),
    )


class ManifestInputTests(unittest.TestCase):
    def run_comparator(self, manifest, installed):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            paths = [root / "manifest.json", root / "installed.json"]
            for path, data in zip(paths, (manifest, installed)):
                path.write_text(json.dumps(data), encoding="utf-8")
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                code = check_templates.main([
                    "--manifest", str(paths[0]), "--installed", str(paths[1]),
                ])
            return code, output.getvalue()

    def assert_blocked(self, manifest, installed, field):
        code, output = self.run_comparator(manifest, installed)
        self.assertEqual(code, 1, output)
        self.assertTrue(output.startswith("BLOQ"), output)
        self.assertIn(field, output)
        self.assertNotIn("Traceback", output)

    def test_comparator_missing_fields_in_both_documents_and_families(self):
        for family in ("template", "script"):
            for side in (0, 1):
                for field in documents(family)[side]:
                    with self.subTest(family=family, side=side, field=field):
                        manifest, installed = documents(family)
                        del (manifest, installed)[side][field]
                        self.assert_blocked(manifest, installed, field)

    def test_comparator_invalid_schema_types_in_both_documents_and_families(self):
        for family in ("template", "script"):
            for side in (0, 1):
                for value in ([], {}, None, 42, True):
                    with self.subTest(family=family, side=side, value=value):
                        manifest, installed = documents(family)
                        (manifest, installed)[side]["schema"] = value
                        self.assert_blocked(manifest, installed, "schema")

    def test_size_gate_missing_fields_in_both_families(self):
        for family in ("template", "script"):
            for field in documents(family)[0]:
                with self.subTest(family=family, field=field):
                    manifest, _ = documents(family)
                    schema = manifest["schema"]
                    del manifest[field]
                    errors = check_sizes._validate_template_manifest(
                        manifest, "manifest", schema)
                    self.assertTrue(errors)
                    self.assertTrue(any(field in error for error in errors), errors)

    def test_size_gate_invalid_schema_types_in_both_families(self):
        for family in ("template", "script"):
            for value in ([], {}, None, 42, True):
                with self.subTest(family=family, value=value):
                    manifest, _ = documents(family)
                    schema = manifest["schema"]
                    manifest["schema"] = value
                    errors = check_sizes._validate_template_manifest(
                        manifest, "manifest", schema)
                    self.assertTrue(any("schema" in error for error in errors))

    def test_valid_documents_still_pass_in_both_families(self):
        for family in ("template", "script"):
            with self.subTest(family=family):
                manifest, installed = documents(family)
                code, output = self.run_comparator(manifest, installed)
                self.assertEqual(code, 0, output)
                self.assertEqual(check_sizes._validate_template_manifest(
                    manifest, "manifest", manifest["schema"]), [])


if __name__ == "__main__":
    unittest.main()
