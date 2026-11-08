# ADR-049: registro de decisiones intermedias en F3 (rulings)

Estado: aceptado (confirmación estructural del Operador, 2026-11-08:
selección «Confirmo los tres (049, 050 y 051)» con el texto de
[PROP-013](../proposals/PROP-013-superpowers-referencia.md) §2 delante,
registrada antes del primer commit fuente).

## Contexto

Durante una TAREA con plan de varias tareas, las decisiones que ni el
plan ni el SPEC contestan (y el progreso intermedio) vivían sólo en el
contexto de la sesión. Una compactación o un relevo las borra: el
re-despacho de trabajo ya completado tras una compactación es el fallo
más caro reportado por adoptantes del método con ejecución por tareas
(Referencia: PROP-013 §2; superpowers executing-plans y
subagent-driven-development — dato de su fuente, no evidencia local).

## Decisión

En F3 (`04` §2): el progreso intermedio y esas decisiones se registran
en archivos con la forma `Ruling: <qué decidí> — <por qué> — <qué coste
si fallo>`; una desviación sin registro es una decisión en secreto.
Tras una compactación o relevo manda el estado de Git y esos archivos,
no el recuerdo de la sesión.

La regla no crea permisos, gate, runtime ni dependencia de memoria o
host: archivos y Git valen con o sin memoria instalada (K4). Su
verificación es de ronda adversarial y dossier, no estructural.

## Consecuencias

- Decisiones intermedias trazables y reanudación verificable tras
  compactación; coste, unos archivos efímeros por tarea y diez líneas
  de norma en `04` (presupuesto re-decidido por ADR-052 en el mismo
  cambio).
- El texto confirmado por el Operador decía «compactación»; el
  aterrizaje añade «relevo de sesión» como caso equivalente — misma
  pérdida de contexto, misma cura — y lo declara aquí para que el
  texto de `04` y la confirmación cuadren.
- El formato obliga a declarar el coste de cada desviación en el
  momento de decidirla, no a posteriori.

Procedencia y razón: [PROP-013](../proposals/PROP-013-superpowers-referencia.md)
§2 (candidato A, destilado por referencia de `obra/superpowers`);
confirmación del Operador el 2026-11-08. La prueba local, si alguna
día se busca, corresponde al programa de evaluación conductual (§5 de
la misma propuesta), nunca a la fuente ajena.
