# PLAN SR — Importación por referencia de superpowers (PROP-013)

Fuente: análisis del 2026-11-07 contra obra/superpowers y autorización
del Operador (redactar plan, ronda adversarial, ejecución local; push,
PR y merge sólo por lote con folio). superpowers es Referencia que
informa, no evidencia (PROP-004; ADR-011); los no-objetivos de PROP-004
siguen vigentes: este plan no convierte Skevi en framework de skills ni
acopla el corpus a ningún harness. La deliberación vive en
docs/proposals/PROP-013-superpowers-referencia.md; nada de lo que viaja
aquí adopta norma: las tres reglas candidatas esperan confirmación
literal de su ADR.

```text
PLAN SR — Importación por referencia de superpowers (PROP-013)
Autoriza: Operador 2026-11-07 (redacción, ronda, ejecución local;
entrega Git por lote con folio).
Clase de tarea: Architectural
Base: 6f6ff38a037413f07c1b91dc9afa7d585ab970e5
Rama: feat/superpowers-referencia (se crea en SR-4; entrega ahí)

Restricciones globales:
- Ninguna adopción normativa viaja aquí: A, C y D van como redacción
  candidata en PROP-013; cada ADR espera confirmación literal del
  Operador, y un «adelante» no la sustituye.
- El corpus sellado no se edita en esta entrega: sin corpus/vN,
  plantillas/vN ni adr/vN; los manifiestos quedan intactos.
- Ninguna regla candidata se justifica citando superpowers como
  evidencia: Referencia que informa (PROP-004, hallazgo MED).
- Toda regla candidata declara su coste sobre la ruta de lectura
  (1620/1620 sin holgura; ADR-038 p3) antes de pedir confirmación.
- La suite debe quedar verde antes de cualquier commit: el fallo
  local del test de JSON anidado bloquea el hook pre-push en este
  host (fail-closed); CI sigue siendo el autoritativo.

TAREAS:
TAREA SR-0 — Robustez del test de JSON anidado
  Objetivo: el test exigía el mensaje de una sola plataforma; en este
    host el parser resuelve la anidación sin RecursionError y la suite
    quedó roja en HEAD con árbol limpio y gates verdes.
  Clase: Bounded
  Base: 6f6ff38a037413f07c1b91dc9afa7d585ab970e5
  Plan: docs/plans/2026-11-07-prop013-superpowers-referencia.md
  Permitido: editar tests/test_template_manifest.py; correr la suite
    local.
  Superficie: shell/Python local; sólo repo Skevi; sin red.
  Prohibido: editar scripts/check_templates.py; entrega Git (va en
    SR-4); tags ni release.
  Presupuesto: sin cuota tarifada; dos fallos exigen diagnóstico previo.
  DoD: ver PLAN SR.
  Parada: suite verde en este host o diagnóstico escrito.
  Consumes: el hallazgo P1 del análisis del 2026-11-07 y las dos ramas
    de fallo controlado del gate de manifiestos
  Produce: el test acepta cualquiera de las dos salidas controladas
  Steps:
  - [ ] Aceptar JSON inválido o raíz no-objeto como salidas controladas,
        nunca un traceback — verificación: python3 -m unittest discover
        -s tests en verde en este host; suite completa, no un test
        suelto.
  - [ ] Documentar en el docstring del test la sensibilidad de
        plataforma — verificación: la explicación de las dos ramas
        queda en el propio test, citando el hallazgo BLOCKER original.

TAREA SR-1 — Redacción de PROP-013 (candidatos A, C, D y programa B)
  Objetivo: deliberación abierta con redacción candidata de tres reglas
    y el diseño preliminar del programa conductual, cada una con
    procedencia, coste y verificación declarados.
  Clase: Architectural
  Base: cierre de SR-0
  Plan: docs/plans/2026-11-07-prop013-superpowers-referencia.md
  Permitido: crear docs/proposals/PROP-013-superpowers-referencia.md;
    lectura del corpus y del análisis del 2026-11-07.
  Superficie: sólo repo Skevi; sin red.
  Prohibido: editar docs sellados (estándar, guía, plantillas); entrega
    Git (va en SR-4); adoptar ADR alguno.
  Presupuesto: sin cuota tarifada; dos fallos exigen diagnóstico previo.
  DoD: ver PLAN SR.
  Parada: propuesta completa o duda que cambie el alcance.
  Consumes: PROP-004, ADR-011, ADR-037, ADR-038, ADR-048 y el análisis
    del 2026-11-07
  Produce: PROP-013 con los ADR 049, 050 y 051 candidatos y programa B
  Steps:
  - [ ] Crea la propuesta con las tres redacciones candidatas y su
        coste de ruta de lectura — verificación: cada candidata cita
        superpowers como Referencia, declara su aterrizaje y qué gate
        la comprobaría, o por qué ninguno.
  - [ ] Tabla de no-adopciones con su razón — verificación: cada skill
        no importada cita dónde ya está cubierta o adjudicada en el
        corpus, con ruta y sección.

TAREA SR-2 — Enmienda 1 del pre-registro del piloto (candidato B)
  Objetivo: conservar re-analizable la evidencia M1-M4 para el programa
    conductual futuro, sin tocar métricas, denominador ni regla de
    éxito, y antes del sellado de PT-1.
  Clase: Architectural
  Base: cierre de SR-1
  Plan: docs/plans/2026-11-07-prop013-superpowers-referencia.md
  Permitido: editar docs/plans/2026-10-29-piloto-adr-043.md, sólo prosa
    previa al fence pre-registrado.
  Superficie: sólo repo Skevi; sin red.
  Prohibido: alterar el bloque de métricas del fence; entrega Git (va
    en SR-4); ejecutar el piloto.
  Presupuesto: sin cuota tarifada; dos fallos exigen diagnóstico previo.
  DoD: ver PLAN SR.
  Parada: enmienda aplicada o duda que cambie el diseño.
  Consumes: PROP-013 sección 5 y el pre-registro vigente del piloto
  Produce: Enmienda 1 declarada, fechada y limitada a prosa
  Steps:
  - [ ] Añadir la enmienda como prosa fechada antes del fence —
        verificación: el diff no toca ninguna línea del bloque
        pre-registrado; check_plans en verde sobre el plan del piloto.

TAREA SR-3 — Ronda adversarial y registro de dos capas
  Objetivo: contexto fresco y separado ataca plan, propuesta, enmienda
    y arreglo de test; hallazgos cerrados antes de commitear.
  Clase: Architectural
  Base: cierre de SR-2
  Plan: docs/plans/2026-11-07-prop013-superpowers-referencia.md
  Permitido: dispatch de sesiones frescas de revisión de sólo lectura;
    correcciones fix-and-retry sobre lo producido en SR-0, SR-1 y
    SR-2; crear el registro de la ronda en docs/reviews.
  Superficie: shell/Python/Git local; sin efectos fuera del repo.
  Prohibido: entrega Git (va en SR-4); editar los ficheros revisados
    desde dentro del revisor; instalar dependencias en el repo.
  Presupuesto: sin cuota tarifada; dos fallos exigen diagnóstico previo.
  DoD: ver PLAN SR.
  Parada: veredicto proceed o escalate registrado.
  Consumes: lo producido en SR-0, SR-1 y SR-2, y el análisis del
    2026-11-07
  Produce: registro de ronda en docs/reviews con capa técnica y hash
  Steps:
  - [ ] Dos sesiones frescas en paralelo: coherencia normativa
        (autoridad, presupuesto, K4, PROP-004) y verificación fáctica
        (citas de la fuente, reglas E1-E6, arreglo de test) —
        verificación: hallazgos con severidad BLOCKER, HIGH, MED o LOW
        y disposición por hallazgo.
  - [ ] Cerrar los hallazgos con fix-and-retry antes de commitear —
        verificación: cada hallazgo con su disposición en el registro;
        reverificación de los gates tras las correcciones.
  - [ ] Crea el registro de dos capas con hash ensamblado por script —
        verificación: check_reports en verde incluyendo el registro
        nuevo; time_utc y head_sha reales, nunca de memoria.

TAREA SR-4 — Entrega Git por lote
  Objetivo: llevar la entrega a main con la forma canónica de ADR-044:
    lote anunciado antes del primer efecto y aceptación registrada del
    folio.
  Clase: Bounded
  Base: cierre de SR-3
  Plan: docs/plans/2026-11-07-prop013-superpowers-referencia.md
  Permitido: rama propia; commits locales; push; PR; espera de CI en
    verde; revisión independiente del head final publicada como
    comentario del PR en ese SHA; merge con merge commit real fijado
    al SHA revisado; borrado de la rama local fusionada.
  Lote: SKV-LOTE-20261107-07
  Superficie: Git y GitHub del repo Skevi.
  Prohibido: force-push; tags; release; merge sin CI verde; merge de un
    SHA distinto al revisado; borrado de la rama remota — fuera del
    lote por ADR-044 y ADR-045: exige autorización humana explícita
    por operación.
  Presupuesto: sin cuota tarifada; dos fallos exigen diagnóstico previo.
  DoD: ver PLAN SR.
  Parada: merge aplicado o lote rechazado.
  Consumes: los cuatro gates y la suite en verde, la ronda con
    veredicto, y el folio aceptado
  Produce: PR fusionado en main con merge commit real; rama local
    limpia
  Steps:
  - [ ] Anunciar el lote con folio y esperar aceptación registrada que
        lo identifique — verificación: aceptación estructural o literal
        que nombre SKV-LOTE-20261107-07, anterior al primer efecto.
  - [ ] Push de la rama con los commits de SR-0 a SR-3, PR, CI verde y
        revisión del head final — verificación: el SHA pusheado
        contiene esos commits; checks pass y comentario del revisor
        independiente publicado en el SHA revisado.
  - [ ] Merge fijado al SHA revisado y limpieza local — verificación:
        merge commit real; rama local fusionada y borrada; árbol local
        limpio y main actualizada con el merge.

TAREA SR-5 — Decisiones reservadas al Operador
  Objetivo: presentar las cinco preguntas de PROP-013 sección 8 y
    registrar la decisión que recaiga.
  Clase: Architectural
  Base: merge de SR-4
  Plan: docs/plans/2026-11-07-prop013-superpowers-referencia.md
  Permitido: conversación con el Operador; registro de la decisión en
    docs/reviews si recae.
  Superficie: conversación; sin red.
  Prohibido: adoptar ADR sin confirmación literal; iniciar el piloto
    ADR-043 sin orden expresa; activar el programa B sin su plan.
  Presupuesto: sin cuota tarifada.
  DoD: ver PLAN SR.
  Parada: decisión registrada o petición formulada.
  Consumes: PROP-013 sección 8 y el cierre de SR-4
  Produce: cinco decisiones registradas o sus preguntas formuladas
  Steps:
  - [ ] Presentar las preguntas con costes y consecuencias —
        verificación: cada pregunta cita la sección de PROP-013 que la
        sustenta y qué cambiaría con cada respuesta.

DoD del plan: suite y cuatro gates en verde antes de cada commit; la
ronda adversarial cierra sus hallazgos antes del primer commit; el lote
se anuncia antes del primer efecto y se ejecuta sólo con aceptación
registrada del folio; ninguna norma se adopta sin confirmación literal
del Operador. La decisión de adopción es del Operador (SR-5), nunca del
ejecutor.
Parada: decisiones registradas o condición de paro por dos fallos del
mismo problema.
```

Notas fuera del fence:

- La copia local de superpowers usada por el análisis vive fuera del
  repo (directorio temporal del host); el revisor fresco la lee de ahí,
  sin instalar nada ni tocar el repo.
- El registro de ronda se ensambla por script — archivo y hash juntos —
  y el recuento de reportes que cite su EVIDENCE se calcula tras añadir
  el archivo, no antes.
