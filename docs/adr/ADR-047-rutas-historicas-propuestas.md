# ADR-047: rutas históricas en referencias hacia propuestas

Estado: aceptado (confirmación literal del Operador, 2026-11-07:
«Confirmo ADR-047», con el texto de la regla delante).

## Contexto

ADR-040 selló la familia `adr/v1` el 2026-10-17: los ADRs aceptados son
inmutables y su listado y digests viven en `docs/adr/MANIFEST.json`. Pero
el plan de PROP-010 §8 (2026-09-18) planeaba, en su tarea T09, actualizar
las referencias de ruta que apuntan a `docs/proposals/` desde `docs/adr/`
— cuando los ADRs aún eran editables. ADR-002 ordena que las
deliberaciones cerradas se trasladen a `docs/history/`. Hoy conviven 13
referencias con ruta hacia material de propuesta en 5 archivos sellados
(`00-INDICE.md`, ADR-020, ADR-035, ADR-036, ADR-037; más ADR-003
definiendo el directorio y ADR-027 citando ya una ruta histórica
inexistente). Ejecutar el traslado literal rompe los enlaces relativos
reales que exige `AGENTS.md`; editar los ADRs rompe su inmutabilidad y el
sello criptográfico. El deadlock está documentado en
`docs/plans/2026-11-06-hoja-de-ruta-verificada.md` y su ronda.

## Decisión

Las referencias de los ADRs sellados conservan la ruta de la fecha de su
redacción — la misma doctrina que ADR-036 aplicó al mover la plantilla de
ADR-010: el cuerpo sellado no se edita y su cita envejece como
procedencia histórica; la ruta vigente vive en el índice
(`docs/adr/00-INDICE.md`), que sí se actualiza, con su bump de manifiesto.

En consecuencia:

- trasladar una deliberación cerrada de `docs/proposals/` a
  `docs/history/` no exige editar ningún ADR sellado;
- los enlaces vivos hacia material trasladado viven sólo en el índice;
- `AGENTS.md` (rutas relativas reales) sigue rigiendo íntegro los
  documentos editables, incluido el propio índice;
- una ruta histórica dentro de un cuerpo sellado no es un defecto: es la
  fecha de su redacción (precedente: ADR-027 ya convive con una).

## Consecuencias

- PROP-010 §8 (T01–T09) queda ejecutable sin romper sellos.
- El índice carga la vigencia de los enlaces y su actualización viaja con
  el bump `adr/vN` que el traslado provoque.
- Un ADR nuevo que necesite apuntar al hogar vigente de un material lo
  hace desde el índice, nunca reescribiendo ADRs previos.
- Coste: quien lea un ADR sellado debe pasar por el índice para localizar
  el hogar actual de lo que cita.

## Procedencia

Decisión del Operador del 2026-11-07 (opción A del deadlock, presentada
con el texto de la regla; registro
`docs/reviews/2026-11-07-decisiones-operador.md`). Rondas: HV de
`docs/reviews/2026-11-06-plan-hv-ronda.md` y análisis previo verificado
contra `74a4714`.
