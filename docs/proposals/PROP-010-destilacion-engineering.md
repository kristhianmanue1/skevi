# PROP-010 — Destilación de Engineering 1.2.0: revisión, diagnóstico e incidentes

> **Estado:** EN DELIBERACIÓN, en `fix-and-retry`. La ronda de contexto
> fresco (§6.2) **ya se ejecutó** el 2026-09-16 y devolvió `fix-and-retry`
> con 2 HIGH, 3 MED y 1 LOW; su disposición está en §6.2 y su registro
> gateado en `../reviews/2026-09-17-prop010-t03.md`. Falta una ronda nueva
> sobre el texto corregido y la aceptación humana registrada (§7). Sin ADR
> ni cambio normativo todavía.
> **Formato:** compacto por decisión del Operador (§2, D-D2): propuesta,
> rondas y decisión en un solo archivo. Al cerrar se mueve a `docs/history/`
> en el mismo cambio que implemente la decisión (`02` §3.3). MED-1 de la
> ronda T03 obligó a una excepción puntual —el registro textual de esa ronda
> vive en `docs/reviews/` para que el gate lo descubra, y aquí queda su
> disposición—; generalizar ese reparto a las rondas siguientes sería
> estrechar D-D2, así que **no** se hace desde aquí: se propone en §7 y lo
> decide el Operador.
> **Origen:** instrucción directa del Operador en conversación (claude.ai,
> 2026-09-16/17). Base original: `main` `a918ceb`; rebasada sobre `main`
> `c2f3720` (v1.4.0) el 2026-09-17. Rama
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

Plantillas nuevas en `templates/skevi/` (salto al siguiente
`plantillas/vN` libre, comprobado contra `main` vigente; no breaking), para que `check_templates` emita señal de
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
  términos de framework o motor. La independencia de plataforma se acredita
  por revisión documentada de supuestos y dependencias, **no** por una
  búsqueda de palabras: una expresión de ese tipo acepta `FastAPI` y rechaza
  `reactivar`, así que sirve de rastreo auxiliar y nada más. Si se usa, va
  con ruta explícita sobre el archivo del catálogo —no sobre el árbol— y se
  interpreta por sus coincidencias, no por su código de salida.
- **REQ-P10-02 — diagnóstico.** Sección del catálogo que da forma al
  "diagnóstico escrito" de `04` §8: reproducción, aislamiento, hipótesis con
  su prueba, causa raíz separada del síntoma.
- **REQ-P10-03 — postmortem.**
  - Minimización obligatoria con frontera declarada, no sólo enunciada
    (estándar §2.3, §2.4, §7). Permitido: identificador de incidente propio
    del postmortem, componente, versión, marca temporal y resultado. Excluido
    sin excepción: identificadores de paciente, de cuenta o de expediente,
    URL que resuelvan a un registro identificable, volcados de payload, y
    cualquier referencia interna que permita reidentificar por cruce. La
    evidencia cruda vive fuera del repositorio y se cita por hash.
  - Comprobación de saneado **antes** de indexar o commitear, registrada como
    línea de evidencia. Cubre el contenido que está a punto de entrar; lo que
    ya entró no está a su alcance y lo cubre la viñeta siguiente.
  - **Revisión del historial antes de publicar**, como paso propio: antes de
    abrir el PR se revisan los commits del rango que se publica —no sólo el
    árbol final— buscando lo que la lista de arriba excluye. La hace quien
    publica, deja su propia línea de evidencia, y su única salida cuando
    encuentra algo es **escalar**: un borrador con datos sensibles ya
    commiteado no se arregla saneando el archivo final, porque el dato sigue
    en el historial.
  - Casos de aceptación sintéticos obligatorios, sin los cuales las dos
    comprobaciones de arriba no tienen contra qué ejecutarse: (1) un postmortem
    con identificador de paciente en el cuerpo; (2) uno con una URL que
    resuelve a un registro identificable; (3) uno saneado cuyo borrador
    anterior ya está commiteado. Los casos (1) y (2) ejercitan la
    comprobación de saneado y pasan cuando ésta los detiene antes de indexar.
    El caso (3) ejercita la revisión del historial de la viñeta anterior, y
    pasa cuando esa revisión lo detecta y el asunto se escala, registrado como
    hallazgo con estado. El humano decide entonces entre reescribir el
    historial con la autorización que eso exige (estándar §4.3, que lista
    `git rebase` de historia compartida entre las operaciones con
    autorización previa) o aceptar el riesgo por escrito. Cerrarlo saneando
    el archivo final no es una opción en ninguno de los tres.
  - Esto es cumplimiento por procedimiento, **no detección automática**: los
    gates de Skevi comprueban forma y no pueden ver un identificador sensible
    ni un borrador anterior (`project-manifest.yaml` §no_ofrece).
  - **Cruce de frontera declarado.** Enumerar categorías de dato sensible roza
    la «clasificación de sensibilidad de datos» que `project-manifest.yaml`
    declara `pospuesto`. La lista de arriba es frontera de proceso —qué no se
    escribe en un artefacto de este repositorio—, no un esquema de
    clasificación ni gobernanza de dominio. Si la aceptación de §7 la
    considera lo segundo, el ADR de §7 debe moverla o retirarla. El criterio
    se toma por analogía de ADR-026, que movió la línea de `no_ofrece` con un
    ADR propio en vez de reinterpretarla desde otro documento; ese ADR no
    enuncia ninguna regla sobre los ítems `pospuesto`, así que la analogía es
    rechazable y §7 A la pone a decisión.
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
    de aprobación, aviso posterior obligatorio.
  - **La lista no es la autoridad; la acredita.** Cada entrada referencia el
    folio de aceptación y la revisión aprobada del runbook. Antes de cada
    ejecución se verifica que el folio sigue vigente, que no fue revocado,
    que el alcance declarado cubre la situación observada y que ninguna
    restricción local más estricta lo prohíbe. Esa verificación se registra
    como línea de evidencia **antes** de ejecutar —comando o fuente →
    resultado, estándar §7—: una comprobación sin artefacto es
    indistinguible de no haberla hecho. Ante cualquier duda de vigencia,
    alcance o entorno: **no se ejecuta**, se escala. Un runbook viejo o
    copiado con los seis campos completos no autoriza nada por sí solo.
  - El rollback se autoriza aparte: estar preautorizada la mitigación no
    preautoriza deshacerla.
  - Lo no listado sigue gateado (estándar §4.3, §6.6). La preautorización
    nunca aplica en el repositorio Skevi, donde rige la restricción local de
    `AGENTS.md` (ADR-018); el riesgo que cubre esta regla es el del adoptante
    que la copie.

### 3.3 Vía de lectura y presupuesto

La ocupación vigente la emite el gate en su línea de salida; este documento
no la transcribe (ADR-025, punto 4: una cifra copiada aquí envejece antes de
que se cierre la propuesta). Lo que sí se declara es el **coste del cambio**:
dos líneas, una en `00-INDICE.md` hacia las plantillas operativas y otra en
`04` §5.1 hacia el catálogo. El techo es 1000, sólo sube con un ADR que dé su
razón (punto 2) y **no** queda congelado por la ocupación del momento;
bajarlo tras comprimir norma no exige ADR (punto 3). Antes de implementar se
comprueba con `python3 scripts/check_sizes.py` que las dos líneas caben; si
no caben, la salida es la de §3.4 del estándar —borrar lo muerto, separar por
vida útil, partir por audiencia o exentar, que son las cuatro del estándar—
o la quinta que añade ADR-025: un ADR que suba el techo con su razón escrita.
Todas son decisiones; ninguna es un ajuste silencioso.

Alternativa evaluada y descartada: el puntero al catálogo en `01`, `02` o
`03` costaría cero líneas, porque de las alternativas sólo cuenta la mayor y
el peor caso es `04`. No se descarta por el gate —esos cuatro archivos están
igualmente dentro de la ruta medida, así que no habría evasión ninguna— sino
por pertinencia: el catálogo se usa en la ronda de `04` §5 y ahí es donde un
ejecutor lo busca. El presupuesto no decide dónde vive una regla.

Sin cambios en `scripts/` (`check_sizes.py` 867/870 el 2026-09-17).

### 3.4 Cambios colaterales

- `project-manifest.yaml`: propósito y `ofrece` reescritos explícitamente
  para incluir operación (D1), no por acumulación.
- `docs/crosswalk-estandares.md`: fila RV.2 cita postmortem y runbook;
  resumen recontado contra filas.
- `skevi-gate.json`: plantillas nuevas en `required`.
- `docs/MANIFEST.json`: salto al siguiente `corpus/vN` libre por los
  cambios en `00` y `04` (ADR-032).
- Antes de implementar, barrido completo de identificadores y versiones
  caducados contra `main` vigente —número de ADR libre, versión de
  plantillas, de corpus y de gate, y cifras medidas—: esta propuesta ya
  envejeció dos veces por citarlos de una base anterior.

### 3.5 Madurez

Cada plantilla nueva declara en su encabezado **estado experimental**,
textual (sin campo de esquema: cambiarlo tocaría `scripts/`). Sale de
experimental cuando se cumplen las cuatro condiciones: criterios de
aceptación definidos **antes** de aplicarla; aplicación en un caso real de un
adoptante con evidencia registrada; resultado atado a la revisión concreta de
la plantilla que se probó; y disposición escrita de los hallazgos que
arrojó. Un piloto fallido con evidencia registrada **no** la saca de
experimental. El caso lo elige el Operador, y la salida la acepta él por
escrito: un caso sigue siendo evidencia de ese caso, no validación general.

## 4. Rechazado

| Skill | Razón |
|---|---|
| `architecture` | `02` §3.2 ya exige alternativas con razón de descarte y desempate |
| `system-design` | Cubierto por `02` §2, §4 y §5 |
| `testing-strategy` | `04` §3 norma el proceso; la pirámide es genérica |
| `tech-debt` | Duplica el backlog de issues (estándar §5.3). La objeción por ADR-009 se retira de aquí: precisar su alcance es materia del ADR de §7, no de esta celda |
| `standup` | Comunicación ritual; reportes en dos capas cubren estado |
| `deploy-checklist` | Fuera por B2; reconsiderable con ADR corto |
| Conectores | Acoplan proveedor; equivalente agnóstico en estándar §6.8 |

## 5. Hueco preexistente (F1)

`templates/plan-de-implementacion.md` y `templates/registro-contexto.md` no
estaban en ningún MANIFEST: no emitían drift. Fuera de esta propuesta; se
registró en issue aparte, como decidió F1.

**Resuelto el 2026-09-18**, fuera del alcance de esta propuesta:
[ADR-036](../adr/ADR-036-hogar-unico-de-plantillas.md) las movió a
`templates/skevi/`, donde el manifiesto vigente las cubre con listado exacto
y digests (issue #48). Las plantillas nuevas que propone §3.1 siguen yendo a
ese mismo directorio; lo que cambia es el salto de versión de partida. Por
eso §3.1 y §3.4 dejaron de nombrar números concretos en este mismo cambio:
`plantillas/v9` y `corpus/v3` ya los consumió ADR-036.

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

**EJECUTADA** el 2026-09-16 por otra herramienta y otro modelo (Codex, GPT-6
**autodeclarado desde las instrucciones de su entorno**: la identidad
efectiva del revisor no se verificó de forma independiente, y el valor de
esta ronda como contexto fresco descansa en ella), sandbox de sólo lectura,
sobre la base `a918ceb` y sobre el archivo con SHA-256
`c389ca32…963b1dbe0`. **Decisión: `fix-and-retry`** — 2 HIGH, 3 MED, 1 LOW.

El informe vive textual, con su envoltorio de registro gateado, en
`../reviews/2026-09-17-prop010-t03.md`. No se anexa aquí por el motivo que da
MED-1: dentro de esta propuesta el gate de reportes no lo descubre —su
`reports.dir` es `docs/reviews`—, así que una capa técnica malformada se
colaría sin que nada lo dijera. El formato compacto (D-D2) se conserva para
la disposición, que es lo que sí vive aquí. Esto es lo que se hizo **con esta
ronda**; que valga para las siguientes es un ajuste de D-D2 y por tanto
decisión del Operador, planteada en §7.

| # | Hallazgo de T03 | Impacto si no se corrige | Corrección aplicada | Estado |
|---|---|---|---|---|
| HIGH-1 | La lista de mitigaciones preautorizadas es confundible con autoridad de ejecución | Un runbook viejo o copiado ejecuta una mitigación cuya autorización fue revocada o cuyo entorno cambió, sin que nadie lo note | REQ-P10-04: la lista acredita, no autoriza; folio y revisión aprobada; verificación de vigencia, alcance y restricción local registrada como evidencia antes de ejecutar; rollback aparte; escalar ante duda | cerrado |
| HIGH-2 | Minimización de datos sin frontera operativa | Un identificador de paciente o una URL identificable entra al repositorio, o un borrador sensible queda en el historial pese a sanear el archivo final | REQ-P10-03: lista cerrada de referencias permitidas y excluidas; evidencia cruda fuera del repo citada por hash; comprobación de saneado antes de indexar; historial cubierto; tres casos de aceptación sintéticos; declaración de que es procedimiento y no detección | cerrado |
| MED-1 | El registro compacto de rondas queda fuera del gate de reportes | Una capa técnica malformada o con hash roto se archiva en `docs/history/` sin que ningún comando la haya verificado | Registro externo de **esta** ronda en `docs/reviews/`, con capa técnica canónica y `report_sha256` reproducible; validación con `python3 scripts/check_reports.py`, cuyo resultado se retiene como evidencia del cambio | cerrado en lo aplicado; generalizar el reparto a las rondas siguientes es decisión del Operador, planteada en §7 |
| MED-2 | El criterio de salida de «experimental» acepta un piloto fallido | Una plantilla pierde la etiqueta experimental sin haber demostrado utilidad ni resuelto sus hallazgos | §3.5: cuatro condiciones, entre ellas criterios de aceptación previos, resultado atado a la revisión probada y disposición escrita de hallazgos | cerrado |
| MED-3 | El rechazo de `tech-debt` malaplica ADR-009 | Un adoptante concluye que priorizar deuda está normativamente prohibido | §4: se rechaza por duplicar el backlog; precisar el alcance de ADR-009 se remite al ADR de §7 | cerrado |
| LOW-1 | La prueba por palabras clave no acredita independencia de plataforma | Material específico de framework pasa el filtro y prosa española corriente lo falla | REQ-P10-01: la búsqueda pasa a rastreo auxiliar con ruta explícita; la independencia se acredita por revisión documentada de supuestos y dependencias | cerrado |

Tres límites de la ronda, declarados y **no** cerrados: la procedencia
upstream de §1.1 quedó `inconclusive` —el sandbox no podía verla, así que
hashes, licencia y cronología siguen siendo afirmación del productor—; las
decisiones del Operador de §2 quedaron `inconclusive` por no aportarse su
registro original; y la identidad del revisor, autodeclarada y no verificada,
es un `inconclusive` sobre la independencia de esta misma ronda. Los tres se
arrastran a §7, donde la aceptación los asume con nombre.

### 6.3 Ronda sobre el texto corregido

PENDIENTE. `04` §5.3, segunda viñeta: tras corregir un hallazgo se repiten
los checks afectados, y la ronda **si el cambio fue material** según los
cuatro disparadores objetivos. Ninguno de los cuatro aplica a un cambio
documental como este, así que lo que la guía exige aquí es **una ronda propia
honesta** (§5.3, cierre del bloque de disparadores), no contexto fresco. Lo
que la eleva a contexto fresco es la **instrucción directa del Operador** en
la conversación que autorizó estas correcciones (AGENTS.md, prioridad 1). En
ningún caso la justifica un adjetivo sobre la gravedad del cambio: ese
criterio subjetivo es justo lo que ADR-008 prohíbe. El ciclo termina en
`proceed` o `escalate`, nunca en «ya está bien».

## 7. Decisión

PENDIENTE (T04). Requiere, tras **§6.3** en `proceed` —§6.2 quedó en
`fix-and-retry` de forma permanente: es historia, no una condición que pueda
satisfacerse—: aceptación humana con fecha, alcance y folio; creación de
**ADR-035** con su fila en
`docs/adr/00-INDICE.md` — ADR-034 ya está ocupado por el gate en CI remoto
(v1.4.0), y el número libre se comprueba contra `main` vigente, no contra
esta línea. Sin esa aceptación no hay ADR ni plan.

La aceptación asume explícitamente **tres límites** que ninguna ronda
cerró:

1. **Procedencia upstream `inconclusive` (§1.1).** Hashes, licencia Apache-2.0,
   ausencia de `NOTICE` y cronología son afirmación del productor: la ronda de
   contexto fresco no tenía acceso a la copia upstream para verificarlos. Si
   la atribución por archivo de §3.1 importa, esa verificación se hace antes
   de firmar, no después.
2. **Decisiones del Operador `inconclusive` (§2).** D1, A1, B2, C2a, D-D2, F1
   y T01/T03 se registran aquí como declaración atribuida; su aceptación
   original no se aportó como registro. La firma de §7 es lo que las
   convierte en decisión verificable.

3. **Identidad del revisor de §6.2 `inconclusive`.** «Codex, GPT-6» es
   autodeclarado; nadie verificó qué modelo respondió. Si la independencia de
   esa ronda es condición de la aceptación, hay que reejecutarla con
   procedencia verificable.

Y **dos decisiones de alcance**, que no son límites sino preguntas que la
firma responde:

A. **Cruce de frontera en REQ-P10-03.** La lista cerrada de referencias
   excluidas enumera categorías de dato sensible, y `project-manifest.yaml`
   declara `pospuesto` la «clasificación de sensibilidad de datos». La
   pregunta que la aceptación responde: ¿es frontera de proceso —qué no se
   escribe en un artefacto de este repositorio— o esquema de clasificación?
   Si lo primero, el ADR de §7 lo declara así y la frontera declarada no se
   mueve. Si lo segundo, la lista se retira o se mueve: el precedente es
   ADR-026, que precisó la línea de `no_ofrece` mediante un ADR propio en vez
   de reinterpretarla desde otro documento. ADR-026 no enuncia esa regla para
   `pospuesto`; se aplica su criterio por analogía, y quien firme puede
   rechazar la analogía.
B. **Registro de rondas.** ¿Se generaliza el reparto que MED-1 obligó a hacer
   en §6.2 —registro textual de cada ronda en `docs/reviews/`, disposición
   aquí— o sigue rigiendo D-D2 sin excepción más allá de la ronda T03?
   Estrecharlo desde el texto de esta propuesta sería reinterpretar una
   decisión del Operador, así que se plantea y no se aplica.

Aceptar los tres límites sin resolverlos es una opción legítima, pero entonces
quedan como riesgos residuales aceptados con nombre, no como huecos
silenciados. Las dos preguntas de alcance sí requieren respuesta: de A depende
si la lista de REQ-P10-03 se queda, y de B si el reparto de §6.2 es excepción
o norma.

## 8. Trabajo derivado tras aceptar

El plan de implementación se escribe en `docs/plans/` sólo después de
ADR-035: T05 (catálogo y diagnóstico), T06 (postmortem, runbook, vía de
lectura, manifest, crosswalk, gate config, salto de plantillas y corpus).
Commit, push y merge se autorizan uno a uno (`AGENTS.md`).
