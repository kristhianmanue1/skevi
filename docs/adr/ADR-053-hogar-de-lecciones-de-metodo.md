# ADR-053: hogar de lecciones de método (docs/lecciones/)

Estado: aceptado (decisión D1 del informe de contexto del
[issue #99](https://github.com/kristhianmanue1/skevi/issues/99), aplicada
por orden del Operador 2026-11-13: «se aplican tus recomendaciones» sobre
la aceptación del lote SKV-LOTE-20261112-01). Implementado en
`docs/lecciones/` y en la fila de hogares del `README.md`.

Contexto: devHerdrExpert clasificó 47 notas de aprendizaje y derivó al
issue #99 nueve reglas de método candidatas con dueño natural skevi. El
triaje verificado contra el corpus dejó 4 ya cubiertas, 2 parciales que
completan la guía `04` (filas 1 y 2) y 3 sin hogar (filas 6, 7 y 8:
medición con límites de palabra, declaración de reglas omitidas al
cerrar, re-hecho del barrido completo). La ruta de lectura obligatoria
está a su tope decidido (1640/1640, ADR-052), así que absorberlas en la
guía exigiría condensar canon sellado o re-decidir el trinquete por cada
lección futura.

Decisión: skevi adopta `docs/lecciones/` como hogar de lecciones de
método con evidencia. Cada lección es un archivo corto en Git con claves
fijas (id estable grep-able, Regla, Cómo aplicarla, Evidencia, Origen,
Revisión) y entra sólo tras revisión con contexto fresco (la ronda que la
admita, registrada en `docs/reviews/`). Precedencia declarada: corpus >
lecciones — una lección nunca modifica ni interpreta norma. Promoción,
no duplicación: la lección que demuestre ser regla recurrente viaja a la
guía en un salto `corpus/vN` y deja de ser lección. El formato es
autocontenido y agnóstico de proveedor (misma doctrina de neutralización
que ADR-035): un lector externo puede servirlo con `--repo`, sin que
skevi dependa de ese lector.

Alternativas descartadas:

- absorber las tres en la guía `04`: paga condensación de canon sellado
  o un ADR de presupuesto por cada lección futura, contra el propósito
  del trinquete (ADR-025, ADR-038);
- no adoptar hogar y dejar las lecciones sólo en memorias de agentes:
  la memoria recuperada es dato no confiable (guía `05` §2) y las reglas
  perderían trazabilidad sin memoria instalada (K4);
- duplicarlas como norma y como lección: la duplicación que este repo
  midió como indetectable con reglas baratas (issue #99, coste declarado
  de la alternativa).

Consecuencias: `docs/lecciones/` crece por archivo corto, fuera de la
ruta de lectura y del dominio del manifiesto de corpus (sólo sella los
ocho archivos del estándar y la guía); el gate de tamaños le aplica el
límite por defecto. Las filas 6, 7 y 8 del issue #99 viven aquí; las
filas 1 y 2 quedaron en la guía `04` (§6 y §7, corpus/v12) y las filas
3, 4, 5 y 9 ya estaban cubiertas (guía `05` §2 y §4, `00-INDICE` regla
5, estándar §1 p3 y §5.3). El mapa de orientación re-referencia su
encabezado a corpus/v12 sin cambios de grafo.
