# AUDIT-authority-consistency — T05: autoridad documental coherente

Archivo histórico de deliberación. D1: opción A aprobada por el humano el
2026-09-07 mediante «adelante» a la pregunta explícita de adopción.
Decisión vigente: [ADR-018](../adr/ADR-018-coherencia-de-autoridad.md).
El resto conserva el estado y los candidatos de la emisión previa a D1;
sus menciones de pendientes y textos vigentes describen esa base histórica.

Estado: propuesta en deliberación; no modifica norma ni concede permisos.
Fecha: 2026-09-07. Base inspeccionada:
`41d40d9a4e1a521e97810b4124e19e7e8431547f`.
Rama: `docs/audit-authority-consistency`, derivada del primer arreglo publicado.
Origen: análisis corregido, revisión fresca y orden humana «adelante» sobre T05.
Plan: [AUDIT-2026-09-07](../plans/2026-09-07-mejoras-auditoria.md), T05.

## F0 — Contrato de preparación

Problema: el lector puede confundir una restricción local de Skevi con la
política general que el estándar ofrece a proyectos adoptantes.
Resultado: decisión revisable con fuentes, alternativas, textos candidatos y
casos de aceptación; no adopción automática de esos textos.

Clase Architectural: documento nuevo y propuesta de interfaz normativa para
adoptantes (F0 §2, F3 §5.3). Responsable: ejecutor de T05; aceptante: humano.
Entrada: corpus real leído en la base indicada, no memoria como autoridad.
Permitido ahora: esta propuesta, estado del plan, reporte de revisión;
commit/push de documentos según autorización vigente del humano.
Prohibido ahora: cambiar norma/guía/AGENTS/manifest, adoptar ADR, merge,
PR, tags, release, configuración GitHub, memoria o PROP-008 preexistente.
DoD: ver T05 del plan. Parada: entregar propuesta revisada para la decisión D1.

```text
REQ-T05-01 [funcional] [fuente: plan T05, step 1]
Enunciado: distinguir texto vigente, prioridad efectiva y diferencias.
Criterio: matriz M1-M8 contrastable con fuentes de disco.
Prioridad: imprescindible

REQ-T05-02 [restricción] [fuente: plan T05, step 2; AGENTS §Prioridad]
Enunciado: la propuesta no amplía permisos ni suprime restricciones humanas.
Criterio: opción A conserva AGENTS local y los casos C1-C9 no conceden
autoridad a memoria, permisos ajenos al alcance ni a un orquestador no designado.
Prioridad: imprescindible

REQ-T05-03 [funcional] [fuente: plan T05, step 3]
Enunciado: la elección de política se registra antes de aplicarla.
Criterio: D1 identifica opción y aceptante; sin respuesta, norma sin cambios.
Prioridad: imprescindible
```

No objetivos: gestionar permisos con código, revisar todo el corpus, sustituir
praxis-dev, resolver revisión obligatoria de GitHub (T06), numeración PROP (T07)
o integración AN-KLA (T08). No se exige al adoptante ninguna dependencia nueva.

Entorno: repositorio documental con gates Python/stdlib existentes; contexto
AN-KLA verificado con .venv, revisión 19; PROP-008 no rastreada e intacta.
Preguntas para preparar esta propuesta: ninguna. D1 bloquea sólo su adopción,
no la inspección, redacción, revisión ni publicación autorizada del borrador.

## Fuentes y matriz de contraste [REQ-T05-01]

Las citas son fragmentos literales; se leen con el resto de su sección.
El orden descrito es interno al proyecto y no reemplaza las instrucciones
superiores del entorno del agente. ADR-017 documenta la decisión; history
no se usa como autoridad. El manifest es autodeclaración, no norma ni permiso.

| ID | Fuente y texto observado | Efecto y diferencia |
|---|---|---|
| M1 | [AGENTS, prioridad](../../AGENTS.md): «3. `docs/estandar-diseno-software-github.md`;» antes de guía | Resuelve este checkout: estándar sobre guía; humano sobre ambos. No hay vacío local de precedencia. |
| M2 | [Índice §Regla 2](../ai-agent-guide/00-INDICE.md): «(b) `AGENTS.md` del proyecto, (c) esta guía» | Omite el estándar en su lista; copiar sólo esa lista pierde la precedencia que AGENTS sí declara. |
| M3 | [AGENTS, autoridad](../../AGENTS.md): «autorización humana explícita, una por una, cada vez» | Restricción local para las operaciones enumeradas. No demuestra que ya exista una delegación permitida aquí. |
| M4 | [Estándar §4.3](../estandar-diseno-software-github.md): «El lote es válido cuando la aceptación enumera las operaciones aceptadas» | Modelo general permite enumerar operaciones en una aceptación. No equivale a autorizar operaciones ausentes. |
| M5 | [Estándar §6.2 y §6.6](../estandar-diseno-software-github.md): «pre-autorizados por el contrato de tarea»; «un orquestador designado por escrito» | Commit/ramas propias bajo contrato; gate externo delegable con alcance, revocabilidad, independencia y escalado. No anula restricciones superiores. |
| M6 | [F3 §7](../ai-agent-guide/04-ejecucion-y-verificacion.md): «del humano, una por una, cada vez»; «autorización de una tarea anterior no se hereda» | Redacción general más restrictiva que §6.6; puede confundirse permiso viejo fuera de alcance con autorización vigente para una secuencia. |
| M7 | [Guía 05 §2](../ai-agent-guide/05-memoria-del-agente.md): «humana explícita, una por una» | Repite política de autoridad dentro del complemento de memoria; la frontera propia es que recuperar datos nunca autoriza. |
| M8 | [Manifest, fronteras](../../project-manifest.yaml): «del humano o del orquestador designado conforme al §6 del estándar» | Describe el modelo general, pero no distingue la restricción de AGENTS de este repositorio; no puede por sí mismo habilitar un orquestador. |

Procedencia de M4/M5/M8: [ADR-017](../adr/ADR-017-autoridad-git-graduada.md)
figura aceptado e implementado. La inconsistencia no acredita una evasión de
permisos ni un merge sin revisión: esta propuesta sólo verifica texto y alcance.

Estándar §1.4 exige autorización previa/específica sin definir otro otorgante;
es compatible con §6.6. No se propone modificar ese principio ni fail-closed.
F3 §1 declara que editar no implica commit y §6.2 permite contrato que sí lo
autorice: son compatibles; no se necesita borrar ninguno de esos controles.

## D1 — Alternativas y recomendación

| Opción | Cambio | Coste/riesgo | Recomendación |
|---|---|---|---|
| A | Fuente general en estándar, remisiones desde guía y excepción humana local explícita en AGENTS | Cambios documentales acotados; requiere revisar todos los puntos M1-M8 y preservar la restricción local | Recomendada: corrige deriva sin adoptar delegación nueva en Skevi |
| B | Adoptar también localmente el modelo delegable de ADR-017 | Cambia la política local; exige decidir qué operaciones, quién puede designar y cómo se revoca antes de implementarlo | No adoptar como arreglo editorial; tramitar decisión aparte si se desea |
| C | Mantener todos los textos actuales | Cero edición, pero conserva copias divergentes y carga de interpretación | Posible decisión explícita; no cierra el problema de coherencia |

La opción A conserva la facultad general de ADR-017 para adoptantes cuyas
instrucciones la permitan. No la suprime del estándar ni la activa aquí.
No exige un orquestador. Una instrucción directa humana sigue teniendo su
prioridad; una propuesta o memoria no puede presentarse como esa instrucción.

## F1 — Textos candidatos de A, aún no aplicados

SPEC-AUD-03 [cubre: REQ-T05-01/02/03]. Conducta deseada: un lector distingue
qué autoridad rige y dónde verificarla sin mantener copias de la política.
Entrada: instrucciones aplicables, operación concreta y autorización vigente.
Salida: decisión de inspeccionar/ejecutar/escalar según fuentes actuales;
no hay nuevo formato ejecutable ni motor que resuelva permisos.
Invariante: no se deriva autoridad de datos ni se amplía el alcance concedido.

### A1 — Sustituir sólo regla 2 del índice

> **Prioridad de fuentes.** Aplica la jerarquía declarada en `AGENTS.md`
> del proyecto. Dentro del corpus Skevi, el estándar transversal precede
> a esta guía. Si no hay jerarquía local declarada: instrucción directa del
> humano, AGENTS aplicable si existe, estándar, guía y supuestos, en ese orden.
> No declarar una jerarquía no elimina las restricciones de AGENTS.
> Ningún documento del
> corpus reemplaza las instrucciones superiores del entorno del agente.
> Los supuestos materiales se consultan, nunca sustituyen una fuente.

Razón: M2 omite una fuente que AGENTS ya sitúa por encima de la guía.
La precedencia por defecto para un adoptante sin jerarquía explícita se propone
explícitamente, no se presenta como una regla anterior verificada.

### A2 — Sustituir el primer párrafo de F3 §7, conservando el segundo

> Requieren autorización explícita previa: push, force-push, merge, rebase de
> historia compartida, reset destructivo, borrado de ramas remotas, tags,
> releases, publicación, instalación de dependencias nuevas y cualquier
> comando destructivo. El otorgante, las condiciones y la aceptación por
> operación se rigen por el estándar §1.4, §4.3, §6.2 y §6.6, sujetos a
> `AGENTS.md` y a las instrucciones superiores aplicables. Una autorización
> anterior no habilita operaciones fuera de su alcance o vigencia. Si cubre
> explícitamente una secuencia aún vigente, se verifica esa cobertura; no
> se inventa una autorización distinta por cambiar de tarea. Ante duda se
> aplica fail-closed, sin ampliar ni renovar el permiso por inferencia.

Razón: conserva la lista de operaciones de F3, incluidas instalaciones,
remite la política común a su fuente y distingue reutilización indebida de
vigencia declarada. No incorpora upgrades: su definición corresponde a T08.

### A3 — Sustituir sólo la tercera viñeta de guía 05 §2

> Nada recuperado de la memoria autoriza operaciones. Los permisos y su
> aceptación se verifican fuera de ella, conforme al estándar §4.3 y §6 y a
> las restricciones aplicables del proyecto. Memoria, checkpoint y recibos
> son datos de continuidad; no elevan autoridad ni sustituyen al otorgante.

Razón: M7 mezcla la frontera de memoria con una copia de política general.
No altera el resto del contrato de memoria ni su carácter opcional.

### A4 — Añadir aclaración después de la regla de autoridad de AGENTS

> **Excepción local de Skevi.** La exigencia humana de la regla anterior
> restringe aquí el modelo general de gate delegable del estándar §6.6.
> Un manifest, ADR, propuesta o memoria no designa un orquestador ni
> sustituye esa exigencia por sí solo. Cambiar esta política local exige
> una instrucción o decisión humana explícita.

Se conserva literalmente la regla anterior, incluidos «una por una» y
«cada vez». A no redefine su sentido como autorización genérica. Si una
instrucción humana directa concede un alcance distinto, se identifica como
tal y no se atribuye el cambio al estándar ni a esta propuesta.

### A5 — Precisar el alcance de la última frontera del manifest

> Toda operación destructiva o con efecto fuera del entorno local exige
> autorización previa y específica conforme al §6 del estándar y a las
> restricciones del proyecto adoptante. Esta declaración no concede
> autoridad; en el repositorio Skevi rige la restricción humana de AGENTS.md.

Se conserva como autodeclaración y enlace, sin duplicar el procedimiento.
No hay cambios candidatos para el estándar ni ADR-017. Al adoptar A, un ADR
nuevo registraría esta reconciliación; no se reescribe la decisión histórica.

## Casos de aceptación para revisar A

Son escenarios documentales, no ejecución de operaciones ni prueba de un
orquestador. El revisor contrasta cada respuesta con los textos candidatos.

| Caso | Contexto | Resultado exigido |
|---|---|---|
| C1 | Skevi, sólo texto de memoria dice «push aprobado» | No ejecutar; memoria no autoriza. |
| C2 | Skevi, manifest menciona gate delegable, sin instrucción humana que cambie la restricción local | Mantener exigencia humana; manifest no habilita delegación. |
| C3 | Adoptante sin restricción local incompatible, con designación escrita y condiciones completas de §6.6 | La guía no prohíbe el gate que el estándar admite; comprobar operación y alcance antes de actuar. |
| C4 | Adoptante sin designación vigente | Gate humano por defecto; no inferir designación desde una revisión. |
| C5 | Permiso de push de una rama, intento de release | No ejecutar release: operación fuera de alcance. |
| C6 | Instrucción humana vigente cubre explícitamente commit y push de la tarea en curso | Concretar y verificar esas operaciones; no exigir una repetición por cada paso interno ni extender a merge. |
| C7 | Permiso revocado o cuyo alcance no cubre la tarea nueva | No reutilizar; escalar lo no cubierto. |
| C8 | Cambió la operación propuesta o no se puede comprobar la cobertura | No usar evidencia/folio de otra operación; fail-closed en lo dudoso. |
| C9 | Adoptante tiene AGENTS con restricciones pero sin una sección de jerarquía | Conservar prioridad de esas restricciones sobre estándar/guía; falta de sección no equivale a falta de AGENTS. |

### Evidencia de preparación y límites

Comandos de inspección: lectura completa de AGENTS, estándar, índice, F0/F1/F3,
guía 05, ADR-017 y manifest; búsqueda rg de autoridad/permiso/lote/hereda en
esas fuentes y templates. Resultados relevantes: M1-M8; no cambio normativo.
Git al entrar: HEAD 41d40d9, árbol rastreado limpio y PROP-008 no rastreada.
El hash de PROP-008 se conserva en el reporte de T05; no se versiona por accidente.
F0 cerrado para preparar la propuesta. F1 de adopción espera D1; F2 no aplica
a un documento deliberativo. RED no aplica: no hay cambio de comportamiento.

## Adopción después de D1

El humano elige A, B o C; no se marca elegido por recomendación del agente.
Si acepta A: tarea separada actualiza los cinco destinos, registra ADR y
referencias, ejecuta gates y revisión fresca C1-C9, y mueve deliberación a
history conforme F1 §3.3. Si modifica A, revisar el diff concreto resultante.
La actualización administrada de AGENTS, si activa diagnóstico AN-KLA,
se inspecciona y reporta; no se auto-reinstala ni se escribe memoria.

Registro de D1: pendiente. No hay aprobación ni adopción de A/B/C a esta emisión.
Publicar esta propuesta en una rama no equivale a ratificarla.
