# PLAN HV — Hoja de ruta verificada del análisis post-ronda

Fuente: la sesión del análisis crítico y propositivo del corpus quedó a
medias tras dos rondas adversariales de contexto fresco (c4aa1048) que
cerraron en `proceed` sin dejar artefacto: el árbol quedó limpio en
`main` `74a4714`, sin plan que convirtiera la hoja de ruta en tareas y
sin registro de las rondas — `docs/reviews/` no las conoce. Este plan
registra el análisis verificado de ese trabajo, corrige lo que no
sostuvo la verificación y convierte el resto en tareas con gate. La
orden del Operador (2026-11-06) cubre el análisis, la redacción de este
plan y su ronda; la ejecución de HV-1..HV-6 queda sujeta a la autoridad
que cada tarea declara.

## Análisis del trabajo previo, verificado contra `main` `74a4714`

Sostenido tras verificación (evidencia citada en las tareas):

- Deriva en `README.md`:124 — cita «1000 líneas» (ADR-021) cuando el
  límite vigente es 1620 (ADR-042); el gate emite 1620/1620.
- Reparto exacto de la ruta de lectura: 1142 líneas propias (AGENTS 109
  + 00-INDICE 114 + estándar 501 + 05 132 + peor caso `04` 286) frente a
  478 de `AN-KLA.md` (29.5%), bajo un trinquete que sólo sube con ADR.
- Doble commit del auto-hospedaje:
  `test_sources_point_to_the_last_bump_of_each_family`
  (tests/test_check_manifests.py:186-205) exige que `source` cargue el
  SHA del último commit que tocó cada manifiesto; un commit no puede
  contener su propio SHA, luego cada bump fuerza un segundo commit
  (329e2b6 tras df1b4e0). El CI coteja los tres espejos en
  `.github/workflows/skevi-gate.yml:51-56`.
- Deadlock ADR-002↔ADR-040: 13 referencias con ruta a `docs/proposals/`
  en los 5 archivos sellados que apuntan a material de propuesta
  (`00-INDICE.md`, ADR-020, ADR-035, ADR-036, ADR-037; ADR-003:19 define
  el directorio y ADR-027:89 ya cita una ruta histórica inexistente — 15
  ocurrencias en 7 sellados); mover las propuestas rompe enlaces o sellos.
- Los planes cerrados de `docs/plans/` siguen bajo regla E5: el gate
  relee todo `*.md` del directorio en cada corrida.
- Filas ADR-009, ADR-017, ADR-020, ADR-021 y ADR-038 del índice sin
  anotación hacia adelante; ADR-014 y ADR-018 sí la tienen.
- PLAN PT (piloto ADR-043): 6/6 tareas sin marcar; el beneficio del
  ciclo autónomo sigue sin medir.
- Crosswalk LLM01 «parcial» + coste declarado de 2 líneas en `04`
  (PROP-010 §3.3): hoy daría 1622/1620 → BLOQ; desbloquear comprimiendo
  no exige ADR (ADR-025 p3).

Correcciones al trabajo previo (hallazgos de esta verificación):

- [MED] «15 archivos en docs/proposals/externals/» es falso: externals/
  contiene 1 archivo (Engineering-1.2.0-v38.zip) con 14 entradas dentro.
  Ninguna lectura da quince. La sustancia —estancamiento desde el
  2026-09— se mantiene; el inventario no.
- [LOW] La evidencia «ADR-034:11» no es un enlace: ese ADR menciona
  `AUDIT-review-enforcement` sin ruta; el enlace vive en 00-INDICE:37.
  El deadlock se apoya en 5 archivos con ruta real, no en 6.
- [LOW] Las dos rondas (c4aa1048) cerraron sin registro en
  `docs/reviews/`: su disposición vive sólo en la conversación, contra
  la doctrina de ADR-037. Este plan registra la suya (HV-7).
- [LOW] Precedente que apoya la opción A de HV-3: ADR-027:89 ya cita
  `docs/proposals/M6-deriva-del-gate-copiable.md`, archivo que hoy no
  existe — el corpus sellado ya tolera rutas históricas de su fecha.
- [LOW] El deadlock es artefacto de fechas: T09 de PROP-010 §8
  (2026-09-18) planeaba actualizar «las tres referencias» cuando los
  ADRs aún eran editables; ADR-040 selló la familia el 2026-10-17 sobre
  un plan abierto. Nadie diseñó el bloqueo: creció bajo el plan.

```text
PLAN HV — Hoja de ruta verificada del análisis post-ronda
Autoriza: Operador 2026-11-06 (contexto, redacción del plan y su ronda)
Clase de tarea: Architectural (ADR-013: este plan existe)
Base: 74a4714c074af49b5bd3045f74de3510c2bae3ce (main; árbol limpio)
Rama: sin rama; este plan no produce efectos Git.

Restricciones globales:
- Ningún efecto Git está autorizado por este plan: commit, push, merge,
  tags y releases exigen dossier de lote aceptado por el Operador antes
  del primer efecto (ADR-044; AGENTS.md §Autoridad por operación).
- Los ADRs aceptados son inmutables (02 §3.2; ADR-040): toda decisión
  nueva viaja en ADR nuevo con confirmación expresa del Operador.
- El trinquete 1620 no se sube aquí (ADR-025 p2; ADR-038 p3): sólo se
  gana holgura por compresión, que no exige ADR (ADR-025 p3).
- La ejecución del piloto PT exige orden expresa del Operador
  (docs/plans/2026-10-29-piloto-adr-043.md); este plan no la activa.
- La disposición de cada ronda se registra en docs/reviews (ADR-037).

TAREAS:
TAREA HV-1 — Corregir la deriva de README.md
  Permitido: la frase de la línea 124 de README.md sobre reading_path.
  Prohibido: tocar archivos sellados o manifiestos; efectos Git.
  Consumes: ADR-025 p4 (la cifra que caduca no se copia sin fechar);
    salida vigente del gate (1620/1620)
  Produce: README.md remitiendo a la salida de check_sizes, sin cifra
  Steps:
  - [x] Sustituir la frase por remisión al gate — verificación: grep
        "1000 líneas" README.md sin coincidencias y check_sizes OK

TAREA HV-2 — Holgura por compresión para desbloquear PROP-010 T06
  Permitido: docs/estandar-diseno-software-github.md (§4.3, §6.2, §6.6),
    docs/ai-agent-guide/04-ejecucion-y-verificacion.md (§7),
    docs/MANIFEST.json para el bump. Superficie ampliada por el Operador
    el 2026-11-07 tras el escalamiento de la ronda (registrado en
    docs/reviews/2026-11-07-hv2-ronda.md): la plantilla
    templates/skevi/corpus-installed.json con salto plantillas/v19 en su
    manifiesto, y los espejos .skevi/corpus-installed.json y
    .skevi/installed.json sincronizados al SHA del commit fuente.
  Prohibido: subir reading_path.limit; editar ADRs; efectos Git sin
    lote aceptado.
  Consumes: duplicación dossier/lote estándar↔04 señalada por la ronda;
    ADR-025 p3; ADR-031 (commit doble del espejo)
  Produce: salida de check_sizes con ruta <=1618; corpus/v9 y
    plantillas/v19 sellados, espejos .skevi/ al día
  Steps:
  - [x] Comprimir la duplicación conservando ambas normas —
        verificación: check_sizes OK con ruta <=1618 y diff sin reglas
        perdidas
  - [x] Bump corpus/v9 y espejo .skevi/ al SHA del commit fuente —
        verificación: unittest discover OK y check_templates al día

TAREA HV-3 — Resolver el deadlock y ejecutar PROP-010 §8
  Permitido: decisión del Operador entre opción A (extender a las
    propuestas la doctrina de rutas históricas que ADR-036 aplicó a
    ADR-010: el cuerpo sellado conserva su ruta y sólo el índice
    actualiza) y opción B (salto breaking de re-sellado); traslado de
    docs/proposals/ a docs/history/; creación de
    templates/skevi/review-defect-catalog.md; fila LLM01 de
    docs/crosswalk-estandares.md; skevi-gate.json y
    project-manifest.yaml según PROP-010 §3.4; punteros de 2 líneas en
    04 §5.1 y §8; nota de la fila README.md:34 si el traslado la deja
    huérfana (describe la convención, no la ocupación)
  Prohibido: editar el texto sellado de ADR-020/034/035/036/037; mover
    archivos sin la decisión registrada; efectos Git sin lote aceptado.
  Consumes: PROP-010 §3.3-§3.5, §7 (riesgo residual firmado) y §8
    (T01-T09); precedente ADR-027:89; holgura ganada en HV-2
  Produce: PROP-010, los 6 AUDIT-*.md y externals/ en docs/history/;
    catálogo experimental creado; LLM01 reevaluada; bumps adr/v7,
    plantillas/vN y corpus/v10 —o viaje conjunto con el corpus/v9 de
    HV-2 si el Operador lo ordena junto—, con los espejos .skevi/ de las
    familias que toque
  Steps:
  - [ ] Registrar la decisión A/B del Operador con folio — verificación:
        transcripción con hora en el registro de la ronda de cierre
  - [ ] Ejecutar T01-T09 de PROP-010 §8 bajo la doctrina elegida —
        verificación: enlaces vivos donde la doctrina los exige;
        check_sizes, check_plans, check_reports, check_templates y
        unittest OK

TAREA HV-4 — Dossier de opciones sobre el doble commit del espejo
  Permitido: análisis y dossier en docs/reviews; la opción elegida toca
    tests/test_check_manifests.py,
    .github/workflows/skevi-gate.yml:51-56 y README.md:67-68, y
    .skevi/installed.json con .skevi/scripts-installed.json y
    .skevi/corpus-installed.json, con ADR nuevo si relaja ADR-031 —
    todo con confirmación del Operador.
  Prohibido: auto-observación de check_templates.py (frontera
    no_ofrece); retirar templates/skevi/*-installed.json (invariante de
    ADR-039); efectos Git sin lote aceptado.
  Consumes: SelfInstalledRecordsStayInSyncTests (último bump por
    familia y digests en el mismo commit); precedentes df1b4e0 ->
    329e2b6
  Produce: dossier con las dos opciones y sus puntos de contacto; la
    decisión del Operador registrada
  Steps:
  - [x] Escribir el dossier con costes y riesgos por opción —
        verificación: cita tests, CI y README con línea exacta
  - [ ] Registrar la decisión — verificación: registro en docs/reviews

TAREA HV-5 — Anotaciones hacia adelante en el índice de ADRs
  Permitido: columna Implementación de las filas ADR-009, ADR-017,
    ADR-020, ADR-021 y ADR-038 de docs/adr/00-INDICE.md, y
    docs/adr/MANIFEST.json para el bump.
  Prohibido: editar el texto sellado de los ADRs; tocar la columna
    Estado (regla del índice, líneas 53-57).
  Consumes: patrón vigente de las filas ADR-014 y ADR-018; pares
    ADR-009->012/013, ADR-017->018/044, ADR-020->028/031/036/039,
    ADR-021->025/038/041/042, ADR-038->042
  Produce: cinco filas anotadas; puede viajar en el mismo bump adr/v7
    de HV-3 si el Operador lo ordena junto
  Steps:
  - [ ] Añadir los punteros hacia adelante — verificación: grep por
        fila muestra el ADR posterior y check_sizes OK

TAREA HV-6 — Disposición de docs/orchestration/
  Permitido: análisis de docs/orchestration/orquestacion-codex-opencode-tmux.md
    y de docs/orchestration/orquestacion-codex-opencode-tmux-runbook.md
    (2026-08); propuesta de actualización o de archivo.
  Prohibido: trasladar sin decisión del Operador; efectos Git sin lote.
  Consumes: ADR-002 (vida útil); desfases contra ADR-016, ADR-017,
    ADR-023 y ADR-044
  Produce: recomendación con tabla de desfases y decisión registrada
  Steps:
  - [x] Cotejar runbook contra el canon vigente — verificación: tabla
        con cita de línea por desfase
  - [ ] Recomendar al Operador — verificación: registro con decisión

TAREA HV-7 — Ronda adversarial sobre este plan
  Permitido: ronda de contexto fresco sobre este archivo y registro en
    docs/reviews.
  Prohibido: que la ronda active tareas, cree autoridad o edite archivos.
  Consumes: este plan; verificación de contexto del 2026-11-06
  Produce: crea docs/reviews/2026-11-06-plan-hv-ronda.md con la decisión
  Steps:
  - [x] Ronda de contexto fresco sobre el plan — verificación: registro
        con decisión y sin HIGH/BLOCKER abiertos
  - [x] Incorporar hallazgos y reverificar — verificación: check_sizes,
        check_plans, check_reports y unittest OK tras la corrección

DoD: análisis del trabajo previo verificado contra la base con sus
correcciones declaradas; ninguna tarea ejecutada sin la autoridad que
declara; rondas y decisiones registradas en docs/reviews; trinquete,
sellos e inmutabilidad intactos; cuatro gates en verde.
Parada: hallazgo HIGH o BLOCKER abierto, base cambiada, o autoridad del
Operador denegada o vencida.
```

Límite declarado: la ronda de HV-7 la ejecuta una sesión fresca del
mismo proveedor salvo que el Operador designe otro revisor; el registro
lo declara. La ejecución de HV-1..HV-6 no fue ordenada en la sesión del
2026-11-06: cada tarea declara la autoridad que exige (efecto local,
decisión del Operador o lote con folio).
