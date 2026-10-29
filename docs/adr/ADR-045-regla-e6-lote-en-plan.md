# ADR-045: regla E6 — la TAREA que permite push o merge nombra su lote

Estado: aceptado el 2026-10-29. El Operador confirmó expresamente la regla
descrita y su salto breaking («Confirmo ADR-045», respuesta a una pregunta
que los describía). Implementado en `scripts/check_plans.py` (gate/v12).

Contexto: los PR #78 y #79 se integraron con permiso de sesión, sin
aceptación registrada contra un folio (estándar §4.3, ADR-044). Los
dossiers retrospectivos de ambos PR lo documentan. El PR #80 añadió a
`04` §7 el lote previo al primer efecto y a la plantilla de plan el campo
`Lote:`, pero sólo como texto. El análisis crítico del 2026-10-29
(recomendación 2, PLAN LG tarea LG-6) propuso que el gate de planes
recuerde ese paso en el momento de planificar.

Decisión: regla E6 de `check_plans`. Dentro de un bloque TAREA, si el
campo `Permitido:`, con sus líneas de continuación más sangradas, nombra
`push` o `merge`, la TAREA declara `Lote:` **al mismo nivel** que
`Permitido:`; un `Lote:` dentro de un step no cuenta. El folio es su
primer token, sin la coma final: caracteres de identificador y al menos
un dígito. Esto rechaza `TBD`, `TODO`, `pendiente`, guiones sueltos y el
marcador `<...>` de la plantilla. E6 verifica la **forma**: no comprueba
que el folio exista, que alguien lo aceptara ni que siga vigente. `Lote:`
nombra el folio y no acredita su aceptación; esa autoridad sigue en §4.3,
ADR-044 y el gate humano.

Sólo `push` y `merge`: son las operaciones que ADR-044 deja proponer al
agente según el avance. Tags, releases, reset, rebase y borrados exigen
autorización humana por operación (§4.3, `AGENTS.md`) y no tienen
excepción de lote que recordar.

Excepción a REQ-2 de ADR-014: REQ-2 (plan
`docs/plans/2026-08-20-a4-gate-de-planes.md`, que procede de PROP-004 §2)
exige «cero detección por vocabulario». E5 ya **exime** por vocabulario
(`crea`); E6 es la primera regla que **hace fallar** por vocabulario. Se
acota así:

- sólo lee el campo `Permitido:`, nunca la prosa ni los steps;
- busca dos palabras con límite de palabra inicial, sin distinguir
  mayúsculas;
- un acierto no basta para fallar: además tiene que faltar un campo
  estructural.

Límites declarados:

- un `Permitido:` que diga «integrar a main» sin la palabra `merge` no
  activa la regla (falso negativo);
- una negación en `Permitido:` («sin push ni merge») sí la activa (falso
  positivo); esa exclusión pertenece a `Prohibido:`;
- una TAREA sin campo `Permitido:`, como la de la plantilla mínima, no
  tiene ancla y no se comprueba;
- `force-push` activa la regla aunque el lote no lo cubra; la exclusión
  sigue siendo del dossier;
- la forma del folio es sintáctica: `TBD-1` pasa y un folio entre
  backticks falla.

Alternativas descartadas:

- Dejarlo sólo en texto: así se integraron #78 y #79, con la regla escrita.
- Exigir `Lote:` en toda TAREA: obliga a escribir folios de relleno donde
  no hay operación Git, y un folio de relleno vale menos que su ausencia.
- Verificar la aceptación: un gate local editable por el ejecutor no puede
  acreditarla. Lo prohíbe ADR-044.

Consecuencias: un plan con entrega Git no pasa el gate sin nombrar el folio
que se propondrá o propuso al humano. El olvido pasa a ser BLOQ, pero un
folio nombrado y no aceptado sigue pasando: E6 recuerda, no autoriza. En
Skevi, la TAREA AG-6 del plan del 2026-10-28 se anotó con los folios que
se anunciaron, sin aceptación registrada. Migración para adoptantes:
añadir `Lote: <folio>` a cada TAREA cuyo `Permitido:` nombre push o merge,
antes de recopiar gate/v12.

Procedencia y razón: recomendación 2 del análisis crítico del 2026-10-29,
aceptada por el Operador («adelante con recomendaciones»), y confirmación
expresa de este ADR por el Operador; estándar §4.3,
[ADR-044](ADR-044-push-merge-condicional.md) y
[ADR-014](ADR-014-gate-de-planes-chequeo-estructural.md). Razón: convertir
en BLOQ el olvido que se repitió dos veces, sin confundir forma con
autoridad.
