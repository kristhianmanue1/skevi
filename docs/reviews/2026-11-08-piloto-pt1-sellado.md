# PT-1 — Sellado del pre-registro del piloto ADR-043

Objeto: ejecución de la TAREA PT-1 de
`docs/plans/2026-10-29-piloto-adr-043.md` — sellado de métricas,
baseline y lista de tareas elegibles — sobre `main`
`511c14d22ba1b573a08bdfd90c443541eb3431bd`, con la autorización expresa
del Operador («Ordeno ejecutar el piloto ADR-043», 2026-11-08,
selección estructural limpia tras reformulación; la selección
contradictoria previa del mismo turno no se registró como orden).

## Sellado

El bloque pre-registrado del plan (único fence del documento) tiene el
SHA-256 `ff22f0923f0a3f5cb5093cba1492793879554643592b84c2c8cef361424f83d4`
contenido UTF-8, LF, sin newline final. Desde este registro, métricas
M1-M4, denominador, fórmula de éxito y condiciones de paro son
inmutables: editarlos invalida la comparación y obliga a declarar
`inconclusive`. La Enmienda 1 (conservación re-analizable de la
evidencia) ya viajaba en `main` vía PR #93, aplicada antes de este
sellado, tal como exige el pre-registro.

## Lista de tareas elegibles (PT-1, step 2)

| Slot | Clase | Tarea real | Anfitrión |
|---|---|---|---|
| A1 | Bounded (docs) | Trasladar PROP-013 de `docs/proposals/` a `docs/history/` — la deliberación quedó decidida con la adopción de ADR-049/050/051; incluye el enlace vivo del índice de ADRs con su bump (ADR-002, ADR-047) | Skevi |
| A2 | Bounded (docs) | Alinear `docs/orchestration/` con los mecanismos aterrizados (rulings y disposiciones, ADR-049/050) | Skevi |
| B1 | Bounded (scripts) | Partir `tests/test_check_templates.py` antes del límite de 800 — hoy 774/800, deuda de contención registrada del gate | Skevi |
| B2 | Bounded (scripts) | Alinear `scripts/hooks/pre-push` con el CI: ejecutar los tres auto-chequeos de check_templates que el hook aún no corre (ADR-034) | Skevi |
| C1 | Architectural (menor) | Redactar el plan pre-registrado del programa B de evaluación conductual (PROP-013 §5, orden del Operador de hoy) | Skevi |
| C2 | Architectural (menor) | **Vacío al sellado** — sin candidato real elegible; si no materializa una tarea real antes de su bloque, se declara `inconclusive` por la regla pre-registrada y el veredicto global la sigue | — |

Las cinco primeras existen sin el piloto y no se auto-miden: el
ejecutor sólo produce evidencia M1-M4; la recomputación es del bloque
(PT-2..PT-4 rondas) y de PT-5. Ninguna tarea piloto define métricas.

## Capa técnica

```text
id = SKV-PT1-SELLADO-20261108-01
date = 2026-11-08
time_utc = 12:56:36Z
head_sha = 511c14d22ba1b573a08bdfd90c443541eb3431bd
model = GLM-5.3 zai-coding-plan (self-declared; not proof)
STATE = OK
GATE = PT-1 del plan 2026-10-29-piloto-adr-043: sellado del
  pre-registro con hash del bloque de metricas y lista de 6 tareas
  elegibles con clase y anfitrion; 5 reales y 1 vacio declarado.
EVIDENCE
- sha256 del unico fence del plan del piloto -> ff22f0923f0a3f5cb5093cba1492793879554643592b84c2c8cef361424f83d4 -> pass
- wc -l tests/test_check_templates.py -> 774/800, deuda real de contencion -> pass
- grep check_templates scripts/hooks/pre-push -> 0 lineas; el CI si lo corre -> pass
- git log --oneline -2 origin/main -> PROP-013 decidida por la adopcion en PR #93 -> pass
- python3 scripts/check_sizes.py -> OK; 211 archivos; ruta 1640/1640 -> pass
- python3 -m unittest discover -s tests -> 297 tests OK -> pass
PENDING = ejecucion de PT-2 (bloque A) en adelante, por bloques con
  ronda propia; C2 sin candidato real al sellado; recomputo de metricas
  del bloque, nunca del ejecutor.
OPERATIONS = sellado de solo lectura sobre el plan del piloto; sin
  efectos Git; el hash se computo por script sobre el fence canonico.
AUTHORITY = Operador 2026-11-08: «Ordeno ejecutar el piloto ADR-043»
  (seleccion estructural que nombra la orden, tras reformular la
  seleccion contradictoria del mismo turno, que no se registro).
RISK = baseline documental parcial (dossiers AG/LG del 2026-10-28/29);
  si una metrica no es comparable, queda inconclusive por regla, sin
  reemplazo.
report_sha256 = e478d519d8659384423320f0574d620ecae1650459c530afbcf688959103d3b3
```
