# Índice de decisiones arquitectónicas (ADR)

| ADR | Título | Estado | Implementación | Origen | Fecha |
|---|---|---|---|---|---|
| ADR-002 | Separación de docs por vida útil | Aceptado | Estructura de `docs/` | Fundacional | 2026-08-12 |
| ADR-003 | Directorios canónicos en inglés | Aceptado | Estructura de `docs/` | Instrucción directa | 2026-08-14 |
| ADR-004 | Graduar fail-closed por clase de operación | Aceptado | `f46dcca` | PROP-003 §3.1 | 2026-08-17 |
| ADR-005 | Resultado por línea de evidencia | Aceptado | `f46dcca` | PROP-003 §3.2 | 2026-08-17 |
| ADR-006 | Gate configurable por proyecto adoptante | Aceptado | `scripts/check_sizes.py` | PROP-002 §A-6 | 2026-08-15 |
| ADR-007 | Validar en la frontera implica fallar controlado | Aceptado | `estandar-diseno-software-github.md` §2.4 | `an-kla-memory` #84 | 2026-08-16 |
| ADR-008 | Disparadores objetivos de rigor | Aceptado | `AGENTS.md`, `04-ejecucion-y-verificacion.md` | PROP-002 §A-8 | 2026-08-15 |
| ADR-009 | Clasificación de tarea por disparadores observables | Aceptado | `01-analisis-y-requerimientos.md` §2, `04` §1 | PROP-004 §2 A-1 | 2026-08-20 |
| ADR-010 | Plan de implementación como artefacto de escala | Aceptado | `templates/skevi/plan-de-implementacion.md` (hogar movido por ADR-036; el cuerpo del ADR conserva la ruta de su fecha), `03` §2, `04` §1 | PROP-004 §2 A-2 | 2026-08-20 |
| ADR-011 | RED-GREEN-REFACTOR como default condicional de F3 | Aceptado | `04-ejecucion-y-verificacion.md` §3 | PROP-004 §2 A-3 | 2026-08-20 |
| ADR-012 | Los archivos de test nuevos no escalan la clase de una tarea | Aceptado | `01-analisis-y-requerimientos.md` §2, ADR-009 (Estado) | `piloto-orbitanova.md` PF-1 | 2026-08-20 |
| ADR-013 | Crear un plan de implementación es disparador de Architectural | Aceptado | `01-analisis-y-requerimientos.md` §2 | `piloto-orbitanova-2.md` PF-2 | 2026-08-20 |
| ADR-014 | Gate de planes con chequeo estructural mínimo (A-4) | Aceptado | `scripts/check_plans.py`, `skevi-gate.json` clave `plans` | PROP-004 §A-4 (condición cumplida) | 2026-08-20 |
| ADR-015 | Convención de idioma: código en inglés, cara al usuario en el idioma del proyecto | Aceptado | `estandar-diseno-software-github.md` §3.1 | Instrucción directa | 2026-09-07 |
| ADR-016 | Reportes de agente en dos capas con bloque de trazabilidad | Aceptado | `00-INDICE.md`, `04` §5.2, estándar §6 | PROP-006 | 2026-09-07 |
| ADR-017 | Autoridad Git graduada (Z1-Z3) con gate delegable | Aceptado | estándar §6.2/§6.6/§4.3, `project-manifest.yaml` | PROP-007 | 2026-09-07 |
| [ADR-018](ADR-018-coherencia-de-autoridad.md) | Coherencia de autoridad general y restricción local | Aceptado | `29243f1` | [T05, opción A](../history/AUDIT-authority-consistency.md) | 2026-09-07 |
| [ADR-019](ADR-019-integracion-ankla-por-contrato.md) | Integración skevi↔AN-KLA por contrato condicional | Aceptado | `05` §6, `04` §7 | [PROP-008](../history/PROP-008-integracion-ankla-por-contrato.md) | 2026-09-07 |
| [ADR-020](ADR-020-adopcion-versionado-plantillas.md) | Adopción del versionado de plantillas (PROP-006@#28 + T09) | Aceptado | `0be3f05` (PR #35): `templates/skevi/MANIFEST.json`, `scripts/check_templates.py`, gate local | [PROP-006@#28](https://github.com/kristhianmanue1/skevi/issues/28), [T09](../proposals/AUDIT-template-provenance.md) | 2026-09-08 |
| [ADR-021](ADR-021-presupuesto-de-ruta-de-lectura.md) | Presupuesto de la ruta de lectura obligatoria | Aceptado | `scripts/check_sizes.py` clave `reading_path`, estándar §3.4 | [SPEC-M6 REQ-M6-05](../specs/SPEC-M6-2026-09-07-seis-mejoras.md) | 2026-09-07 |
| [ADR-022](ADR-022-gate-de-reportes-de-dos-capas.md) | Gate estructural de reportes de dos capas | Aceptado | `scripts/check_reports.py`, `skevi-gate.json` clave `reports` | [SPEC-M6 REQ-M6-02](../specs/SPEC-M6-2026-09-07-seis-mejoras.md) | 2026-09-07 |
| [ADR-023](ADR-023-superficie-de-ejecucion.md) | Superficie de ejecución declarada del ejecutor | Aceptado | estándar §6.8 | [PREGUNTA-M6-1, opción A](../specs/SPEC-M6-2026-09-07-seis-mejoras.md) | 2026-09-07 |
| [ADR-024](ADR-024-componentes-con-salida-no-determinista.md) | Complemento de fase para componentes con salida no determinista | Aceptado | `docs/ai-agent-guide/06-componentes-con-llm.md`, `04` §1 | [SPEC-M6 REQ-M6-04](../specs/SPEC-M6-2026-09-07-seis-mejoras.md) | 2026-09-07 |
| [ADR-025](ADR-025-trinquete-no-techo-derivado.md) | El presupuesto de lectura es un trinquete, no un techo derivado | Aceptado | estándar §3.4; sustituye la cláusula de techo de ADR-021 | Ronda adversarial 2026-09-08 | 2026-09-08 |
| [ADR-026](ADR-026-fronteras-unilaterales-y-alcance-de-artefacto.md) | Precisión de la frontera de autoridad y alcance de artefacto | Aceptado | `project-manifest.yaml` §no_ofrece y §fronteras_de_confianza | [PREGUNTA-M6-3, opción A](../specs/SPEC-M6-2026-09-07-seis-mejoras.md) | 2026-09-08 |
| [ADR-027](ADR-027-identidad-y-caducidad-del-gate-copiable.md) | Identidad y autocaducidad del gate copiable | Aceptado | `scripts/check_sizes.py` (`GATE_VERSION`, `gate_staleness`) | Barrido de adoptantes (documento de origen retirado, ver ADR) | 2026-09-08 |
| [ADR-028](ADR-028-manifest-de-scripts.md) | Extensión del versionado de MANIFEST a scripts/ | Aceptado | `scripts/MANIFEST.json`, `templates/skevi/scripts-installed.json`, `check_templates.py` (segunda familia de esquema) | Instrucción directa | 2026-09-08 |
| [ADR-029](ADR-029-eleccion-de-idioma-humano.md) | Elección explícita del idioma humano | Aceptado | Estándar §3.1, F0/F3 y plantilla usage-guide; incremento local sin commit | Instrucción directa | 2026-09-12 |
| [ADR-030](ADR-030-gate-mide-disco.md) | El gate mide el disco, no el índice de Git | Aceptado | `scripts/check_sizes.py` (gate/v4), clave `exempt_names` | [Issue #41](https://github.com/kristhianmanue1/skevi/issues/41); instrucción directa | 2026-09-13 |
| [ADR-031](ADR-031-procedencia-cerrada-source.md) | Procedencia cerrada del registro de instalación | Aceptado | `scripts/check_templates.py` (gate/v5), plantillas (plantillas/v5) | [PROP-002 §A-7](../history/PROP-002-decision-2026-08-15.md); [issue #40](https://github.com/kristhianmanue1/skevi/issues/40) | 2026-09-13 |
| [ADR-032](ADR-032-manifiesto-de-corpus.md) | Manifiesto de corpus: el canon normativo versionado | Aceptado | `docs/MANIFEST.json` (corpus/v1), `check_sizes.py`/`check_templates.py` (gate/v6), plantillas (plantillas/v6) | [Issue #40](https://github.com/kristhianmanue1/skevi/issues/40) §2; [PROP-002-correcciones](../history/PROP-002-correcciones-desde-adoptantes.md) §4 | 2026-09-13 |
| [ADR-033](ADR-033-arboles-congelados.md) | Complemento de adopción para árboles congelados (aterriza A-2) | Aceptado | `templates/skevi/frozen-trees.md` (plantillas/v7) | [PROP-009](../history/PROP-009-codigo-generado-congelado.md); [issue #43](https://github.com/kristhianmanue1/skevi/issues/43); PROP-002 §A-2 | 2026-09-13 |
| [ADR-034](ADR-034-gate-en-ci-remoto.md) | Gate en CI remoto; hook local como verificación rápida (sustituye ADR-001) | Aceptado | `.github/workflows/skevi-gate.yml` | Instrucción directa; disparador de ADR-001 y [AUDIT-review-enforcement](../proposals/AUDIT-review-enforcement.md) §3 | 2026-09-17 |
| [ADR-035](ADR-035-catalogo-de-defectos-destilado.md) | Catálogo de clases de defecto, destilado de material ajeno | Aceptado | `templates/skevi/review-defect-catalog.md` (pendiente del plan de PROP-010 §8) | [PROP-010](../proposals/PROP-010-destilacion-engineering.md) §7, folio `SKV-ACC-PROP010-20260918-01` | 2026-09-18 |
| [ADR-036](ADR-036-hogar-unico-de-plantillas.md) | Hogar único de plantillas copiables en `templates/skevi/` | Aceptado | `templates/skevi/MANIFEST.json` (plantillas/v9), `check_sizes.py` (gate/v7), `docs/MANIFEST.json` (corpus/v3) | [Issue #48](https://github.com/kristhianmanue1/skevi/issues/48); hallazgo F1 de [PROP-010](../proposals/PROP-010-destilacion-engineering.md) §5 | 2026-09-18 |

**Reglas de este índice**

- Estado: solo `Aceptado` figura aquí; rechazados, diferidos o sustituidos se
  registran en el ADR que los reemplaza o en `docs/history/`.
- Implementación: commit, archivo o sección donde la decisión se materializó.
- Origen: si procede de una propuesta, se vincula; si es fundacional o externa,
  se declara como tal.
- Fecha: del commit o decisión que originó el ADR, no de la última edición.
