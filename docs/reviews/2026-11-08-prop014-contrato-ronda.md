# Ronda adversarial — PROP-014: contrato de coordinación v0.2.1-candidata

Objeto: `docs/proposals/PROP-014-contrato-coordinacion-multi-proyecto.md`
— encabezado de propuesta en español y «Multi-Project Agent
Coordination Contract» v0.2.1-candidata — sobre `main`
`e0f8b65c2f250ee64f7d4c77511c674be82789e8` con cambios sin commit.
Original v0.2.0 preservado fuera del repo para el difuso.

Revisó una sesión fresca del mismo proveedor (GLM), sin contexto de
autoría, con mandato de falsificación (AR1 del propio contrato) y de
sólo lectura. Verificó: fidelidad del delta (diff byte a byte contra el
original), ataque a las dos enmiendas, contradicciones internas,
divergencias diagrama/texto, fences con parser real y formato del
anfitrión.

Veredicto: **fix-and-retry** — y el reintento se ejecutó: los hallazgos
del texto 0.2.1 quedaron corregidos y reverificados antes de este
registro; los heredados de v0.2.0 se derivaron al Operador (pila «del
Operador», ADR-050) sin editar su texto.

## Hallazgos y disposición

1. [HIGH] H1 — La Rule A4 original era puerta de una sola dirección:
   prohibía que el contrato relajara el canon local, pero no que un
   canon local más laxo desplazara a A1–A3 dentro del proyecto; y nadie
   clasificaba qué es «local» vs «cross-project». Cerrado: A4 ahora
   fija A1–A3 y §7.1 como piso mínimo («stricter» se computa contra
   este contrato como línea base), nadie autoriza dentro de un proyecto
   lo que A1–A3 reserva, y la clasificación la registra el Verifier,
   disputable por §6.
2. [HIGH] H2 — Divergencia diagrama/texto en §4, heredada de v0.2.0:
   el path del diagrama WO `blocked → adversarial_review → completed`
   se salta `verification`; las colaboraciones carecen de
   `verifying → blocked`. **Del Operador**: no se parchea aquí (rompería
   la fidelidad del texto entregado); queda como feedback 0.2.2
   (pregunta abierta 5 de la propuesta).
3. [MED] M1 — La cláusula AR5 carecía de árbitro para «causa incierta»
   vs «causada por el ejecutor», y «executor» no es un rol definido.
   Cerrado: «executor» definido (el worker/runtime del WO bajo
   revisión), atribución de causa como campo registrado del check
   (`executor-caused | external-uncertain`, con base) clasificado por
   el Verifier, disputable por §6.
4. [MED] M2 — Cánones que discrepan sobre la misma evidencia: A4 sólo
   resolvía conflictos «dentro» de un proyecto. Cerrado: los checks
   compartidos de un IA/CC pasan sólo si satisfacen todos los cánones
   aplicables; el conflicto canon-canon escala a §6 (Humano), nunca al
   Coordinator.
5. [MED] M3 — §11 congelada en 0.2.0: las enmiendas nuevas viajaban sin
   auto-revisión. Cerrado: fila SR-08 (desplazamiento por canon laxo →
   regla de piso) y nota en limitaciones residuales de la revisión
   externa del 2026-11-08 con sus hallazgos heredados abiertos.
6. [MED] M4 — El encabezado atribuía al manifiesto una declaración de
   plano inter-proyectos que no existe, y el contrato roza el plano
   cedido a epistates («contrato de tarea ejecutable ni máquina de
   estados de auditoría»). Cerrado: redacción anclada en lo real (gates
   per-repo) y solapamiento con epistates anotado como deliberación.
7. [MED] M5 — Nadie designa al Cross-Project Coordinator (bootstrap
   circular) y el registro §8 no tiene hogar. **Del Operador**:
   pregunta abierta 4 (¿0.2.2 o condición de adopción en §10?); el
   hogar ya era pregunta abierta 1.
8. [LOW] L1 — Título del encabezado a 90 columnas. Cerrado: acortado.
9. [LOW] L2/L3 — Heredados de v0.2.0: `verifying → blocked` ausente en
   colaboraciones; el diagrama de secuencia se lee como escritura del
   Coordinator en los proyectos. **Del Operador**: feedback 0.2.2
   (pregunta abierta 5).

La fidelidad del delta verificó PASS exacto antes de las correcciones
(sólo las cuatro diferencias declaradas) y los seis fences mermaid
salieron VALID con parser real (mermaid v11 + jsdom, directorio
temporal fuera del repo).

## Capa técnica

```text
id = SKV-PROP014-CONTRATO-RONDA-20261108-01
date = 2026-11-08
time_utc = 23:16:20Z
head_sha = e0f8b65c2f250ee64f7d4c77511c674be82789e8
model = GLM-5.3 zai-coding-plan; revisor fresco (self-declared; not proof)
STATE = OK
GATE = ronda adversarial de solo lectura en sesion fresca sobre PROP-014
  (contrato v0.2.1-candidata con las dos enmiendas ordenadas); 2 HIGH,
  4 MED y 3 LOW; los del texto 0.2.1 corregidos y reverificados; los
  heredados de v0.2.0 derivados al Operador (ADR-050) sin editar su
  texto.
EVIDENCE
- diff byte a byte propuesta vs original v0.2.0 -> solo las 4 diferencias declaradas -> pass
- parser mermaid v11 sobre los 6 fences -> 6/6 VALID -> pass
- wc -l de la propuesta -> 415/800 antes de correcciones; limite respetado -> pass
- check_sizes + check_plans + check_reports -> OK; 1640/1640; 13 planes; 50 reportes -> pass
- contraejemplo H1 reproducido en texto -> canon laxo desplazaba A3; piso minimo ahora lo impide -> pass
- clasificacion de disposiciones -> 6 cerrados en texto 0.2.1; 3 derivados al Operador (H2, M5, L2/L3) -> pass
PENDING = aprobacion del contrato por el Operador (checklist §10);
  preguntas abiertas 1-5 de la propuesta (hogar del estado, piloto,
  designacion del Coordinator, feedback 0.2.2); entrega Git de esta
  propuesta por lote.
DECISION = fix-and-retry
OPERATIONS = ronda de solo lectura via subagente fresco; correcciones
  sobre el texto 0.2.1 de la propuesta; validacion mermaid con parser
  real en directorio temporal fuera del repo; sin efectos Git.
AUTHORITY = Operador 2026-11-08, en conversacion: «aplica las dos
  enmiendas luego ronda adversarial fresca y crea un *.md de propuesta
  del contrato»; las correcciones adicionales son fix-and-retry sobre
  el texto nuevo de la propia propuesta, no edicion del texto v0.2.0
  del Operador.
RISK = revisor del mismo proveedor y familia que el autor; el contrato
  no ha corrido piloto alguno: sus reglas son diseno no probado (§11
  del propio contrato).
report_sha256 = 8647d20d7dae2f951123af29d32eb425e90a2ba6d8393b0d21fd3a4dab3524e1
```
