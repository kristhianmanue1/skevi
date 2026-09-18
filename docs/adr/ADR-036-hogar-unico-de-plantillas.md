# ADR-036: Hogar único de plantillas copiables

Estado: aceptado; implementado en `templates/skevi/` (plantillas/v9),
`scripts/check_sizes.py` y `scripts/MANIFEST.json` (gate/v7, **breaking**),
`docs/MANIFEST.json` (corpus/v3), los tres ejemplos `*-installed.json` de
`templates/skevi/`, `skevi-gate.json`, `tests/test_check_sizes.py`, la fila de
ADR-010 en `docs/adr/00-INDICE.md`, la tabla de estructura de `README.md`, las
referencias de `docs/ai-agent-guide/03-cascaron-proyecto.md` y `docs/plans/`, y
la nota de resolución de `docs/proposals/PROP-010-destilacion-engineering.md`
§5. El cuerpo de ADR-010 **no** se toca: los ADR son inmutables (`02` §3.2;
la checklist de cierre vive en §3.3) y su cita conserva la ruta de su fecha.

Contexto: `templates/plan-de-implementacion.md` y
`templates/registro-contexto.md` vivían en la raíz de `templates/`, fuera de
todo manifiesto. `templates/skevi/MANIFEST.json` cubre sólo su propio
directorio y `docs/MANIFEST.json` cubre estándar y guía, así que
`check_templates.py` no podía avisar a un adoptante de que copió una versión
antigua de esas dos. El README lo declaraba como deuda —«Sin versionar
(issue #48)»— y el hueco lo levantó la deliberación de PROP-010, que lo
registró aparte por decisión del Operador (F1).

El riesgo no era simétrico. `plan-de-implementacion.md` enseña exactamente la
estructura que `check_plans.py` exige —Consumes/Produce/Steps con criterio de
verificación por paso—, de modo que un adoptante con copia antigua escribe
planes que su propio gate rechaza, sin forma de diagnosticar por qué.
`registro-contexto.md` no tiene gate acoplado: su drift es de contenido, no de
verificación.

Decisión: **un solo hogar para las plantillas copiables**, `templates/skevi/`,
cubierto por el manifiesto que ya existe. No se crea una cuarta familia de
manifiesto ni un manifiesto nuevo en `templates/`.

Consecuencias mecánicas, todas verificadas antes de aceptar:

- Las dos plantillas entran en `templates/skevi/MANIFEST.json`, que valida
  **listado exacto del directorio más digests**: un archivo añadido ahí no
  puede volver a quedar fuera del manifiesto por olvido. Ese es el invariante
  que hace preferible este hogar a una lista mantenida a mano.
- `check_sizes.py` cablea las dos rutas en su conjunto `REQUIRED`, que rige
  para el adoptante que copia el script sin `skevi-gate.json`. Actualizarlas
  es cambio de código: sube `gate/v6` → `gate/v7`, y el salto se declara
  **breaking**: se verificó que un adoptante con las plantillas en la ruta
  antigua pasa de `OK` a «falta archivo requerido» sólo con re-copiar el
  script. La migración —mover los dos archivos o declarar `required` propio—
  va escrita en el `changes` del manifiesto, no sólo en este ADR.
- Nada verificaba que las rutas de `REQUIRED` existieran: la suite construye
  su repositorio de prueba a partir de ese mismo conjunto. Se añaden dos
  casos en `tests/test_check_sizes.py` que lo atan al repositorio real y a
  `skevi-gate.json`, y se comprobó que fallan en rojo con una ruta inventada.
- `docs/ai-agent-guide/03-cascaron-proyecto.md` cita la ruta y está declarado
  en el manifiesto de corpus: cambiarlo obliga a `corpus/v2` → `corpus/v3`.
- Dos planes cerrados de `docs/plans/` referencian la ruta antigua y la regla
  E5 de `check_plans` exige que exista toda ruta backtickada dentro de un
  bloque TAREA en fence que lleve separador `/`, extensión de su lista
  conocida y ningún `://`; además indulta la línea entera cuando contiene una
  palabra que empieza por «crea». Un nombre de archivo suelto, sin
  directorio, no se comprueba.
  Se verificó que en estos dos casos sí muerde: sin actualizarlos,
  `check_plans` da `BLOQ`. Se actualizan:
  `docs/plans/` no está declarado inmutable —a diferencia de `docs/adr/`, que
  sólo crece, y de `docs/reviews/`, congelado al cerrar— y el gate existe
  precisamente para que esas referencias sigan siendo ciertas.

Alternativas descartadas:

- **Cuarto manifiesto en `templates/`.** Exige una cuarta familia de esquema
  en `check_templates.py` (`MANIFEST_SCHEMAS`, `INSTALL_SCHEMAS` y
  `SCHEMA_NAMESPACE`, que falla en cerrado ante un esquema sin namespace) y,
  además, cablearlo en `check_sizes.py`, que valida los tres manifiestos por
  ruta fija: sin eso, el manifiesto nuevo no se verificaría nunca —el mismo
  defecto que este ADR cierra—. Dos scripts, dos suites y un espacio de
  nombres nuevo para dos archivos.
- **Declararlas en `docs/MANIFEST.json` con claves `../templates/…`.**
  Funciona hoy sin tocar código: se verificó que el digest se comprueba en
  cada ejecución y que un cambio sin bump emite `digest desactualizado`. Se
  descarta por dos razones. La primera es de contrato: ADR-032 declara ese
  manifiesto como «el canon declarado: estándar + guía», con rutas que
  «pueden anidar subdirectorios» —descender, no ascender—, así que la vía
  exigiría enmendar ADR-032. La segunda es de audiencia: quien copia
  plantillas rastrea `plantillas/vN`, y bajo esa vía recibiría avisos de
  recopia de dos formatos cada vez que cambiara el estándar. Señal ruidosa es
  señal que se ignora.
- **Aceptar el riesgo por escrito.** Es la opción que el propio issue #48
  admitía. Se descarta por el acoplamiento de `plan-de-implementacion.md` con
  `check_plans`: el drift silencioso ahí produce fallos no diagnosticables en
  el repositorio del adoptante.

Procedencia: [issue #48](https://github.com/kristhianmanue1/skevi/issues/48),
levantado como hallazgo lateral (F1) de
`docs/proposals/PROP-010-destilacion-engineering.md` §5. Precedentes del
mecanismo: [ADR-020](ADR-020-adopcion-versionado-plantillas.md),
[ADR-028](ADR-028-manifest-de-scripts.md) y
[ADR-032](ADR-032-manifiesto-de-corpus.md).
