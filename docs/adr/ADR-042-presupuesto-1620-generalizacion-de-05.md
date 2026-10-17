# ADR-042: Presupuesto de lectura 1620 — la generalización de 05 lo agotó

Estado: aceptado; implementado en `skevi-gate.json` clave `reading_path`.

Contexto: ADR-038 fijó el límite en 1600 (1592 observados el 2026-10-17)
con holgura deliberada de 8 y una política: el crecimiento que agote la
holgura exige re-decidir el número con su propio ADR, en el mismo cambio,
nunca en silencio. Ese caso llegó el mismo día: la aceptación de PROP-011
generaliza `05` (frontera agnóstica, escritura gobernada como condición,
mapeo neutro) y el documento pasa de 116 a 132 líneas; la ruta declara
**1608/1600** y el gate BLOQuea — el trinquete funcionó como fue diseñado.

Decisión: el límite sube a **1620**. Cifras históricas, fechadas
(ADR-025 p4): 1608 observados el 2026-10-17 tras la generalización de
`05`; holgura de 12, el mismo margen del precedente del adoptante
lalia-akuo (#63: 1388/1400). La política de ADR-038 p3 queda reafirmada
sin cambios: el próximo crecimiento que agote la holgura —el driver
sigue siendo la plantilla de AN-KLA, hoy en 478— exige su propio ADR.

Alternativas descartadas: recortar la generalización para caber en 1600
(hacer decir menos a la norma por el techo, no por la decisión); holgura
amplia tipo 1700 (contador, no trinquete).

Procedencia: política de [ADR-038](ADR-038-presupuesto-de-lectura-con-memoria-activa.md)
p3; aceptación de
[PROP-011](../history/PROP-011-frontera-memoria-agnostica.md);
[ADR-025](ADR-025-trinquete-no-techo-derivado.md) p4 por las cifras.
