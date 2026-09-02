# PROP-005 — Salida de Alpha y cierre formal del issue #25

> **Estado:** en deliberación — no normativo hasta su adopción.
> **Origen:** piloto infosalud (`docs/history/piloto-infosalud.md`),
> issue #25 (cerrado vía PR #26) y verificación independiente del
> registro. Este documento resuelve lo que el cierre del #25 dejó sin
> entregar y lo que el piloto habilita.

## Contexto

El README §Estado fija el criterio de salida de Alpha: «Sube a versión
estable cuando exista un piloto F0→F3 completo con evidencia». El
2026-09-01 ese piloto corrió (infosalud) y su evidencia está verificada
en el registro citado. En paralelo, el #25 se cerró con 2 de 5 puntos
sin entrega ni decisión documentada en contra. Esta propuesta resuelve
ambas cosas — más una fricción menor detectada en el `05` — en una sola
deliberación, porque comparten las mismas fuentes.

## D1 — Promoción Alpha → estable

**Propuesta:** ejecutar la promoción con estos cambios concretos.

1. `README.md` §Estado: sustituir «ninguna fase F0→F3 corrió todavía de
   punta a punta» por la referencia al registro del piloto; conservar la
   advertencia de que el gate sólo corre localmente (sigue siendo
   cierta).
2. `project-manifest.yaml`: retirar de `pospuesto` la primera entrada
   (piloto F0→F3) y dejar constancia de su ejecución; añadir a `ofrece`
   que la guía F0→F3 tiene un ciclo completo validado sobre proyecto
   real.
3. La cadena de custodia queda: registro en `history/` (evidencia) →
   decisión aquí → cambio de autodescripción en PR propio.

**Alternativa:** no promover todavía y fijar qué falta. Si se elige,
debe quedar escrito qué requisito adicional se exige — el criterio
actual ya está cumplido y dejarlo en Alpha sin criterio nuevo es
decidir por omisión (§8 del estándar).

**Recomendación:** promover. El criterio fue escrito antes del piloto,
no después: mover la meta ahora sería lo que el estándar llama revisar
lo estable cada vez que se mueve lo volátil.

## D2 — Punto 4 del #25: checkpoint de memoria en el checklist §7

El punto pedía añadir al checklist del estándar «la escritura de
checkpoint/registro en memoria como evidencia complementaria».

**Opción A — añadir la línea al §7.** Coste: el checklist pasa a
presuponer una dependencia opcional (`project-manifest.yaml`: «Skevi
funciona sin ninguna, y así debe seguir»); el §8.4 del propio estándar
penaliza añadir dependencias.

**Opción B — no añadir; el `05` §3-4 ya lo cubre como recomendación
vinculante sólo para quien adopte memoria.** El estándar §7 queda
agnóstico de herramienta. La «evidencia complementaria» ya tiene hogar
normativo: la frontera del `05` §2 (la memoria jamás cierra un gate).

**Recomendación:** B. Si algún adoptante quiere la línea, la añade a su
copia del checklist por escrito — igual que fija sus límites de tamaño.

## D3 — Punto 5 del #25: política CI local-only en la capa normativa

El punto pedía declarar la política «como parte del método». Ya está
declarada donde corresponde:

- `docs/adr/ADR-001-gate-local-sin-ci.md` — la decisión estructural,
  con su condición de revisión explícita («no se agrega un workflow de
  Actions en silencio»).
- `README.md` §Verificación — la política operativa.

El estándar es deliberadamente agnóstico de hospedaje y presupuesto: la
política de CI es decisión por proyecto, no norma transversal.

**Recomendación:** dar el punto por servido con artefactos existentes
(ADR-001 + README); no se edita el estándar. Queda registrado aquí como
decisión, para que el #25 no quede con puntos abiertos implícitos.

## D4 — Referencia externa en `05-memoria-del-agente.md` §4

El §4 manda «revisar el wrapper de consumo real
(`infosalud/scripts/mem`) como referencia» — una ruta a un repo ajeno
dentro de un documento de reglas obligatorias-si-se-adopta. Si el repo
desaparece o muta, la referencia se pudre.

**Propuesta:** sustituir la frase por la descripción del patrón en el
propio documento — «empaquetar el protocolo en un wrapper del proyecto
(plan-write/commit-write-plan + guardias de fences + hook pre-commit),
instalable sin red» — y degradar el enlace de infosalud a nota de
procedencia al pie («referencia de consumo real: issue #25»). El
registro del piloto ya documenta el patrón con sus commits.

## Criterios de decisión aplicados

§8 del estándar, en orden: la opción más simple de entender (D2-B, D3),
la más fácil de revertir (D1 promover es reversible con PR; no promover
sin criterio nuevo no lo es), la de menor superficie de mantenimiento
(D4: cero enlaces vivos a repos ajenos en la capa normativa-adjacente)
y la que no añade dependencias (D2-B).

## Adopción

Si se aprueba: un PR con los cambios de D1 (README + manifest), la
edición de D4 y el cierre formal de esta PROP en `docs/history/`
(siguiendo el patrón PROP-004: propuesta primero, adopción después).
El registro del piloto (`piloto-infosalud.md`) entra con el mismo PR o
en uno previo — es evidencia, no norma, y no depende de esta decisión.
