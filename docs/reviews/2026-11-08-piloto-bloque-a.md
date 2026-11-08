# Piloto ADR-043 — bloque A (PT-2): A1 y A2 medidas

Objeto: ejecución y cierre del bloque A del piloto pre-registrado
(`docs/plans/2026-10-29-piloto-adr-043.md`, sellado en
`docs/reviews/2026-11-08-piloto-pt1-sellado.md`) — tareas A1 y A2 bajo
el ciclo autónomo, con su ronda adversarial de bloque — sobre rama
`feat/piloto-adr-043`, commit `96ef6ae` sobre `main` `27d13eb`.

## Las dos tareas y sus pasos

**A1 (Bounded docs) — traslado de PROP-013 a history.** La deliberación
quedó decidida con la adopción de ADR-049/050/051 (PR #94): ADR-002
ordena el traslado y ADR-047 lo hace sin tocar cuerpos sellados. Pasos
reversibles ejecutados sin consulta: (1) `git mv` del documento,
(2) retirada del directorio `docs/proposals/` vacío, (3) actualización
de los tres enlaces vivos del índice de ADRs, (4) bump adr/v9 → adr/v10
con history, (5) corrida de gates. Rename 100 % — el contenido no se
editó; los cuerpos de los ADR citan la ruta de su fecha de redacción
(procedencia histórica legítima, ADR-047).

**A2 (Bounded docs) — alineación de orquestación.** El protocolo
`orquestacion-codex-opencode-tmux.md` gana dos punteros a ADR-049 y
ADR-050 (dependencias conceptuales y objetivos); el runbook se acota
fuera deliberadamente porque declara «no contiene reglas nuevas». Pasos
reversibles: (1) lectura del protocolo, (2) lectura del runbook,
(3) edición de la línea de dependencias, (4) edición del bullet de
objetivos, (5) corrida de gates.

## Métricas del bloque (evidencia del ejecutor; el recomputo es de PT-5)

| Métrica | A1 | A2 | Evidencia |
|---|---|---|---|
| M1 consultas al Operador | 0 | 0 | ninguna pausa ni pregunta durante el bloque; el único turno con el Operador previo fue la orden de ejecución del piloto |
| M2 pasos reversibles sin consulta | 5 | 5 | enumeración arriba; commits `96ef6ae` y el registro presente |
| M3 hallazgos HIGH/BLOCKER | 0 | 0 | ronda del bloque: `proceed`, sin HIGH ni BLOCKER |
| M4 re-trabajos por capacidad del host | 0 | 0 | ningún reintento por sandbox, Git o herramientas |

La ronda del bloque dejó dos LOW: el `generated_at` de adr/v10 quedó
posterior al commit (patrón anterior era anterior-al-commit; usar hora
real en el próximo bump) y los prompts base del runbook aún no mencionan
rulings ni pilas (alineación acotada al protocolo por diseño; el runbook
declara no contener reglas). Consigna además una corrección de un
registro anterior: el sellado PT-1 cita «adopción en PR #93» en su
evidencia; la precisión es «decisión en conversación registrada antes
del commit fuente, adopción fusionada en PR #94» — el sellado está
sellado por hash y no se edita; esta consignación es su corrección.

## Capa técnica

```text
id = SKV-PT2-BLOQUE-A-20261108-01
date = 2026-11-08
time_utc = 14:15:00Z
head_sha = 96ef6aee16d91b58260325f8eac82475794d290e
model = GLM-5.3 zai-coding-plan (self-declared; not proof)
STATE = OK
GATE = PT-2 del plan 2026-10-29-piloto-adr-043: dos tareas reales
  (A1 y A2) ejecutadas bajo el ciclo, M1-M4 registrados por tarea con
  evidencia y ronda adversarial del bloque con decision.
EVIDENCE
- git show 96ef6ae -M -> 4 ficheros; rename 100% sin edicion; 3 enlaces y bump adr/v10 -> pass
- shasum del archivo movido -> identico en ruta nueva y en 27d13eb:docs/proposals -> pass
- grep proposals/PROP-013 en docs -> 9 coincidencias, todas procedencia historica legitima -> pass
- check_sizes + check_plans + check_reports -> OK; 1640/1640; 12 planes; 46 reportes -> pass
- ronda del bloque (sesion fresca) -> proceed; M3 = 0 HIGH, 0 BLOCKER; 2 LOW -> pass
- M1/M2/M4 por tarea -> 0/5/0 y 0/5/0, self-declared, enumerados arriba -> pass
PENDING = bloque B (B1 partir test_check_templates 774/800; B2 hook con
  check_templates) y bloque C (C1 plan del programa B; C2 vacio
  declarado); los dos LOW del bloque viajan a PT-5.
OPERATIONS = tarea A1 y A2 en rama feat/piloto-adr-043 sin entrega Git;
  ronda de solo lectura; sin consultas al Operador durante el bloque.
AUTHORITY = Operador 2026-11-08: «Ordeno ejecutar el piloto ADR-043»
  (registrada en el sellado PT-1); bloques pre-registrados e
  inmutables desde el sellado.
RISK = M1/M2/M4 son recuentos self-declared del ejecutor; la ronda del
  bloque verifico coherencia perimetral y el recomputo final es de
  PT-5 contra el baseline documental.
report_sha256 = 5f79c411eae691ff406b23ef6c32530daa2d3fb969fce9ae42cb056fcee31310
```
