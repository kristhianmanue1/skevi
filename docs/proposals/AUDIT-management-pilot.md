# AUDIT-management-pilot — Piloto de gestión proporcionada sobre el propio programa

> **Estado:** RESUELTA — D1-D4 aceptadas por el humano (2026-09-07, en
> conversación). Los veredictos alimentan el cierre (T12) y el dossier
> de publicación (T13), sin cambios normativos adicionales.
> **Origen:** plan AUDIT-2026-09-07, tarea T11 (REQ-AUD-06). Consume T10.
> La muestra del piloto es el propio programa AUDIT: once tareas con
> datos observables en Git, plan, reportes y checkpoint. Un caso no
> permite generalizar (advertencia ya presente en el plan).

## D1 — Piloto fijado antes de medir

- **Beneficiario**: el humano mantenedor — visibilidad y control del
  programa con la mínima ceremonia que los datos sostengan.
- **Resultado deseado**: continuar un programa multi-tarea entre
  sesiones sin pérdida de contexto y sin que un defecto material
  sobreviva a la revisión.
- **Línea base**: estimaciones del plan §Gobierno (P0: 1 sesión; P1:
  1-2; P2: 1-2; P3: 2-3; P4: 2-3; P5: 1) y el defecto conocido
  pre-programa: el falso OK del gate, confirmado y corregido en T02-T04.
- **Métrica**: (a) desviación sesiones reales vs estimadas por fase;
  (b) defectos reales detectados por ronda adversarial, por tarea;
  (c) retrabajo post-cierre (tareas descubiertas después); (d) coste
  documental por cierre.
- **Muestra**: T00-T10 (11 tareas), tres tramos de trabajo observables
  por marcas de commit (mañana: adopciones PROP #29-#33; mediodía:
  P1 y T05/T05-A; tarde: T06-T10, cinco tareas seguidas).
- **Límite de esfuerzo**: evaluación sólo con datos existentes — cero
  herramientas nuevas, cero gasto adicional.
- **Umbral de adopción por práctica**: se adopta si detectó o bloqueó
  ≥1 defecto real **o** permitió continuar entre sesiones sin
  re-trabajo de contexto, **y** su coste documental cabe en los
  formatos ya existentes. No supera el umbral → se descarta con razón.

## D2 — Seguimiento proporcional ejecutado (datos)

- **Responsables**: humano acepta políticas y autoriza por operación
  (seis autorizaciones commit/push registradas hoy); agente ejecuta y
  reporta; revisor en contexto fresco.
- **Hitos/dependencias**: P0→P1→P2→P3 sin salto; T14 descubierto por
  revisión se insertó antes de P2; P3 esperó a T05/T07 según plan.
- **Esfuerzo real**: P2 (T05-T07) consumió su tope estimado (2
  tramos); P3 (T08-T09) quedó por debajo de la estimación (2-3 →
  menos de 1 tramo); P4 va por debajo (T10 dentro del mismo tramo).
- **Riesgos y cambios con impacto**: T14 (nueva tarea por hallazgo de
  revisión), T05-A (división de T05 en adopción separada) y tres
  ciclos fix-and-retry documentados en el repo: PROP-008 con 2 BLOCKER
  + 1 HIGH (su cabecera), D3/T06 con 3 MED corregidos (reporte de
  aterrizaje) y T08 con evidencia rehecha por artefacto de layout
  (propuesta T08 §1) — coste real de la frescura, no de la gestión.

## D3 — Evaluación beneficio frente a carga

- **Ronda adversarial fresca** (04 §5) — dato: detectó el falso OK del
  gate (T04), retiró R1/R2 de PROP-008, expuso artefactos de layout
  (T08). **Adoptada**: umbral (i) con tres defectos reales.
- **Checkpoint de continuidad** (05 §6) — dato: la retoma de hoy
  partió del checkpoint sin re-trabajo de contexto. **Adoptada**:
  umbral (ii).
- **Estado + checkboxes del plan** — dato: once tareas trazables en
  todo momento; T14 y T05-A se insertaron sin pérdida. **Adoptada**:
  umbral (ii), coste ~0.
- **Reportes en dos capas** (ADR-016) — dato: trazabilidad útil; el
  hash cubre forma, no verdad — el reporte D3 registró evidencia que
  la ronda luego corrigió. **Ajustada**: reservarla a cambios
  materiales (disparadores 04 §5.3).
- **Duración real registrada por tarea** — dato: «Esfuerzo observado»
  sólo en 2 de los cierres; la desviación de P3/P4 fue visible
  igualmente por checkpoints y commits. **Ajustada**: registrar
  esfuerzo en el checkpoint, no en prosa de cada reporte.
- **Informes periódicos de estado (estilo PMI)** — dato: sin defecto
  que los justifique; R2 del plan los señala como burocracia sin
  valor. **Descartada**: sin procedencia que los pida.

## D4 — Prácticas propuestas (sólo las que superan)

Ninguna regla nueva: el piloto **ratifica** con datos las prácticas ya
normadas — ronda fresca (04 §5, ADR-008), checkpoint (05 §6, ADR-019),
plan viviente (ADR-010/014) y dos capas para material (ADR-016) — y
registra dos ajustes de práctica, sin norma: esfuerzo real en el
checkpoint; reportes en dos capas sólo bajo disparadores. Excepción
declarada: muestra única, no generalizable; la evaluación se repite si
el programa crece.

## Criterios de decisión aplicados

§8 del estándar: evaluar con datos que ya existen es lo más simple y
lo más reversible; no añade dependencias ni ceremonia; lo descartado
(informes periódicos) queda registrado con su razón para no
reintroducirse por hábito. Sin certificación PMI ni conformidad —
no objetivos de la SPEC.

## Adopción

D1-D4 quedan aceptadas o rechazadas por el humano en conversación.
Con la aprobación, este documento queda como registro del piloto
(cabecera RESUELTA); los veredictos alimentan el cierre (T12) y el
dossier de publicación (T13), sin cambios normativos adicionales.
