# PROP-010 — Destilación de Engineering 1.2.0: revisión, diagnóstico e incidentes

> **Estado:** EN DELIBERACIÓN. Falta la ronda de contexto fresco (§6.2) y la
> aceptación humana registrada (§7). Sin ADR ni cambio normativo todavía.
> **Formato:** compacto por decisión del Operador (§2, D-D2): propuesta,
> rondas y decisión en un solo archivo. Al cerrar se mueve a `docs/history/`
> en el mismo cambio que implemente la decisión (`02` §3.3).
> **Origen:** instrucción directa del Operador en conversación (claude.ai,
> 2026-09-16/17). Base: `main` `a918ceb`; rama
> `docs/prop-010-engineering-distillation`.
> **Autor:** agente redactor en claude.ai; autorrevisiones de la misma
> instancia (§6.1), no independientes.

## 1. Contexto

El plugin Engineering 1.2.0 de Anthropic ofrece diez skills (code-review,
debug, incident-response, deploy-checklist, documentation, architecture,
system-design, testing-strategy, tech-debt, standup) y conectores MCP. Es un
productor de entregables; Skevi es norma de proceso. Se propone **destilar**
contenido agnóstico —criterios y estructuras— reescrito con las garantías de
Skevi, sin importar mecanismos de proveedor (slash commands, frontmatter de
skills, `.mcp.json`).

### 1.1 Procedencia verificada (T01)

- Copia local: `/Users/krisnova/www/playGround/Engineering-1.2.0-v38`
  (14 archivos, sin `LICENSE`).
- Coincidencia exacta por SHA-256 de los 14 archivos con
  `anthropics/knowledge-work-plugins@58da91d19dac075bc4d6dc2071500eeba3178c4b`
  (2026-05-19), y con el árbol `engineering/` de `HEAD` `bdf7160` observado
  el 2026-09-17. Las 8 revisiones anteriores difieren (2 a 18 líneas de
  hash).
- Licencia: Apache-2.0 en esa revisión (212 líneas, con texto ajeno al final
  del archivo). Sin archivo `NOTICE`: no aplica §4(d). Skevi es Apache-2.0:
  compatible.
- Cadencia upstream de `engineering/`: 9 commits entre 2026-02-23 y
  2026-05-19; ninguno posterior hasta la observación.
- Corrección a un hallazgo previo: las URL vacías de `gmail` y
  `google calendar` en `.mcp.json` son marcadores intencionales de upstream
  (commit `3b505c1`, #184), no configuración rota por error.

## 2. Decisiones del Operador ya tomadas

Tomadas en conversación el 2026-09-16/17. Se registran aquí como
**declaración del Operador**; su aceptación formal con fecha y alcance va en
§7.

| ID | Decisión |
|---|---|
| D1 | Respuesta a incidentes y postmortems entran en el alcance de Skevi |
| A1 | Toda la destilación vive en Skevi; repositorio o fork separado en suspenso |
| B2 | Se destilan catálogo de defectos, diagnóstico, postmortem y runbook; preparación de despliegue queda fuera |
| C2a | Mitigaciones preautorizadas en runbook; aprueba el responsable humano; el impacto de dominio (p. ej. clínico) lo asigna un profesional nombrado |
| D-D2 | Ciclo completo en formato compacto (este archivo) |
| F1 | Hueco preexistente de plantillas raíz sin MANIFEST: issue aparte |
| T01/T03 | Autorizados: procedencia con red de lectura; ronda fresca con Codex |

## 3. Propuesta

### 3.1 Qué se destila y dónde

Plantillas nuevas en `templates/skevi/` (salto `plantillas/v7` →
`plantillas/v8`, no breaking), para que `check_templates` emita señal de
drift. Nombres en inglés, prosa en español (ADR-015, ADR-029).

| Archivo | Fuente upstream | Tipo de derivación |
|---|---|---|
| `review-defect-catalog.md` | `code-review`, `debug` | Derivada: atribución por archivo |
| `postmortem.md` | `incident-response` | Mayormente original; atribución en ADR |
| `runbook.md` | `documentation` (sección runbook) | Mayormente original; atribución en ADR |

### 3.2 Requisitos

- **REQ-P10-01 — catálogo.** Clases agnósticas de lenguaje y plataforma:
  entrada no confiable e inyección (incluye OWASP LLM01 y LLM05),
  autorización, secretos, concurrencia, recursos no liberados, trabajo no
  acotado, errores silenciados, contrato roto y test que no prueba el
  requisito. Cada clase con pregunta de ataque y evidencia esperada. Sin
  términos de framework o motor: verificable con
  `rg -i 'sql|xss|csrf|n\+1|react|django|postgres|mysql|mongo'` → 0.
- **REQ-P10-02 — diagnóstico.** Sección del catálogo que da forma al
  "diagnóstico escrito" de `04` §8: reproducción, aislamiento, hipótesis con
  su prueba, causa raíz separada del síntoma.
- **REQ-P10-03 — postmortem.**
  - Minimización obligatoria: sin datos personales ni clínicos
    identificables; referencias a identificadores internos (estándar §2.3).
  - Severidad técnica por disparadores observables **separada** del impacto
    de dominio; este último lo asigna un profesional nombrado, nunca el
    agente.
  - Línea de tiempo en UTC; evidencia `pass|fail|inconclusive`; causa raíz
    con procedencia; hallazgos con estado (`cerrado|abierto|aceptado como
    riesgo`); riesgos residuales enumerados.
- **REQ-P10-04 — runbook.**
  - Precondiciones verificables; pasos con verificación; rollback; escalado.
  - Mitigaciones preautorizadas (C2a) en lista cerrada: acción exacta,
    disparador observable, alcance, reversibilidad, aprobador humano y fecha
    de aprobación, aviso posterior obligatorio. Lo no listado sigue gateado
    (estándar §4.3, §6.6). La preautorización nunca aplica en el repositorio
    Skevi, donde rige la restricción local de `AGENTS.md` (ADR-018).

### 3.3 Vía de lectura y presupuesto

Ruta de lectura medida con `wc -l` el 2026-09-16: 993/1000 (AGENTS 105,
00-INDICE 114, estándar 501, peor caso `04` 273). Se añade una línea en
`00-INDICE.md` hacia las plantillas operativas y una en `04` §5.1 hacia el
catálogo: objetivo ≈995. Sin cambios en `scripts/` (`check_sizes.py`
867/870).

### 3.4 Cambios colaterales

- `project-manifest.yaml`: propósito y `ofrece` reescritos explícitamente
  para incluir operación (D1), no por acumulación.
- `docs/crosswalk-estandares.md`: fila RV.2 cita postmortem y runbook;
  resumen recontado contra filas.
- `skevi-gate.json`: plantillas nuevas en `required`.
- `docs/MANIFEST.json`: salto de corpus por los cambios en `00` y `04`
  (ADR-032).

### 3.5 Madurez

Cada plantilla nueva declara en su encabezado **estado experimental**,
textual (sin campo de esquema: cambiarlo tocaría `scripts/`). Sale de
experimental cuando se aplica en al menos un caso real de un adoptante con
evidencia registrada. El caso lo elige el Operador.

## 4. Rechazado

| Skill | Razón |
|---|---|
| `architecture` | `02` §3.2 ya exige alternativas con razón de descarte y desempate |
| `system-design` | Cubierto por `02` §2, §4 y §5 |
| `testing-strategy` | `04` §3 norma el proceso; la pirámide es genérica |
| `tech-debt` | Puntuación subjetiva (contra ADR-009); los issues ya son backlog (estándar §5.3) |
| `standup` | Comunicación ritual; reportes en dos capas cubren estado |
| `deploy-checklist` | Fuera por B2; reconsiderable con ADR corto |
| Conectores | Acoplan proveedor; equivalente agnóstico en estándar §6.8 |

## 5. Hueco preexistente (F1)

`templates/plan-de-implementacion.md` y `templates/registro-contexto.md` no
están en ningún MANIFEST: no emiten drift. Fuera de esta propuesta; se
registra en issue aparte.

## 6. Rondas

### 6.1 Autorrevisiones de la misma instancia (no independientes)

Resumen de hallazgos incorporados arriba:

| Ronda | Hallazgo decisivo | Resolución |
|---|---|---|
| H | Catálogo dentro de `04` excedía el presupuesto (BLOCKER) | Plantilla fuera de la ruta; puntero de 1 línea |
| H | Checklist web contradice independencia de plataforma | Clases agnósticas (REQ-P10-01) |
| H | Postmortem sí amplía alcance | Decisión D1 |
| P | Plan autorizado por el ADR que producía (BLOCKER) | Fase previa T01–T04 separada del PLAN |
| P | Rutas sin backticks: regla E5 de `check_plans` no verificaba nada | Backticks y `crea` en Produce |
| A | Postmortem sin minimización de datos | REQ-P10-03 |
| A | Severidad clínica asignable por agente | Separación técnica/dominio |
| A | Autorización uno a uno vs urgencia | Mitigaciones preautorizadas (C2a) |
| A | Plantillas en raíz sin drift | `templates/skevi/` (§3.1) |
| A | `corpus-installed.json` usado como registro real | Verificar con registro de adoptante o fixture |

### 6.2 Ronda de contexto fresco (T03)

PENDIENTE. Otra sesión y otro modelo (Codex), sandbox de sólo lectura,
formato `04` §5.2 en dos capas. Se anexa aquí sin editar su contenido.

## 7. Decisión

PENDIENTE (T04). Requiere, tras §6.2 en `proceed`: aceptación humana con
fecha, alcance y folio; creación de ADR-034 con su fila en
`docs/adr/00-INDICE.md`. Sin esa aceptación no hay ADR ni plan.

## 8. Trabajo derivado tras aceptar

El plan de implementación se escribe en `docs/plans/` sólo después de
ADR-034: T05 (catálogo y diagnóstico), T06 (postmortem, runbook, vía de
lectura, manifest, crosswalk, gate config, salto de plantillas y corpus).
Commit, push y merge se autorizan uno a uno (`AGENTS.md`).
