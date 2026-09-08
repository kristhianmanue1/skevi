# ADR-025: El presupuesto de lectura es un trinquete declarado, no un techo derivado

Estado: aceptado. Sustituye la **cláusula de techo** de
[ADR-021](ADR-021-presupuesto-de-ruta-de-lectura.md); su mecanismo —clave
`reading_path`, espina sumada, alternativas por su máximo, fail-closed— sigue
vigente sin cambio.

Contexto: §3.4 del estándar deriva su límite por archivo. Escribe, textual,
que 800 está «calibrado sobre la ventana de lectura típica de un ejecutor
automatizado (del orden de 2000 líneas por lectura, con margen para que el
archivo entre completo junto a su contexto)». Es una estimación, pero es una
estimación **declarada y auditable**.

ADR-021 no hizo lo mismo. Fijó 1000 líneas para la ruta de lectura y no
justificó la cifra en ninguna parte: se eligió porque la ocupación medida el
2026-09-07 quedaba justo por debajo. Una ronda adversarial sobre las
recomendaciones que salieron de ADR-021 lo encontró al preguntar de dónde
salía el número, y con razón: un límite sin derivación no se puede defender
cuando aprieta, y apretó dentro del mismo programa que lo creó.

La tentación inmediata fue peor que el defecto: sacar §4 y §5 del estándar de
la ruta obligatoria para que la cifra bajara unas cien líneas. Se descartó porque §4.1
dice que la regla de rama «aplica desde el primer commit del repositorio»:
las prácticas de Git no son lectura condicional. Mover contenido obligatorio
fuera del numerador habría bajado el número sin que un ejecutor leyera una
línea menos — un gate que mide lo que no importa, que es el anti-patrón que
ADR-014 bloqueó al construir el gate de planes.

Decisión: **no se inventa una derivación que no existe**. El presupuesto se
declara por lo que realmente es: un **trinquete sobre lo observado**. Su
función no es afirmar cuánta norma cabe en una ventana de contexto —eso no se
puede medir desde este repositorio— sino impedir que la ruta crezca sin que
alguien lo decida. En consecuencia:

1. El techo se fija por encima de la ocupación observada, con margen
   deliberadamente escaso. No pretende ser el máximo tolerable.
2. **Subirlo exige un ADR nuevo con su razón escrita.** No es un parámetro de
   configuración que se ajuste cuando estorba: ajustarlo en silencio convierte
   el trinquete en un contador.
3. **Bajarlo no exige ADR**: reducir el techo tras borrar o comprimir norma es
   consolidar una mejora, y el trinquete sólo debe resistir en una dirección.
4. Ninguna cifra de ocupación **vigente** se copia a un documento normativo:
   la emite el gate en su línea de salida. Una cifra **histórica y fechada**
   sí puede citarse, porque no pretende describir el presente. ADR-021
   aprendió la diferencia por las malas: declaró su ocupación tres veces en
   una sola sesión y las tres envejecieron antes de cerrarla.

El techo permanece en **1000**. No se sube para acomodar la ocupación del
momento —cualquiera que sea cuando se lea esto—: eso sería exactamente el
ajuste silencioso que el punto 2 prohíbe. Si la próxima
regla no cabe, la salida es la de §3.4 —borrar lo muerto, separar por vida
útil, partir por audiencia, o exentar— o un ADR que suba el techo con su
razón. Las cuatro son decisiones; ninguna es automática.

Alternativas descartadas:

- **Derivar el techo de la ventana de contexto.** Es lo que se pidió y no se
  puede hacer con honestidad: la ventana útil depende del modelo, del tamaño
  del trabajo en curso y de la herramienta, y ninguno de los tres es medible
  desde aquí. Una derivación inventada sería peor que un trinquete declarado,
  porque parecería fundamento.
- **Subir el techo a 1200 o 1400.** Números igual de arbitrarios que el 1000,
  con la desventaja de retirar la presión justo cuando empezó a funcionar: el
  trinquete ya forzó a mirar la ruta dos veces en un solo programa.
- **Partir el estándar para bajar el numerador.** Descartada por el argumento
  de §4.1 de arriba.
- **Retirar el presupuesto.** Devuelve el corpus al estado en que nada acotaba
  la ruta acumulada, que es el problema que ADR-021 identificó correctamente.

Consecuencias: el presupuesto deja de presentarse como una medida de lo que
cabe y pasa a presentarse como lo que hace —resistir el crecimiento no
decidido—. Quien lo encuentre apretado no puede resolverlo editando
`skevi-gate.json`; tiene que decidir y escribir por qué. La asimetría del
punto 3 hace que comprimir norma sea barato y ampliarla caro, que es la
polaridad que el proyecto quiere.

Verificación: `python3 scripts/check_sizes.py` → `OK`, y su línea de salida
publica ahora `ruta de lectura N/limite` también al pasar — sin eso, la
delegación del punto 4 apuntaría a un gate que no reporta nada (hallazgo de la
ronda fresca del 2026-09-08, corregido en el mismo cambio que este ADR);
`grep -n "del orden de 2000" docs/estandar-diseno-software-github.md` →
devuelve la derivación que §3.4 sí tiene y que ADR-021 no tenía.

Procedencia: [ADR-021](ADR-021-presupuesto-de-ruta-de-lectura.md), cuya
cláusula de techo sustituye; §3.4 del estándar (el modelo de derivación
declarada que ADR-021 no siguió); ronda adversarial del 2026-09-08 sobre las
recomendaciones del programa M6, que refutó tanto la cifra sin derivar como
la propuesta de partir el estándar; instrucción directa del humano, 2026-09-08.
Razón: declarar la naturaleza real del límite en vez de fabricarle un
fundamento, y hacer cara su ampliación y barata su reducción.
