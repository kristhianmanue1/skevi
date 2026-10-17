# ADR-041: El presupuesto de lectura cubre la entrada del ejecutor

Estado: aceptado; implementado en `scripts/check_sizes.py` (gate/v11).

Contexto: la coherencia `root_markdown` ↔ `reading_path` (gate/v10, #63)
gobierna sólo los Markdown de raíz **extra** que el adoptante declara. El
conjunto intrínseco — `AGENTS.md`, `CLAUDE.md`, `README.md` — quedaba
exento: un proyecto con `CLAUDE.md` como entrada del agente y presupuesto
activo que no lo declara mide una ruta incompleta, la misma falsa comodidad
de #63, sin señal. La ronda del gate/v10 lo señaló como MED y la decisión
quedó escalada al Operador; la instrucción del 2026-10-17 («adelante con
tus recomendaciones») aceptó la recomendación: extender, agrupada con la
familia adr/v1 en un único salto breaking.

Decisión: con `reading_path` activo, `AGENTS.md` y `CLAUDE.md` —sólo si
existen como archivo en la raíz— deben figurar en `reading_path.files`.
`README.md` queda fuera por deliberación: es cara humana, no entrada
obligatoria del ejecutor. La exigencia es de existencia condicional: un
proyecto sin `CLAUDE.md` no debe declararlo.

Consecuencias: el presupuesto declarado vuelve a coincidir con la ruta que
cualquier ejecutor lee de verdad, cualquiera que sea su archivo de entrada;
los fixtures de prueba de `reading_path` que modelan repos con `AGENTS.md`
pasan a declararlo, como los repos reales. Salto breaking por la nueva
condición de fallo para adoptantes con presupuesto activo y entrada sin
presupuestar; la migración es declarar el archivo, no re-copiar nada más
que el gate.

Procedencia: hallazgo MED de la ronda
[2026-10-17-gate-v10-coherencia.md](../reviews/2026-10-17-gate-v10-coherencia.md);
instrucción directa del Operador (2026-10-17);
[ADR-021](ADR-021-presupuesto-de-ruta-de-lectura.md) y
[ADR-038](ADR-038-presupuesto-de-lectura-con-memoria-activa.md) por la
materia.
