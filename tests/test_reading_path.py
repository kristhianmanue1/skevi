"""Tests del presupuesto de ruta de lectura (ADR-021, ADR-025) y de la
identidad y autocaducidad del gate copiable (ADR-027).

Separados de `test_check_sizes.py` por vida útil y por concern: aquél ancla
límites, bloque de registro y manifiesto de plantillas; éste, dos decisiones
posteriores sobre el mismo script. La partición la forzó el propio gate al
exceder el archivo original su límite de 800 líneas (estándar §3.4).
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
from datetime import date
from pathlib import Path
from unittest.mock import patch

SCRIPTS_DIR = Path(__file__).resolve().parent.parent / "scripts"
_SPEC = importlib.util.spec_from_file_location(
    "check_sizes", SCRIPTS_DIR / "check_sizes.py"
)
check_sizes = importlib.util.module_from_spec(_SPEC)
sys.modules["check_sizes"] = check_sizes
_SPEC.loader.exec_module(check_sizes)


class GateVersionTests(unittest.TestCase):
    """Versión visible y autocaducidad (ADR-027).

    El gate es lo único que un adoptante ya ejecuta; si la señal de vejez no
    va ahí, no llega a quien no sabe que tiene un problema. Once adoptantes
    corrían copias de hace tres semanas sin manera de notarlo.
    """

    def test_version_constants_exist(self):
        self.assertRegex(check_sizes.GATE_VERSION, r"^gate/v\d+$")
        self.assertRegex(check_sizes.GATE_GENERATED_AT, r"^\d{4}-\d{2}-\d{2}$")
        self.assertIsInstance(check_sizes.GATE_STALE_AFTER_DAYS, int)

    def test_fresh_copy_reports_version_without_warning(self):
        aviso = check_sizes.gate_staleness(hoy=date(2026, 9, 10))
        self.assertIsNone(aviso)

    def test_threshold_is_ninety_days(self):
        """Anclado a un literal, no a la constante: un test que lee el umbral
        se mueve con él y sobrevive a la mutación (ronda 2026-09-08)."""
        self.assertEqual(check_sizes.GATE_STALE_AFTER_DAYS, 90)

    def test_threshold_boundary_at_literal_days(self):
        from datetime import timedelta
        gen = date.fromisoformat(check_sizes.GATE_GENERATED_AT)
        self.assertIsNone(check_sizes.gate_staleness(hoy=gen + timedelta(days=89)))
        self.assertIsNotNone(check_sizes.gate_staleness(hoy=gen + timedelta(days=90)))

    def test_non_string_generated_at_does_not_raise(self):
        """«mal editado al copiar devuelve None en vez de fallar» incluye
        que alguien borre las comillas y deje un número."""
        original = check_sizes.GATE_GENERATED_AT
        try:
            check_sizes.GATE_GENERATED_AT = 20260908
            self.assertIsNone(check_sizes.gate_staleness(hoy=date(2027, 1, 1)))
        finally:
            check_sizes.GATE_GENERATED_AT = original

    def test_stale_copy_warns_with_its_age(self):
        aviso = check_sizes.gate_staleness(hoy=date(2027, 1, 1))
        self.assertIsNotNone(aviso)
        self.assertIn("115 días", aviso)
        self.assertIn(check_sizes.GATE_VERSION, aviso)

    def test_warning_never_claims_a_newer_version_exists(self):
        """El gate no observa a nadie: sabe que es viejo, no que haya otro."""
        aviso = check_sizes.gate_staleness(hoy=date(2027, 1, 1))
        for palabra in ("nueva versión", "actualiza", "disponible"):
            self.assertNotIn(palabra, aviso.lower())

    def test_clock_before_generation_does_not_warn(self):
        self.assertIsNone(check_sizes.gate_staleness(hoy=date(2020, 1, 1)))


class ReadingPathTests(unittest.TestCase):
    """`reading_path` — presupuesto de la ruta de lectura obligatoria.

    §3.4 acota cada archivo por separado; nada acotaba el camino completo
    que un ejecutor debe leer antes de actuar. Procedencia: ADR-021.
    """

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self._orig_root = check_sizes.ROOT
        check_sizes.ROOT = self.root
        self._orig_reading_path = dict(check_sizes.READING_PATH)
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
                p.name: "sha256:" + hashlib.sha256(p.read_bytes()).hexdigest()
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
        check_sizes.READING_PATH.clear()
        check_sizes.READING_PATH.update(self._orig_reading_path)

    def _write_config(self, data):
        (self.root / check_sizes.CONFIG_NAME).write_text(
            json.dumps(data), encoding="utf-8"
        )

    def _write_lines(self, relative, count):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("\n".join(f"l{i}" for i in range(count)) + "\n",
                        encoding="utf-8")

    def _run_main(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            exit_code = check_sizes.main()
        return exit_code, buf.getvalue()

    def test_absent_key_checks_nothing(self):
        """Fail-closed como `plans` (ADR-006): sin clave, gate inactivo."""
        self._write_lines("docs/uno.md", 500)
        self._write_lines("docs/dos.md", 500)
        exit_code, output = self._run_main()
        self.assertEqual(exit_code, 0)
        self.assertNotIn("ruta de lectura", output)

    def test_sum_over_limit_fails(self):
        self._write_lines("docs/uno.md", 400)
        self._write_lines("docs/dos.md", 201)
        self._write_config(
            {"reading_path": {"limit": 600,
                              "files": ["docs/uno.md", "docs/dos.md"]}}
        )
        exit_code, output = self._run_main()
        self.assertEqual(exit_code, 1)
        self.assertIn("ruta de lectura obligatoria: 601 líneas > límite 600",
                      output)

    def test_ok_line_reports_the_occupancy(self):
        """La norma delega la cifra vigente al gate; el gate debe emitirla
        también cuando pasa, o el trinquete no es auditable sin un script
        ad-hoc (hallazgo de la ronda fresca del 2026-09-08)."""
        self._write_lines("docs/uno.md", 400)
        self._write_config(
            {"reading_path": {"limit": 600, "files": ["docs/uno.md"]}}
        )
        exit_code, output = self._run_main()
        self.assertEqual(exit_code, 0, output)
        self.assertIn("ruta de lectura 400/600", output)

    def test_ok_line_omits_occupancy_when_inactive(self):
        exit_code, output = self._run_main()
        self.assertEqual(exit_code, 0)
        self.assertNotIn("ruta de lectura", output)

    def test_sum_at_limit_passes(self):
        self._write_lines("docs/uno.md", 400)
        self._write_lines("docs/dos.md", 200)
        self._write_config(
            {"reading_path": {"limit": 600,
                              "files": ["docs/uno.md", "docs/dos.md"]}}
        )
        exit_code, output = self._run_main()
        self.assertEqual(exit_code, 0)

    def test_missing_file_in_path_fails(self):
        """Una ruta que no existe no acredita tamaño cero (ADR-007)."""
        self._write_config(
            {"reading_path": {"limit": 600, "files": ["docs/ausente.md"]}}
        )
        exit_code, output = self._run_main()
        self.assertEqual(exit_code, 1)
        self.assertIn("docs/ausente.md", output)
        self.assertNotIn("Traceback", output)

    def test_invalid_type_is_config_error(self):
        """Un typo no puede apagar el gate: mismo criterio que `plans`."""
        self._write_config({"reading_path": ["docs/uno.md"]})
        exit_code, output = self._run_main()
        self.assertEqual(exit_code, 1)
        self.assertTrue(output.startswith("BLOQ"))
        self.assertIn("reading_path", output)

    def test_limit_must_be_integer(self):
        self._write_config(
            {"reading_path": {"limit": "600", "files": ["docs/uno.md"]}}
        )
        exit_code, output = self._run_main()
        self.assertEqual(exit_code, 1)
        self.assertIn("reading_path", output)

    def test_path_escaping_root_is_rejected(self):
        self._write_config(
            {"reading_path": {"limit": 600, "files": ["../fuera.md"]}}
        )
        exit_code, output = self._run_main()
        self.assertEqual(exit_code, 1)
        self.assertTrue(output.startswith("BLOQ"))
        self.assertNotIn(str(self.root), output)

    def test_unreadable_file_does_not_credit_size(self):
        """Igual que count_text_lines: lectura fallida ≠ verificado.

        Se parchea **sólo** la lectura del archivo objetivo. Parchear
        Path.read_text entero rompía antes load_config, el test pasaba por
        el diagnóstico de configuración y la rama OSError de la ruta de
        lectura no llegaba a ejecutarse (hallazgo de la ronda fresca del
        2026-09-08)."""
        self._write_lines("docs/uno.md", 10)
        self._write_config(
            {"reading_path": {"limit": 600, "files": ["docs/uno.md"]}}
        )
        original = Path.read_text

        def falla_sólo_el_objetivo(self_path, *args, **kwargs):
            if self_path.name == "uno.md":
                raise OSError("payload")
            return original(self_path, *args, **kwargs)

        with patch.object(Path, "read_text", falla_sólo_el_objetivo):
            exit_code, output = self._run_main()
        self.assertEqual(exit_code, 1)
        self.assertIn("ruta de lectura obligatoria: no se pudo leer", output)
        self.assertIn("docs/uno.md", output)
        self.assertNotIn("payload", output)
        self.assertNotIn("Traceback", output)

    def test_worst_case_counts_only_the_largest(self):
        """La espina se lee siempre; de las fases, sólo una por sesión.
        Sumarlas todas mediría un camino que nadie recorre."""
        self._write_lines("docs/espina.md", 100)
        self._write_lines("docs/fase-corta.md", 50)
        self._write_lines("docs/fase-larga.md", 90)
        self._write_config({"reading_path": {
            "limit": 190,
            "files": ["docs/espina.md"],
            "worst_case_of": ["docs/fase-corta.md", "docs/fase-larga.md"],
        }})
        exit_code, output = self._run_main()
        self.assertEqual(exit_code, 0, output)

    def test_worst_case_over_limit_fails(self):
        self._write_lines("docs/espina.md", 100)
        self._write_lines("docs/fase-corta.md", 50)
        self._write_lines("docs/fase-larga.md", 91)
        self._write_config({"reading_path": {
            "limit": 190,
            "files": ["docs/espina.md"],
            "worst_case_of": ["docs/fase-corta.md", "docs/fase-larga.md"],
        }})
        exit_code, output = self._run_main()
        self.assertEqual(exit_code, 1)
        self.assertIn("191 líneas > límite 190", output)

    def test_worst_case_missing_file_fails(self):
        self._write_lines("docs/espina.md", 10)
        self._write_config({"reading_path": {
            "limit": 190,
            "files": ["docs/espina.md"],
            "worst_case_of": ["docs/ausente.md"],
        }})
        exit_code, output = self._run_main()
        self.assertEqual(exit_code, 1)
        self.assertIn("docs/ausente.md", output)

    def test_worst_case_is_optional(self):
        self._write_lines("docs/espina.md", 10)
        self._write_config({"reading_path": {
            "limit": 190, "files": ["docs/espina.md"]}})
        exit_code, output = self._run_main()
        self.assertEqual(exit_code, 0, output)

if __name__ == "__main__":
    unittest.main()
