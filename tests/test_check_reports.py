"""Tests para scripts/check_reports.py. Runner: `python3 -m unittest`.

Ancla el CONTRATO skevi/check-reports v1 (ADR-022): forma de la capa
técnica de ADR-016, nunca honestidad de su contenido.
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

SCRIPTS_DIR = Path(__file__).resolve().parent.parent / "scripts"
_SPEC = importlib.util.spec_from_file_location(
    "check_reports", SCRIPTS_DIR / "check_reports.py"
)
check_reports = importlib.util.module_from_spec(_SPEC)
sys.modules["check_reports"] = check_reports
_SPEC.loader.exec_module(check_reports)


BASE = {
    "id": "SKV-T00-20260907-01",
    "date": "2026-09-07",
    "time_utc": "19:06:21Z",
    "head_sha": "41d40d9a4e1a521e97810b4124e19e7e8431547f",
    "model": "Modelo (self-declared)",
    "STATE": "OK (alcance local)",
    "GATE": "Gates locales en verde.",
}
EVIDENCE = ["- python3 scripts/check_sizes.py -> OK -> pass"]
TAIL = {"PENDING": "ninguno"}


def render(claves=None, evidencia=None, cola=None, hash_valido=True,
           con_fence=True):
    """Construye un reporte de dos capas con hash canónico correcto."""
    claves = {**BASE, **(claves or {})}
    cola = {**TAIL, **(cola or {})}
    lineas = [f"{k} = {v}" for k, v in claves.items()]
    lineas.append("EVIDENCE")
    lineas.extend(EVIDENCE if evidencia is None else evidencia)
    lineas.extend(f"{k} = {v}" for k, v in cola.items())
    canon = "\n".join(lineas)
    digest = hashlib.sha256(canon.encode("utf-8")).hexdigest()
    if not hash_valido:
        digest = "0" * 64
    lineas.append(f"report_sha256 = {digest}")
    cuerpo = "\n".join(lineas)
    if not con_fence:
        return f"# Registro\n\n{cuerpo}\n"
    return f"# Registro\n\n## Capa tecnica\n\n```text\n{cuerpo}\n```\n\nCapa humana.\n"


class ContractShapeTests(unittest.TestCase):
    """Cada campo del CONTRATO existe en la firma real (04 §9)."""

    def test_public_names_exist(self):
        for nombre in ("CONFIG_NAME", "CONFIG_KEY", "REQUIRED_KEYS",
                       "OPTIONAL_KEYS", "MARKS", "STATES", "DECISIONS",
                       "comprobar_reporte", "reportes_declarados", "main"):
            self.assertTrue(hasattr(check_reports, nombre), nombre)

    def test_marks_are_the_three_of_adr_005(self):
        self.assertEqual(check_reports.MARKS, {"pass", "fail", "inconclusive"})

    def test_states_are_english_technical_layer(self):
        self.assertEqual(check_reports.STATES, {"OK", "PARTIAL", "BLOCKED"})


class ReportShapeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)

    def _check(self, texto):
        return check_reports.comprobar_reporte("r.md", texto)

    def test_valid_report_passes(self):
        self.assertEqual(self._check(render()), [])

    def test_missing_technical_layer_fails(self):
        fallos = self._check(render(con_fence=False))
        self.assertTrue(any("capa técnica" in f for f in fallos), fallos)

    def test_missing_required_key_fails(self):
        texto = render().replace("head_sha = 41d40d9a4e1a521e97810b4124e19e7e8431547f\n", "")
        fallos = self._check(texto)
        self.assertTrue(any("head_sha" in f for f in fallos), fallos)

    def test_unknown_key_fails(self):
        """Polaridad cerrada: una clave inventada no se ignora."""
        fallos = self._check(render(cola={"INVENTADA": "x"}))
        self.assertTrue(any("INVENTADA" in f for f in fallos), fallos)

    def test_optional_keys_are_accepted(self):
        self.assertEqual(
            self._check(render(cola={
                "DECISION": "proceed (alcance local)",
                "OPERATIONS": "commit",
                "AUTHORITY": "humano",
                "RISK": "ninguno",
            }, claves={"session": "s-1"})),
            [],
        )

    def test_bad_state_fails(self):
        fallos = self._check(render(claves={"STATE": "CASI (algo)"}))
        self.assertTrue(any("STATE" in f for f in fallos), fallos)

    def test_spanish_state_fails(self):
        """La capa técnica es inglés autoritativo (ADR-016)."""
        fallos = self._check(render(claves={"STATE": "BLOQ"}))
        self.assertTrue(any("STATE" in f for f in fallos), fallos)

    def test_bad_decision_fails(self):
        fallos = self._check(render(cola={"DECISION": "ya está bien"}))
        self.assertTrue(any("DECISION" in f for f in fallos), fallos)

    def test_evidence_section_required(self):
        texto = render().replace("EVIDENCE\n", "")
        fallos = self._check(texto)
        self.assertTrue(any("EVIDENCE" in f for f in fallos), fallos)

    def test_evidence_needs_at_least_one_line(self):
        fallos = self._check(render(evidencia=[]))
        self.assertTrue(any("EVIDENCE" in f for f in fallos), fallos)

    def test_evidence_line_without_arrow_fails(self):
        fallos = self._check(render(evidencia=["- corrí los gates y pasaron"]))
        self.assertTrue(any("->" in f for f in fallos), fallos)

    def test_invalid_single_word_mark_fails(self):
        """`addressed` ocupa el lugar de la marca sin ser una de las tres."""
        fallos = self._check(render(evidencia=["- algo -> resultado -> addressed"]))
        self.assertTrue(any("addressed" in f for f in fallos), fallos)

    def test_typo_in_mark_fails(self):
        fallos = self._check(render(evidencia=["- algo -> resultado -> passed"]))
        self.assertTrue(any("passed" in f for f in fallos), fallos)

    def test_unmarked_line_is_accepted_during_transition(self):
        """ADR-005: el validador acepta la línea con marca y sin ella."""
        self.assertEqual(
            self._check(render(evidencia=[
                "- algo -> resultado observado en varias palabras"])),
            [],
        )

    def test_bad_head_sha_fails(self):
        fallos = self._check(render(claves={"head_sha": "41d40d9"}))
        self.assertTrue(any("head_sha" in f for f in fallos), fallos)

    def test_bad_date_fails(self):
        fallos = self._check(render(claves={"date": "07-09-2026"}))
        self.assertTrue(any("date" in f for f in fallos), fallos)

    def test_bad_time_fails(self):
        fallos = self._check(render(claves={"time_utc": "19:06:21"}))
        self.assertTrue(any("time_utc" in f for f in fallos), fallos)

    def test_irreproducible_hash_fails(self):
        fallos = self._check(render(hash_valido=False))
        self.assertTrue(any("report_sha256" in f for f in fallos), fallos)

    def test_hash_is_canonical_form(self):
        """UTF-8, LF, sin newline final, excluida la línea del hash."""
        self.assertEqual(self._check(render()), [])


class MultipleLayersTests(unittest.TestCase):
    """Un archivo puede llevar más de una capa técnica (registro de dos
    emisiones). Validar sólo la primera dejaría la segunda sin gate."""

    def _check(self, texto):
        return check_reports.comprobar_reporte("r.md", texto)

    def test_second_layer_is_also_validated(self):
        bueno = render()
        malo = render(claves={"STATE": "PARCIAL"})
        combinado = bueno + "\n## Segunda emision\n\n" + malo
        fallos = self._check(combinado)
        self.assertTrue(any("STATE" in f for f in fallos), fallos)

    def test_two_valid_layers_pass(self):
        combinado = render() + "\n## Segunda emision\n\n" + render(
            claves={"id": "SKV-T00-20260907-02"})
        self.assertEqual(self._check(combinado), [])

    def test_fence_without_technical_layer_is_ignored(self):
        """Un fence ```text de salida de comando no es una capa técnica."""
        extra = "\n```text\nOK - 99 archivos dentro de limites\n```\n"
        self.assertEqual(self._check(render() + extra), [])


class ConfigTests(unittest.TestCase):
    """Fail-closed por configuración, con el patrón de `plans` (ADR-006)."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "docs" / "reviews").mkdir(parents=True)
        (self.root / "docs" / "reviews" / "r.md").write_text(
            render(), encoding="utf-8")

    def _config(self, data):
        (self.root / check_reports.CONFIG_NAME).write_text(
            json.dumps(data), encoding="utf-8")

    def _run(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = check_reports.main(["--root", str(self.root)])
        return code, buf.getvalue()

    def test_absent_key_checks_nothing(self):
        self._config({"plans": "docs/plans"})
        code, output = self._run()
        self.assertEqual(code, 0)
        self.assertIn("inactivo", output)

    def test_declared_directory_is_checked(self):
        self._config({"reports": {"dir": "docs/reviews"}})
        code, output = self._run()
        self.assertEqual(code, 0, output)
        self.assertIn("1", output)

    def test_invalid_type_is_error(self):
        self._config({"reports": "docs/reviews"})
        code, output = self._run()
        self.assertEqual(code, 1)
        self.assertTrue(output.startswith("BLOQ"))

    def test_missing_directory_is_error(self):
        self._config({"reports": {"dir": "docs/ausente"}})
        code, output = self._run()
        self.assertEqual(code, 1)

    def test_broken_report_fails_the_gate(self):
        (self.root / "docs" / "reviews" / "malo.md").write_text(
            render(hash_valido=False), encoding="utf-8")
        self._config({"reports": {"dir": "docs/reviews"}})
        code, output = self._run()
        self.assertEqual(code, 1)
        self.assertIn("malo.md", output)

    def test_exempt_report_is_skipped_but_counted(self):
        (self.root / "docs" / "reviews" / "viejo.md").write_text(
            render(hash_valido=False), encoding="utf-8")
        self._config({"reports": {"dir": "docs/reviews",
                                  "exempt": ["docs/reviews/viejo.md"]}})
        code, output = self._run()
        self.assertEqual(code, 0, output)
        self.assertIn("exent", output.lower())

    def test_file_without_technical_layer_is_ignored(self):
        """docs/reviews/ también aloja prosa; sólo se validan los que
        declaran capa técnica. Un archivo sin fence no es un reporte roto."""
        (self.root / "docs" / "reviews" / "prosa.md").write_text(
            "# Notas\n\nSin capa tecnica.\n", encoding="utf-8")
        self._config({"reports": {"dir": "docs/reviews"}})
        code, output = self._run()
        self.assertEqual(code, 0, output)

    def test_unreadable_report_does_not_pass_silently(self):
        (self.root / "docs" / "reviews" / "bin.md").write_bytes(b"\xff\xfe")
        self._config({"reports": {"dir": "docs/reviews"}})
        code, output = self._run()
        self.assertEqual(code, 1)
        self.assertNotIn("Traceback", output)


class LayerSelectionTests(unittest.TestCase):
    """Qué archivo lleva capa técnica y cuál no. Hallazgos de la ronda fresca
    del 2026-09-08: el filtro de main() anclaba en el fence y comprobar_reporte
    en `report_sha256`, y esa asimetría producía a la vez un fail-open y un
    falso positivo."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "docs" / "reviews").mkdir(parents=True)

    def _config(self, data):
        (self.root / check_reports.CONFIG_NAME).write_text(
            json.dumps(data), encoding="utf-8")

    def _run(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = check_reports.main(["--root", str(self.root)])
        return code, buf.getvalue()

    def test_technical_layer_in_plain_fence_is_not_skipped(self):
        """Fail-open: una capa con report_sha256 en un fence sin `text`
        no puede colarse sin comprobación."""
        (self.root / "docs" / "reviews" / "plain.md").write_text(
            "# r\n\n```\nSTATE = INVENTADO\ndate = 9999-99-99\n"
            "report_sha256 = " + "0" * 64 + "\n```\n", encoding="utf-8")
        self._config({"reports": {"dir": "docs/reviews"}})
        code, output = self._run()
        self.assertEqual(code, 1, output)

    def test_command_output_fence_is_not_a_missing_layer(self):
        """Falso positivo: capa humana sola es válida (00-INDICE, tarea
        trivial); un fence ```text de salida de comando no la convierte en
        un reporte roto."""
        (self.root / "docs" / "reviews" / "trivial.md").write_text(
            "# trivial\n\nCapa humana sola.\n\n```text\nOK - 107 archivos\n```\n",
            encoding="utf-8")
        self._config({"reports": {"dir": "docs/reviews"}})
        code, output = self._run()
        self.assertEqual(code, 0, output)

    def test_lone_command_fence_reported_only_on_direct_call(self):
        """main() ignora el archivo (test anterior); la llamada directa sí
        declara que no hay capa. Las dos conductas son distintas a propósito:
        el filtro vive en main(), el diagnóstico en comprobar_reporte."""
        fallos = check_reports.comprobar_reporte(
            "x.md", "# n\n\n```text\nOK - salida\n```\n")
        self.assertTrue(any("capa técnica" in f for f in fallos), fallos)


class ConfigPathBoundaryTests(unittest.TestCase):
    """`reports.dir` es entrada no confiable: se valida como ruta relativa
    contenida en la raíz, igual que `_safe_relative_paths` en check_sizes."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "docs" / "reviews").mkdir(parents=True)
        (self.root / "fuera.md").write_text(render(), encoding="utf-8")

    def _run(self, dir_valor):
        (self.root / check_reports.CONFIG_NAME).write_text(
            json.dumps({"reports": {"dir": dir_valor}}), encoding="utf-8")
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = check_reports.main(["--root", str(self.root)])
        return code, buf.getvalue()

    def test_absolute_dir_is_config_error_not_traceback(self):
        code, output = self._run("/etc")
        self.assertEqual(code, 1)
        self.assertTrue(output.startswith("BLOQ"))
        self.assertNotIn("Traceback", output)
        self.assertNotIn("/etc", output)

    def test_dir_escaping_root_is_rejected(self):
        code, output = self._run("..")
        self.assertEqual(code, 1)
        self.assertTrue(output.startswith("BLOQ"))
        self.assertNotIn("fuera.md", output)

    def test_home_dir_is_rejected(self):
        code, output = self._run("~/docs")
        self.assertEqual(code, 1)
        self.assertTrue(output.startswith("BLOQ"))


class CanonicalHashTests(unittest.TestCase):
    """La forma canónica de ADR-016 se prueba rompiéndola, no repitiendo
    el caso feliz (hallazgo de la ronda fresca del 2026-09-08)."""

    def _capa(self, hash_de):
        cuerpo = "\n".join(
            [f"{k} = {v}" for k, v in BASE.items()] + ["EVIDENCE"]
            + EVIDENCE + [f"{k} = {v}" for k, v in TAIL.items()])
        digest = hashlib.sha256(hash_de(cuerpo).encode("utf-8")).hexdigest()
        return f"# r\n\n```text\n{cuerpo}\nreport_sha256 = {digest}\n```\n"

    def test_trailing_newline_breaks_reproduction(self):
        fallos = check_reports.comprobar_reporte(
            "r.md", self._capa(lambda c: c + "\n"))
        self.assertTrue(any("report_sha256" in f for f in fallos), fallos)

    def test_crlf_breaks_reproduction(self):
        fallos = check_reports.comprobar_reporte(
            "r.md", self._capa(lambda c: c.replace("\n", "\r\n")))
        self.assertTrue(any("report_sha256" in f for f in fallos), fallos)

    def test_including_own_line_breaks_reproduction(self):
        fallos = check_reports.comprobar_reporte(
            "r.md", self._capa(lambda c: c + "\nreport_sha256 = x"))
        self.assertTrue(any("report_sha256" in f for f in fallos), fallos)

    def test_exact_canonical_form_reproduces(self):
        self.assertEqual(
            check_reports.comprobar_reporte("r.md", self._capa(lambda c: c)), [])


class DuplicateKeyTests(unittest.TestCase):
    def test_duplicate_key_is_a_failure(self):
        """`STATE = BLOCKED` seguido de `STATE = OK` no puede pasar: la
        última ganaba en silencio."""
        texto = render().replace("GATE = ", "STATE = BLOCKED\nGATE = ")
        fallos = check_reports.comprobar_reporte("r.md", texto)
        self.assertTrue(any("duplicada" in f for f in fallos), fallos)

    def test_prefixed_key_is_not_confused_with_the_hash(self):
        """El hash se excluye por clave exacta, no por prefijo."""
        self.assertTrue(any(
            "report_sha256_prev" in f
            for f in check_reports.comprobar_reporte(
                "r.md", render(cola={"report_sha256_prev": "x"}))))


class CliBoundaryTests(unittest.TestCase):
    """La frontera de argumentos también falla controlado (ADR-007).

    Hallazgos de la ronda adversarial del 2026-09-07 sobre este mismo
    script: F-1 traceback con `--root` sin valor; F-2 raíz inexistente
    reportada como «inactivo», es decir fail-open.
    """

    def _run(self, argv):
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = check_reports.main(argv)
        return code, buf.getvalue()

    def test_root_without_value_fails_controlled(self):
        code, output = self._run(["--root"])
        self.assertEqual(code, 1)
        self.assertTrue(output.startswith("BLOQ"))
        self.assertNotIn("Traceback", output)

    def test_missing_root_directory_is_blocked_not_inactive(self):
        code, output = self._run(["--root", "/tmp/skevi-no-existe-xyz"])
        self.assertEqual(code, 1)
        self.assertNotIn("inactivo", output)

    def test_unknown_argument_fails_controlled(self):
        code, output = self._run(["--verbose"])
        self.assertEqual(code, 1)
        self.assertTrue(output.startswith("BLOQ"))


class SymlinkTests(unittest.TestCase):
    """check_sizes ya rechaza symlinks en su listado; check_reports y
    check_plans hacían glob sin ese filtro y leían fuera de la raíz,
    emitiendo cadenas tomadas del contenido ajeno (ronda fresca 2026-09-08)."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "docs" / "reviews").mkdir(parents=True)
        self.fuera = self.root.parent / f"fuera-{self.root.name}.md"
        self.fuera.write_text("SECRETO-FUERA-DE-LA-RAIZ\n", encoding="utf-8")
        self.addCleanup(self.fuera.unlink)
        (self.root / check_reports.CONFIG_NAME).write_text(
            json.dumps({"reports": {"dir": "docs/reviews"}}), encoding="utf-8")

    def test_symlink_escaping_root_is_not_read(self):
        (self.root / "docs" / "reviews" / "enlace.md").symlink_to(self.fuera)
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = check_reports.main(["--root", str(self.root)])
        salida = buf.getvalue()
        self.assertNotIn("SECRETO-FUERA-DE-LA-RAIZ", salida)
        self.assertEqual(code, 0, salida)

class SharedConfigKeyTests(unittest.TestCase):
    """La config es una sola, de polaridad cerrada compartida (ADR-006).

    Copiar check_reports.py sin actualizar check_sizes.py deja un gate que
    rechaza la clave `reports` como desconocida: se ancla aquí para que el
    error de instalación se vea en la suite y no en el repo del adoptante.
    """

    def _cargar(self, nombre):
        spec = importlib.util.spec_from_file_location(
            nombre, SCRIPTS_DIR / f"{nombre}.py")
        modulo = importlib.util.module_from_spec(spec)
        sys.modules[nombre] = modulo
        spec.loader.exec_module(modulo)
        return modulo

    def test_check_sizes_accepts_the_reports_key(self):
        self.assertIn(check_reports.CONFIG_KEY,
                      self._cargar("check_sizes").CONFIG_KEYS)

    def test_check_plans_fallback_accepts_it_too(self):
        check_plans = self._cargar("check_plans")
        self.assertIn(check_reports.CONFIG_KEY, check_plans._claves_validas())


if __name__ == "__main__":
    unittest.main()
