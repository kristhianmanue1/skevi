# ADR-043: continuación autónoma dentro de la TAREA

Estado: aceptado el 2026-10-28; implementado en `corpus/v6`. El Operador
aprobó B al precisar que push/merge se
proponen según el avance y se ejecutan por instrucción humana aplicable o
configuración futura válida. Esa precisión de autoridad se registra en
ADR-044; no concede una operación Git concreta.

Contexto: [SPEC-AGENTIC](../specs/SPEC-AGENTIC-2026-10-28.md) plantea que
Skevi ya permite resolver detalles internos y diagnosticar fallos, pero el
ciclo de trabajo autorizado queda disperso entre F0 y F3. No se ha medido
que la excepción de autoridad de ADR-018 cause las interrupciones. La
[propuesta](../history/PROP-012-continuacion-agentica-acotada.md) expone
tres opciones con costes distintos.

Decisión: explicitar en F0/F3 la investigación, descomposición,
implementación, diagnóstico, corrección y verificación autónomos **dentro**
de una TAREA vigente. Las preguntas que cambian diseño, objetivo, autoridad,
superficie o riesgo se escalan como antes. La regla no crea un cuarto eje de
clasificación ni da permiso a un skill, plugin, memoria o modelo.

Alternativas descartadas:

- A, dejar la guía dispersa: cero edición, pero mantiene consultas
  redundantes y no ofrece un ciclo observable para el piloto.
- C, delegar de inmediato push/merge sin gate: podría reducir esperas
  finales, pero no puede ejecutarse sin custodia y autorización verificables.
  ADR-044 admite una vía futura condicionada, no esta delegación inmediata.

Consecuencias: el agente agota el trabajo permitido antes de consultar, sin
convertir cada corrección en nueva solicitud; también debe justificar con
evidencia cuándo se detiene. El coste es más texto en la ruta de lectura y
un piloto necesario para medir beneficio real. F0 §5, F3 §3-§5/§7-§8 y el
estándar conservan sus gates. Este ADR no sustituye ADR-018; ADR-044 trata
la excepción local por separado. Un adoptante sin
memoria ni integración de proveedor sigue pudiendo aplicar la guía.

Procedencia y razón: decisión del Operador citada arriba, casos C1-C10 de
SPEC-AGENTIC y ronda documental
[2026-10-28](../reviews/2026-10-28-prop-012-spec-agentic.md). Se registra
la elección B conforme a `02` §3.1; el beneficio queda por comprobar en un
piloto y no se infiere de este ADR.
