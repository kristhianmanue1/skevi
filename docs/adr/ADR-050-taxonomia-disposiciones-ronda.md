# ADR-050: taxonomía de disposiciones de la ronda adversarial

Estado: aceptado (confirmación estructural del Operador, 2026-11-08:
selección «Confirmo los tres (049, 050 y 051)» con el texto de
[PROP-013](../proposals/PROP-013-superpowers-referencia.md) §3 delante,
registrada antes del primer commit fuente).

## Contexto

ADR-037 fijó el hogar de la disposición de cada hallazgo (el registro
de la ronda, no la propuesta), pero dejó su vocabulario libre: cada
ronda inventaba sus categorías y las comparaciones entre rondas se
degradaban. La fuente del candidato (PROP-013 §3) observó en referencias
ajenas dos prácticas de cierre: clasificar cada observación en tres
pilas y re-graduar la severidad por efecto real sobre quien usa el
software — «quien puso minor porque el spec calló graduó el spec, no el
efecto» — con los hallazgos menores registrados pero fuera del pase de
arreglos.

## Decisión

En F3 (`04` §5.2): la disposición de cada hallazgo nombra una de tres
pilas — resuelto con una fuente ya existente (se cita), menor con
decisión del ejecutor registrada, o del Operador (se formula la
pregunta). La severidad se re-gradúa por el efecto real sobre el
consumidor del artefacto, no por lo que el SPEC calló. Los hallazgos
informativos quedan registrados con su disposición y no abren pase de
arreglos.

No cambia quién decide ni qué hallazgos bloquean (`04` §5.3 vigente):
BLOCKER y HIGH se corrigen siempre; MED se corrige o se justifica. El
hogar de la disposición sigue siendo el registro (ADR-037); este
complemento fija su vocabulario.

## Consecuencias

- Registros de ronda comparables entre sí; coste, nueve líneas en `04`
  (presupuesto re-decidido por ADR-052 en el mismo cambio).
- La re-graduación exige leer el efecto sobre el consumidor, no el
  silencio del SPEC: mueve el debate de «¿lo dice el spec?» a «¿qué le
  pasa al usuario si esto sale?».

Procedencia y razón: [PROP-013](../proposals/PROP-013-superpowers-referencia.md)
§3 (candidato C/C', destilado por referencia de `obra/superpowers`);
confirmación del Operador el 2026-11-08.
