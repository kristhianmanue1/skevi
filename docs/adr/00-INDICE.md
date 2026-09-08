# Índice de decisiones arquitectónicas (ADR)

| ADR | Título | Estado | Implementación | Origen | Fecha |
|---|---|---|---|---|---|
| ADR-001 | Gate local sin CI remoto | Aceptado | `scripts/hooks/pre-push` | Fundacional | 2026-08-12 |
| ADR-002 | Separación de docs por vida útil | Aceptado | Estructura de `docs/` | Fundacional | 2026-08-12 |
| ADR-003 | Directorios canónicos en inglés | Aceptado | Estructura de `docs/` | Instrucción directa | 2026-08-14 |
| ADR-004 | Graduar fail-closed por clase de operación | Aceptado | `f46dcca` | PROP-003 §3.1 | 2026-08-17 |
| ADR-005 | Resultado por línea de evidencia | Aceptado | `f46dcca` | PROP-003 §3.2 | 2026-08-17 |
| ADR-006 | Gate configurable por proyecto adoptante | Aceptado | `scripts/check_sizes.py` | PROP-002 §A-6 | 2026-08-15 |
| ADR-007 | Validar en la frontera implica fallar controlado | Aceptado | `estandar-diseno-software-github.md` §2.4 | `an-kla-memory` #84 | 2026-08-16 |
| ADR-008 | Disparadores objetivos de rigor | Aceptado | `AGENTS.md`, `04-ejecucion-y-verificacion.md` | PROP-002 §A-8 | 2026-08-15 |
| ADR-009 | Clasificación de tarea por disparadores observables | Aceptado | `01-analisis-y-requerimientos.md` §2, `04` §1 | PROP-004 §2 A-1 | 2026-08-20 |
| ADR-010 | Plan de implementación como artefacto de escala | Aceptado | `templates/plan-de-implementacion.md`, `03` §2, `04` §1 | PROP-004 §2 A-2 | 2026-08-20 |
| ADR-011 | RED-GREEN-REFACTOR como default condicional de F3 | Aceptado | `04-ejecucion-y-verificacion.md` §3 | PROP-004 §2 A-3 | 2026-08-20 |
| ADR-012 | Los archivos de test nuevos no escalan la clase de una tarea | Aceptado | `01-analisis-y-requerimientos.md` §2, ADR-009 (Estado) | `piloto-orbitanova.md` PF-1 | 2026-08-20 |
| ADR-013 | Crear un plan de implementación es disparador de Architectural | Aceptado | `01-analisis-y-requerimientos.md` §2 | `piloto-orbitanova-2.md` PF-2 | 2026-08-20 |
| ADR-014 | Gate de planes con chequeo estructural mínimo (A-4) | Aceptado | `scripts/check_plans.py`, `skevi-gate.json` clave `plans` | PROP-004 §A-4 (condición cumplida) | 2026-08-20 |
| ADR-015 | Convención de idioma: código en inglés, cara al usuario en el idioma del proyecto | Aceptado | `estandar-diseno-software-github.md` §3.1 | Instrucción directa | 2026-09-07 |
| ADR-016 | Reportes de agente en dos capas con bloque de trazabilidad | Aceptado | `00-INDICE.md`, `04` §5.2, estándar §6 | PROP-006 | 2026-09-07 |
| ADR-017 | Autoridad Git graduada (Z1-Z3) con gate delegable | Aceptado | estándar §6.2/§6.6/§4.3, `project-manifest.yaml` | PROP-007 | 2026-09-07 |
| [ADR-018](ADR-018-coherencia-de-autoridad.md) | Coherencia de autoridad general y restricción local | Aceptado | `29243f1` | [T05, opción A](../history/AUDIT-authority-consistency.md) | 2026-09-07 |
| [ADR-019](ADR-019-integracion-ankla-por-contrato.md) | Integración skevi↔AN-KLA por contrato condicional | Aceptado | `05` §6, `04` §7 | [PROP-008](../history/PROP-008-integracion-ankla-por-contrato.md) | 2026-09-07 |

**Reglas de este índice**

- Estado: solo `Aceptado` figura aquí; rechazados, diferidos o sustituidos se
  registran en el ADR que los reemplaza o en `docs/history/`.
- Implementación: commit, archivo o sección donde la decisión se materializó.
- Origen: si procede de una propuesta, se vincula; si es fundacional o externa,
  se declara como tal.
- Fecha: del commit o decisión que originó el ADR, no de la última edición.
