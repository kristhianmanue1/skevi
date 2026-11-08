# ADR-051: Review Focus opcional en la plantilla de plan

Estado: aceptado (confirmación estructural del Operador, 2026-11-08:
selección «Confirmo los tres (049, 050 y 051)» con el texto de
[PROP-013](../proposals/PROP-013-superpowers-referencia.md) §4 delante,
registrada antes del primer commit fuente).

## Contexto

El gate de planes (`check_plans`, ADR-014) comprueba estructura — cada
tarea con Consumes/Produce/Steps, cada step con verificación — pero
ningún artefacto declara lo que los steps **no** ejercitan: las clases
de entrada o modos de fallo que el SPEC implica y que ninguna prueba
cubre. La ronda adversarial las descubría tarde y sin lista que mirar.
La fuente del candidato (PROP-013 §4) sitúa esa lista en la cabecera
del plan, tras las restricciones globales, con un máximo de cinco
clases y la prueba que fija cada una en su tarea dueña.

## Decisión

La plantilla de plan
(`templates/skevi/plan-de-implementacion.md`, plantillas/v23) incorpora
la sección opcional **Review Focus**: hasta cinco clases de entrada o
modos de fallo que el SPEC implica y ningún step ejercita, cada una con
el step que la fija. Sin la sección, el plan sigue válido; con ella, la
ronda adversarial la usa como lente de revisión.

Sin regla E nueva: `check_plans` no la exige ni la valida — opcional por
diseño, igual que el gate sigue comprobando forma y no contenido.

## Consecuencias

- Los planes declaran explícitamente lo que sus pruebas no cubren; la
  ronda deja de descubrirlo por búsqueda libre.
- Bump plantillas/v22 → v23 con cascada de digests y espejos en el
  commit fuente (ADR-048); la sección vive en la plantilla, fuera de la
  ruta de lectura.

Procedencia y razón: [PROP-013](../proposals/PROP-013-superpowers-referencia.md)
§4 (candidato D, destilado por referencia de `obra/superpowers`
writing-plans); confirmación del Operador el 2026-11-08.
