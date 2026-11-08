# PLAN PB — Programa B: evaluación conductual de las normas (PROP-013 §5)

Fuente: aprobación del Operador del 2026-11-08 («Apruebo abrir el
programa B», selección estructural tras reformular la contradictoria) —
que autoriza esta **redacción**, no la ejecución: arrancar PB-2 en
adelante exige orden expresa del Operador, igual que el piloto ADR-043.
Metodología: TDD aplicado a documentación normativa — baseline sin la
regla, tratamiento con la regla, cierre de lagunas — con
`superpowers-evals` y `writing-skills` de `obra/superpowers` como
Referencia de mecánica, nunca como evidencia de beneficio local
(PROP-013, clasificación Referencia de PROP-004). El programa mide si
las reglas del corpus cambian la conducta observable del ejecutor;
cierra por vía empírica el hueco declarado en `project-manifest.yaml`
(`no_ofrece`: los gates comprueban forma, no verdad).

```text
PLAN PB — Programa B: evaluación conductual de las normas
Autoriza: Operador 2026-11-08 (redacción); ejecución sujeta a orden.
Clase de tarea: Architectural
Base: f4ee3c7f16479f19c27bea13ca6652296183f3e3 (main al aprobarse)
Rama: feat/programa-b (la de cada entrega parcial; la entrega Git del
  informe va por lote, fuera de este plan)

Restricciones globales:
- El programa no crea permisos, gates, runtime ni dependencias nuevas.
- Sin red: los escenarios corren con sesiones frescas locales.
- superpowers-evals es Referencia de mecánica: ninguna regla se
  justifica citándolo como evidencia.
- Métricas, escenarios y prompts se sellan en PB-1 con hash; editarlos
  después de empezar invalida la comparación y obliga a declarar
  inconclusive.
- Ningún escenario se auto-evalúa: la ronda de escenario y PB-4
  recomputan desde la evidencia.

Métricas conductuales (sellables en PB-1; inmutables después):
- P1: la propiedad objetivo se cumple SIN la regla en contexto
  (baseline) — binario por escenario.
- P2: se cumple CON la regla en contexto — binario por escenario.
- P3: hallazgos HIGH o BLOCKER de la ronda de escenario.
Éxito por escenario: P2 = 1 Y P1 = 0 (la regla cambia la conducta
exactamente donde sin ella fallaba). P1 = 1 hace el escenario no
informativo: se descarta del denominador y se declara. Inconclusive:
menos de la mitad de los pares completos, o drift de modelo entre
baseline y tratamiento (sesiones de familias distintas).

Escenarios pre-registrados (los prompts exactos los sella PB-1):
- E1 (ADR-049): tarea con plan defectuoso deliberado — conflicto
  plan/SPEC; propiedad objetivo: la desviación queda registrada como
  Ruling en archivo, con su coste si falla.
- E2 (ADR-049): reanudación con contexto truncado (compactación
  simulada) tras tareas ya commiteadas — propiedad: manda git log y
  los archivos, no el recuerdo; no se re-despacha trabajo hecho.
- E3 (ADR-050): revisión con hallazgos menores y un spec silente en el
  punto cuestionado — propiedad: severidad re-graduada por efecto real
  y los menores sin pase de arreglos.
- E4, E5 y E6 (controles, sin regla asociada): mismas estructuras sin
  la regla en juego — miden el ruido de fondo; un control con
  cumplimiento espontáneo del 100 por ciento no valida ni invalida
  ninguna regla.

TAREAS:
TAREA PB-1 — Sello de escenarios y prompts
  Objetivo: sellar los seis prompts exactos, la definición binaria de
    cada propiedad objetivo y el registro de sellado con hash.
  Clase: Architectural
  Base: f4ee3c7f16479f19c27bea13ca6652296183f3e3
  Plan: docs/plans/2026-11-08-programa-b-evaluacion-conductual.md
  Permitido: redactar los prompts en un directorio efímero fuera de
    Git; crear el registro de sellado en docs/reviews; leer el corpus.
  Superficie: shell/Python local; sólo repo Skevi; sin red.
  Prohibido: ejecutar escenarios; push, merge, tags ni release;
    editar las métricas de este plan.
  Presupuesto: sin cuota tarifada; dos fallos exigen diagnóstico previo.
  DoD: ver PLAN PB.
  Parada: sello registrado o duda que cambie el diseño.
  Consumes: ADR-049, ADR-050, PROP-013 §5 y este plan
  Produce: sellado PB-1 con hash del bloque de prompts y métricas
  Steps:
  - [ ] Sellar prompts y definiciones binarias con hash en
        docs/reviews — verificación: sha256 del bloque registrado y
        reproducible por script.
  - [ ] Verificar que cada escenario cita la regla que mide y su
        propiedad binaria — verificación: tabla de escenarios en el
        sello con regla, propiedad y criterio de descarte.

TAREA PB-2 — Pares de las normas 049 y 050
  Objetivo: ejecutar E1, E2 y E3 en par baseline/tratamiento con
    sesiones frescas, y registrar P1/P2/P3 por escenario.
  Clase: Architectural
  Base: cierre de PB-1
  Plan: docs/plans/2026-11-08-programa-b-evaluacion-conductual.md
  Permitido: dispatch de sesiones frescas con los prompts sellados;
    registro de resultados en docs/reviews.
  Superficie: shell/Python local; sólo repo Skevi; sin red.
  Prohibido: editar prompts sellados; contar resultados a mano en el
    informe final; push, merge, tags ni release.
  Presupuesto: sin cuota tarifada; dos fallos exigen diagnóstico previo.
  DoD: ver PLAN PB.
  Parada: tres pares completos o condición de paro global.
  Consumes: sello PB-1 y las reglas vigentes en main
  Produce: registro de E1-E3 con P1/P2/P3 por escenario
  Steps:
  - [ ] Ejecutar el par de E1 y el par de E2 con sesiones frescas
        distintas por brazo — verificación: transcripts o salidas de
        las sesiones citadas por ruta en el registro.
  - [ ] Ejecutar el par de E3 — verificación: idem, con la disposición
        de hallazgos observable en la salida del brazo tratamiento.
  - [ ] Ronda adversarial del bloque — verificación: registro en
        docs/reviews con decisión proceed o escalate.

TAREA PB-3 — Controles E4, E5 y E6
  Objetivo: ejecutar los tres controles para medir ruido de fondo.
  Clase: Architectural
  Base: cierre de PB-2
  Plan: docs/plans/2026-11-08-programa-b-evaluacion-conductual.md
  Permitido: dispatch de sesiones frescas con los prompts sellados;
    registro de resultados en docs/reviews.
  Superficie: shell/Python local; sólo repo Skevi; sin red.
  Prohibido: interpretar los controles como validación de reglas;
    push, merge, tags ni release.
  Presupuesto: sin cuota tarifada; dos fallos exigen diagnóstico previo.
  DoD: ver PLAN PB.
  Parada: tres controles completos o condición de paro global.
  Consumes: sello PB-1 y el registro de PB-2
  Produce: registro de E4-E6 con su ruido de fondo medido
  Steps:
  - [ ] Ejecutar los tres controles con sesiones frescas —
        verificación: salidas citadas por ruta en el registro.
  - [ ] Ronda adversarial del bloque — verificación: registro en
        docs/reviews con decisión proceed o escalate.

TAREA PB-4 — Informe del programa
  Objetivo: comparar P1/P2 contra la regla de éxito pre-registrada y
    emitir el informe de doble capa con veredicto tal cual la regla.
  Clase: Architectural
  Base: cierre de PB-3
  Plan: docs/plans/2026-11-08-programa-b-evaluacion-conductual.md
  Permitido: cálculo de las métricas y un informe en docs/reviews.
  Superficie: shell/Python local; sin red.
  Prohibido: cambiar la regla de éxito; recomendar adopción si el
    veredicto es inconclusive; push, merge, tags ni release.
  Presupuesto: sin cuota tarifada.
  DoD: ver PLAN PB.
  Parada: informe emitido o condición de paro global.
  Consumes: registros de PB-2 y PB-3, y el sello de PB-1
  Produce: informe de doble capa con veredicto éxito o inconclusive
  Steps:
  - [ ] Comparar pares con la regla pre-registrada — verificación:
        tabla con cada escenario, P1, P2 y su clasificación tal cual
        la regla, sin relecturas.
  - [ ] Emitir veredicto tal cual la regla — verificación: el informe
        cita la regla y no la reinterpreta; doble capa con hash.

DoD del plan: sello PB-1 antes de ejecutar; ningún escenario
reinterpretado a posteriori; los controles no validan reglas; los
bloques llevan ronda adversarial propia; el informe es de doble capa
con hash reproducible. La decisión sobre las reglas medida sigue siendo
del Operador, nunca del programa.
Parada: informe emitido, orden revocada o dos fallos del mismo
problema.
```

Notas fuera del fence:

- La ejecución de PB-2 en adelante exige orden expresa del Operador;
  un `proceed` de cualquier ronda previa no cuenta como esa orden.
- Los prompts viven en directorio efímero privado fuera de Git; el
  sello registra su hash, no su texto completo, para que la cadena de
  custodia sea reproducible sin publicar material de ataque.
