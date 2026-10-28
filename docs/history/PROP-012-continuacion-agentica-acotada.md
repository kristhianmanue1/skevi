# PROP-012 — Continuación agéntica acotada en Skevi

> **Estado:** B aprobada por el Operador el 2026-10-28 con una precisión:
> push y merge pueden ejecutarse por instrucción humana aplicable o futura
> configuración válida, y el agente debe proponerlos según el avance. La
> [SPEC](../specs/SPEC-AGENTIC-2026-10-28.md) registra los casos. Esta
> decisión no autoriza un push/merge concreto ni activa configuración.
> Las rondas y disposiciones viven en `docs/reviews/` (ADR-037).

## Problema comprobable

El Operador busca menos intervenciones humanas y tareas más agénticas. Skevi
ya permite inferir detalles internos de bajo riesgo (`01` §5), exige una
TAREA cerrada (`04` §1), diagnóstico después de dos fallos (`04` §8) y una
ronda adversarial (`04` §5). Por tanto, no está demostrado que cambiar la
excepción de autoridad local sea el primer remedio. Faltan un ciclo
operativo explícito para agotar trabajo autorizado y una comparación de su
efecto real. La [SPEC](../specs/SPEC-AGENTIC-2026-10-28.md) fija los casos
que una futura redacción y piloto tendrían que satisfacer.

El material externo analizado en la conversación ofrece ideas de artefactos,
diagnóstico y revisión, pero sus equivalencias entre archivos de hosts y
sus hooks no son contrato de Skevi. Una cadena Git registra cambios; no
acredita por sí sola aprobación, revisión ni activación.

## Alternativas

- **A. Conservar F0/F3:** cero cambio y permisos intactos. La continuidad
  entre investigación, corrección y cierre sigue dispersa, sin piloto
  comparable.
- **B. Explicitar el ciclo y medirlo:** puede reducir consultas redundantes
  sin cambiar por sí solo autoridad. Añade texto y coste de piloto; un caso
  pequeño no prueba seguridad general.
- **C. Delegar ya push y merge:** podría reducir esperas finales. No hay
  gate designado ni runtime verificado; contradice `AGENTS.md` y ADR-018.

**Recomendación: B.** A deja sin resolver la necesidad expresada; C requiere
una decisión de autoridad y garantías que el repositorio no ofrece. La
elección B conserva la jerarquía y el gate de diseño de `01` §5. Procedencia:
petición del Operador, SPEC-AGENTIC y reglas actuales de F0/F3. Razón:
obtener primero evidencia de autonomía útil sin elevar permisos por inferencia.

## Incremento documental propuesto si B se acepta

1. En `01-analisis-y-requerimientos.md`, añadir una instrucción breve para
   investigar antes de preguntar, presentar pregunta material con evidencia,
   alternativas y recomendación, y continuar partes independientes. Mantener
   literalmente la frontera de decisiones de diseño de §5.
2. En `04-ejecucion-y-verificacion.md`, reunir en un párrafo el ciclo dentro
   de TAREA: descomposición sin nuevo objetivo, implementación, tests,
   diagnóstico y corrección, revalidación y cierre. Remitir a §8 para el
   diagnóstico tras dos fallos y a §5 para la ronda. No crear DoD duplicado
   ni cambiar el presupuesto tarifado de §1.
3. Añadir sólo si es necesario un ejemplo breve en una plantilla existente.
   Un anexo informativo podrá mapear capacidades verificadas de Codex,
   Claude y OpenCode, con skills/plugins como medios opcionales. No se
   presupone equivalencia `CLAUDE.md`/`AGENTS.md` ni capacidad de un host.
4. Registrar la elección entre A/B/C y su procedencia en un ADR nuevo,
   porque son alternativas con costes distintos (`02` §3.1). No reescribir
   ADRs aceptados.
   Actualizar `docs/MANIFEST.json` por cambios canónicos y, si aplica,
   `docs/adr/MANIFEST.json`, índice de ADR y versiones/registros de
   plantillas. Revisar compatibilidad de adoptantes y enlaces.

La ruta de lectura tiene presupuesto cerrado (`skevi-gate.json`, ADR-042).
El gate debe medir la ocupación vigente antes de escribir F0/F3. Primero
condensar texto redundante; si no cabe, una decisión escrita de presupuesto
debe preceder la ampliación. No desplazar reglas a un archivo obligatorio
oculto para eludir el cálculo.

### Redacción candidata, sin vigencia normativa

Para `01` §5, después de la prohibición de supuestos silenciosos:

> Antes de preguntar, investiga con las fuentes y herramientas permitidas:
> separa hechos, hipótesis y la decisión que falta; presenta opciones con su
> efecto y recomendación. Continúa las partes independientes de la TAREA ya
> autorizada. Esta continuidad no resuelve por inferencia las decisiones de
> diseño enumeradas arriba ni amplía alcance o permisos. Procedencia:
> ADR-043. Razón: reducir consultas evitables sin saltar el gate de F0.

Para `04` §1, después de las reglas del contrato de tarea:

> Dentro de la TAREA vigente, investiga, divide pasos sin crear otro objetivo,
> implementa, prueba, diagnostica y corrige fallos; repite los checks
> afectados durante el arreglo y cumple §3-§5 antes de cerrar. Tras dos
> fallos aplica §8. Si falta una decisión de diseño (01 §5), permiso o
> evidencia concluyente, detén la parte dependiente, presenta opciones y
> sigue sólo trabajo permitido e independiente. Ni clase de tarea ni
> `proceed` conceden autoridad (§7). Procedencia: ADR-043. Razón: agotar el
> alcance autorizado sin consultas por cada paso interno.

Estas frases fueron candidatas durante la deliberación. Su integración en
F0/F3 requiere el cambio canónico, versionado y revisión de este incremento.

## Decisión del Operador y alcance adicional

El Operador aprobó B y precisó que el agente **propone** push/merge al
alcanzar hitos verificables; puede **ejecutarlos** por instrucción humana
aplicable o por configuración futura válida. Es una decisión de método y
autoridad condicional, no un permiso para la rama de este incremento. ADR-043
registra B; un ADR distinto registra la sustitución parcial de la excepción
local de ADR-018. Hasta que exista configuración adoptada y gate real, el
otorgante sigue siendo el humano. `Push` en esta vía significa push
ordinario; `force-push` conserva su gate separado.

## Piloto 1: autonomía local, sin autoridad nueva

Antes de ejecutarlo, registrar una línea base exploratoria de tareas reales
comparables por clase, riesgo, superficie y criterio de cierre. Fijar la
selección y los denominadores antes de observar resultados: consultas al
humano por motivo, tiempo de ciclo, reintentos, coste, escapes de alcance y
defectos hallados después del cierre. Registrar también interrupciones
causadas por el host o por requisitos incompletos. No atribuirlas a F0/F3
por descarte.

Ejecutar la SPEC en una rama o fixture local sin push ni PR. Incluir C1-C10,
controles positivos y negativos, y una revisión semántica humana competente.
Fijar antes el umbral de decisión y las condiciones de parada: permiso
excedido, evidencia inconsistente, `BLOCKER`/`HIGH`, dato sensible fuera de
alcance o estado desconocido tras timeout. Si la muestra no permite concluir
que el método mejora el flujo sin escapes materiales, declarar
`inconclusive`; no activar una fase externa por un promedio favorable.

El piloto es evidencia de sus casos y condiciones, no promesa para todos los
adoptantes. La clasificación Spike/Bounded/Architectural, la materialidad
de `04` §5.3 y la autoridad por operación son ejes distintos.

## Configuración futura separada de la decisión actual

La decisión actual permite documentar una vía de configuración futura. No
existe todavía configuración activa ni gate designado. Un lote de
operaciones individualizadas necesitará concesión humana verificable, gate
externo independiente, alcance, usos, vigencia y revocación. El nuevo ADR
sustituye sólo la prohibición local de delegar push/merge de ADR-018; su
jerarquía, memoria y compatibilidad subsisten. El estándar ya contempla un
gate designado (§6.6), pero no designa uno en este repositorio.

La SPEC de esa etapa tendría que exigir procedencia de concesión y revisión,
identificadores deduplicables, conciliación tras timeout y comprobación de
commit/base/destino, política y revocación inmediatamente antes del efecto.
Sin runtime real, custodia y operación condicional verificadas, el gate
permanece humano. Un primer ensayo externo podría autorizar crear un PR;
merge sería decisión y ensayo distintos. Tags, release, despliegue,
destructivas y datos sensibles quedarían fuera de la delegación inicial.
Skevi documenta el método; `project-manifest.yaml` excluye ejecutable propio,
orquestador y garantía de que el gate comprueba la verdad de la evidencia.

## Criterios de aceptación de la propuesta

- Los casos C1-C17 tienen respuesta normativa localizable sin añadir un
  permiso ni una herramienta obligatoria.
- Una tarea sin memoria, skills o plugins puede seguir F0→F3.
- F0 §5 conserva el gate de diseño; `AGENTS.md` y `04` §7 sólo cambian en la
  vía condicional de push/merge, sin configurar ni ejecutar un gate nuevo.
- El gate de tamaños y ruta, manifiestos, enlaces y reportes pasa con
  evidencia ejecutada; la revisión adversarial fresca dispone hallazgos.
- El piloto distingue progreso observado, fallo y resultado inconcluso;
  no convierte el veredicto `proceed` en autorización externa.

## Frontera de esta entrega

Esta propuesta registra la deliberación y la decisión del Operador. La
implementación local, la revisión, el piloto y una configuración futura son
estados separados. Commit, push, PR, merge, tags y release conservan sus
permisos por operación; esta decisión no ejecuta ninguno.
