# PLAN AUDIT-2026-09-07 — Mejora de Skevi por evidencia

Autoriza: [SPEC-AUDIT](../specs/SPEC-AUDIT-2026-09-07-mejoras.md), derivada
de la instrucción humana del 2026-09-07: persistir el plan detallado e iniciar.
Clase de tarea: Architectural — crear plan multi-tarea (F0 §2, ADR-013).
Estado: T00-T10, T05-A y T14 completos; T06-T10 cerrados por decisión; siguiente T11.
Base: `17413f150d08e1e65b72f70a858104505950e751`.
Rama de retoma: `docs/adopt-authority-consistency`. El plan es dueño de steps/DoD.

## Propósito, alcance y restricciones

Resultado esperado: eliminar el falso éxito del gate y conducir las demás
mejoras a decisiones y entregables verificables. El primer cierre incluye
plan completo, SPEC, arreglo y revisión; no promete completar todo el programa
en esta sesión. Planificar una decisión no significa aceptarla.

Restricciones globales, verbatim de SPEC-AUDIT:
- No modificar PROP-008 preexistente durante el primer incremento.
- No adoptar propuestas por el solo hecho de planificarlas.
- No escribir memoria ni checkpoints; la persistencia solicitada es Markdown.
- No modificar GitHub, consumidores, hooks, dependencias ni política de CI.
- Sin commit, push, merge, tags ni releases en este incremento.

Las restricciones de ejecución externa se levantan sólo por autorización
específica posterior y su registro; este plan nunca concede esa autoridad.
No se incorporan AN-KLA obligatorio, motores de gobernanza ni certificaciones.

Actualización de autoridad, 2026-09-07: el humano autoriza «commit y push
segun creas correponda» y continuar T14. Se permite versionar T00-T04 y T14,
y publicar fix/audit-gate-read-errors en origin; ninguna otra operación externa.
La restricción anterior describe el primer incremento antes de esta autorización.
Retoma T05: «adelante», con permiso vigente de commit/push a criterio del agente;
publicación documental en docs/audit-authority-consistency, sin adoptar política.
Evidencia T05/A: [adopción y cierre](../reviews/2026-09-07-t05-adoption.md).

## Gobierno, calendario y medición

Responsable de ejecución local: agente de esta tarea. Aceptante de políticas
y operaciones protegidas: humano propietario. Revisor: contexto fresco,
distinto del ejecutor; otra sesión no acredita otro modelo.
Cada retoma registra responsable efectivo, rama, SHA y diferencias explicadas.

Secuencia: P0 → P1 → P2; P3 depende de P2; P4 depende de decisiones de P2/P3;
P5 integra sólo incrementos aceptados. Cada incremento vuelve a F0→F3 cuando
sus disparadores lo requieran; P0-P5 son fases del programa, no reemplazos.

| Fase | Tareas | Salida | Esfuerzo inicial estimado |
|---|---|---|---|
| P0 Preparación | T00-T01 | alcance, SPEC y plan verificados | 1 sesión |
| P1 Gate | T02-T04, T14 | correcciones con RED/GREEN y revisión | 1-2 sesiones |
| P2 Coherencia | T05-T07 | matriz, decisiones e IDs trazables | 1-2 sesiones |
| P3 Integración y adopción | T08-T09 | propuestas con casos negativos | 2-3 sesiones |
| P4 Calidad y gestión | T10-T11 | piloto acotado y evaluación | 2-3 sesiones |
| P5 Cierre y mantenimiento | T12-T13 | transferencia y dossier | 1 sesión |

Estimaciones orientativas, sin fecha comprometida: dependen de revisión y
decisiones. Registrar duración real al cerrar cada tarea; recalibrar tras P1.
Límite de trabajo simultáneo: un cambio de producción y una revisión de lectura.
Coste inmediato: stdlib y herramientas existentes; cero instalación o servicio
nuevo. Ante necesidad de gasto, detener esa tarea y presentar coste y motivo.

Indicadores: falsos OK reproducidos/corregidos; contradicciones abiertas;
referencias ambiguas; tiempo y retrabajo por tarea. Para el piloto medir
beneficio y carga documental antes/después; un caso no permite generalizar.
Una tarea cerrada tiene evidencia; una descartada tiene razón y aceptante.

## P0 — Preparación y diseño

```text
TAREA T00
  Consumes: SPEC-AUDIT, REQ-AUD-01/05; `AGENTS.md`
  Produce: base y alcance verificables en SPEC-AUDIT
  Steps:
  - [x] Leer guía y fronteras — verificación: restricciones de SPEC-AUDIT
        mantienen independencia, gate local y operaciones separadas.
  - [x] Verificar Git y AN-KLA — verificación: SHA base confirmado, sólo
        PROP-008 preexistente, context/verify OK con entorno virtual.
  - [x] Aislar rama propia — verificación: git branch --show-current devuelve
        fix/audit-gate-read-errors; ningún cambio ajeno eliminado.
TAREA T01
  Consumes: REQ-AUD-01/06; `templates/plan-de-implementacion.md`
  Produce: plan completo y SPEC-AUD-01 con F0/F1 de entrada
  Steps:
  - [x] Definir requisitos, no objetivos y casos — verificación: SPEC-AUDIT
        identifica seis REQ, casos C1-C6 y ausencia de preguntas para P1.
  - [x] Comprobar estructura y tamaño — verificación: ambos gates OK;
        este plan <=300 líneas y cada tarea cumple E1-E5.
```

## P1 — Corrección del gate y evidencia

```text
TAREA T02
  Consumes: T01; SPEC-AUD-01; `tests/test_check_sizes.py`
  Produce: pruebas de regresión del CLI/coordinador existente
  Steps:
  - [x] Añadir casos C1-C4 — verificación: README ilegible, Markdown no
        canónico ilegible, UTF-8 inválido y segunda lectura del registro.
  - [x] Ejecutar RED antes del arreglo — verificación: fallan por OK/0
        indebido o excepción sin controlar; guardar salida y conteos reales.
  - [x] Cubrir exenciones C5 — verificación: ruta/extensión exenta no se
        lee; fixture aislada, sin chmod dependiente del usuario del sistema.
TAREA T03
  Consumes: T02; SPEC-AUD-01; `scripts/check_sizes.py`
  Produce: bloqueo controlado de errores de lectura
  Steps:
  - [x] Propagar errores del conteo — verificación: None queda reservado
        a exenciones y entradas no verificables no producen éxito.
  - [x] Controlar ambas lecturas — verificación: BLOQ/1 con ruta relativa
        y motivo fijo, sin traceback, bytes de entrada ni excepción cruda.
  - [x] Ejecutar GREEN focal y suite — verificación: casos nuevos y las
        62 pruebas previas pasan; exenciones previas y límites se conservan.
  - [x] Declarar binarios locales comprobados en `skevi-gate.json` —
        verificación: sólo .DS_Store y docs/.DS_Store, file confirma tipo
        Apple Desktop Services Store; motivo en SPEC, sin patrón global nuevo.
TAREA T04
  Consumes: T03; SPEC-AUDIT, REQ-AUD-05
  Produce: crea `docs/reviews/2026-09-07-mejoras-auditoria.md`
  Steps:
  - [x] Revisar diff y gates — verificación: diff --check limpio, ambos
        gates OK, sólo SPEC, plan, reporte, script, test y configuración local.
  - [x] Ronda adversarial fresca — verificación: revisor lee diff/SPEC,
        comprueba casos y emite proceed; HIGH corregidos antes del cierre.
  - [x] Persistir evidencia en dos capas — verificación: comandos, RED,
        GREEN, base, hashes, hallazgos y límites reproducibles en reporte.
  - [x] Actualizar avance — verificación: sólo steps acreditados marcados;
        el plan completo continúa abierto y no hubo commit/publicación.
```

DoD del primer incremento: T00-T04 completos, SPEC-AUD-01 satisfecha, gates y
suite verdes, revisión fresca proceed, evidencia persistida. Parada de esta
sesión: entregar ese incremento local, con el siguiente trabajo identificado.

Seguimiento descubierto por la revisión fresca, posterior al primer cierre:

```text
TAREA T14
  Consumes: T04; SPEC-AUD-02/REQ-AUD-07; `scripts/check_sizes.py`
  Produce: diagnóstico saneado de configuración en incremento separado
  Steps:
  - [x] Fijar SPEC acotada de configuración — verificación: delimita lectura
        y validación, sin atribuir a SPEC-AUD-01 saneamiento de todo el CLI.
  - [x] Reproducir payload en error de load_config — verificación: RED
        falla porque BLOQ imprime la excepción cruda, no por salida exitosa.
  - [x] Corregir y revisar — verificación: diagnóstico útil sin payload,
        GREEN focal/suite, gates y revisión fresca; mantener configuración válida.
```

T14 precede a P2. No bloquea T04: el defecto ya existía antes del arreglo y
no está en las lecturas del recorrido cubiertas por SPEC-AUD-01. T14 cerrado:
[evidencia y dossier](../reviews/2026-09-07-t14-config-diagnostics.md).

## P2 — Coherencia documental y revisión exigible

```text
TAREA T05
  Consumes: T04; REQ-AUD-06; `docs/estandar-diseno-software-github.md`
  Produce: deliberación archivada en `docs/history/AUDIT-authority-consistency.md`
  Steps:
  - [x] Contrastar AGENTS, índice, F3 §7, guía 05 y estándar §6 —
        verificación: tabla con texto, prioridad efectiva y diferencia.
  - [x] Proponer excepción local explícita o remisión a fuente única —
        verificación: no ampliar permisos ni borrar restricciones humanas.
  - [x] Presentar decisión — verificación: aceptante elige A («adelante»);
        sólo después, tarea separada aplica norma/guía y revisa referencias.
TAREA T05-A
  Consumes: T05/D1=A; SPEC-AUD-03; aprobación humana del 2026-09-07
  Produce: ADR-018 y cinco destinos A1-A5; reporte t05-adoption en reviews
  Steps:
  - [x] Aplicar A y archivar deliberación — verificación: ADR/índice y links.
  - [x] Verificar y revisar — verificación: C1-C9, gates y ronda fresca proceed.
  - [x] Cerrar rastro Git — verificación: header con commit y SHA remoto exacto.
TAREA T06
  Consumes: T05; REQ-AUD-06; `docs/adr/ADR-001-gate-local-sin-ci.md`
  Produce: crea `docs/proposals/AUDIT-review-enforcement.md`
  Steps:
  - [x] Leer configuración remota vigente — verificación: registrar
        revisión exigida, bypass y protección; no inferir historial de merges.
  - [x] Comparar revisión obligatoria con excepción compensada local —
        verificación: cada opción liga evidencia a SHA y declara riesgo/coste.
  - [x] Preparar cambio exacto o excepción — verificación: decisión humana
        registrada antes de configurar GitHub; no añadir Actions por omisión.
TAREA T07
  Consumes: T05; REQ-AUD-06; `docs/adr/ADR-016-reportes-en-dos-capas.md`
  Produce: crea `docs/proposals/AUDIT-proposal-identifiers.md`
  Steps:
  - [x] Inventariar PROP-006 local e issue 28 — verificación: títulos y
        enlaces exactos distinguen reportes de versionado de plantillas.
  - [x] Proponer ID inequívoco y alias histórico — verificación: referencias
        entrantes inventariadas; ninguna evidencia histórica se reescribe.
  - [x] Aplicar resolución tras decisión — verificación: búsquedas locales
        no ambiguas y cambio de issue sólo con autorización externa específica.
```

## P3 — Contratos de integración y adopción

```text
TAREA T08
  Consumes: T05/T07; REQ-AUD-06
  Produce: crea `docs/proposals/AUDIT-ankla-contract-review.md`
  Steps:
  - [x] Revisar el contrato aterrizado (05 §6) — verificación: separar
        estados ausente, válido, dañado e inspección imposible por estado.
  - [x] Revisar upgrades y checkpoint — verificación: clasificación por
        disparadores; cadencia nunca concede escritura en una tarea de lectura.
  - [x] Definir folios y concurrencia — verificación: alcance de unicidad
        explícito y dos productores desde la misma base no duplican folio.
  - [x] Ejercitar casos negativos y sin memoria — verificación: no hay
        activación silenciosa ni reparación automática; revisión fresca proceed.
  - [x] Presentar D1-D2 y compatibilidad — verificación: decisión humana
        registrada en conversación antes de aterrizar; ADR-019.
TAREA T09
  Consumes: T07; REQ-AUD-06; `templates/skevi/usage-guide.md`
  Produce: crea `docs/proposals/AUDIT-template-provenance.md`
  Steps:
  - [x] Reconciliar con issue 28 — verificación: una sola propuesta viva
        por objetivo; no duplicar el trabajo de versionado existente.
  - [x] Definir origen/versiones/adaptaciones — verificación: tres casos
        separan copia antigua compatible, incompatible y personalizada.
  - [x] Diseñar migración reversible — verificación: no comparar como
        iguales los bytes de plantilla y relleno; no mutar consumidores.
  - [x] Pilotar con fixture local tras decisión de diseño — verificación:
        un adoptante identifica origen exacto y cambios sin requerir red.
```

## P4 — Calidad, mantenimiento y gestión proporcionada

```text
TAREA T10
  Consumes: T05/T08/T09; REQ-AUD-06
  Produce: crea `docs/proposals/AUDIT-quality-maintenance-pilot.md`
  Steps:
  - [x] Elegir caso y atributos relevantes — verificación: escenarios de
        adopción/cambio/fallo con estímulo, respuesta, medida y responsable.
  - [x] Definir mantenimiento — verificación: dueño, canal de defectos,
        triage de seguridad, compatibilidad y retirada según el caso elegido.
  - [x] Comparar con F3 existente — verificación: sólo extender carencias
        observadas, sin declarar ausente el trabajo continuo ya documentado.
TAREA T11
  Consumes: T10; REQ-AUD-06
  Produce: crea `docs/proposals/AUDIT-management-pilot.md`
  Steps:
  - [ ] Fijar piloto antes de medir — verificación: beneficiario, resultado,
        línea base, métrica, muestra, límite de esfuerzo y umbral acordados.
  - [ ] Ejecutar seguimiento proporcional — verificación: responsables,
        hitos/dependencias, esfuerzo real, riesgos y cambios con impacto.
  - [ ] Evaluar beneficio frente a carga — verificación: datos de tiempos
        y retrabajo sustentan adoptar, ajustar o descartar; no certificación PMI.
  - [ ] Proponer sólo prácticas que superen el piloto — verificación:
        cada regla tiene procedencia, coste y excepción según contexto.
```

## P5 — Transferencia y cierre gobernado

```text
TAREA T12
  Consumes: incrementos aceptados de T05-T11; REQ-AUD-06
  Produce: crea `docs/reviews/AUDIT-program-closeout.md`
  Steps:
  - [ ] Conciliar entregables y pendientes — verificación: cada tarea tiene
        evidencia, decisión o descarte; ningún piloto equivale a regla aceptada.
  - [ ] Preparar transferencia — verificación: mantenedor, limitaciones,
        seguimiento, notas de compatibilidad y comandos locales reproducibles.
  - [ ] Revisión fresca del conjunto — verificación: no contradicciones
        HIGH abiertas, gates verdes, links reales y autoridad intacta.
TAREA T13
  Consumes: T12; REQ-AUD-05; estándar §4.3
  Produce: dossier exacto de publicación, sólo si se solicita
  Steps:
  - [ ] Preparar diff final y operaciones — verificación: archivos propios,
        SHA revisado y operaciones enumeradas; no incluir trabajo ajeno.
  - [ ] Obtener autoridad por operación — verificación: aceptación vigente
        para commit/push/PR/merge/tag/release según lo que se proponga.
  - [ ] Verificar después de cada operación autorizada — verificación:
        SHA remoto, revisión y estado real; sin permiso, queda no ejecutada.
```

## Riesgos, cambios y cierre del programa

R1: falsos BLOQ sobre binarios no exentos → documentar UTF-8/exenciones;
responsable ejecutor; no ampliar exenciones por conveniencia.
R2: burocracia sin valor → piloto T11 y descarte explícito; aceptante humano.
R3: autoridad inferida del plan → gates T05/T06/T08/T13; responsable ejecutor.
R4: trabajo ajeno alterado → comprobar árboles ajenos antes/después; ejecutor.
R5: hashes confundidos con autoridad → sólo integridad, nunca aceptación;
responsable revisor. Fallos HIGH paran el incremento afectado.

Cambios: registrar motivo, impacto en tareas/plazo/coste/calidad y aceptante.
No cambiar DoD para ocultar un fallo. Sin evidencia, el step permanece abierto.
DoD del programa: tareas ejecutadas o descartadas por decisión trazable;
gates y pruebas aplicables verdes; mantenimiento transferido. T13 es condicional:
sin solicitud de publicación, su no ejecución no invalida el resultado local.

Referencias informativas, sin autoridad normativa nueva:
[PMI](https://www.pmi.org/standards/pmbok),
[arc42](https://docs.arc42.org/section-10/),
[NIST SSDF](https://csrc.nist.gov/pubs/sp/800/218/final).
Base de priorización: ronda fresca SKV-AUDIT-20260907T182032Z en conversación.
