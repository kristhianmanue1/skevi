# ADR-052: presupuesto de lectura 1640 — la adopción de 049 y 050 lo consume

Estado: aceptado (consecuencia declarada de la confirmación de ADR-049
y ADR-050, 2026-11-08: la selección «Confirmo los tres (049, 050 y
051)» citaba expresamente que la adopción «exige ADR de presupuesto de
lectura en el mismo cambio»; política p3 de ADR-038, registrada antes
del primer commit fuente).

## Contexto

ADR-042 fijó el presupuesto de la ruta de lectura en 1620/1620 con
holgura cero y como trinquete deliberado (ADR-038 p3): todo crecimiento
exige su propio ADR re-decidiendo el presupuesto en el mismo cambio.
La adopción de ADR-049 añade diez líneas a `04` §2 y la de ADR-050,
otras diez a §5.2 — nueve de norma más la línea en blanco de
separación —: `04` pasa de 286 a 306 líneas y la suma de la ruta, de
1620 a 1640.

## Decisión

El presupuesto de la ruta de lectura pasa de 1620 a **1640** líneas:
la suma exacta de la espina (109 de `AGENTS.md`, 114 de `00-INDICE.md`,
501 del estándar, 132 de `05`, 478 de `AN-KLA.md`) más el peor caso de
los complementos de fase (`04`, 306). Se mantiene la política del
trinquete: número exacto, holgura cero, y cualquier crecimiento futuro
exige su propio ADR en el mismo cambio.

`04` no entra por sí misma en la espina: es el peor caso de
`worst_case_of`, igual que en ADR-042.

## Consecuencias

- La ruta de lectura del ejecutor crece veinte líneas exactas — las
  dos reglas adoptadas y nada más.
- El valor vigente lo emite `check_sizes` en su salida (ADR-025 p4);
  `skevi-gate.json` (`reading_path.limit`) y el mapa de orientación se
  sincronizan en el mismo commit.

Procedencia y razón: política p3 de
[ADR-038](ADR-038-presupuesto-de-lectura-con-memoria-activa.md), con el
precedente de fijación exacta de
[ADR-042](ADR-042-presupuesto-1620-generalizacion-de-05.md); disparo:
la adopción confirmada de ADR-049 y ADR-050.
