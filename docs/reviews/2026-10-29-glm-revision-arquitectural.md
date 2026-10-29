# Revisión arquitectural — ADR-044, ADR-045 y E6 (familia distinta)

Veredicto: **proceed** para el diseño vigente, con dos hallazgos MED
abiertos como seguimiento y cuatro LOW. Objeto:
[ADR-044](../adr/ADR-044-push-merge-condicional.md),
[ADR-045](../adr/ADR-045-regla-e6-lote-en-plan.md), la implementación de
E6 en `scripts/check_plans.py` y la coherencia con `04` §7 y `AGENTS.md`,
todos en `main` `262f2a9` (merge del PR #81).

Revisó una sesión fresca de la familia GLM, sin contexto previo del
trabajo; el corpus revisado es autoría de Claude Opus (sesiones del
2026-10-28/29). Contexto separado real, filesystem compartido, sin acceso
a la conversación original. Cumple el requisito de «otra familia» de la
recomendación 4 del análisis crítico.

## Hallazgos

- [MED] M1 — `OPERACION_RE` carece de frontera final
  (`\b(?:push|merge)` sin `\b` de cierre): «sin pushes» o «ya merged» en
  `Permitido:` activan E6 — repro ejecutado — y no hay tests de flexiones
  (búsqueda sin coincidencias). ADR-045 declara el falso positivo por
  negación pero no esta clase. Impacto: BLOQ espurio que invita a un
  folio de relleno, degradando la señal del campo. Corrección sugerida:
  frontera final más tests, o declarar el límite. Cambiar el gate es
  normativo (gate/v13 con ADR propio): **abierto como seguimiento**.
- [MED] M2 — E6 sólo ancla en `Permitido:`: un `DoD:` o un step que
  nombre push/merge no pide `Lote:`. La regla lo declara («sólo lee el
  campo `Permitido:`») pero el caso concreto no figura entre los límites.
  Impacto bajo: la operación real sigue exigiendo dossier y aceptación en
  §7; E6 es recordatorio, no frontera. **Abierto como seguimiento
  documental.**
- [LOW] L1 — un folio con forma de ruta con dígito (`docs/plan-v2`)
  pasa: declarado en el ADR y verificado. Sin acción.
- [LOW] L2 — un folio entre backticks falla: declarado y verificado.
  Sin acción.
- [LOW] L3 — un `Lote:` en la continuación de un step a la misma sangría
  que un `Permitido:` anidado contaría como válido: constructo irreal con
  las TAREA al nivel 0. Sin acción.
- [LOW] L4 — el formato de folio sólo lo fija E6 en planes: un dossier
  fuera de plan podría nombrar un folio que E6 rechazaría. Coherencia de
  forma entre artefactos: seguimiento.

## Coherencia verificada

E6 verifica la **forma** y no la aceptación, coherente con ADR-044 (a)/(b)
y con la imposibilidad de que un gate editable por el ejecutor acredite
autoridad. La excepción a REQ-2 de ADR-014 queda acotada por tres cierres
(campo único, límite de palabra inicial, exigencia de falta estructural).
`_permitido` (unión de repeticiones a mínima sangría, corrección de la
ronda del #81) y `_agrupar_steps`/E4 se revisaron sin defectos nuevos. El
lote previo al primer efecto de `04` §7 coincide con ADR-044 y con el
dossier vigente de los lotes 02-03.

## Verificaciones

Ver la capa técnica. La evidencia es de comandos, no de lectura, salvo la
revisión línea a línea de los helpers, que se declara como lectura.

## Capa técnica

```text
id = SKV-GLM-REV-ARCH-20261029-01
date = 2026-10-29
time_utc = 15:12:53Z
head_sha = 262f2a951945b70c20a80b7211a2ae82c9da6bfc
model = GLM 5.3 Flash (self-declared; not proof)
STATE = OK
GATE = Independent review of ADR-044/ADR-045/E6 at 262f2a9; no HIGH/BLOCKER.
EVIDENCE
- python3 scripts/check_plans.py -> OK; 8 planes; E1-E6 -> pass
- python3 scripts/check_sizes.py -> OK; reading path 1620/1620 -> pass
- regex repro OPERACION_RE -> «sin pushes»/«ya merged» trigger E6 -> pass
- regex repro control -> «emergencia» does not trigger E6 -> pass
- rg flexions in tests -> 0 results; inflection class untested -> pass
- FOLIO_RE repro -> path-like folio passes; backticked folio fails -> pass
- read of _permitido/_agrupar_steps/_fallo_lote -> no new defects -> pass
PENDING = M1: trailing boundary plus tests or declared limit (gate/v13);
M2: documentary note; Operator decides the follow-up vehicle.
DECISION = proceed
OPERATIONS = read-only review; grants no permission.
AUTHORITY = Operator «adelante con recomendaciones procede»;
different-family review was recommendation 4 of the critical analysis.
RISK = reviewer of another family than the author (GLM vs Claude Opus);
M1/M2 remain open as declared follow-ups.
report_sha256 = 80ff29f68d732e69acf0af7294b4c20b2ebee905aa68e502c7de7253e05b7be9
```
