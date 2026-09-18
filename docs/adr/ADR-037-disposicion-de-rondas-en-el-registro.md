# ADR-037: La disposición de cada ronda vive en su registro, no en la propuesta

Estado: aceptado; implementado en `docs/ai-agent-guide/02-specs-adr-contratos.md`
§3.3 (corpus/v4).

Contexto: ADR-016 fijó el reporte de dos capas y PROP-010 §7 B decidió, con
firma del Operador el 2026-09-18 (folio `SKV-ACC-PROP010-20260918-01`), que el
informe textual de cada ronda viva en `docs/reviews/` **y que la disposición
de sus hallazgos quede en la propuesta**. Este ADR **sustituye esa segunda
mitad**: la disposición se va con el informe. No es un resto por omisión, es
una decisión firmada que se revisa a la luz de lo que pasó después, y por eso
hace falta un ADR y no una corrección silenciosa. Lo que pasó después: la
deliberación de PROP-010 necesitó **rondas sucesivas** —las que registra su
§6.5— y, pasadas las primeras, los hallazgos dejaron de ser sobre lo que la
propuesta proponía y pasaron a ser sobre lo que la propuesta decía de sí
misma — cuántas rondas habían corrido, qué
encontró cada una, si una tabla tenía la fila que le tocaba.

El mecanismo está documentado en
`../reviews/2026-09-18-prop010-recorte.md`: cada corrección cambia el
documento, el cambio deja obsoleta su autodescripción, y la ronda siguiente
lo marca. El documento es su propio sujeto. La propuesta llegó a declarar una
regla interna para romper el bucle —la ronda en curso se registra al
commitear— y la ronda siguiente encontró que la regla protegía la tabla pero
no la prosa que la rodeaba.

Decisión: **el informe y la disposición de una ronda viven en el mismo sitio,
su registro de `docs/reviews/`**. La propuesta remite al registro y no
enumera rondas, veredictos ni hallazgos. Sustituye la segunda mitad de
PROP-010 §7 B —«en la propuesta queda su disposición»—, que se firmó antes de
que se viera el efecto; la primera mitad, que el informe viva en
`docs/reviews/`, sigue vigente y este ADR la refuerza.

**Hogar de la regla: `02` §3.3, por materia.** Esa sección es la del cierre de
una deliberación y ya dice dónde va su material —«el material de deliberación
se movió a `docs/history/` en el mismo cambio»—; dónde vive el resultado de
cada ronda es la misma pregunta. `04` §5 norma **cómo se ejecuta** una ronda,
no dónde se archiva lo que produce. Se deja además un puntero desde `04` §5.2
para quien llegue por ahí.

Y una restricción que conviene declarar, porque un lector la reharía: `04` es
el peor caso del presupuesto de lectura de ADR-021, así que el párrafo ahí
habría dado 1001/1000 y `BLOQ`; en `02`, que no es el máximo, cuesta cero.
Materia y presupuesto apuntaban al mismo sitio, pero sólo uno de los dos era
opcional. Si hubieran apuntado a sitios distintos, la salida legítima sería
una de las cuatro de §3.4 del estándar o un ADR que suba el techo, nunca
mover una regla al archivo más barato.

Consecuencias:

- Una corrección cambia el registro, que es de una sola ronda y no se
  reescribe después; deja de cambiar el documento que la ronda siguiente
  revisa. El bucle no tiene dónde formarse.
- La disposición queda junto al informe, en un archivo que `check_reports`
  recorre. **Su contenido no queda gateado**: ese comando valida la capa
  técnica de esquema cerrado —claves obligatorias y hash reproducible—, no la
  prosa; y una clave nueva en la capa sería rechazada. Lo que mejora es que
  informe y disposición dejen de vivir en documentos con vidas útiles
  distintas, no la verificación automática.
- El formato compacto de una propuesta (todo en un archivo) sigue siendo
  legítimo: lo que sale no son las rondas, sino su contabilidad.
- No cambia nada de lo ya escrito. PROP-010 conserva sus tablas de
  disposición como está: reescribirlas para cumplir una regla posterior sería
  rehacer historia, y el rastro de cómo se llegó hasta aquí es justamente lo
  que sostiene este ADR. Lo mismo vale para los registros ya escritos:
  `../reviews/2026-09-18-prop010-recorte.md` delega en la propuesta el
  recuento de rondas, y `../reviews/2026-09-17-prop010-t03.md` dice que la
  disposición de sus hallazgos vive en la propuesta y no en él. Las dos
  frases describen el reparto anterior, que es el que esta regla cambia: son
  los casos que la motivaron, no ejemplos de cómo aplicarla. **No se
  corrigen**: `docs/reviews/` está declarado «congelado al cerrar» en la
  tabla de vidas útiles del README, y reescribir un registro para que cumpla
  una norma posterior sería rehacer evidencia.

Alternativas descartadas:

- **Dejarlo como está y confiar en el cuidado del redactor.** Es lo que se
  intentó durante cuatro rondas; el resultado fue una regla interna que
  tampoco bastó. Un defecto que reaparece cada vez que alguien corrige algo
  no se arregla con atención.
- **Prohibir que una propuesta mencione sus rondas.** Demasiado estricto: la
  propuesta necesita decir en qué estado está y por qué se corrigió algo.
  Remitir al registro cubre eso sin copiar cifras que caducan.

Procedencia: deliberación de
[PROP-010](../proposals/PROP-010-destilacion-engineering.md) y las rondas que
registra su §6.5, con sus informes en `../reviews/`. Ese material sigue en
`docs/proposals/` al aceptarse este ADR: su traslado a `docs/history/` es la
tarea T09 del plan de PROP-010, no de aquí. Precedente del mismo criterio para otra
cifra viva: [ADR-025](ADR-025-trinquete-no-techo-derivado.md), punto 4 — una
ocupación copiada a un documento normativo envejece antes de que ese
documento se cierre.
