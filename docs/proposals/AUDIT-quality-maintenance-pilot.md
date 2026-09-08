# AUDIT-quality-maintenance-pilot — Piloto acotado de calidad y mantenimiento

> **Estado:** RESUELTA — D1-D3 aceptadas por el humano (2026-09-07, en
> conversación). El piloto se mide en el próximo cambio normativo que
> califique; su resultado alimenta T11-T13.
> **Origen:** plan AUDIT-2026-09-07, tarea T10 (REQ-AUD-06). Consume
> T05/T08/T09. Comparación con la práctica existente en §3: sólo se
> extiende lo observado como carencia; nada de lo ya documentado se
> declara ausente.

## 1. Caso elegido y escenarios

**Caso: cambio de norma → alineación de plantillas y guía de
adopción.** Las plantillas (`templates/skevi/usage-guide.md`,
`architecture-overview.md`) citan rutas y secciones de la norma
(`docs/ai-agent-guide/00-INDICE.md`, §3.5 del estándar, rutas de
ADRs). La convención de editar (AGENTS.md) exige verificar referencias
tras mover archivos, pero ningún gate ni paso de F3 cubre las
referencias **dentro de `templates/`**: una edición normativa puede
dejar la guía del adoptante apuntando a algo que ya no existe, sin
evidencia de que nadie lo miró.

- **Adopción** — estímulo: adoptante copia plantillas vigentes;
  respuesta esperada: copia con procedencia registrada (`source` +
  revisión, esquema T09/#28); medida: el adoptante identifica origen y
  fase sin preguntar (el fixture de T09 ya lo demostró); responsable:
  agente ejecutor de la adopción.
- **Cambio** — estímulo: edición normativa que toca rutas/secciones
  citadas por plantillas; respuesta esperada: barrido de referencias
  de `templates/` en el mismo cambio, con resultado en el reporte de
  la tarea; medida: referencias rotas en `templates/` tras el cambio
  (objetivo: 0); responsable: ejecutor del cambio normativo.
- **Fallo** — estímulo: defecto reportado sobre plantilla
  desalineada; respuesta esperada: triage en el issue y arreglo en el
  mismo ciclo o hallazgo registrado; medida: días entre reporte y
  decisión registrada; responsable: mantenedor decide, agente ejecuta.

## D2 — Mantenimiento según el caso

- **Dueño**: el humano propietario del repo acepta políticas y
  retiradas; el agente ejecutor propone, ejecuta y reporta. Sin
  orquestador designado (ADR-017 default: gate humano).
- **Canal de defectos**: los issues de este repo — canal único, con
  precedentes vivos (#25 consumido por PROP-005; #28 = PROP-006@#28).
- **Triage de seguridad**: el corpus no ejecuta código; el riesgo
  dominante es instrucción inyectada en contenido adoptado o
  recuperado — ya cubierto por la regla de datos no confiables
  (AGENTS.md; estándar §1; AN-KLA.md). Los hallazgos HIGH de una
  ronda adversarial paran el incremento (04 §5.3). No se añade
  mecanismo nuevo.
- **Compatibilidad**: el versionado de plantillas vive en
  PROP-006@#28 con las enmiendas de T09; hasta su adopción, un cambio
  de plantilla es un commit normal con revisión. Este piloto no lo
  duplica.
- **Retirada**: una plantilla se retira cuando la norma que sirve
  desaparece o cambia de forma que la guía engañe; la retirada es
  explícita, con decisión registrada — nunca silenciosa.

## 3. Comparación con la práctica existente (F3 y afines)

- Gates de estructura, tamaños y planes + suite + hook pre-push
  (ADR-001/006/014; T02-T04) — no se toca.
- Ronda adversarial con disparadores objetivos y contexto fresco
  (04 §5; ADR-008) — no se toca.
- Verificación de referencias al mover archivos (convención de
  edición, AGENTS.md) — se **extiende** a `templates/` con evidencia
  en el reporte.
- Canal de issues con ciclo PROP (#25 → PROP-005; #28 = PROP-006@#28)
  — se reutiliza; no se crea otro.
- Reportes en dos capas + checkpoint de sesión (ADR-016; 05 §6) — la
  medida del escenario Cambio viaja en el reporte.
- Cierre del programa con revisión fresca del conjunto (plan P5, T12)
  — el barrido final de enlaces ya vive allí; sin cadencia nueva.

Carencia observada y única extensión: la alineación de `templates/`
frente a cambios de norma (escenario Cambio). Es verificación en
tarea de edición — no gate nuevo, no script, no cadencia.

## Piloto (acotado)

Se ejecuta en el **próximo cambio normativo real** que toque rutas o
secciones citadas por `templates/` — no en artificial: si T11 o el
cierre no producen ese cambio, el piloto queda pendiente y se declara
tal. Atributos medidos: referencias rotas en `templates/` (objetivo
0), constancia del barrido en el reporte de dos capas, y canal issue
único ante fallo. Sin coste: grep + lectura; cero dependencias.

## Criterios de decisión aplicados

§8 del estándar: extender una convención existente con evidencia es
lo más simple y lo más reversible (dejar de registrar el barrido);
minimiza superficie (cero código nuevo) y no añade dependencias. Un
gate de enlaces de plantillas se consideraría sólo si el piloto
mide fallos repetidos — decisión para el cierre (T12), no ahora.

## Adopción

D1-D3 (caso/escenarios, mantenimiento, extensión única) quedan
aceptadas o rechazadas por el humano en conversación. Con la
aprobación, este documento queda como registro del piloto (cabecera
RESUELTA) y sus atributos se miden en el próximo cambio normativo que
califique; el resultado alimenta T11-T13.
