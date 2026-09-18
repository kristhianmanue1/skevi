# PROP-010 — Destilación de Engineering 1.2.0: revisión y diagnóstico

> **Estado:** **ACEPTADA** el 2026-09-18 (§7, folio
> `SKV-ACC-PROP010-20260918-01`), pendiente de que ADR-035 y el plan de §8
> la materialicen. Las rondas ejecutadas, sus veredictos, sus
> registros y dónde se dispone cada una están en **§6.5**, la única sección
> que los cuenta: este encabezado no los repite, porque una cifra copiada
> aquí caduca con la ronda siguiente. **Alcance recortado el 2026-09-18** (§7 A: no se amplía):
> queda una plantilla —catálogo de defectos y diagnóstico—, y salen
> postmortem, runbook y con ellos la minimización de datos, la custodia de
> evidencia y los folios. Falta la aceptación humana (§7). Sin ADR ni cambio
> normativo todavía.
> **Formato:** compacto por decisión del Operador (§2, D-D2): propuesta,
> rondas y decisión en un solo archivo, y al cerrar se mueve a
> `docs/history/` en el mismo cambio que implemente la decisión (`02` §3.3).
> Con una excepción **ya decidida** (§7 B, 2026-09-18): el registro textual
> de cada ronda vive en `docs/reviews/`, donde `check_reports` lo alcanza.
> ~~Y su disposición en este archivo~~ — esa segunda mitad la sustituyó
> **ADR-037** el mismo día: la disposición se va con el informe.
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

**Alcance tras la decisión del Operador del 2026-09-18 (§7 A: no se amplía).**
Skevi es «cuerpo normativo para diseñar software y para operar **agentes de
IA** que crean y mantienen proyectos». «Operar» ahí significa operar al
ejecutor, no operar sistemas en producción. Respuesta a incidentes y runbooks
son operación del sistema del adoptante: otro plano, otro dueño. De la
destilación queda lo que sí cae dentro —criterios para revisar código y para
diagnosticar un fallo, que es trabajo del ejecutor— y salen postmortem y
runbook. Con ellos salen también la minimización de datos, la custodia de
evidencia y los folios de autorización: nada de eso pertenece a un corpus
agnóstico que no toca sistemas en producción ni datos de nadie.

### 1.1 Procedencia verificada (T01)

- Copia verificada: el bundle que el Operador aportó al repositorio el
  2026-09-18, `docs/proposals/externals/Engineering-1.2.0-v38.zip` (14
  archivos, sin `LICENSE` dentro), fuera del control de versiones y del
  alcance del gate. La afirmación original citaba una copia en
  `~/www/playGround`; lo comprobado es el bundle, no aquella ruta.
- Coincidencia exacta por SHA-256 de los 14 archivos con
  `anthropics/knowledge-work-plugins@58da91d19dac075bc4d6dc2071500eeba3178c4b`
  (2026-05-19): **verificada uno a uno el 2026-09-18**. Las afirmaciones
  originales sobre `HEAD` `bdf7160` y sobre las 8 revisiones anteriores
  **no** se comprobaron y se retiran de aquí: no sostienen nada que la
  propuesta necesite, porque el único archivo que se deriva se atribuye
  contra la revisión nombrada arriba.
- Licencia: Apache-2.0 en esa revisión (212 líneas, con texto ajeno al final
  del archivo). Sin archivo `NOTICE`: no aplica §4(d). Skevi es Apache-2.0:
  compatible.
- Cadencia upstream de `engineering/`: 9 commits entre 2026-02-24 y
  2026-05-19; ninguno posterior hasta la observación.

**Verificado el 2026-09-18**, con el bundle que aportó el Operador y consulta
autorizada a GitHub oficial: los catorce archivos coinciden por SHA-256, la
licencia y la ausencia de `NOTICE` se confirman, y no hay commit posterior.
Evidencia y comandos en `../reviews/2026-09-18-prop010-procedencia.md`. La
fecha inicial de la cadencia se corrigió aquí: era 2026-02-24, no el 23.
Acredita procedencia, **no dependencia**: Skevi no copia código ni sigue ese
repositorio, y el bundle no se versiona.
- Corrección a un hallazgo previo: las URL vacías de `gmail` y
  `google calendar` en `.mcp.json` son marcadores intencionales de upstream
  (commit `3b505c1`, #184), no configuración rota por error.

## 2. Decisiones del Operador ya tomadas

Tomadas en conversación el 2026-09-16/17. Se registran aquí como
**declaración del Operador**; su aceptación formal con fecha y alcance va en
§7.

| ID | Decisión |
|---|---|
| D1 | ~~Respuesta a incidentes y postmortems entran en el alcance de Skevi~~ — **retirada por el Operador el 2026-09-18** (§7 A): confundía operar agentes con operar sistemas en producción. Skevi no amplía su alcance |
| A1 | Toda la destilación vive en Skevi; repositorio o fork separado en suspenso |
| B2 | ~~Se destilan catálogo de defectos, diagnóstico, postmortem y runbook~~ — **acotada el 2026-09-18** a catálogo de defectos y diagnóstico; postmortem, runbook y preparación de despliegue quedan fuera |
| C2a | ~~Mitigaciones preautorizadas en runbook~~ — **retirada el 2026-09-18**: exigía un registro de folios vigentes y revocados que Skevi no define, y construirlo sería gobernanza de autoridad, cedida en `project-manifest.yaml`. Sin runbook, la decisión queda sin objeto |
| D-D2 | Ciclo completo en formato compacto (este archivo) |
| F1 | Hueco preexistente de plantillas raíz sin MANIFEST: issue aparte |
| T01/T03 | Autorizados: procedencia con red de lectura; ronda fresca con Codex |
| §7 A | **No** se amplía el alcance declarado de Skevi a operación (2026-09-18) |
| §7 B | **Sí**: el registro textual de cada ronda vive en `docs/reviews/`; ~~en la propuesta queda su disposición~~ — **la segunda mitad la sustituye ADR-037** el mismo día: la disposición se va con el informe, porque dejarla aquí es lo que hizo que este documento necesitara rondas para arreglar su propia narración (2026-09-18) |

## 3. Propuesta

### 3.1 Qué se destila y dónde

Plantilla nueva en `templates/skevi/` (salto al siguiente
`plantillas/vN` libre, comprobado contra `main` vigente; no breaking), para que `check_templates` emita señal de
drift. Nombres en inglés, prosa en español (ADR-015, ADR-029).

| Archivo | Fuente upstream | Tipo de derivación |
|---|---|---|
| `review-defect-catalog.md` | `code-review`, `debug` | Derivada: atribución por archivo |

Una sola plantilla, tras acotar B2. Con ella la propuesta vuelve a ser lo que
su título dice: destilación de material ajeno, no obra propia con atribución
de cortesía — y por eso la atribución por archivo aquí sí importa, y al
escribirla hay que comprobar que no arrastra expresión literal del original
(REQ-P10-01 exige clases redactadas desde cero).

Efecto sobre quien ya adoptó, medido en copia: un adoptante en la versión
anterior de plantillas recibe un aviso de «re-copia opcional» y sale con
código 0. No es breaking y no exige migración; sí conviene que
`usage-guide.md` explique qué es la plantilla nueva, porque el aviso sólo da
el nombre del archivo.

### 3.2 Requisitos

- **REQ-P10-01 — catálogo.** Clases agnósticas de lenguaje y plataforma:
  entrada no confiable e inyección (incluye OWASP LLM01 y LLM05),
  autorización, secretos, concurrencia, recursos no liberados, trabajo no
  acotado, errores silenciados, contrato roto y test que no prueba el
  requisito. Cada clase con pregunta de ataque y evidencia esperada. Sin
  términos de framework o motor.
- **Quién lo ejecuta.** El catálogo y el diagnóstico los aplica el ejecutor,
  que normalmente es un agente. Eso no los exime de ADR-024 ni de
  `06-componentes-con-llm.md`: la salida de una revisión asistida es salida
  no determinista, y el catálogo no la convierte en verificación por el hecho
  de estar estructurada. Lo que aporta es forma comprobable —clase, pregunta
  de ataque, evidencia esperada—, no certeza. La independencia de plataforma se acredita
  por revisión documentada de supuestos y dependencias, **no** por una
  búsqueda de palabras: una expresión de ese tipo acepta `FastAPI` y rechaza
  `reactivar`, así que sirve de rastreo auxiliar y nada más. Si se usa, va
  con ruta explícita sobre el archivo del catálogo —no sobre el árbol— y se
  interpreta por sus coincidencias, no por su código de salida.
- **REQ-P10-02 — diagnóstico.** Sección del catálogo que da forma al
  "diagnóstico escrito" de `04` §8: reproducción, aislamiento, hipótesis con
  su prueba, causa raíz separada del síntoma.
**Retirados el 2026-09-18** (§7 A): REQ-P10-03 (postmortem) y REQ-P10-04
(runbook). Normaban la operación de sistemas en producción, que no es el
alcance de Skevi. Con ellos salen del corpus, y de esta propuesta, la
minimización de datos personales, la custodia de evidencia cruda, la
severidad de impacto de dominio y los folios de autorización de ejecución:
todo eso pertenece al proyecto que opera el sistema, no a un cuerpo normativo
agnóstico que sólo dice cómo se diseña software y cómo trabaja el agente que
lo construye. El rastro de por qué llegaron a estar aquí queda en §6.4 y en
los registros de `docs/reviews/`.

### 3.3 Vía de lectura y presupuesto

La ocupación vigente la emite el gate en su línea de salida; este documento
no la transcribe (ADR-025, punto 4: una cifra copiada aquí envejece antes de
que se cierre la propuesta). Lo que sí se declara es el **coste del cambio**:
**dos** líneas, ambas en `04` e incorporadas al párrafo existente, sin línea
en blanco propia: una en §5.1 hacia el catálogo —que es donde se usa en la
ronda— y otra en §8, donde vive el disparador real del diagnóstico escrito
(«llevas dos intentos fallidos; el tercero empieza con un diagnóstico
escrito»). Sin la segunda, REQ-P10-02 quedaría alcanzable sólo desde la ronda
adversarial. Ya no hace falta puntero desde `00-INDICE.md`: no hay plantillas
operativas que anunciar. Una medición sobre copia dio 998/1000 con dos
punteros separados por línea en blanco; sin separador, dos cuestan dos
líneas. El techo es 1000, sólo sube con un ADR que dé su
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

**Segundo presupuesto, el que la propuesta había olvidado:** lo que encargan
REQ-P10-01 y REQ-P10-02 vive bajo `templates/`, donde rige un techo duro de
**300 líneas por archivo** (`TEMPLATE_LIMIT`), no la ruta de lectura. Las
plantillas vigentes van de 20 a 125 líneas. El contenido encargado —nueve
clases de defecto con pregunta de ataque y evidencia esperada, más la sección
de diagnóstico— cabe en ese techo si cada clase se redacta en cuatro o cinco
líneas; si al escribirlo no cabe, la salida es partir por audiencia —catálogo
y diagnóstico en dos archivos—, nunca exentar una plantilla que el adoptante
copia.

Sin cambios en `scripts/` (`check_sizes.py` 867/870 el 2026-09-17).

### 3.4 Cambios colaterales

- `project-manifest.yaml`: **`proposito` y `no_ofrece` sin cambios** — la
  decisión §7 A dejó el alcance donde estaba—, pero **sí una línea nueva en
  `ofrece`**, con su ADR, como hacen las demás capacidades que nacen de una
  decisión estructural y la citan. Que el catálogo quepa en el alcance no
  significa que pueda entrar sin declararse: una oferta no declarada es
  crecimiento por acumulación, que es justamente lo que la versión anterior
  de esta viñeta quería evitar. Declarar una capacidad dentro del alcance
  vigente no lo amplía. **La línea dice que la plantilla es experimental**,
  porque lo es (§3.5), y el procedimiento de retirada de §3.5 la borra junto
  con la plantilla: `ofrece` no debe seguir anunciando lo que ya no existe.
- `docs/crosswalk-estandares.md`: **la fila LLM01**, hoy «parcial» con el
  hueco declarado «falta el procedimiento» — que es justamente lo que el
  catálogo aporta; la tarea evalúa si ese hueco se cierra o sólo se reduce.
  **LLM05 no cambia**: ya figura como «cubre», y el catálogo no añade
  cobertura ahí; se comprobó antes de encargar la tarea, después de que esta
  propuesta afirmara lo contrario por error. La fila RV.2 tampoco cambia: se
  preveía tocarla por el postmortem y el runbook, que salieron del alcance —
  su texto vigente no los menciona. Resumen recontado contra filas, con la
  advertencia de recuento que el propio archivo declara.
- `skevi-gate.json`: la plantilla nueva en `required`.
- `templates/skevi/MANIFEST.json`: salto al siguiente `plantillas/vN` libre,
  con la entrada nueva y su digest. El manifiesto valida **listado
  exacto** del directorio (ADR-036), así que una plantilla sin entrada da
  `BLOQ`.
- `templates/skevi/installed.json` y `templates/skevi/corpus-installed.json`:
  ejemplos de versión sincronizados con los saltos. **Ningún gate lo
  comprueba** —se verificó: el gate da `OK` con los ejemplos desfasados—, y
  el historial del manifiesto registra ese mismo olvido en v3, v5, v6, v8 y
  v9. Es el punto que más veces se ha escapado.
- `templates/skevi/usage-guide.md`: puntero a la plantilla nueva, como hizo
  `plantillas/v7` con `frozen-trees.md`. Sin él, un adoptante no se entera de
  que existe.
- `docs/MANIFEST.json`: salto al siguiente `corpus/vN` libre por los dos
  punteros en `04` (ADR-032). `00-INDICE.md` ya no cambia.
- Antes de implementar, barrido completo de identificadores y versiones
  caducados contra `main` vigente —número de ADR libre, versión de
  plantillas, de corpus y de gate, y cifras medidas—: esta propuesta ya
  envejeció dos veces por citarlos de una base anterior.

### 3.5 Madurez

La plantilla nueva declara en su encabezado **estado experimental**,
textual (sin campo de esquema: cambiarlo tocaría `scripts/`). Sale de
experimental cuando se cumplen las cuatro condiciones: criterios de
aceptación definidos **antes** de aplicarla; aplicación en un caso real con
evidencia registrada; resultado atado a la revisión concreta de la plantilla
que se probó; y disposición escrita de los hallazgos que arrojó. Un piloto
fallido con evidencia registrada **no** la saca de experimental.

**Qué acredita el caso y quién lo verifica.** El artefacto es un registro de
dos capas en `docs/reviews/` —el mismo formato que ya gatea
`check_reports`—, con su identificador de reporte, la revisión exacta de la
plantilla probada y la disposición de hallazgos. El caso puede ser de un
adoptante, si aporta ese registro, **o del propio Skevi sobre sí mismo**: la
plantilla que queda se usa en la ronda adversarial, que este repositorio
ejecuta en cada cambio material.
Lo elige el Operador y la salida la acepta él por escrito: un caso sigue
siendo evidencia de ese caso, no validación general.

**Retirada.** Si el piloto falla, o si a los doce meses de su aceptación la
plantilla no ha salido de experimental, se retira —y con ella su línea de
`ofrece`, que dejaría de ser cierta—: se borra del
directorio con su salto de versión y su entrada de historia, y el ADR de §7
queda superado por uno nuevo que lo diga. Una plantilla experimental
indefinida es deuda con apariencia de norma.

**Mantenimiento.** El dueño es quien mantiene el corpus de Skevi; no hay
re-sincronización automática con el material de origen —Skevi no depende de
él y no lo sigue—: si upstream cambia, se decide caso por caso y por
propuesta, nunca por copia.

## 4. Rechazado

| Skill | Razón |
|---|---|
| `incident-response` | Opera el sistema del adoptante, no el trabajo del agente que lo construye: fuera del alcance declarado de Skevi (§7 A, 2026-09-18) |
| `documentation` (runbook) | Misma razón: procedimiento de operación en producción |
| `architecture` | `02` §3.2 ya exige alternativas con razón de descarte y desempate |
| `system-design` | Cubierto por `02` §2, §4 y §5 |
| `testing-strategy` | `04` §3 norma el proceso; la pirámide es genérica |
| `tech-debt` | Duplica el backlog de issues (estándar §5.3). La objeción por ADR-009 se retira de aquí: precisar su alcance es materia del ADR de §7, no de esta celda |
| `standup` | Comunicación ritual; reportes en dos capas cubren estado |
| `deploy-checklist` | Fuera por B2. Si alguna vez se reconsidera, entra por el mismo ciclo que todo lo demás —propuesta, ronda y aceptación—, no por un ADR corto: esta propuesta no preautoriza su propia ampliación |
| Conectores | Acoplan proveedor; equivalente agnóstico en estándar §6.8 |

## 5. Hueco preexistente (F1)

`templates/plan-de-implementacion.md` y `templates/registro-contexto.md` no
estaban en ningún MANIFEST: no emitían drift. Fuera de esta propuesta; se
registró en issue aparte, como decidió F1.

**Resuelto el 2026-09-18**, fuera del alcance de esta propuesta:
[ADR-036](../adr/ADR-036-hogar-unico-de-plantillas.md) las movió a
`templates/skevi/`, donde el manifiesto vigente las cubre con listado exacto
y digests (issue #48). La plantilla nueva que propone §3.1 sigue yendo a
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
| A | Severidad clínica asignable por agente | Separación técnica/dominio en REQ-P10-03, **sin objeto desde el 2026-09-18**: el postmortem salió del alcance |
| A | Autorización uno a uno vs urgencia | Mitigaciones preautorizadas (C2a), **retiradas después**: ver §2 y §6.4 |
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
colaría sin que nada lo dijera. En su momento el formato compacto (D-D2) se
conservó para la disposición, que quedó aquí; **eso lo sustituyó ADR-037**,
que se lleva la disposición al registro junto con el informe. Lo de este
párrafo es lo que se hizo **con esta ronda**, antes de esa decisión.

| # | Hallazgo de T03 | Impacto si no se corrige | Corrección aplicada | Estado |
|---|---|---|---|---|
| HIGH-1 | La lista de mitigaciones preautorizadas es confundible con autoridad de ejecución | Un runbook viejo o copiado ejecuta una mitigación cuya autorización fue revocada o cuyo entorno cambió, sin que nadie lo note | Primero se reescribió la regla para que la lista acreditara sin autorizar; la ronda §6.3 demostró que esa verificación era inejecutable —Skevi no define vigencia ni revocación de folio— y el Operador retiró C2a. Al salir el runbook entero (§7 A), el requisito desapareció | **sin objeto**: el mecanismo que lo causaba ya no está en la propuesta |
| HIGH-2 | Minimización de datos sin frontera operativa | Contenido no previsto entra al cuerpo del postmortem, o un borrador queda en el historial pese a sanear el archivo final | Se corrigió en dos pasos —frontera operativa y luego lista blanca cerrada sin categorías de dato— hasta que el postmortem salió del alcance (§7 A) | **sin objeto**: no queda regla de minimización en la propuesta |
| MED-1 | El registro compacto de rondas queda fuera del gate de reportes | Una capa técnica malformada o con hash roto se archiva en `docs/history/` sin que ningún comando la haya verificado | Registro externo de **esta** ronda en `docs/reviews/`, con capa técnica canónica y `report_sha256` reproducible; validación con `python3 scripts/check_reports.py`, cuyo resultado se retiene como evidencia del cambio | cerrado en lo aplicado; generalizar el reparto a las rondas siguientes es decisión del Operador, planteada en §7 |
| MED-2 | El criterio de salida de «experimental» acepta un piloto fallido | Una plantilla pierde la etiqueta experimental sin haber demostrado utilidad ni resuelto sus hallazgos | §3.5: cuatro condiciones, entre ellas criterios de aceptación previos, resultado atado a la revisión probada y disposición escrita de hallazgos | cerrado |
| MED-3 | El rechazo de `tech-debt` malaplica ADR-009 | Un adoptante concluye que priorizar deuda está normativamente prohibido | §4: se rechaza por duplicar el backlog; precisar el alcance de ADR-009 se remite al ADR de §7 | cerrado |
| LOW-1 | La prueba por palabras clave no acredita independencia de plataforma | Material específico de framework pasa el filtro y prosa española corriente lo falla | REQ-P10-01: la búsqueda pasa a rastreo auxiliar con ruta explícita; la independencia se acredita por revisión documentada de supuestos y dependencias | cerrado |

Tres límites declaró esta ronda, todos `inconclusive` en su momento: la
procedencia upstream de §1.1 —el sandbox no podía verla—, las decisiones del
Operador de §2 por no aportarse su registro original, y la identidad
autodeclarada del propio revisor. El primero **se cerró después**, el
2026-09-18, fuera de esta ronda y con evidencia propia (§1.1 y
`../reviews/2026-09-18-prop010-procedencia.md`). Los otros dos siguen
abiertos y §7 los asume con nombre.

### 6.3 Ronda sobre el texto corregido

**EJECUTADA** el 2026-09-18, contexto fresco, sobre el contenido de la
propuesta —no sobre el cambio que la registró—. **Decisión:
`fix-and-retry`**: 2 BLOCKER, 5 HIGH, 5 MED, 3 LOW. Disposición en §6.4; el
informe, en `../reviews/2026-09-18-prop010-63.md`.

Procedencia de la regla: `04` §5.3, segunda viñeta: tras corregir un hallazgo se repiten
los checks afectados, y la ronda **si el cambio fue material** según los
cuatro disparadores objetivos. Ninguno de los cuatro aplica a un cambio
documental como este, así que lo que la guía exige aquí es **una ronda propia
honesta** (§5.3, cierre del bloque de disparadores), no contexto fresco. Lo
que la eleva a contexto fresco es la **instrucción directa del Operador** en
la conversación que autorizó estas correcciones (AGENTS.md, prioridad 1). En
ningún caso la justifica un adjetivo sobre la gravedad del cambio: ese
criterio subjetivo es justo lo que ADR-008 prohíbe. El ciclo termina en
`proceed` o `escalate`, nunca en «ya está bien».

### 6.4 Disposición de la ronda §6.3

Los quince hallazgos y su desenlace. El informe está en
`../reviews/2026-09-18-prop010-63.md`: es transcripción fiel, no verbatim, y
sus líneas de evidencia citan el comando que las sostiene, pero las
simulaciones se corrieron en copias temporales que no se conservan — se
pueden repetir, no auditar.

| Severidad | Hallazgo | Disposición | Estado |
|---|---|---|---|
| BLOCKER | La verificación de vigencia de folio de REQ-P10-04 no es ejecutable: Skevi no define registro de folios ni revocación | El Operador retiró C2a el 2026-09-18 y después el runbook entero (§7 A). Ningún folio de autorización queda en la propuesta | cerrado |
| BLOCKER | §7 no ponía a firma la ampliación de `proposito` y `ofrece` a operación | Es ahora la pregunta A de §7, con el encuadre corregido: la decisión real es D1, no la destilación | cerrado |
| HIGH | §3.4 no listaba los dos `*-installed.json`, el puntero de `usage-guide.md` ni el salto del manifiesto de plantillas | Los cuatro añadidos, con la advertencia de que ese olvido se repitió en cinco saltos anteriores, y en singular tras el recorte | cerrado |
| HIGH | §3.3 no medía el techo de 300 líneas por plantilla | Segundo presupuesto declarado, con estimación por archivo y la salida si no cabe | cerrado |
| HIGH | La salida de «experimental» era inalcanzable para el runbook y no comprobable | §3.5 nombra el artefacto que acredita el caso y quién lo verifica; el piloto interno es posible desde que cayó C2a | cerrado |
| HIGH | §8 no asignaba ronda adversarial y agrupaba ocho objetivos en una tarea | Una tarea por objetivo, cada una con ronda de contexto fresco por el disparador 4 de `04` §5.3. Tras el recorte son cinco, no siete | cerrado |
| HIGH | Faltaba el puntero desde `04` §8, donde vive el disparador del diagnóstico | Puntero desde `04` §8 presupuestado, sin línea en blanco propia. Tras el recorte son dos punteros en total, no tres: el de `00-INDICE.md` ya no hace falta | cerrado |
| MED | El cotejo de estándares no preveía la fila LLM01 | Añadida a §3.4. Una ronda posterior corrigió de paso un error propio de este documento: LLM05 ya figura como «cubre» y no cambia, verificado contra el cotejo el 2026-09-18 | cerrado |
| MED | Las comprobaciones de REQ-P10-03 no traían comando ni custodia | Se les puso procedimiento y custodia; después el requisito salió del alcance (§7 A) | **sin objeto** |
| MED | Faltaban retirada, mantenimiento, efecto sobre adoptantes y cruce con ADR-024 | Retirada y mantenimiento en §3.5, efecto sobre adoptantes en §3.1. El cruce con ADR-024 se había escrito en REQ-P10-04 y se perdió con el recorte: **repuesto en REQ-P10-01**, que es donde ahora aplica —el catálogo lo ejecuta un agente— | cerrado |
| MED | §4 preautorizaba reconsiderar `deploy-checklist` con un ADR corto | Suprimido: entra por el mismo ciclo que todo lo demás | cerrado |
| MED | REQ-P10-02 quedaba alcanzable sólo desde la ronda adversarial | Resuelto con el puntero desde `04` §8 | cerrado |
| LOW | El gate fallaba en local por un `.DS_Store` nuevo | `skevi-gate.json` pasa a `exempt_names`, que cura la clase **para el límite de tamaño**. No para el listado exacto del manifiesto, que no consulta exención alguna: eso volvió a dar `BLOQ` horas después y quedó en el issue #59, con la corrección en `scripts/` y su salto de gate. Fuera del alcance de esta propuesta | cerrado en parte; resto en #59 |
| LOW | Bundle upstream sin versionar dentro del árbol | Se retira del control de versiones con `.gitignore`. No hacía falta más: el `.zip` ya quedaba exento por sufijo, y se comprobó que el gate da el mismo resultado con y sin exención de directorio. Se probó `skip_dirs: ["externals"]` y se retiró: casa por nombre de directorio en cualquier punto del árbol, así que creaba un punto ciego mayor que el hueco que cerraba | cerrado |
| LOW | Nadie asignaba el traslado a `docs/history/` ni el registro de cierre | Tarea T09 de §8, que además actualiza las tres referencias de ruta desde `docs/adr/` — hay una cuarta mención sin ruta, que no se rompe al mover el archivo | cerrado |

### 6.5 Rondas

Numerarlas como subsecciones propias hizo que el documento se contradijera
sobre cuál había corrido. **Todas viven en esta tabla, y ninguna otra sección
las cuenta:**

| Ronda | Fecha | Sobre qué | Veredicto | Registro | Disposición |
|---|---|---|---|---|---|
| T03 | 2026-09-16 | La propuesta, por otro modelo | `fix-and-retry` (2 HIGH, 3 MED, 1 LOW) | [`…-t03.md`](../reviews/2026-09-17-prop010-t03.md) | §6.2 |
| §6.3 | 2026-09-18 | El contenido de la propuesta | `fix-and-retry` (2 BLOCKER, 5 HIGH, 5 MED, 3 LOW) | [`…-63.md`](../reviews/2026-09-18-prop010-63.md) | §6.4 |
| R1 | 2026-09-18 | El recorte de alcance y sus restos | `fix-and-retry` (2 BLOCKER, 6 HIGH, 6 MED, 3 LOW) | [`…-recorte.md`](../reviews/2026-09-18-prop010-recorte.md), capa 1 | aquí |
| R2 | 2026-09-18 | Las correcciones de R1 | `fix-and-retry` (1 BLOCKER, 4 HIGH, 5 MED, 2 LOW) | mismo archivo, capa 2 | aquí |
| R3 | 2026-09-18 | Las correcciones de R2 | `fix-and-retry` (1 HIGH, 6 MED, 3 LOW) | mismo archivo, capa 3 | aquí |
| R4 | 2026-09-18 | Las correcciones de R3 | `fix-and-retry` (2 HIGH, 3 MED) | mismo archivo, capa 4 | aquí |
| R5 | 2026-09-18 | Las correcciones de R4 y barrido completo | `fix-and-retry` (2 HIGH, 3 MED, 1 LOW) | mismo archivo, capa 5 | aquí |
| R6 | 2026-09-18 | Las correcciones de R5 | `fix-and-retry` (1 BLOCKER, 2 MED, 1 LOW) | mismo archivo, capa 6 | aquí |

**Regla que rompe el bucle, declarada tras el hallazgo de R4.** Una tabla no
puede contener la fila de la ronda que la está revisando en ese momento: si
cada ronda exige que el documento ya registre su propio veredicto, el
documento nunca queda commiteable y el ciclo no termina nunca. Por eso **la
ronda en curso se registra al commitear el cambio que corrige sus
hallazgos**, no antes. Una fila ausente al final de esta tabla es el estado
normal mientras hay una ronda corriendo, no un defecto.

La regla tuvo que afinarse dos veces. R5 encontró que protegía la tabla pero
no la prosa que la rodea, que volvió a describir un estado superado — de ahí
que esta sección describa el conjunto por la tabla y no por cifras sueltas.
R6 encontró la otra mitad: si el cambio que corrige los hallazgos de una
ronda no registra esa ronda, el registro nunca llega. Por eso **el commit que
corrige los hallazgos de una ronda la registra en el mismo cambio**, y por
eso R5 y R6 tienen su fila arriba.

**Y el cierre, que es lo que permite terminar:** la ronda que devuelva
`proceed` se registra en el commit de cierre y **ese registro no abre ronda
nueva**. Añadir una fila y una capa que sólo dicen «esta ronda no encontró
nada» no es cambio material; exigir otra ronda para verificarlo sería el
bucle otra vez, con otro nombre.

Todas corren con el mismo criterio que la primera: la guía pediría ronda
propia honesta —ningún disparador objetivo aplica a un cambio documental— y
la instrucción del Operador la eleva a contexto fresco. Los hallazgos de R1 a
R5 se disponen en el texto directamente, no en tablas nuevas: R1 dejó el
documento sin restos del recorte; R2 corrigió la contradicción sobre
`ofrece`, el conteo de límites, una frase rota de §7 y tres tareas; R3
enderezó el encabezado, las cifras y el registro que no transcribía hallazgos;
R4 nombró el bucle y obligó a registrar cada ronda; R5 lo persiguió hasta la
prosa y hasta dos atribuciones equivocadas; R6 lo cerró exigiendo que el
commit registre la ronda que corrige.

**Hallazgo dispuesto aquí.** Lo levantaron R1 y R2 como LOW y lo reabrió R4
como MED; se dispone en esta sección, y no en §6.4, porque trata de la
configuración del repositorio y no del contenido de la propuesta. ADR-030 dice que Skevi «no cambia su propia config» y que migrar
sus `exempt_paths` de `.DS_Store` a `exempt_names` «es opcional y no
perseguida aquí»; este cambio hace exactamente esa migración, así que esa
frase queda caduca. **El ADR no se edita**: son inmutables (`02` §3.2), y
editar el cuerpo de uno aceptado ya se marcó como hallazgo grave en esta
misma sesión. Queda como riesgo aceptado con nombre, registrado en el issue
[#59](https://github.com/kristhianmanue1/skevi/issues/59) junto con el hueco
de exenciones que lo motivó.

## 7. Decisión

**ACEPTADA** el 2026-09-18, folio `SKV-ACC-PROP010-20260918-01`.

**Alcance de lo aceptado:** la destilación se reduce a una plantilla,
`templates/skevi/review-defect-catalog.md`, con el catálogo de clases de
defecto (REQ-P10-01) y la sección de diagnóstico (REQ-P10-02). Quedan fuera
postmortem, runbook, preparación de despliegue y las seis skills rechazadas
en §4. `proposito` y `no_ofrece` de `project-manifest.yaml` no se tocan;
`ofrece` gana una línea para el catálogo, marcada como experimental. La
aceptación habilita ADR-035 y el plan de §8; no autoriza por sí sola ningún
commit, push ni merge, que siguen gateados uno a uno (`AGENTS.md`).

**Procedencia de la aceptación:** instrucción directa del Operador en
conversación, el 2026-09-18 — «autorizo firma», tras responder «a, no» y «b,
sí» a las dos preguntas de alcance y ordenar antes retirar C2a y la
enumeración de categorías de dato. Como las decisiones de §2, su registro es
este documento y no un acta independiente; lo asume el límite 1.

**Condición no cumplida, aceptada con nombre.** Esta sección exigía una ronda
previa en `proceed` y **ninguna la dio**: las seis cerraron en
`fix-and-retry`. Las cuatro últimas ya no hallaban defectos del contenido
sino de la autodescripción del documento —efecto del formato compacto, §6.5—,
y el Operador decidió detener el ciclo y firmar. La instrucción humana
prevalece sobre la condición que este mismo documento se había puesto
(`AGENTS.md`, prioridad 1), pero la condición existía por una razón y no se
declara satisfecha: se declara **omitida por decisión**, y ese es el cuarto
riesgo residual que la firma asume.

Sigue vigente el resto: **ADR-035** con su fila en `docs/adr/00-INDICE.md` —
ADR-034 ya está ocupado por el gate en CI remoto (v1.4.0), y el número libre
se comprueba contra `main` vigente, no contra esta línea.

Cada ronda cerrada se queda con el veredicto que emitió: las ejecutadas hasta
hoy quedaron en `fix-and-retry` de forma permanente, son historia y no
condiciones que puedan satisfacerse. La que habilita la firma es la que
cierre en `proceed`, y por la regla de §6.5 se registra al commitear el
cambio que la produce.

La aceptación asume explícitamente **tres límites** que ninguna ronda cerró:

1. **Decisiones del Operador `inconclusive`.** Las de §2 vigentes —A1, D-D2,
   F1, T01/T03— se registran como declaración atribuida, sin que se aportara
   su acta. **Y las del 2026-09-18 tienen el mismo defecto de evidencia**:
   las respuestas A y B, la retirada de C2a, la acotación de B2 y la orden de
   quitar las categorías de dato se tomaron en conversación y las transcribió
   el agente; se presentan como decididas porque lo están, pero su registro
   es este documento, no un acta independiente. La firma de §7 es lo que
   convierte a todas en decisión verificable. D1 no se firma: está retirada
   (§2), y su rastro vive en §2, §6.4 y los registros de `docs/reviews/`.
2. **Identidad del revisor de §6.2 `inconclusive`.** «Codex, GPT-6» es
   autodeclarado; nadie verificó qué modelo respondió.
3. **Independencia de §6.3 y §6.5 `inconclusive`.** Las rondas sobre las que
   descansa el recorte corrieron con contexto fresco real, pero **del mismo
   modelo que el redactor**, no de otro proveedor; sus propios registros lo
   declaran. Son revisión honesta con memoria limpia, no independencia de
   modelo. Si eso último es condición de la aceptación, hay que reejecutar
   con procedencia verificable.

**Cerrado desde entonces, en su alcance exacto:** la procedencia upstream de
§1.1 era un límite y **dejó de serlo el 2026-09-18** en lo que se verificó —el
bundle aportado contra la revisión declarada—; lo no verificado se retiró de
§1.1 en vez de darse por bueno. Lo comprobado: los catorce archivos coinciden por
SHA-256 con `anthropics/knowledge-work-plugins@58da91d`, la licencia es
Apache-2.0 de 212 líneas, no hay `NOTICE` y no existe commit posterior sobre
`engineering/`. La verificación, con sus comandos, está en
`../reviews/2026-09-18-prop010-procedencia.md`. Nada de esto crea dependencia:
Skevi no copia código ni sigue ese repositorio; la comprobación acredita **de
dónde se leyó**, que es lo que §3.1 necesita para atribuir.

Y **dos decisiones de alcance**, que no son límites sino preguntas que la
firma responde:

A. **Ampliación del alcance declarado de Skevi. RESPONDIDA: no**
   (2026-09-18). Skevi es «cuerpo normativo para diseñar software y para
   operar **agentes de IA** que crean y mantienen proyectos», y es agnóstico:
   operar al ejecutor no es operar sistemas en producción. `proposito` y
   `no_ofrece` no se tocan. `ofrece` gana **una línea**, la del catálogo,
   como tiene cada capacidad declarada del proyecto: declarar algo que cabe
   en el alcance vigente no lo amplía, y omitirlo sería crecer por
   acumulación. La propuesta queda reducida al catálogo de defectos
   y al diagnóstico; postmortem y runbook salen, y con ellos la minimización
   de datos personales, la custodia de evidencia y los folios de
   autorización, que pertenecen a quien opera el sistema y no a este corpus.

B. **Registro de rondas. RESPONDIDA: sí** (2026-09-18). El registro textual
   de cada ronda vive en `docs/reviews/`, con capa técnica gateada. ~~Y en la
   propuesta queda su disposición~~ — **sustituido por ADR-037** el mismo
   día, al verse que dejar la disposición aquí es lo que obligó a este
   documento a gastar rondas arreglando su propia narración. No rompe D-D2:
   la deliberación sigue en un solo archivo; lo que sale es su contabilidad.

**Desaparecida, no resuelta:** hubo una tercera pregunta sobre la frontera de
datos de REQ-P10-03. Dejó de existir el 2026-09-18 en dos pasos: el Operador
ordenó primero retirar la enumeración de categorías y después, al responder
que no se amplía el alcance, salió el requisito entero. **No queda regla de
minimización de datos en esta propuesta ni en el corpus**: nunca llegó a ser
norma.

Con A y B respondidas, lo que falta para firmar es que la última ronda de
§6.5 cierre en `proceed` y la aceptación misma: fecha, alcance y folio.
Aceptar los tres límites sin resolverlos es legítimo, pero entonces
quedan como riesgos residuales aceptados con nombre, no como huecos
silenciados.

## 8. Trabajo derivado tras aceptar

El plan de implementación se escribe en `docs/plans/` sólo después de
ADR-035. Una tarea, un objetivo (`04` §1), y por eso el T06 original —que
agrupaba ocho— se parte:

| Tarea | Objetivo |
|---|---|
| T05 | `review-defect-catalog.md` con el catálogo y la sección de diagnóstico |
| T06 | Punteros de la vía de lectura (`04` §5.1 y §8) y comprobación del presupuesto |
| T07 | Manifiestos, ejemplos y declaración: `templates/skevi/MANIFEST.json`, `docs/MANIFEST.json`, los dos `*-installed.json`, el puntero de `usage-guide.md`, `skevi-gate.json` y la línea del catálogo en `ofrece` de `project-manifest.yaml` |
| T08 | `docs/crosswalk-estandares.md`: fila LLM01, comprobando que LLM05 sigue en «cubre» y no se toca; recuento contra filas |
| T09 | Cierre: mover esta propuesta a `docs/history/`, actualizar las tres referencias de ruta que la apuntan desde `docs/adr/` —ningún gate revisa enlaces— y registrar la ronda de cierre en `docs/reviews/` |

**Cada tarea lleva su ronda adversarial de contexto fresco.** No es opcional
ni depende del criterio de quien la ejecute: las plantillas y los manifiestos
son interfaz hacia un consumidor que no controla el mismo autor —el
adoptante—, que es el disparador 4 de `04` §5.3. ADR-036 acaba de demostrar
lo que está en juego: un salto de versión declarado no-breaking que sí rompía
al adoptante, detectado sólo por una ronda de contexto fresco.

Commit, push y merge se autorizan uno a uno (`AGENTS.md`).
