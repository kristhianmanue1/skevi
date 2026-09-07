# Registro — Primer incremento del plan de mejoras

Plan: [AUDIT-2026-09-07](../plans/2026-09-07-mejoras-auditoria.md).
Contrato: [SPEC-AUDIT](../specs/SPEC-AUDIT-2026-09-07-mejoras.md).

## Capa técnica

```text
id = SKV-IMPL-20260907-01
date = 2026-09-07
time_utc = 18:35:11Z
head_sha = 17413f150d08e1e65b72f70a858104505950e751
model = GPT-6 (self-declared)
STATE = OK (T00-T04 only)
GATE = T00-T04 verified; fresh code and final artifact reviews returned proceed.
EVIDENCE
- Git -> branch fix/audit-gate-read-errors; HEAD unchanged; no commit or publication -> pass
- AN-KLA virtualenv preflight -> context and integrity OK at revision 19; no memory writes -> pass
- RED focal suite before production fix -> 45 tests, 3 failures and 1 error for expected defects -> pass
- GREEN focal suite -> 45 tests OK -> pass
- Full suite -> 68 tests OK, including 62 preexisting tests -> pass
- Real gate after code fix -> two unexempted Finder binaries blocked; exact local exemptions documented -> pass
- file and git check-ignore -> .DS_Store and docs/.DS_Store are ignored Apple Desktop Services Store files -> pass
- Final artifact gates -> 73 text files and 2 plans OK; plan 282 lines; relative links and report hash verified -> pass
- Fresh reviewer -> no BLOCKER/HIGH; second-read UTF-8 and subsequent read error both block without payload -> pass
- MED-01 -> preexisting load_config handler can expose exception payload; deferred to T14 outside traversal scope -> fail
- PROP-008 digest -> f4a478fab5ad6bc0187a358fa8aeb7c87281af448f20f02169c15683dd95b721 unchanged -> pass
PENDING = T14 and P2-P5 remain unexecuted. No universal CLI sanitization or snapshot guarantee.
DECISION = proceed (T00-T04 only)
report_sha256 = 7bf7aedddc5f224c5eba512d77d01d1e01d73c469739432caaa529b7d9fbfe0b
```

Hash: UTF-8, LF, sin newline final, excluida la línea report_sha256.
El hash cubre únicamente la capa técnica; no acredita autorización.
La hora identifica esta emisión del reporte, no cada comando registrado.

## Capa humana

T00-T04 verificados. El arreglo y este registro obtuvieron proceed en revisión
fresca. El programa completo continúa abierto; siguiente tarea: T14.
El gate ya bloquea los errores de lectura y UTF-8 en archivos descubiertos,
incluida la segunda lectura del registro; conserva las exenciones explícitas.
No se afirma saneamiento de toda la CLI ni consistencia de snapshot.

## Evidencia reproducible

Comandos ejecutados desde la raíz, con Python 3.9.6 para la verificación local:

```bash
python3 -B -m unittest discover -s tests -p test_check_sizes.py
python3 -B -m unittest discover -s tests
python3 -B scripts/check_sizes.py
python3 -B scripts/check_plans.py
git diff --check
git status --short
shasum -a 256 docs/proposals/PROP-008-integracion-ankla-por-contrato.md
```

RED anterior al arreglo: `Ran 45 tests`, `FAILED (failures=3, errors=1)`.
Los tres fallos fueron salida 0 en vez de 1 para README ilegible, Markdown no
canónico ilegible y UTF-8 inválido. El error fue PermissionError propagado en
la segunda lectura de AGENTS. Son reproducciones en fixtures/mocks, no daños
en los documentos reales. GREEN: 45 focales OK; suite completa: 68 OK.
Los seis tests nuevos incluyen dos controles de exención sin intento de lectura.

Primer gate real tras GREEN: BLOQ por .DS_Store y docs/.DS_Store. `file` los
identificó como Apple Desktop Services Store; `git check-ignore -v` confirmó
.gitignore:1 y `git ls-files` no los listó. Se declararon sólo esas dos rutas
en exempt_paths. Gate posterior: 72 archivos OK; planes: 2 OK, antes de añadir
este registro. Verificación final: 73 archivos y 2 planes OK; plan de 282 líneas.

## Ronda adversarial y riesgos residuales

Revisor: sesión fresca `/root/review_gate_increment`, sin atribuir independencia
de modelo. Folio de revisión: SKV-AUDIT-20260907-REVIEW-01. Revisó diff real,
SPEC y plan; repitió suite/gates, verificó el hash de PROP-008 y atacó la
segunda lectura con UTF-8 inválido seguida de otro archivo con OSError.
Resultado: ambos fallos se agregan como BLOQ/1 sin payload; cero HIGH/BLOCKER.
Segunda revisión: SKV-AUDIT-20260907-REVIEW-02, proceed sobre SPEC, plan y
registro final. Comprobó 45 focales, gates, enlaces y hash; el RED es evidencia
histórica del ejecutor, no reproducción independiente del revisor.

MED-01: el manejador preexistente de load_config imprime excepción cruda.
Mock observado por el revisor: PermissionError con payload → BLOQ/1 con
payload visible. Corrección aplicada: ninguna en este incremento. Estado:
abierto, seguimiento T14 antes de P2. Razón de diferimiento: ocurre antes del
recorrido, fuera de SPEC-AUD-01; el arreglo no lo introduce ni empeora.
Este registro no constituye aceptación humana del riesgo ni saneamiento global.

PROP-008 preexistente quedó intacta, con el digest de la capa técnica.
Sin cambios de memoria, dependencias, hooks, GitHub, commit, push ni release.
La siguiente tarea es T14; las demás fases conservan sus decisiones de entrada.
