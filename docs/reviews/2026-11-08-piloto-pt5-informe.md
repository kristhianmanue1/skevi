# PT-5 — Informe del piloto ADR-043: veredicto `inconclusive`

Objeto: recomputo de M1-M4 contra el baseline documental pre-registrado
(tareas AG-1..AG-6 y LG-1..LG-7 con sus dossiers del 2026-10-28/29) y
veredicto tal cual la regla, sobre `feat/piloto-adr-043` con los tres
bloques cerrados (A, B y C — registros del 2026-11-08).

## Datos del piloto (los cinco de la lista sellada; C2 vacío)

| Tarea | Clase | M1 | M2 | M3 | M4 |
|---|---|---|---|---|---|
| A1 (PROP-013 a history) | Bounded docs | 0 | 5 | 0 | 0 |
| A2 (orquestación alineada) | Bounded docs | 0 | 5 | 0 | 0 |
| B1 (partición de test_check_templates) | Bounded scripts | 0 | 5 | 0 | 0 |
| B2 (paridad hook↔CI) | Bounded scripts | 0 | 2 | 0 | 0 |
| C1 (PLAN PB) | Architectural | 0 | 10 | 3 (+1 MED) | 0 |
| C2 | Architectural | — | — | — | — |

M3 de C1 en detalle: 3 HIGH (PB-1 fuera de la exigencia de orden;
base que main nunca pisó; custodia no auditable a posteriori) y 1 MED
(definiciones binarias no obligadas a scriptables), todos corregidos
en `27e9f56` antes del cierre del bloque y verificados por su ronda.
Los bloques A y B cerraron con `proceed` y cero HIGH/BLOCKER.

## Comparación contra el baseline (tal cual la regla)

- **Denominador:** 5 de 6 tareas completas — C2 quedó sin candidato
  real, declarado en el sellado. La regla pre-registrada dice
  «Inconclusive: menos de 6 tareas completas» → **disparada**.
- **M1:** los dossiers AG/LG no registran consultas al Operador por
  tarea — el baseline documental no permite computar la media de su
  clase. La regla anticipa el caso: «si no permite comparar una
  métrica, esa métrica queda inconclusive — nunca se reemplaza por
  otra» → **inconclusive** en las cinco tareas, pese a que el dato del
  piloto (0 consultas) es real.
- **M3:** los hallazgos de las rondas AG/LG están registrados por
  entrega, no mapeados por tarea; la comparación «sin aumento» contra
  la media de su clase no es derivable mecánicamente del registro →
  **inconclusive**, con la nota de que el único M3 positivo del piloto
  (C1, 3 HIGH) atacó un pre-registro nuevo, no código de producción.
- **M2 y M4:** el baseline no las cubre (el sellado las declaraba
  parciales); quedan como registro del ejecutor, sin comparación.

## Veredicto

**`inconclusive`** — por dos de las tres vías pre-registradas
(denominador 5/6 y baseline incomparable para M1; M3 sin mapeo por
tarea). Conforme a PT-5 `Prohibido`: no se recomienda adopción ni
ajuste del ciclo desde este informe; la decisión sigue en PT-6.

## Capa técnica

```text
id = SKV-PT5-INFORME-20261108-01
date = 2026-11-08
time_utc = 15:00:00Z
head_sha = cac9469da70dd46b6ed518187a5e071ad43028e3
model = GLM-5.3 zai-coding-plan (self-declared; not proof)
STATE = OK
GATE = PT-5 del plan 2026-10-29-piloto-adr-043: comparacion M1-M4 con
  la regla pre-registrada y veredicto tal cual la regla, sin
  reinterpreacion; tabla con el estado de cada tarea.
EVIDENCE
- denominador -> 5/6 tareas completas; C2 vacio declarado en el sellado -> pass
- grep -i consulta en los dossiers AG/LG -> 0 registros por tarea -> pass
- grep HIGH/BLOCKER en los dossiers AG/LG -> presentes por entrega, sin mapeo por tarea -> pass
- tabla del piloto -> A1/A2/B1/B2 con M3 = 0; C1 con M3 = 3 (+1 MED), corregidos en 27e9f56 -> pass
- regla citada -> «Inconclusive: menos de 6 tareas completas, o baseline incomparable» -> pass
- python3 scripts/check_sizes.py -> OK; 217 archivos; ruta 1640/1640 -> pass
- python3 scripts/check_reports.py -> OK; 49 reportes + este informe -> pass
PENDING = PT-6: recomendacion con opciones y costes al Operador;
  entrega Git de la rama del piloto por lote, fuera de este plan.
DECISION = proceed
OPERATIONS = recomputo de solo lectura sobre los registros de los tres
  bloques y los dossiers del baseline; sin efectos Git.
AUTHORITY = Operador 2026-11-08: «Ordeno ejecutar el piloto ADR-043»
  (sellado PT-1); metricas y regla de exito inmutables desde el sello.
RISK = el baseline documental resulto mas parcial de lo que el sellado
  esperaba; una medicion futura exige dossiers que registren consultas
  por tarea desde el inicio.
report_sha256 = e82e34f2f567bed2e1a43e5a463f010ad709468135c7e3cd1dda69b88b2cbba5
```
