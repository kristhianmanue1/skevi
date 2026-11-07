# AUDIT-template-provenance — Procedencia de plantillas y migración reversible

> **Estado:** RESUELTA — D1-D3 aceptadas por el humano (2026-09-07, en
> conversación) como enmiendas registradas a PROP-006@#28; aterrizan
> cuando el issue se adopte. Piloto formal del paso 4: PoC re-ejecutado
> tras la decisión (ver §2).
> **Origen:** plan AUDIT-2026-09-07, tarea T09 (REQ-AUD-06). Consume la
> decisión O-A de T07: la propuesta de versionado se cita
> `PROP-006@#28` ([issue 28](https://github.com/kristhianmanue1/skevi/issues/28)),
> distinta de la PROP-006 local (reportes en dos capas, ADR-016).
> PoC ejecutado el 2026-09-07 sobre fixtures en directorio temporal:
> sin red, sin mutar consumidores.

## 1. Reconciliación con PROP-006@#28: una sola propuesta viva

PROP-006@#28 es y sigue siendo la **única propuesta viva de
versionado** de plantillas: D1 manifiesto del lado fuente
(`skevi/template-manifest/v1`), D2 registro de instalación del lado
consumidor (`skevi/template-install/v1` con `source` y `customized`),
D3 anti-drift por versión declarada (los bytes de una copia rellenada
difieren por diseño; el señal válido es la versión). Este documento
no compite: define la **capa de procedencia y migración** como
enmiendas concretas a D1/D3 de #28, para que aterricen juntas cuando
#28 se adopte.

## D1 — Enmienda al manifiesto: historia por salto con bandera breaking

El manifiesto de #28 (D1) añade `history`: un registro por salto de
versión con `from`, `to`, `breaking` (bool) y `changes` (archivo →
resumen). Sin esto, los tres casos de abajo no son decidibles en
local: el consumidor no puede inferir del delta de bytes qué rompe y
qué no — la compatibilidad la declara el lado fuente, que es quien
editó las plantillas. Bandera conservadora: un salto marcado breaking
clasifica como incompatible toda copia obsoleta que no haya declarado
el archivo como `customized`.

## D2 — Los tres casos (detección local, acción)

- **A — copia antigua compatible**: versión instalada ≠ vigente y
  toda la cadena de saltos hasta la vigente es no-breaking. Acción:
  aviso; re-copiar es opcional.
- **B — copia antigua incompatible**: versión instalada ≠ vigente y
  la cadena contiene al menos un salto breaking. Acción: la que #28
  D3.2 fije para el drift (fallo o aviso fuerte — decisión abierta
  que sigue en #28, no se duplica aquí).
- **C — personalizada**: el archivo está en `customized[]` del
  registro de instalación. Acción: listado como re-copia bajo
  responsabilidad del consumidor; anula A/B **por archivo declarado**,
  no por el resto.
- **Versión desconocida** (no aparece en `history`): se trata como B
  — fail-closed, consistente con ADR-007.

## D3 — Migración reversible, sin comparar relleno contra plantilla

- La comparación de migración es **versión contra versión en el lado
  fuente** (la `history` del manifiesto), nunca bytes de copia
  rellenada contra plantilla: el relleno es la finalidad de la
  plantilla, no drift (misma corrección de la autorevisión de #28).
- `installed.json` registra qué se instaló, de dónde (`source`) y con
  qué digests: con el delta por salto, el consumidor puede re-aplicar
  su relleno sobre la versión nueva sin adivinar.
- Skevi no muta consumidores (frontera del manifest): la migración la
  ejecuta el consumidor, manual, una vez, gobernada por el flujo
  normal. La reversibilidad es informativa (history + digests), no
  automática.

## 2. PoC con fixture local (evidencia)

Fixture en directorio temporal: dos manifiestos escenario (cadena
no-breaking `v1→v1.1`; cadena breaking `v1→v2`) y tres consumidores
con `installed.json` (A: v1 sin customizar; B: v1 sin customizar;
C: v1 con `usage-guide.md` en `customized`). Clasificador stdlib-only,
sólo lectura:

- A contra manifiesto no-breaking → `A-compatible` (delta aditivo).
- B contra manifiesto breaking → `B-incompatible` (reestructura).
- C contra manifiesto no-breaking → `A-compatible` + `C-personalizada`
  (anula por archivo declarado).
- Sin red; los tres `usage-guide.md` de los consumidores quedaron con
  sus bytes intactos tras la ejecución.

Observación de diseño que el PoC evidenció: con un salto breaking en
la cadena, **todo** consumidor obsoleto no customizado clasifica B —
el caso A sólo existe mientras la cadena no tenga saltos breaking.
Es consecuencia querida de la bandera conservadora, no un defecto.

## Criterios de decisión aplicados

§8 del estándar: una bandera por salto y una tabla de tres casos son
lo más simple de mantener; nada cambia en #28 hasta que su adopción
aterrice (las enmiendas viajan con ella); no añade dependencias ni
red; revertir es ignorar este documento.

## Adopción

D1-D3 quedan aceptadas o rechazadas por el humano en conversación.
Con la aprobación: este documento queda como registro de las
enmiendas (cabecera RESUELTA) y el piloto formal — re-ejecución del
PoC sobre los fixtures — se registra como evidencia del paso 4 de
T09. Proponer las enmiendas en el issue #28 (comentario o edición)
es operación externa separada: requiere autorización específica y no
se ejecuta por omisión.
