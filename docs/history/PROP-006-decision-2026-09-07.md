# PROP-006 — Reportes de agente en dos capas con bloque de trazabilidad

> **Estado:** ADOPTADA — D1-D2 aprobadas por el humano (2026-09-07, en
> conversación). Piloto F1-F4 corrido sobre los folios
> `SKV-2026-09-07-01`/`-02` de esa misma sesión; D3 ejecutada vía
> ADR-016 y el PR de adopción (00-INDICE, 04 §5.2, estándar §6).
> Registro histórico: evidencia de decisión, no norma vigente.
> **Origen:** instrucción directa del humano (2026-09-07) y análisis en
> conversación. Corolario de ADR-015: aplica a los reportes la misma
> polaridad de idioma que la convención aplica al proyecto.

## Contexto

Los formatos de reporte vigentes — el bloque de fase de `00-INDICE.md`
y el reporte adversarial de `04` §5.2 — son de una sola capa: mezclan
datos para máquina y prosa para humano en el mismo texto. Quien
supervisa al agente debe leer la pared técnica completa; quien parsea
(agentes, orquestadores) debe extraer datos desde prosa. La hipótesis
del humano añade un bloque de trazabilidad (identificador, fecha, hora,
hash, firma del modelo) y separa la audiencia en dos capas. El humano
ya opera fuera de este repo un cierre humanizado por respuesta
(instrucción directa, no verificable desde el repo): esta propuesta lo
generaliza y lo norma.

## D1 — Dos capas con autoridad explícita

**Propuesta:** todo reporte de tarea material lleva dos capas.

- **Capa técnica** (inglés, autoritativa): estado, gate, evidencia en
  líneas `comando → resultado → pass|fail|inconclusive`, pendientes.
  Es la que consumen parsers y rondas adversariales.
- **Capa humana** (idioma del proyecto, redacción natural, jerga
  mínima): proyección legible de la técnica. No introduce afirmaciones
  ausentes en la capa técnica; ante contradicción, gana la técnica —
  principio análogo al de §3.5 (cuyo alcance cerrado no se extiende
  aquí): el contenido sustantivo vive en un solo lugar.

**Alternativa descartada:** una sola capa bilingüe — más barata, pero
obliga a cada público a leer el idioma ajeno y a parsear prosa.

## D2 — Bloque de trazabilidad graduado

**Propuesta:** esquema cerrado, claves en inglés, presente sólo en
tarea material (disparadores de `04` §5.3) o en cierre de fase:

```text
id            = <folio monótono de la tarea dentro del proyecto>
date          = <AAAA-MM-DD>
time_utc      = <HH:MM:SSZ>
head_sha      = <sha del HEAD al cerrar la tarea>
report_sha256 = <sha256 del contenido canónico de la capa técnica>
model         = <nombre y versión del modelo, autodeclarado>
session       = <identificador de sesión, si existe>
```

La entrada `model` es procedencia declarada, nunca prueba: un modelo no
firma criptográficamente y el principio 7 del estándar prohíbe que un
campo autodeclarado eleve confianza. Tarea trivial queda exenta (mínimo
necesario): capa humana sola basta. El folio necesita mecanismo: el
piloto fija una secuencia en archivo con escritura atómica (§2.2) o su
equivalente derivado de Git, de modo que dos sesiones concurrentes no
puedan asignar el mismo folio. La forma canónica de la capa técnica
(normalización de líneas, codificación) la fija el propio piloto y
queda documentada como evidencia; la adopción la ratifica o corrige.
Sin forma canónica, F3 no es testeable.

**Alternativas descartadas:** metadata obligatoria en cada mensaje
(ceremonia sin riesgo real); no llevar bloque (el id, la fecha y el
hash que pide el humano quedan dispersos en la prosa, sin esquema).

## Criterios de aceptación (falsables)

La propuesta se adopta sólo si un piloto real — una sesión material de
skevi reportada así de punta a punta — cumple:

- F1: un parser determinista extrae estado, gate y evidencia leyendo
  sólo la capa técnica.
- F2: un humano que lee sólo la capa humana responde, sin ver la
  técnica, tres preguntas cerradas — qué se hizo, qué gate quedó y
  qué falta; si falla cualquiera o afirma algo ausente de la técnica,
  F2 se refuta.
- F3: `report_sha256` es reproducible sobre la capa técnica canónica y
  el folio no colisiona dentro del proyecto.
- F4: cero desincronización — toda afirmación de la capa humana existe
  en la técnica.

Si el piloto refuta alguno, la propuesta muere o se corrige aquí antes
de tocar norma.

## D3 — Aterrizaje normativo

Si se aprueba: editar `00-INDICE.md` (formato de fase: capa humana y
bloque), `04` §5.2 (reporte adversarial: ídem) y el estándar §6 (regla
general de reporte de ejecutores); producir el ADR de la decisión y
mover esta PROP a `docs/history/` en el mismo cambio, siguiendo el
patrón PROP-004 (propuesta primero, adopción después).

## Criterios de decisión aplicados

§8 del estándar, en orden: la capa técnica única es lo más simple de
entender para una máquina y lo más fácil de revertir (añadir la capa
humana después es barato; quitarse el hábito de parsear prosa, no);
el bloque graduado minimiza la superficie de mantenimiento y no añade
dependencias. «Firma del modelo» se degrada a `model` autodeclarado:
prometer firma criptográfica sería prometer lo imposible.

## Adopción

D1-D2 quedan aceptadas o rechazadas por el humano en conversación; con
la aprobación, un PR ejecuta D3 con el piloto documentado. Mientras
tanto, este documento no obliga a nada.
