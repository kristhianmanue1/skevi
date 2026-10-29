# ADR-046: frontera final en E6 — flexiones no activan la regla

Estado: aceptado el 2026-10-29. El Operador confirmó la regla descrita
con la frase «Confirmo ADR-046», registrada en la conversación antes del
commit fuente (16:35Z del agente), en respuesta al bloque que enumeraba
las tres frases de cierre. Precedente ADR-045: la aceptación se registra
contra la confirmación, no contra un «adelante» previo al texto.

Contexto: la revisión arquitectural del 2026-10-29 (hallazgo M1,
familia GLM sobre corpus de Claude Opus) detectó que `OPERACION_RE`
carece de frontera final: `\b(?:push|merge)` activa E6 con «pushes»,
«merged» o «mergeable», y no había tests de flexiones. ADR-045 declaró
el falso positivo por negación pero no esta clase. Impacto: un BLOQ
espurio invita a nombrar un folio de relleno, degradando la señal del
campo `Lote:`, cuyo valor es justamente recordar el lote real.

Decisión: la regex pasa a `\b(?:push|merge)\b`. Sólo la palabra exacta,
con o sin mayúsculas, activa la regla. «Force-Push» sigue activando:
hay límite de palabra tras el guión. «Sin push ni merge» sigue
activando: el límite declarado por negación no cambia. No se toca ni la
ancla (`Permitido:` con sus continuaciones) ni la forma del folio.

Límites que permanecen: «integrar a main» sin la palabra no activa;
la negación activa (esa exclusión pertenece a `Prohibido:`); el análisis
sigue limitado al campo `Permitido:` (el hallazgo M2 de esa misma
revisión queda como límite documental, sin cambio de gate). Borde nuevo:
«push_» o «force_push» dejan de activar — el subrayado es carácter de
palabra—; caso construido, se acepta.

Alternativas descartadas:

- Declarar el límite sin cambiar el gate: deja vivo el BLOQ espurio que
  el ADR-045 quiso evitar con `FOLIO_RE`.
- Una lista de excepciones léxicas: reintroduce sorpresas palabra a
  palabra; la frontera es la regla general del español y del inglés.

Consecuencias: no breaking — ningún plan que pasaba deja de pasar. Los
BLOQ por flexión desaparecen, pero no toda flexión era espuria:
«hacer merged del PR» o «subir commits ya merged» nombraban la operación
y en v12 pedían folio; en v13 pasan sin pedirlo. Es el falso negativo de
la misma clase que ADR-045 ya aceptó con «integrar a main». Tests: tres
casos negativos nuevos de flexión, junto a los positivos de fuerza
existentes. La excepción a REQ-2 de ADR-014 queda acotada igual que en
ADR-045: campo único, límite de palabra inicial y final ahora, y
exigencia de falta estructural.

Procedencia y razón: hallazgo M1 de la
[revisión GLM](../reviews/2026-10-29-glm-revision-arquitectural.md) y su
ronda adversarial del 2026-10-29. Razón: eliminar el falso positivo de
flexión sin ampliar la excepción léxica más allá de lo ya declarado.
