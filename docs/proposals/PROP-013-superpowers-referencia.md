# PROP-013 — Importación por referencia de superpowers

**Estado: PROPUESTO. Deliberación abierta; nada de este documento es norma
vigente.** Fecha: 2026-11-07.

Origen: análisis del 2026-11-07 contra `obra/superpowers` — README público
y las quince skills leídas de una copia local del repositorio — con
autorización del Operador para redactar plan, rondarlo adversarialmente y
ejecutar la parte no normativa. Plan que lo ejecuta:
`2026-11-07-prop013-superpowers-referencia.md` en `docs/plans/`.

## 1. Objeto y procedencia

PROP-004 (2026-08-20) ya analizó `obra/superpowers` y lo clasificó
**Referencia que informa, no evidencia**; sus no-objetivos siguen vigentes:
no convertir Skevi en un framework de skills ni acoplar el pipeline a un
harness. Desde entonces la fuente cambió: marketplaces oficiales, soporte
de unos dieciséis hosts, un harness de evaluación conductual
(`superpowers-evals`) y la skill de diagnóstico de sesiones. Este documento
reabre el cotejo con esa versión y propone cuatro importaciones acotadas.

Regla de procedencia de PROP-004 (ronda del 2026-08-20, hallazgo MED):
«Superpowers demuestra» no eleva una Referencia a Evidencia. Toda cita a
superpowers en este documento informa una decisión; no la prueba. La
prueba local, si algún candidato se adopta, la daría el programa de la
sección 5 o el piloto de ADR-043, nunca la fuente.

## 2. Candidato A — registro de decisiones intermedias (rulings)

**Qué observó la fuente.** Las skills de ejecución de planes exigen un
libro de registro por plan con líneas de la forma `Ruling: <qué decidí> —
<por qué> — <qué coste si fallo>`, declaran que la memoria de conversación
no sobrevive a la compactación y reportan — como su fallo más caro
observado — ejecutores que, tras compactar, re-despacharon secuencias de
tareas ya completadas. Auto-reportado: Referencia, no evidencia.

**Qué propone Skevi.** Una regla en F3 para tareas con plan de varias
tareas: el progreso intermedio y las decisiones que ni el plan ni el SPEC
contestan se registran en archivos con el formato de ruling; tras una
compactación, manda el estado de Git y esos archivos, no el recuerdo de la
sesión. Es agnóstico de memoria (K4): archivos y Git, sin AN-KLA ni
dependencia de host. Encaja con la doctrina de evidencia: una decisión sin
registro es una decisión en secreto, igual que una afirmación sin salida de
comando.

**Aterrizaje.** `docs/ai-agent-guide/04` (sección 2 o 4) y, opcionalmente,
un campo en la plantilla de plan. Coste estimado: entre diez y catorce
líneas nuevas en 04. La ruta de lectura está en 1620/1620 sin holgura, así
que la adopción exige ADR propio que re-decida el presupuesto en el mismo
cambio (política p3 de ADR-038) o compensación neto-cero. Verificación: la
comprueba la ronda adversarial y la revisión del dossier, no un gate
estructural — norma conducta, no forma de artefacto.

**ADR candidato (texto para ADR-049, PROPUESTO).**

> Decisión: en una TAREA con plan de varias tareas, el ejecutor mantiene
> el progreso intermedio y sus decisiones no contestadas por plan o SPEC
> en archivos de registro con la forma `Ruling: <qué> — <por qué> —
> <coste si fallo>`; tras una compactación, el estado de Git y esos
> archivos prevalecen sobre el recuerdo de la sesión. La regla no crea
> permisos, ni gate nuevo, ni dependencia de memoria o host.
> Alternativas: (a) no hacer nada — la compactación sigue borrando el
> contexto de decisiones; (c) delegar el registro en una memoria
> instalada — viola K4. Consecuencias: más archivos efímeros por tarea y
> una regla más en la ruta de lectura; a cambio, decisiones trazables y
> reanudación verificable.

## 3. Candidato C — taxonomía de disposiciones de ronda

**Qué observó la fuente.** El builder check del diseño (skill de
brainstorming) ordena cada pregunta de su revisor en tres pilas — ya
respondida por la conversación o el proyecto, menor (la resuelve el
ejecutor y la marca como suya), o del humano —; la revisión final de la
rama (skill de ejecución inline) re-gradúa cada hallazgo por el efecto
real sobre quien usa el software — quien puso «Minor» porque el spec
calló graduó el spec, no el efecto — y los hallazgos menores jamás
entran al pase de arreglos: se registran y se informan. Auto-reportado:
Referencia.

**Qué propone Skevi.** Refinar la disposición de hallazgos de la ronda
(`04` §5.2; `02` §3.3 si procede) con tres reglas: (1) cada hallazgo se
recibe en una de las tres pilas; (2) la severidad se re-gradúa por efecto
sobre el consumidor del artefacto, no por el silencio del SPEC; (3) los
hallazgos informativos se registran con disposición y no abren pase de
arreglos. Es coherente con ADR-037: la disposición vive en el registro de
la ronda; esto sólo precisa qué disposiciones existen.

**Coste.** Entre ocho y doce líneas en `04` §5; mismo freno de presupuesto
que el candidato A. Verificación: la comprueba la ronda adversarial sobre
los registros — no un gate estructural: norma el contenido de la
disposición, no su forma.

**ADR candidato (texto para ADR-050, PROPUESTO).**

> Decisión: la disposición de cada hallazgo de ronda declara una de tres
> pilas — resuelto con fuente existente, menor con decisión del ejecutor
> registrada, o del Operador — y la severidad se re-gradúa por efecto
> real sobre el consumidor del artefacto; los hallazgos informativos se
> registran sin abrir pase de arreglos. No cambia quién decide ni qué
> hallazgos bloquean (§5.3 vigente).
> Alternativas: (a) dejar la disposición libre — cada ronda inventa su
> taxonomía y las comparaciones entre rondas se degradan; (c) tablas de
> severidad fijas — rigidez que el estándar evita por diseño.
> Consecuencias: registros de ronda más comparables; coste, unas líneas
> de norma y disciplina extra en cada cierre.

## 4. Candidato D — sección Review Focus en la plantilla de plan

**Qué observó la fuente.** La skill de redacción de planes exige en la
cabecera del plan — tras las restricciones globales — una lista corta —
cinco o menos — de clases de entrada o modos de fallo que el spec
implica y que ningún test de las tareas ejercita, cada una con la
prueba que la fija en la tarea dueña.

**Qué propone Skevi.** Sección opcional `Review Focus` en
`templates/skevi/plan-de-implementacion.md`: clases de entrada o fallo no
ejercitadas por los steps, cada una con el paso que la fija. Sin regla E
nueva: `check_plans` no la exige ni la valida; la ronda adversarial la
usa como lente de revisión. Es opcional por diseño: el gate sigue
comprobando forma, no contenido.

**Coste.** Edición de plantilla sellada: bump `plantillas/vN` con cascada
de digests y espejos sincronizados en el commit fuente (ADR-048). Entre
seis y diez líneas de plantilla, fuera de la ruta de lectura.

**ADR candidato (texto para ADR-051, PROPUESTO).**

> Decisión: la plantilla de plan incorpora la sección opcional Review
> Focus — hasta cinco clases de entrada o fallo no ejercitadas por los
> steps, cada una con el paso que la fija. Opcional: sin ella, el plan
> sigue válido; con ella, la ronda la usa como lente. Sin regla E nueva.
> Alternativas: (a) exigirla — otro campo obligatorio sin caso observado
> local; (c) norma en 04 en vez de plantilla — más ruta de lectura para
> lo que es formato de artefacto. Consecuencias: bump de plantillas/vN y
> cascada de digests; a cambio, los planes declaran lo que sus pruebas
> no cubren.

## 5. Programa B — evaluación conductual de las normas (programa futuro)

**Qué observó la fuente.** `writing-skills` define TDD aplicado a
documentación normativa: escenario de presión sin la regla (baseline),
redacción de la regla contra las racionalizaciones observadas, re-prueba
con la regla, cierre de lagunas; existe un harness externo para
escenificarlo.

**Qué propone Skevi.** Un programa futuro — no texto normativo y no
ejecución ahora: medir si las reglas del corpus cambian la conducta
observable del ejecutor, con escenarios pre-registrados, baseline sin
regla, veredicto `inconclusive` sin evidencia suficiente y métricas
selladas antes de empezar. Requiere plan propio pre-registrado y orden
expresa del Operador; el harness ajeno entra como Referencia de mecánica,
nunca como prueba de beneficio local. Cierra, por vía empírica, el hueco
que `project-manifest.yaml` declara en `no_ofrece`: los gates comprueban
forma, no que la norma se siguiera.

**Enlace con el piloto ADR-043.** Enmienda 1 ya aplicada al pre-registro
(`docs/plans/2026-10-29-piloto-adr-043.md`, antes del sellado de PT-1): la
evidencia M1-M4 queda conservada para re-análisis por este programa. La
enmienda no añade métricas, no cambia la regla de éxito ni el denominador.

## 6. No-adopciones y razón

| Skill de la fuente | Por qué no se importa |
|---|---|
| test-driven-development (borrado del código prematuro) | Adjudicado: PROP-004 §A-3 y ADR-011 exigen el RED como evidencia; F3 §3 vigente |
| verification-before-completion | Principio 3, F3 §4 y los gates: mismo principio con semántica pass/fail/inconclusive |
| systematic-debugging | F3 §8 — dos fallos exigen diagnóstico escrito antes del tercer intento |
| requesting-code-review | La ronda de `04` §5 es obligatoria; el contexto fresco real es obligatorio ante los disparadores de §5.3, y ronda propia honesta en su defecto |
| using-git-worktrees y finishing-a-development-branch | §4-§5 del estándar y ADR-044; Skevi es más estricto en autoridad |
| using-superpowers (bootstrap de sesión) | Acoplado a hooks del harness; rompería la neutralidad de host (PROP-004 §3) |
| dispatching-parallel-agents y guía de modelos | Orquestación concreta: hogar posible en `docs/orchestration/`, no en el corpus |
| diagnosing-superpowers | La disciplina de cita precisa ya es doctrina; el forense de sesiones no está pedido |

## 7. Costes y secuencia si el Operador adopta

0. Los números 049, 050 y 051 son tentativos mientras no haya
   confirmación; la numeración final se fija al crear cada ADR (la
   colisión de números reservados tiene precedente en ADR-008 §74-78).
1. Confirmación literal de cada ADR: 049 (A), 050 (C), 051 (D).
2. A y C exigen, en el mismo cambio, el ADR de presupuesto de lectura
   (política ADR-038 p3), bump `corpus/vN` y bump `adr/vN` del manifiesto.
3. D exige bump `plantillas/vN` con cascada de digests y espejos en el
   commit fuente (ADR-048).
4. Ronda adversarial por cada cambio material; los cuatro gates y la
   suite en verde antes de declarar terminado cada uno.

## 8. Preguntas al Operador

1. ¿Confirma ADR-049 — registro de decisiones intermedias?
2. ¿Confirma ADR-050 — taxonomía de disposiciones de ronda?
3. ¿Confirma ADR-051 — Review Focus en la plantilla de plan?
4. ¿Ordena ejecutar el piloto ADR-043 tal cual quedó pre-registrado?
5. ¿Aprueba abrir el programa B con su plan pre-registrado propio?
