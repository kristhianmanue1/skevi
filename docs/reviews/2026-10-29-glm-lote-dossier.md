# Dossier de lote — SKV-LOTE-20261029-04 (P1 fix y revisión GLM)

Registro previo al primer efecto. Rama propuesta:
`docs/glm-pendientes-p1` desde `main` `262f2a9` (merge del PR #81).
Contenido: el fix «(E1–E5)» → «(E1–E6)» de `AGENTS.md` (pendiente del
checkpoint) y la [revisión arquitectural
GLM](2026-10-29-glm-revision-arquitectural.md) (recomendación 4 del
análisis crítico: otra familia de modelos).

## Operaciones enumeradas

1. Crear la rama `docs/glm-pendientes-p1` desde `main` `262f2a9`.
2. Commit único: `AGENTS.md` (una línea), informe de revisión GLM, ronda
   adversarial y este dossier; condición: los cuatro gates en verde en
   local.
3. Push ordinario de la rama a `origin`; condición: hook pre-push OK.
4. PR a `main`.
5. Revisión del head final por agente con contexto fresco, publicada como
   comentario en el PR, sobre el mismo SHA que el CI.
6. Merge con `--merge` fijado a ese SHA (`--match-head-commit`);
   condiciones: CI requerido en verde y paso 5 favorable.
7. Tras el merge: `main` local por fast-forward y borrado de la rama
   local ya integrada con `git branch -d` (no fuerza). Las ramas remotas
   no se borran.

Fuera del lote: force-push, rebase de historia compartida, reset
destructivo, borrado de ramas remotas, **tags y releases** — la
publicación de v1.6.0 con notas de migración para el salto breaking
gate/v12 queda fuera y exigirá autorización humana expresa por operación.

## Evidencia, riesgos y recomendación

Evidencia (en `262f2a9`, hoy): `check_sizes` OK (ruta 1620/1620,
gate/v12), `check_plans` OK (8 planes, E1–E6), `check_reports` OK, suite
295 en verde. El fix de `AGENTS.md` está aplicado y sin commitear en el
árbol; el diff es de una línea. La revisión GLM se escribió con contexto
fresco de familia distinta a la autora (Claude Opus). El baseline AN-KLA
se adoptó tras el fix, con el drift explicado (`02dcc71`) y confirmado
por el Operador («adelante con recomendaciones procede»).

Riesgos:

- Revisor de la ronda adversarial del diff del mismo proveedor (GLM):
  la independencia de familia está en la revisión arquitectural, no en
  la ronda del propio diff.
- Contenido documental: sin salto de gate ni breaking para adoptantes.
- El fix toca `AGENTS.md`, instrucciones de agente: el cambio es una
  actualización de exactitud (E6 ya rige en el gate desde gate/v12).

Recomendación: aceptar.

## Aceptación

El Operador escribió en la conversación, a las 16:35Z del 2026-10-29
(hora de registro del agente): «acepto SKV-LOTE-20261029-04», junto a
«Confirmo ADR-046» y «acepto SKV-LOTE-20261029-05», en respuesta al
bloque que enumeraba las tres frases de cierre. Aceptación humana
previa, explícita, vigente y registrada contra este folio antes del
primer efecto remoto (ADR-044 a). Los pasos 1-2 (rama y commit) se
ejecutaron antes como concesión de clase de sesión local; push, PR,
revisión y merge se ejecutan bajo esta aceptación, revalidando justo
antes de cada efecto. Revocable hasta cada efecto.

## Capa técnica

```text
id = SKV-LOTE-20261029-04
date = 2026-10-29
time_utc = 15:20:00Z
head_sha = 262f2a951945b70c20a80b7211a2ae82c9da6bfc
model = GLM 5.3 Flash (self-declared; not proof)
STATE = PARTIAL
GATE = Per-folio acceptance registered before the first remote effect;
steps 3-7 (push, PR, head review, pinned merge, cleanup) executing.
EVIDENCE
- python3 scripts/check_sizes.py -> OK; gate/v12; path 1620/1620 -> pass
- python3 scripts/check_plans.py -> OK; 8 planes; E1-E6 -> pass
- python3 scripts/check_reports.py -> OK; 31 at hashing; ronda after -> pass
- python3 -m unittest discover -s tests -> 295 tests OK -> pass
- git diff of AGENTS.md -> single line E1-E5 to E1-E6 -> pass
- AN-KLA baseline adopted after the fix; drift 02dcc71 accepted -> pass
- Operator acceptance -> «acepto SKV-LOTE-20261029-04» at 16:35Z -> pass
PENDING = steps 3-7 under the registered acceptance;
v1.6.0 release stays outside the lote.
DECISION = proceed
OPERATIONS = proposed: branch, one commit, push, PR, head review
comment, pinned --merge, local cleanup of merged branches.
AUTHORITY = «acepto SKV-LOTE-20261029-04» registered 2026-10-29 16:35Z.
RISK = same-provider round reviewer; doc-only change; no breaking jump.
report_sha256 = bd847bdf6f2f2e96f78695b2dc6be8587b03bcfd508bd00f55564a6120fadb30
```
