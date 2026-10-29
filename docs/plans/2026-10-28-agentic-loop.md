# PLAN AG — Continuación autónoma acotada

Autoriza: el Operador aprobó B y precisó el 2026-10-28 que el agente puede
proponer push/merge según el avance y ejecutarlos por instrucción humana
aplicable o por una configuración futura válida. Consume la
[SPEC](../specs/SPEC-AGENTIC-2026-10-28.md) y
[PROP-012](../history/PROP-012-continuacion-agentica-acotada.md).
Alcance: implementar B y esa política condicional en documentos locales;
la regla general no autoriza un push o merge concreto. El Operador autorizó
después commits, push y merge convenientes para esta sesión (AG-6).
Clase Architectural: cambia una interfaz para adoptantes (`04` §5.3).

Fuente única de los pasos y del DoD de este incremento. Los casos de la SPEC
viven en la SPEC; este plan fija cómo comprobarlos. La propuesta y la
SPEC son fuente de requisitos, no aceptación de un gate externo.

```text
PLAN AG — Continuación autónoma acotada
Autoriza: Operador 2026-10-28, B y política condicional de push/merge
Clase de tarea: Architectural
Base: a105549d0f471acf0250adb17ca08fe9629475de
Rama: docs/agentic-loop-spec-proposal

Restricciones globales:
- Cambiar sólo push ordinario/merge: instrucción humana o config válida.
- Force-push, tags, releases y destructivas conservan su gate separado.
- Sin configuración vigente ni instrucción específica, el gate es humano.
- No agregar runtime, dependencia, skill, plugin o memoria obligatorios.
- Commit, push y merge sólo con autorización aplicable; la sesión actual la
  tiene para AG-6. No tags, release ni despliegue.

TAREAS:
TAREA AG-1 — Decisión de alcance B
  Objetivo: registrar la elección B sin alterar ADR-018.
  Clase: Architectural
  Base: a105549d0f471acf0250adb17ca08fe9629475de
  Plan: docs/plans/2026-10-28-agentic-loop.md
  Permitido: SPEC, propuesta, ADR nuevo e índice de ADR locales.
  Superficie: shell/Python/Git local; sólo repo Skevi y temporales; sin red.
  Prohibido: cambiar ADR-018 o permisos Git; commit y efectos externos.
  Presupuesto: sin cuota tarifada; dos fallos exigen diagnóstico antes de otro intento.
  DoD: ver PLAN AG.
  Parada: ADR-043 e índice coherentes con la instrucción del Operador.
  Consumes: SPEC-AG-01 y PROP-012
  Produce: ADR-043 aceptado, índice y PROP-012 en historia
  Steps:
  - [x] Registrar alcance y alternativas sin editar ADR-018 —
        verificación: leer ADR-043, ADR-018 e índice; comparar autoridad.
  - [x] Mover PROP-012 a docs/history y reparar enlaces — verificación:
        rg de la ruta antigua y comprobación de enlaces nuevos.

TAREA AG-2 — Regla mínima en F0 y F3
  Objetivo: aplicar el ciclo autónomo dentro de TAREA.
  Clase: Architectural
  Base: a105549d0f471acf0250adb17ca08fe9629475de
  Plan: docs/plans/2026-10-28-agentic-loop.md
  Permitido: guía F0/F3 y correcciones de SPEC vinculadas.
  Superficie: shell/Python/Git local; sólo repo Skevi y temporales; sin red.
  Prohibido: ampliar autoridad, superficie o presupuesto de lectura en silencio.
  Presupuesto: sin cuota tarifada; dos fallos exigen diagnóstico antes de otro intento.
  DoD: ver PLAN AG.
  Parada: C1-C10 trazables o contradicción que exija otra decisión.
  Consumes: SPEC-AG-01, ADR de AG-1 y guía actual
  Produce: F0 §5 y F3 §1 actualizados; §8 sigue como regla referida
  Steps:
  - [x] Explicitar investigación previa y pregunta material en F0 —
        verificación: C4/C8 y frontera de diseño siguen localizables.
  - [x] Explicitar ciclo dentro de TAREA en F3 sin DoD paralelo —
        verificación: C1-C3/C5-C10 y §3-§5/§7-§8 compatibles.

TAREA AG-3 — Push/merge con autoridad condicional
  Objetivo: normar propuesta proactiva y fuentes válidas de autorización.
  Clase: Architectural
  Base: a105549d0f471acf0250adb17ca08fe9629475de
  Plan: docs/plans/2026-10-28-agentic-loop.md
  Permitido: ADR nuevo, AGENTS.md, F3 §7, SPEC y project-manifest.
  Superficie: shell/Python/Git local; sólo repo Skevi y temporales; sin red.
  Prohibido: ejecutar push/merge o activar una configuración inexistente;
    force-push, rebase compartido, reset y borrado remoto fuera de alcance.
  Presupuesto: sin cuota tarifada; dos fallos exigen diagnóstico antes de otro intento.
  DoD: ver PLAN AG.
  Parada: reglas coherentes con §4.3/§6.6 o duda de autoridad.
  Consumes: instrucción del Operador y estándar §4.3/§6.6
  Produce: ADR nuevo, regla local y propuesta al gate desde F3
  Steps:
  - [x] Definir instrucción humana y configuración futura sin auto-otorgar
        permisos — verificación: C13-C17 incluyen controles positivos y
        negativos, con force-push explícitamente fuera.
  - [x] Proponer push/merge al gate en hitos verificables — verificación:
        F3 §7 exige dossier y no interpreta progreso como autorización.

TAREA AG-4 — Versionado y compatibilidad
  Objetivo: sellar exactamente los archivos fuente modificados.
  Clase: Architectural
  Base: a105549d0f471acf0250adb17ca08fe9629475de
  Plan: docs/plans/2026-10-28-agentic-loop.md
  Permitido: manifests fuente, ejemplos y registros de instalación propios.
  Superficie: shell/Python/Git local; sólo repo Skevi y temporales; sin red.
  Prohibido: source ficticio, commit sin permiso y efectos externos.
  Presupuesto: sin cuota tarifada; dos fallos exigen diagnóstico antes de otro intento.
  DoD: ver PLAN AG.
  Parada: digests, versiones y procedencia correctos o falta commit fuente.
  Consumes: archivos canónicos de AG-1..AG-3 y manifiestos vigentes
  Produce: corpus y ADR manifests actualizados; registros afectados
  Steps:
  - [x] Sellar ADRs y corpus con versiones correctas — verificación:
        check_sizes y comparación independiente de hashes.
  - [x] Inspeccionar referencias, ruta de lectura y adopción —
        verificación: enlaces resuelven y check_sizes muestra ruta <=1620.
  - [x] Sincronizar ejemplos e instalación con procedencia real —
        verificación: suite y check_templates; si falta commit fuente,
        reportar PARCIAL sin inventar source.

TAREA AG-5 — Revisión y cierre local
  Objetivo: refutar y verificar el incremento documental local.
  Clase: Architectural
  Base: a105549d0f471acf0250adb17ca08fe9629475de
  Plan: docs/plans/2026-10-28-agentic-loop.md
  Permitido: diff, checks, tests y registro de revisión en docs/reviews.
  Superficie: shell/Python/Git local; sólo repo Skevi y temporales; sin red.
  Prohibido: cierre OK con gate rojo; commit y efectos externos.
  Presupuesto: sin cuota tarifada; dos fallos exigen diagnóstico antes de otro intento.
  DoD: ver PLAN AG.
  Parada: proceed verificado o escalate por autoridad/procedencia.
  Consumes: SPEC-AG-01, resultado AG-1..AG-4 y gates del repo
  Produce: registro de ronda y reporte con límites del piloto
  Steps:
  - [x] Ejecutar gates y tests pertinentes — verificación: salida real de
        check_sizes, check_plans, check_reports y unittest.
  - [x] Revisar con contexto fresco y disponer hallazgos — verificación:
        registro en docs/reviews con proceed o escalate, hash reproducible.

TAREA AG-6 — Entrega Git autorizada
  Objetivo: fijar procedencia y entregar la norma por PR sin publicar release.
  Clase: Architectural
  Base: a105549d0f471acf0250adb17ca08fe9629475de
  Plan: docs/plans/2026-10-28-agentic-loop.md
  Permitido: commits locales de fuente y registros .skevi/; push de esta
    rama, PR a main y merge si CI y revisión cumplen el gate.
  Lote: SKV-AG-PUSH-20261028-01, SKV-AG-MERGE-20261028-01 (anotado el
    2026-10-29 por E6: folios anunciados antes de cada efecto, sin
    aceptación registrada; ver docs/reviews/2026-10-28-pr78-git-dossier.md)
  Superficie: Git y gh con origin; red sólo para fetch, push, PR y checks.
  Prohibido: force-push, tag, release, despliegue y cambios fuera de alcance.
  Presupuesto: sin cuota tarifada; dos fallos exigen diagnóstico previo.
  DoD: ver PLAN AG y estándar §4.3/§5; fuente y .skevi/ trazables.
  Parada: CI rojo, revisión bloqueante, base cambiada o autoridad incierta.
  Consumes: autorización del Operador de esta sesión y AG-1..AG-5
  Produce: dos commits, PR integrado y árbol local/remoto conciliado
  Steps:
  - [x] Commit fuente y registrar SHA real — verificación: Git log del
        manifest y diff del commit; primer estado .skevi/ transitorio.
  - [x] Sincronizar .skevi/ y cerrar gates — verificación: unittest y los
        tres checkers en verde, check_templates y source@SHA real.
  - [ ] Push, PR y merge condicionado — verificación: CI del commit,
        revisión, estado de protección y SHA remoto final.

DoD: casos de SPEC trazables en F0/F3, autorización condicional sin config
activa ni permiso autodeclarado; PROP-012 en historia, ADRs con cabecera,
índice y versión de implementación coherentes; diff revisado; gates y tests
pertinentes OK; ronda fresca sin HIGH/BLOCKER abiertos. La copia .skevi/
se actualiza sólo con procedencia verificable; no se inventa source. El
cierre local revisado no acredita commit/PR/publicación; si la prueba de
procedencia exige un commit no autorizado, el estado sigue PARCIAL.
Parada: implementación local revisada o dependencia de nueva autoridad.
```

El piloto de tareas reales, una configuración futura y cada push/merge
concreto son fases u operaciones posteriores. Un `proceed` no los activa.

Las fichas de AG-1..AG-4 se incorporaron después de comenzar el borrador
local, por un hallazgo HIGH de la ronda anterior. Fijan el trabajo restante
y permiten auditar alcance, sin acreditar un preflight que no ocurrió.

Cierre de AG-6 (2026-10-29, PLAN LG tarea LG-2): el push y el merge del
PR #78 se ejecutaron, pero el último step queda sin marcar porque su
verificación no se cumplió: no consta revisión registrada del head final
ni aceptación por folio. Hechos y límites en
[el dossier del PR #78](../reviews/2026-10-28-pr78-git-dossier.md) y
[el del PR #79](../reviews/2026-10-29-pr79-git-dossier.md).
