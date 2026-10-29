# Dossier de lote — SKV-LOTE-20261029-01 (PLAN LG)

Propuesta al gate humano **antes** del primer efecto Git de
[PLAN LG](../plans/2026-10-29-lote-git.md). Primer uso del campo `Lote:`
de la plantilla de plan (plantillas/v16). Este archivo no es aceptación:
la aceptación del Operador se transcribe abajo, con hora, sólo cuando
exista, y también en la descripción de cada PR.

## Operaciones enumeradas

PR A — rama `docs/lote-git-y-deuda-pr79` → `main` (LG-1..LG-5):

1. Commit fuente con PLAN LG, 04 §7, plantilla, dossier del #79, índice,
   nota de AG-6 y manifiestos; condición: gates OK salvo procedencia de
   `.skevi/`, que depende del SHA de este commit.
2. Commit de sincronización de `.skevi/` al SHA del paso 1; condición:
   suite completa y los tres `check_templates` de CI en verde.
3. Push ordinario de la rama a `origin`; condición: hook pre-push OK.
4. PR a `main` con este folio y la aceptación transcrita.
5. Comentario en el PR con la revisión registrada del head final.
6. Merge con commit de fusión (`gh pr merge --merge`, sin squash ni
   rebase: preservan los SHA de procedencia); condición: checks requeridos
   verdes y revisión del paso 5 sobre el mismo SHA del head.

PR B (LG-6..LG-7: ADR-045, regla E6 breaking, gate/v12) **no** está en
este lote: trae una decisión normativa y un cambio incompatible que el
Operador aún no ha visto. Se parte en dos lotes propios (N1 y R1):
SKV-LOTE-20261029-02 para commits, push y PR en borrador, propuesto antes
de su primer commit, y SKV-LOTE-20261029-03 para el merge, con su head
existente y confirmación expresa de ADR-045 y del salto breaking.

## Evidencia, riesgos y recomendación

Evidencia actual del PR A: `check_sizes` OK con ruta 1620/1620,
`check_plans` OK, `check_reports` OK, 276 tests con los dos fallos
esperados de `.skevi/`. Ronda adversarial 1: `fix-and-retry` con un HIGH
(04 §7 debilitaba la autoridad) y diez más; ronda 2: `proceed`, con H1-H11
verificados como cerrados y cuatro hallazgos nuevos; ronda 3: `proceed`,
N1-N4 verificados y R1-R3 atendidos ([registro](2026-10-29-lote-git-ronda.md)).

Riesgos: la revisión del head final la hace un agente con contexto fresco
del mismo proveedor y con filesystem compartido; no es independencia
fuerte. La protección de `main` exige cero aprobaciones, así que el
paso 5 no lo impone GitHub sino este lote.

Recomendación: aceptar. Si prefieres otro revisor del head final (humano
u otra familia de modelos), indícalo y el paso 5 lo espera.

Fuera del lote: force-push, rebase compartido, reset destructivo, borrar
ramas locales o remotas, tags, releases y despliegue.

Vigencia: hasta el merge del PR A o el 2026-10-31, lo que ocurra antes;
revocable en cualquier momento. Una parada del plan (CI rojo, HIGH
abierto, base cambiada) suspende los pasos pendientes hasta revalidar.

## Aceptación

El Operador respondió «aceptado» en la conversación (2026-10-29T10:11:11Z, hora de
registro del agente) a la petición que nombraba como único folio pendiente
SKV-LOTE-20261029-01 y pedía la forma «acepto SKV-LOTE-20261029-01». La
forma literal difiere; el objeto no es ambiguo porque no había otro folio
pendiente. Transcripción del agente, sin fuente primaria consultable fuera
de la conversación; se repite en la descripción del PR A.

## Capa técnica

```text
id = SKV-LOTE-20261029-01
date = 2026-10-29
time_utc = 10:11:11Z
head_sha = 8b1fb3f877510299b9bd3b7d82c4e8115f4deeba
model = Claude Opus 5.5 (self-declared; not proof)
STATE = OK
GATE = Lote proposed before any Git effect and accepted by the Operator before the first effect.
EVIDENCE
- python3 scripts/check_sizes.py -> OK; reading path 1620/1620 -> pass
- python3 scripts/check_plans.py -> OK 8 plans -> pass
- python3 scripts/check_reports.py -> OK -> pass
- python3 -m unittest discover -s tests -> 276; 2 expected .skevi provenance failures -> fail
- adversarial round 1 -> fix-and-retry; 1 HIGH and 10 more -> pass
- adversarial round 2 -> proceed; H1-H11 closed; N1 MED, N2-N4 LOW -> pass
- adversarial round 3 -> proceed; N1-N4 closed; R1 MED, R2-R3 LOW -> pass
- Operator reply in conversation -> «aceptado» at 2026-10-29T10:11:11Z -> pass
PENDING = lote steps 1-6; final-head review is step 5.
DECISION = proceed
OPERATIONS = proposed: commits, push, PR, PR comment and --merge for PR A only.
AUTHORITY = Operator replied «aceptado» at 2026-10-29T10:11:11Z to the request naming only this folio.
RISK = same-provider final-head review; PR B needs lotes 02 and 03.
report_sha256 = 0331047f400f8ab4d4b995b3d717959c128295e53e011d74a4e7d0672d252ef0
```
