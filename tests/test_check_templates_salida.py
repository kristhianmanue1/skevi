"""Tests de salida de check_templates.py: cadena de avisos y saneado.

Partido de tests/test_check_templates.py para contencion de tamano
(B1 del piloto ADR-043, deuda registrada del gate en 774/800).
Runner: `python3 -m unittest`.
"""

from __future__ import annotations

import importlib.util
import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent.parent / "scripts"
_SPEC = importlib.util.spec_from_file_location(
    "check_templates_salida", SCRIPTS_DIR / "check_templates.py"
)
check_templates = importlib.util.module_from_spec(_SPEC)
sys.modules["check_templates_salida"] = check_templates
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


def files_for(names):
    return {name: "sha256:" + "a" * 64 for name in names}


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
