# ADR-024: Complemento de fase para componentes con salida no determinista

Estado: aceptado; implementado en
`docs/ai-agent-guide/06-componentes-con-llm.md`, con alta en el índice de la
guía y el campo `Presupuesto` del contrato de tarea de `04` §1.

Contexto: el corpus se declara «para operar agentes de IA que crean y
mantienen proyectos» y no tenía procedimiento para el caso en que el
**producto** depende de un LLM. `04` §3 impone RED-GREEN-REFACTOR sobre
tests deterministas; `04` §5.3 disparador 2 reconoce el componente que actúa
sobre salida de un modelo, pero sólo para elevar el rigor de la revisión, no
para verificarlo. El cotejo de
[`crosswalk-estandares.md`](../crosswalk-estandares.md) marcó OWASP LLM10
«Unbounded Consumption» como no cubierto: cero presupuesto de contexto,
tokens o coste en todo el corpus —las cuatro apariciones de «token» en el
estándar son credenciales de §5.4—. La búsqueda de `evals` en `docs/` daba
cero: los aciertos eran el verbo español «evalúa».

Decisión: un **complemento de fase** de lectura condicional, no una fase
nueva ni una regla transversal. Fija: disparadores observables de §1 (salida
no reproducible, consumo de salida de LLM, consumo de cuota tarifada); qué
es RED cuando el test no es binario —la propiedad, no el texto; umbral
declarado **antes** de medir; aleatoriedad fijada o declarada—; conjunto de
referencia versionado en el repositorio con procedencia por caso; campo
`Presupuesto` en el contrato de tarea, obligatorio bajo el disparador 3, con
fallo explícito al agotarse; y validación de la salida del modelo en la
frontera, remitiendo al principio 7 y a §2.4 sin reenunciarlos.

**Complemento, no fase.** Se numera `06` junto a `05-memoria-del-agente.md`,
que ya establece el género: recomendación de lectura condicional cuyas
reglas son obligatorias **si** el caso aplica. Queda por tanto **fuera** de
la ruta de lectura obligatoria de ADR-021: incorporarlo habría consumido 104
líneas de un presupuesto que ya está en 972 de 1000.

Alternativas descartadas:

- **Reglas transversales en el estándar.** El estándar es independiente de
  herramientas y proveedores; un procedimiento de verificación no
  determinista sólo aplica a un subconjunto de proyectos. Habría violado la
  regla 3 de `00-INDICE.md` —mínimo necesario— para todos los demás.
- **Extender `04` §3 en línea.** `04` es el archivo de fase más largo (256
  líneas) y el que fija el máximo de la ruta de lectura: cada línea añadida
  ahí la paga toda sesión, aplique o no el caso.
- **Normar elección de modelo, catálogo o comparativa.** Cedido a
  `escrubery` por `project-manifest.yaml` §no_ofrece; el complemento lo dice
  en su encabezado para que la frontera se lea donde se aplica.
- **Exigir un umbral numérico concreto** (p. ej. 95%). Depende del dominio y
  del coste del error; fijarlo aquí sería generalidad especulativa. Lo que
  se exige es que el umbral, la muestra y el criterio de regresión se
  declaren **antes** de medir — un umbral elegido a posteriori no es un
  criterio, es una justificación.

Consecuencias: LLM10 pasa de «no cubre» a cubierto en el cotejo; el
disparador 2 de `04` §5.3 gana el procedimiento que le faltaba. Un
componente con salida no determinista deja de poder cerrarse con un test que
no prueba nada, que es el anti-patrón que `03` §7 ya prohíbe en el cascarón
y que aquí no tenía equivalente. El campo `Presupuesto` es opcional por
defecto: una tarea que no consume cuota tarifada no gana ceremonia.

Verificación: `python3 scripts/check_sizes.py` → `OK`, con la ruta de lectura
dentro de su presupuesto tras el alta en el índice y el campo nuevo de `04`;
el complemento no entra en la ruta por ser de lectura condicional. El conteo
de archivos y la ocupación vigentes los reporta el gate: copiarlos aquí los
deja obsoletos con el archivo siguiente.

Procedencia: [SPEC-M6](../specs/SPEC-M6-2026-09-07-seis-mejoras.md)
REQ-M6-04 y T06 del [plan M6](../plans/2026-09-07-seis-mejoras.md);
[`crosswalk-estandares.md`](../crosswalk-estandares.md) (OWASP LLM10 y el
límite de LLM05); [ADR-008](ADR-008-disparadores-objetivos-de-rigor.md)
(disparadores observables en vez de calificativos);
[ADR-011](ADR-011-red-green-refactor-default-condicional.md) (la regla que
este complemento precisa sin sustituir).
Razón: dar procedimiento donde el corpus sólo tenía el caso determinista,
sin cargar a los proyectos que no lo necesitan.
