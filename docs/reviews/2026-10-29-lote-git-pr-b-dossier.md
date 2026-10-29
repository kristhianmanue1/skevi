# Dossier de lotes — SKV-LOTE-20261029-02 y -03 (PLAN LG, PR B)

Registro previo al primer commit del PR B (LG-6..LG-7). Rama
`feat/gate-v12-campo-lote` desde `main` `a080151` (merge del PR #80).

## Operaciones enumeradas

Lote 02 — hasta PR en borrador:

1. Commit fuente: E6 en `check_plans`, tests, ADR-045, índice, gate/v12,
   corrección del MED de la revisión del PR #80 en 04 §7, hallazgos LOW,
   manifiestos; condición: gates OK salvo procedencia de `.skevi/`.
2. Commit de sincronización de `.skevi/` al SHA del paso 1; condición:
   suite completa y los tres `check_templates` en verde (en local).
3. Push ordinario de la rama a `origin`; condición: hook pre-push OK.
4. PR a `main` en borrador.

Lote 03 — merge:

5. Revisión del head final por agente con contexto fresco, publicada como
   comentario en el PR, sobre el mismo SHA que el CI.
6. PR listo para revisión y merge con `--merge`, fijado a ese SHA
   (`--match-head-commit`); condiciones: CI requerido verde, paso 5
   `approve` y **confirmación expresa del Operador** del texto de ADR-045
   y de su salto breaking, registrada antes del commit fuente (hallazgo
   HIGH de la ronda del PR B; disposición R1 del PR A).
7. Tras el merge: `main` local por fast-forward y borrado de las ramas
   locales ya integradas con `git branch -d` (no fuerza). Las ramas
   remotas no se borran.

Fuera de ambos lotes: force-push, rebase compartido, reset destructivo,
borrado de ramas remotas, tags, releases y despliegue.

## Evidencia, riesgos y recomendación

Evidencia: PR A integrado en `a080151`, con CI de `main` en `success`. El
plan LG fija las tareas LG-6 y LG-7.

Riesgos:

- E6 es **breaking**: un adoptante con planes cuyo `Permitido:` mencione
  push o merge sin `Lote:` pasa a BLOQ.
- E6 se activa por vocabulario (`push`, `merge`), en tensión con REQ-2 de
  ADR-014. ADR-045 lo declara como excepción acotada.
- Revisor del mismo proveedor.

Recomendación: aceptar.

## Aceptación

El Operador escribió en la conversación, a las 2026-10-29T10:32Z (hora de
registro del agente): «tienes permisos para esta esta seion para github ,
commits, merges pr etc y dejar tree limpio». Es una instrucción humana
directa, de prioridad 1 en `AGENTS.md`, que precede a todos los efectos de
este registro y enumera las clases de operación. **No se emitió contra
estos folios**: los folios se crean después, para dar trazabilidad. Esto
cumple la jerarquía, pero no la forma «registrada contra el folio» de
ADR-044 (a). Es la misma forma de permiso de sesión que el análisis señaló
en el PR #78; aquí se declara antes del efecto, no después.

La instrucción no nombra `push` ni borrado de ramas: el agente los infiere
de «github … etc» y de «dejar tree limpio». Tampoco acepta el contenido de
ADR-045; por eso el paso 6 exige la confirmación aparte. El Operador la
dio a las 2026-10-29T10:55:28Z (hora de registro del agente), antes del
commit fuente, eligiendo «Confirmo ADR-045» en una pregunta que describía
la regla, su salto breaking y la excepción a REQ-2.

Vigencia: esta sesión. Revocable.

## Capa técnica

```text
id = SKV-LOTE-20261029-02-03
date = 2026-10-29
time_utc = 10:55:28Z
head_sha = a080151ed0d216d1e09175f164816eaea99a53dc
model = Claude Opus 5.5 (self-declared; not proof)
STATE = PARTIAL
GATE = Lotes 02-03 recorded before the first PR B effect; authority is a session-class human grant.
EVIDENCE
- gh pr view 80 -> MERGED 10:32:26Z; merge a080151 -> pass
- gh run view (main) -> success at a080151 -> pass
- Operator session instruction -> classes github, commits, merges, PR; precedes effects -> pass
- acceptance recorded against folio 02/03 (ADR-044 a) -> session grant, not per folio -> fail
- Operator confirmation of ADR-045 text and breaking jump -> «Confirmo ADR-045» at 2026-10-29T10:55:28Z -> pass
PENDING = lote steps 1-7.
DECISION = proceed
OPERATIONS = proposed: commits, push, draft PR, PR comment, --merge, local branch -d.
AUTHORITY = Operator direct session instruction (priority 1), not folio-bound.
RISK = breaking E6 for adopters; lexical trigger vs ADR-014 REQ-2; same-provider review.
report_sha256 = b302249725afb2c1dd9eab33474129cea1c387a8c628694b2c76476fc0643fd1
```
