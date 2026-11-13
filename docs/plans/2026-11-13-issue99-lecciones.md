# PLAN LC — Issue #99: lecciones de método y calibración del reporte

Fuente: informe de contexto del issue #99
(`/var/tmp/skevi-capitan/informe-contexto-99.md`, 2026-11-12) y aceptación
del Operador (2026-11-13): «acepto publicar : publicar 95aeb5d y el lote
SKV-LOTE-20261112-01 para el #99.» más «se aplican tus recomendaciones»
sobre las decisiones D1–D4. El issue #99 es un CC desde devHerdrExpert con
9 lecciones candidatas: 4 ya cubiertas, 2 parciales que completan la guía
04 (filas 1 y 2) y 3 que nacen como lecciones (filas 6, 7 y 8).

```text
PLAN LC — Issue #99: lecciones de método y calibración del reporte
Autoriza: Operador 2026-11-13 (aceptación textual del lote
  SKV-LOTE-20261112-01 y de las recomendaciones D1-D4 del informe de
  contexto del issue #99).
Clase de tarea: Architectural
Base: 7d7d06bec8b986b24e093f62f0f5c24a3c2436d2
Rama: docs/issue99-lecciones-metodo (ya creada)

Restricciones globales:
- Ruta de lectura <= 1640/1640 sin holgura: toda línea añadida a la guía
  04 se compensa con condensación de significado preservado en el mismo
  archivo, en el mismo commit (ADR-038 p3; ADR-052).
- La cascada de versiones viaja en un solo commit: corpus/v12 (guía 04)
  arrastra plantillas/v24 y los espejos .skevi/ re-apuntados a @HEAD
  (ADR-048).
- Las lecciones no son norma: precedencia corpus > lecciones; jamás
  editan ni reinterpretan el canon.
- Sin squash, force-push, tags, releases ni borrado de ramas (mandato 2
  del capitán, 2026-11-13).
- Suite y gates en verde antes de cada commit; el hash del registro de
  ronda se ensambla por script, nunca a mano.

TAREAS:
TAREA LC-0 — Guía 04: calibrar el reporte y acotar el CI remoto (filas 1-2)
  Objetivo: completar las secciones parciales del issue #99 — verbos de
    reporte y no de certificación con instrumento por señal (§6), y
    depuración en local antes de gastar la matriz del CI (§7) — con
    condensación neta cero en el mismo archivo.
  Clase: Bounded
  Base: 7d7d06bec8b986b24e093f62f0f5c24a3c2436d2
  Plan: docs/plans/2026-11-13-issue99-lecciones.md
  Permitido: editar docs/ai-agent-guide/04-ejecucion-y-verificacion.md;
    regenerar docs/MANIFEST.json (corpus/v12); actualizar
    templates/skevi/corpus-installed.json, templates/skevi/installed.json
    y templates/skevi/MANIFEST.json (plantillas/v24); sincronizar
    .skevi/corpus-installed.json y .skevi/installed.json; correr los
    gates y la suite.
  Superficie: shell/Python local; sólo repo skevi; sin red.
  Prohibido: tocar otros archivos del corpus; subir el presupuesto de
    ruta de lectura; edición de texto sellado sin bump.
  Presupuesto: sin cuota tarifada; dos fallos exigen diagnóstico previo.
  DoD: ver PLAN LC.
  Parada: ruta de lectura <= 1640 con guía 04 editada, o BLOQ.
  Consumes: issue #99 filas 1-2; informe de contexto §3; ADR-038 p3
  Produce: guía 04 con filas 1-2 cubiertas; salto corpus/v11 a corpus/v12
    con plantillas/v24 y espejos sincronizados en el mismo commit
  Steps:
  - [ ] Añadir en §6 la calibración de verbos (reporte, no certificación;
        instrumento por señal; sin sumar evidencias; universales
        contrastados) y en §7 el presupuesto del CI remoto — verificación:
        el texto nuevo cita el issue #99 y condensa igual número de líneas
        en el mismo archivo; la ruta de lectura reportada por
        check_sizes queda <= 1640.
  - [ ] Regenerar la cascada completa de manifiestos en un solo commit —
        verificación: python3 scripts/check_sizes.py OK; los tres
        check_templates contra .skevi/ al día; suite unittest en verde.
  - [ ] Condensar sólo prosa descriptiva (§5.2, §5.4, §9) sin perder
        procedencia ni referencias — verificación: diff leído completo;
        ninguna referencia a ADR o archivo eliminada.

TAREA LC-1 — Hogar docs/lecciones/ con ADR-053 y las filas 6, 7 y 8
  Objetivo: crear el hogar de lecciones de método con formato servible,
    precedencia declarada y tres lecciones con su evidencia; decidirlo en
    ADR-053 con su entrada de índice y bump adr/v11.
  Clase: Architectural
  Base: cierre de LC-0
  Plan: docs/plans/2026-11-13-issue99-lecciones.md
  Permitido: crear docs/lecciones/README.md y las lecciones
    docs/lecciones/medicion-grep-limites-de-palabra.md,
    docs/lecciones/declarar-salto-de-regla-al-cerrar.md y
    docs/lecciones/rehacer-el-barrido-no-parchear-el-caso.md; crear
    docs/adr/ADR-053-hogar-de-lecciones-de-metodo.md; editar
    docs/adr/00-INDICE.md y docs/adr/MANIFEST.json (adr/v11); editar
    README.md (tabla de hogares) y docs/mapa-orientacion.md (referencia
    del encabezado a corpus/v12).
  Superficie: sólo repo skevi; sin red.
  Prohibido: editar el corpus sellado (ya cubierto por LC-0); crear
    normativa nueva en las lecciones; exceder límites de tamaño.
  Presupuesto: sin cuota tarifada; dos fallos exigen diagnóstico previo.
  DoD: ver PLAN LC.
  Parada: hogar completo con ADR aceptado o BLOQ.
  Consumes: issue #99 filas 6, 7 y 8; decisión D1 aceptada por el
    Operador; ADR-002 (vida útil); ADR-040 (familia adr)
  Produce: docs/lecciones/ con README y 3 lecciones; ADR-053 con índice y
    adr/v11; fila en README y mapa re-referenciado
  Steps:
  - [ ] Crear el README del hogar con formato, precedencia corpus mayor
        que lecciones, promoción a guía y servicio externo sin copia —
        verificación: ninguna frase del README repite norma del corpus;
        cita ADR-053 como fuente.
  - [ ] Crear las tres lecciones con id estable, Regla, Cómo aplicarla,
        Evidencia, Origen y Revisión — verificación: cada lección cita el
        issue #99 y su fila; ids grep-ables únicos.
  - [ ] Crear ADR-053 y actualizar índice y manifiesto — verificación:
        docs/adr/MANIFEST.json en adr/v11 con el archivo listado y su
        digest real; check_sizes OK; suite en verde.

TAREA LC-2 — Ronda adversarial de otra familia y registro en dos capas
  Objetivo: atacar el cambio completo con contexto fresco real de otra
    familia de modelo hasta proceed; registrar ronda y disposiciones.
  Clase: Architectural
  Base: cierre de LC-1
  Plan: docs/plans/2026-11-13-issue99-lecciones.md
  Permitido: despachar subagente de revisión de otra familia con contexto
    fresco; correcciones fix-and-retry sobre lo producido en LC-0 y LC-1;
    crear el registro de la ronda en docs/reviews con hash ensamblado por
    script.
  Superficie: subagente de sólo lectura sobre este checkout; Python local.
  Prohibido: que el revisor edite; commitear con hallazgos BLOCKER o HIGH
    abiertos; inventar time_utc o head_sha.
  Presupuesto: sin cuota tarifada; dos fallos exigen diagnóstico previo.
  DoD: ver PLAN LC.
  Parada: veredicto proceed o escalate registrado.
  Consumes: el diff completo de LC-0 y LC-1; el catálogo de defectos de
    templates/skevi/review-defect-catalog.md
  Produce: registro docs/reviews/2026-11-13-issue99-lecciones.md con capa
    técnica y hash reproducible
  Steps:
  - [ ] Despachar la ronda con las clases del catálogo sobre el diff real
        — verificación: hallazgos con severidad y evidencia; disposiciones
        por tres pilas (ADR-050).
  - [ ] Cerrar hallazgos con fix-and-retry y reverificar gates —
        verificación: cada hallazgo con disposición; gates y suite en
        verde tras las correcciones.
  - [ ] Crear el registro con hash por script — verificación:
        python3 scripts/check_reports.py OK incluyendo el registro nuevo;
        date, time_utc y head_sha tomados de fuentes reales.

TAREA LC-3 — Entrega Git por lote y respuesta al issue #99
  Objetivo: publicar por la forma canónica de ADR-044 bajo el lote aceptado
    y responder el CC con la tabla de veredictos.
  Clase: Bounded
  Base: cierre de LC-2
  Plan: docs/plans/2026-11-13-issue99-lecciones.md
  Permitido: commits locales; push de la rama; PR a main; espera de CI en
    verde; revisión independiente de la cabeza final publicada como
    comentario del PR en ese SHA; merge con merge commit real fijado al
    SHA revisado; comentario de respuesta en el issue #99 con la tabla de
    veredictos; sincronizar main local.
  Lote: SKV-LOTE-20261112-01
  Superficie: Git y GitHub del repo skevi (gh autenticado).
  Prohibido: squash; force-push; tags; releases; borrado de ramas;
    merge de un SHA distinto al revisado; merge sin CI verde.
  Presupuesto: sin cuota tarifada; dos fallos exigen diagnóstico previo.
  DoD: ver PLAN LC.
  Parada: merge aplicado y issue respondido, o lote detenido.
  Consumes: los gates en verde, la ronda con proceed y el folio aceptado
    SKV-LOTE-20261112-01
  Produce: PR fusionado en main con merge commit real; issue #99 con la
    tabla de veredictos y citas
  Steps:
  - [ ] Commits locales con gates en verde, push de la rama y PR con body
        por archivo — verificación: el SHA pusheado contiene LC-0 a LC-3;
        checks 3.9 y 3.12 pass.
  - [ ] Revisión de cabeza final como comentario del PR y merge fijado a
        ese SHA — verificación: comentario publicado antes del merge;
        mergeCommit con --match-head-commit al SHA revisado; main local
        sincronizado con origin.
  - [ ] Responder el issue #99 con la tabla de las 9 filas (veredicto,
        evidencia con ruta y sección, salida) y cita del ADR-053 —
        verificación: el comentario distingue dato de instrucción y no
        reafirma norma del corpus.

DoD del plan: guía 04 con filas 1-2 integradas y ruta de lectura <= 1640;
hogar docs/lecciones/ con ADR-053 aceptado; ronda de otra familia con
proceed; entrega por lote canónico; issue #99 respondido. Ningún archivo
excede su límite; la cascada de manifiestos queda en un solo commit.
Parada: proceed o escalate en la ronda; BLOQ ante autoridad faltante.
```

Notas fuera del fence:

- La ocupación de la ruta de lectura se lee de la salida de check_sizes,
  nunca de cifras copiadas (ADR-025 p4).
- El registro de ronda se ensambla con
  `/var/tmp/skevi-capitan/ensamblar-registro.py` (fuera del repo); el
  recuento de reportes que cite su EVIDENCE se calcula tras añadir el
  archivo.
- Los ids de lección son estables y grep-ables: skevi/medicion-grep-limites,
  skevi/declarar-salto-de-regla, skevi/rehacer-el-barrido.
