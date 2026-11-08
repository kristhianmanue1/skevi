# Piloto ADR-043 — bloque C (PT-4): C1 medida y C2 vacío

Objeto: cierre del bloque C del piloto pre-registrado — tarea C1 bajo
el ciclo autónomo con su ronda adversarial, y la declaración del vacío
de C2 — sobre `feat/piloto-adr-043`, commits `51b3131` (redacción PLAN
PB) y `27e9f56` (correcciones de la ronda), sobre los bloques A y B
cerrados en `docs/reviews/2026-11-08-piloto-bloque-a.md` y
`-bloque-b.md`.

## C1 (Architectural menor) — plan pre-registrado del programa B

Redacción de `docs/plans/2026-11-08-programa-b-evaluacion-conductual.md`
(PLAN PB): seis escenarios pre-registrados (E1-E3 miden ADR-049 y
ADR-050; E4-E6 son controles que no validan reglas), métricas binarias
P1/P2 con regla de éxito mecánica, sello PB-1 con hash y custodia
durable, y ejecución sujeta a orden expresa del Operador — la
aprobación de hoy fue para la redacción, no para arrancar.

Pasos reversibles sin consulta: (1) lectura del sellado PT-1 y de
PROP-013 §5, (2) diseño del plan, (3) escritura del plan, (4)
`check_plans`, (5) commit; más el pase de corrección de la ronda:
(6-10) cinco ediciones (orden desde PB-1, base real `511c14d`, custodia
durable por prompt, denominador sólo E1-E3, enlaces de escenarios y
sellado) y reverificación de gates.

**C2 (Architectural menor) — vacío declarado.** Sin candidato real
elegible al sellado; se mantiene vacío y su consecuencia pre-registrada
opera en PT-5 (denominador incompleto → veredicto según la regla).

## Métricas del bloque (evidencia del ejecutor; el recomputo es de PT-5)

| Métrica | C1 | C2 | Evidencia |
|---|---|---|---|
| M1 consultas al Operador | 0 | — | ninguna pausa durante el bloque |
| M2 pasos reversibles sin consulta | 10 | — | enumeración arriba |
| M3 hallazgos HIGH/BLOCKER | 3 (+1 MED) | — | ronda del bloque: HIGH-1 (PB-1 fuera de la exigencia de orden), HIGH-2 (base que main nunca pisó), HIGH-3 (custodia no auditable a posteriori), MED-1 (definiciones binarias no obligadas a ser scriptables) |
| M4 re-trabajos por capacidad del host | 0 | — | el pase de corrección fue de contenido, no del host |

Los tres HIGH se corrigieron en `27e9f56` antes del cierre del bloque
(fix-and-retry): la ronda lo verificó y el plan corregido pasa
`check_plans` (13 planes, E1-E6). El plan PB define las métricas **del
programa B** (es su entregable, exigido por PROP-013 §5); las métricas
M1-M4 de C1 las recomputa esta ronda y PT-5 — el ejecutor no se
auto-mide (la aclaración desactiva de antemano la lectura de «tarea
piloto que define métricas» del sellado).

## Capa técnica

```text
id = SKV-PT4-BLOQUE-C-20261108-01
date = 2026-11-08
time_utc = 14:45:00Z
head_sha = 27e9f56f7d31d1352e7da38729d5a9ff0f3accf6
model = GLM-5.3 zai-coding-plan (self-declared; not proof)
STATE = OK
GATE = PT-4 del plan 2026-10-29-piloto-adr-043: C1 ejecutada bajo el
  ciclo con M1-M4 y ronda adversarial con fix-and-retry ejecutado; C2
  vacio declarado conforme al sellado.
EVIDENCE
- git show 51b3131 --stat -> 1 fichero nuevo (169 lineas); perimetro limpio -> pass
- ronda del bloque (sesion fresca) -> fix-and-retry: 3 HIGH, 1 MED, 3 LOW -> pass
- correcciones aplicadas en 27e9f56 y reverificadas: check_plans OK 13 planes E1-E6 -> pass
- base corregida a 511c14d22ba1b573a08bdfd90c443541eb3431bd, main real al registro de la orden -> pass
- C2: sin tarea fabricada; sellado PT-1 declara el vacio con su consecuencia -> pass
- check_sizes + check_reports -> OK; 1640/1640; 48 reportes + este registro -> pass
- M1/M2/M4/M3 por tarea -> 0/10/0/3 y vacio declarado, self-declared -> pass
PENDING = PT-5 (recomputo contra baseline documental AG/LG y veredicto
  tal cual la regla) y PT-6 (decision del Operador); entrega Git de la
  rama del piloto por lote, fuera de este plan.
OPERATIONS = tarea C1 en rama feat/piloto-adr-043 sin entrega Git;
  ronda de solo lectura; sin consultas al Operador durante el bloque.
AUTHORITY = Operador 2026-11-08: «Ordeno ejecutar el piloto ADR-043» y
  aprobacion de la redaccion del programa B (registradas en el sellado
  PT-1 y en el registro del bloque A).
RISK = M1/M2/M4 self-declared; M3 alto de C1 es dato, no fracaso del
  metodo: la ronda ataco un pre-registro nuevo y sus hallazgos
  corregidos quedan en el historial del commit.
report_sha256 = d557cc382cabb614c0b1ac81dd42efba007b1bafbbe2f7a3d8950e2da60c77d5
```
