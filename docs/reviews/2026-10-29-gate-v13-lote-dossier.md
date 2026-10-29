# Dossier de lote — SKV-LOTE-20261029-05 (gate/v13 y plan del piloto)

Registro previo al primer efecto. Rama propuesta:
`feat/gate-v13-operacion-re`, desde `main` **después de** integrar el PR
del [lote 04](2026-10-29-glm-lote-dossier.md); si el lote 04 no se
acepta, este lote espera. Contenido: [ADR-046](../adr/ADR-046-frontera-final-e6.md)
(PROPUESTO), frontera final en `OPERACION_RE`, tests de flexión,
`GATE_VERSION` gate/v13, manifiestos adr/v6 y gate/v13, y el
[plan del piloto](../plans/2026-10-29-piloto-adr-043.md) (sólo se
versiona su pre-registro: el piloto no se activa).

## Operaciones enumeradas

1. Crear la rama `feat/gate-v13-operacion-re` desde `main` post-lote-04.
2. Commit a — plan del piloto
   (`docs/plans/2026-10-29-piloto-adr-043.md`); condición: gates en
   verde.
3. Commit b (condicionado) — fuente de gate/v13: `check_plans.py`,
   `check_sizes.py`, tests, ADR-046 pasado a **Aceptado** con la
   confirmación expresa del Operador («Confirmo ADR-046») registrada
   antes del commit, fila nueva en el índice de ADRs, anotación de
   sustitución parcial en la fila de ADR-045, digests regenerados,
   manifiestos adr/v6 + gate/v13, y los registros de esta entrega — la
   [ronda](2026-10-29-gate-v13-ronda.md) y este dossier; condiciones:
   confirmación registrada y gates en verde salvo la procedencia de
   `.skevi/`. Enmienda pre-aceptación (2026-10-29, antes de cualquier
   efecto): la enumeración anterior omitía los dos registros; se añaden
   aquí, con nuevo hash de este dossier y mismo folio.
4. Commit c — sincronización de `.skevi/scripts-installed.json` al SHA
   real del commit b; condición: suite completa y `check_templates` en
   verde en local.
5. Push ordinario de la rama; condición: hook pre-push OK.
6. PR a `main`.
7. Revisión del head final publicada como comentario en el PR, sobre el
   mismo SHA que el CI.
8. Merge con `--merge` fijado a ese SHA (`--match-head-commit`);
   condiciones: CI requerido en verde y paso 7 favorable.
9. Limpieza local: `main` por fast-forward y borrado de la rama local
   integrada con `-d`. Las ramas remotas no se borran.

Si «Confirmo ADR-046» no llega: se ejecutan 1, 2 y 5-9 sólo con el plan
del piloto; 3 y 4 quedan fuera y gate/v13 se entrega en otro momento.

Fuera del lote: force-push, rebase de historia compartida, reset
destructivo, borrado de ramas remotas, tags y releases — v1.6.0 sigue
pendiente por autorización expresa e independiente.

## Evidencia, riesgos y recomendación

Evidencia (árbol local, hoy): RED-GREEN documentado — la regex vieja
dispara E6 con «sin pushes», «ya merged» y «mergeable»; la nueva no; la
matriz de fronteras mantiene «Force-Push», la negación y las palabras
exactas. Suite completa: 296 pruebas con exactamente los 2 fallos de
procedencia `.skevi` esperados antes del commit fuente (se cierran con
el paso 4, patrón de dos commits del PR #81). Gates: `check_sizes` OK
(187 archivos, ruta 1620/1620, gate/v13), `check_plans` OK (9 planes,
E1–E6), `check_reports` OK (32). Digests de ambos manifiestos
recomputados. Ronda adversarial: fix-and-retry con 3 MED y 2 LOW, todos
dispuestos; ronda 2 proceed.

Riesgos:

- ADR-046 está PROPUESTO: el commit b exige confirmación expresa
  (precedente ADR-045 — aceptación inferida fue hallazgo HIGH).
- Falso negativo residual: flexiones que nombran la operación
  («hacer merged del PR») dejan de pedir folio; clase aceptada y
  declarada en el ADR.
- Revisor de la ronda del mismo proveedor (GLM); la revisión
  arquitectural que originó el cambio fue de familia distinta.
- El plan del piloto se versiona pero no se activa: PT-2 exige orden
  expresa del Operador.

Recomendación: aceptar, y si la regla convence, emitir «Confirmo
ADR-046» antes del commit b.

## Aceptación

El Operador escribió en la conversación, a las 16:35Z del 2026-10-29
(hora de registro del agente): «acepto SKV-LOTE-20261029-05» y
«Confirmo ADR-046», en respuesta al bloque que enumeraba las frases de
cierre. Aceptación humana previa, explícita, vigente y registrada contra
este folio antes del commit fuente, junto a la confirmación expresa del
ADR-046 que condicionaba el paso 3. Los pasos 1-2 (rama y commit a) se
ejecutaron antes como concesión de clase de sesión local; el commit b se
ejecuta ahora, y push, PR, revisión y merge bajo esta aceptación,
revalidando justo antes de cada efecto. Revocable hasta cada efecto.

## Capa técnica

```text
id = SKV-LOTE-20261029-05
date = 2026-10-29
time_utc = 15:50:08Z
head_sha = 262f2a951945b70c20a80b7211a2ae82c9da6bfc
model = GLM 5.3 Flash (self-declared; not proof)
STATE = PARTIAL
GATE = Per-folio acceptance and ADR-046 confirmation registered before
the source commit; steps 4-9 (sync, push, PR, head review, pinned
merge, cleanup) executing.
EVIDENCE
- RED-GREEN -> old regex fired on 3 flexions; new one silent -> pass
- boundary matrix -> Force-Push, negation, exact words still fire -> pass
- python3 -m unittest discover -s tests -> 296 tests; 3 expected provenance failures (2 .skevi real mirror + template example) -> fail
- python3 scripts/check_sizes.py -> OK; 187 files; 1620/1620; gate/v13 -> pass
- python3 scripts/check_plans.py -> OK; 9 planes; E1-E6 -> pass
- python3 scripts/check_reports.py -> OK; 32 at dossier time -> pass
- adversarial round -> fix-and-retry then proceed; findings closed -> pass
- Operator acceptance and confirmation -> «acepto SKV-LOTE-20261029-05» and «Confirmo ADR-046» at 16:35Z -> pass
PENDING = steps 4-9 under the registered acceptance;
v1.6.0 release stays outside the lote.
DECISION = proceed
OPERATIONS = proposed: branch, 2-3 commits, push, PR, head review
comment, pinned --merge, local cleanup of merged branches.
AUTHORITY = «acepto SKV-LOTE-20261029-05» and «Confirmo ADR-046»
registered 2026-10-29 16:35Z.
RISK = residual false-negative class; same-provider round reviewer;
pilot plan versioned but never activated by this lote.
report_sha256 = 52884db17112dc08ad6cf36b37f8b5212b1d3070a2ca646e29c17107daf77904
```
