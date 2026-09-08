# ADR-021: Presupuesto de la ruta de lectura obligatoria

Estado: aceptado.

El vocabulario de `02` §3.2 —`propuesto | aceptado | rechazado | sustituido
por ADR-<m>`— no admite sustitución parcial, así que este ADR **no** se marca
sustituido: sigue aceptado y su mecanismo vigente. Lo que cambia es la
**justificación** del techo, que rehace
[ADR-025](ADR-025-trinquete-no-techo-derivado.md): donde aquí se presentaba
1000 como límite, ADR-025 lo declara trinquete sobre lo observado. Ante
contradicción entre ambos textos gana ADR-025, por posterior y explícito.
Implementado en `scripts/check_sizes.py` (clave `reading_path` de
`skevi-gate.json`) y en el §3.4 del estándar.

Contexto: §3.4 acota **cada archivo** porque «un archivo que no cabe en una
lectura se aplica a medias». El argumento es correcto y estaba aplicado a
medias: nada acotaba la **suma** que un ejecutor debe leer antes de poder
actuar. El 2026-09-07 esa suma era de 923 líneas —`AGENTS.md` 104,
`00-INDICE.md` 113, el estándar 450 y el archivo de fase más largo, `04`,
256— y crecía con cada mejora sin que ningún gate lo notara. El corpus
completo pasaba de 10 900 líneas de Markdown con 20 ADRs. La misma
patología que §3.4 diagnostica en un archivo grande —quien lo lee actúa
sobre una vista parcial creyéndola completa— se reproduce a escala de
corpus, y ahí no había verificador.

Decisión: extender `check_sizes.py` con una clave nueva `reading_path` en
`skevi-gate.json`, de tres campos: `limit` (entero positivo), `files`
(rutas que **se suman**: la espina que se lee en toda sesión) y
`worst_case_of` (rutas **excluyentes** de las que sólo cuenta la mayor).
El gate suma la espina más el máximo de las alternativas y falla si excede
`limit`. **Fail-closed** como `plans` (ADR-006): sin la clave no comprueba
nada; con la clave mal tipada, con subclave desconocida, con `limit` no
entero o con ruta que escapa la raíz, es `BLOQ`. Un archivo ausente o
ilegible de la ruta **no acredita tamaño cero**: es fallo, con la misma
lógica que ADR-007 impone al resto del gate.

Límite de Skevi sobre sí mismo: **1000 líneas**, declarado por escrito
—no heredado en silencio, como exige §3.4—. Espina: `AGENTS.md`,
`00-INDICE.md` y el estándar. Alternativas: los cuatro archivos de fase
`01`–`04`. Ocupación al medirla por primera vez, el 2026-09-07: 923 de 1000,
el 92%. La cifra vigente la reporta el gate y no se copia a ningún documento
normativo: la norma que este mismo ADR añade a §3.4 ya consumió parte del
margen, y eso es la regla funcionando, no un descuido. La holgura
es deliberadamente escasa: el valor de la regla es forzar una decisión
—borrar, partir o exentar— la próxima vez que la ruta crezca, no dar
margen para que crezca sin que nadie decida.

Alternativas descartadas:

- **Sumar todos los archivos de fase.** Mide un camino que nadie recorre:
  un ejecutor lee el archivo de la fase en la que está, no los cinco. Con
  esa cuenta la ruta daría 1378 líneas y el número no significaría nada.
  De ahí `worst_case_of`, que no es generalidad especulativa: modela una
  exclusión que ya existe hoy en la estructura del corpus.
- **Un límite por archivo más estricto.** No resuelve el problema: cuatro
  archivos de 200 líneas suman lo mismo que uno de 800 y ninguno viola su
  límite individual.
- **Contar caracteres o tokens en vez de líneas.** Más fiel a la ventana
  real del ejecutor, pero incomparable con el resto de §3.4 —que ya mide
  líneas— e imposible de reproducir sin fijar un tokenizador, es decir,
  sin acoplarse a un proveedor de modelo. Se descarta por el criterio 4 de
  §8: no añadir dependencias.
- **Un script aparte, `check_reading_path.py`.** Se descarta por el
  criterio contrario al de ADR-014: allí eran dos responsabilidades
  distintas (estructura de planes ≠ tamaños); aquí es literalmente la misma
  —contar líneas contra un límite— y separarla duplicaría el descubrimiento
  y la lectura de configuración.
- **No medirlo.** Deja la regla insignia del proyecto aplicada a medias y
  sin verificador, que es exactamente lo que §3.4 reprocha.

Consecuencias: la ruta de lectura pasa a ser una magnitud gobernada, no un
efecto colateral. Añadir norma al estándar o a `AGENTS.md` deja de ser
gratis: consume presupuesto, y agotarlo obliga a las mismas cuatro salidas
de §3.4 —borrar lo muerto, separar por vida útil, partir por fase o
audiencia, o exentar con motivo escrito—. Los archivos complementarios
(`05-memoria-del-agente.md` y los que se añadan como complemento) quedan
**fuera** de la ruta por ser de lectura condicional; incorporarlos exigiría
declararlos en la clave y absorber su coste. Para el adoptante el cambio es
inerte salvo que declare la clave: sin ella, cero comprobaciones. La clave
vive en el conjunto cerrado compartido con `check_plans.py`, de modo que un
`check_sizes.py` desactualizado la rechaza con `BLOQ` en vez de ignorarla.

Verificación: `python3 scripts/check_sizes.py` → `OK` con la clave activa y
la ruta dentro de su presupuesto; los 12 tests de esta clave viven en
`tests/test_check_sizes.py` (`ReadingPathTests`), los 8 primeros ejecutados
en RED antes del código y los 4 de `worst_case_of` en RED antes de su
implementación. El total vigente de la suite lo reporta la suite.

Procedencia: `docs/estandar-diseno-software-github.md` §3.4 (el argumento
que este ADR completa); [SPEC-M6](../specs/SPEC-M6-2026-09-07-seis-mejoras.md)
REQ-M6-05 y T03 del [plan M6](../plans/2026-09-07-seis-mejoras.md);
instrucción directa del humano, 2026-09-07.
Razón: aplicar al corpus el mismo argumento que §3.4 aplica al archivo.
