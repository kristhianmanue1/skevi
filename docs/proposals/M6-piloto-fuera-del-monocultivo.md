# M6 — Piloto fuera del monocultivo: criterio de entrada

> **Tipo:** propuesta. **No es norma** y ninguna regla del estándar o de la
> guía la referencia como obligatoria. Existe para que, cuando aparezca un
> adoptante que cumpla el criterio, el piloto se ejecute contra un criterio
> escrito de antemano y no contra uno acomodado al caso que llegó.
> **Procedencia:** [SPEC-M6](../specs/SPEC-M6-2026-09-07-seis-mejoras.md)
> REQ-M6-06 y T07 del [plan M6](../plans/2026-09-07-seis-mejoras.md).
> **Bloqueo:** PREGUNTA-M6-2 de la SPEC — depende de un adoptante externo,
> fuera del control local. Su no ejecución no invalida el resto del programa.

## 1. El monocultivo, con evidencia por piloto

Los cinco pilotos registrados en `docs/history/`, verificados con
`wc -l` sobre cada archivo y `grep` sobre los repositorios que citan:

| Piloto | Archivo | Proyecto | Naturaleza |
|---|---|---|---|
| Autoaplicación | `../history/piloto-autoaplicacion-skevi.md` (182 líneas) | el propio Skevi | corpus documental sobre sí mismo |
| Skopos | `../history/piloto-skopos.md` (185 líneas) | Skopos | único con dependencias reales (MongoDB, Ollama) y datos de usuario |
| orbitaNova I | `../history/piloto-orbitanova.md` (133 líneas) | `kristhianmanue1/orbitaNova` | tarea Bounded, corrección documental |
| orbitaNova II | `../history/piloto-orbitanova-2.md` (128 líneas) | `kristhianmanue1/orbitaNova` | tarea Architectural con plan, contenido documental |
| infosalud | `../history/piloto-infosalud.md` (105 líneas) | `kristhianmanue1/infosalud` | primer F0→F3 completo; CLI Python stdlib-only |

**Variables constantes en los cinco**, y por tanto no probadas:

1. **Autoría única.** Todos los repositorios citados pertenecen a la misma
   cuenta que mantiene Skevi. Ningún piloto tuvo un revisor humano
   independiente del autor del método.
2. **Sin CI remoto.** ADR-001 mantiene el gate local por límite de minutos
   de la cuenta; ningún piloto ejerció el gate dentro de un pipeline.
3. **Sin lenguaje compilado.** Python, JavaScript y Markdown. Nada que
   ejercite PW.6 del cotejo (configuración de compilación) ni tiempos de
   build reales.
4. **Sin base de código heredada grande.** El mayor ejercicio sobre repo
   existente fue una tarea Bounded sobre un README.
5. **Sin equipo.** Ningún piloto ejerció §5.2 del estándar —revisión
   independiente, «el autor no aprueba su propio PR»— con dos personas
   reales.

## 2. Criterio de entrada

Un piloto califica cuando rompe **al menos dos** de las cinco variables de
§1 **a la vez**, y sólo entonces. La razón de exigir dos: romper una sola
produce un caso más del mismo monocultivo con una variante; el corpus ya
tiene cinco de esos.

El criterio es falsable por construcción — cada variable se comprueba con un
hecho observable, no con un adjetivo:

| Variable rota | Cómo se comprueba |
|---|---|
| Autoría distinta | el repositorio pertenece a una cuenta u organización que no mantiene Skevi, verificable en el remoto |
| CI remoto real | existe un workflow que ejecuta el gate y su corrida es consultable |
| Lenguaje compilado | el manifiesto declara un toolchain con paso de compilación |
| Legado grande | el repositorio supera 10 000 líneas de código de producción antes de que el piloto empiece |
| Equipo | al menos un PR del piloto lo aprueba una persona distinta del autor |

«Al menos dos a la vez» significa en el **mismo** piloto, no dos pilotos con
una variable cada uno: lo que está sin probar es la interacción, no cada
variable por separado.

## 3. Qué quedaría respaldado, y qué no

Hoy, `project-manifest.yaml` §`fronteras_de_confianza` limita el alcance de
lo afirmable con esta línea literal:

> «los pilotos registrados son evidencia de un caso, no generalización»

Al ejecutarse un piloto que cumpla §2, quedaría respaldado que el método
**se puede ejecutar** fuera de la autoría y las condiciones que lo
produjeron. **No** quedaría respaldado —y la línea del manifiesto seguiría
vigente sin cambio— que adoptarlo mejore un proyecto: eso es lo que
`no_ofrece` declara explícitamente y un piloto más no lo convierte en
promesa. Seis casos siguen siendo seis casos.

Tampoco respaldaría la frase «mejores estándares de la industria». Esa la
mide el cotejo de [`../crosswalk-estandares.md`](../crosswalk-estandares.md)
control por control, no el número de pilotos.

## 4. Primera aplicación del criterio — 2026-09-08

> **Tercera emisión de esta sección.** Las dos primeras fueron falsas y la
> lección vale más que el resultado. La primera midió la población equivocada
> —los cinco proyectos a los que `no_ofrece` **cede plano**, que no son los
> que **adoptan**— y concluyó «ninguno califica». La segunda corrigió la
> población pero no la medida: contó `.venv/`, `build/` y `references/` como
> código de producción, inflando `epistates` de 8 562 a 22 704 líneas y
> `escrubery` de 12 150 a 19 125. Ambas emisiones dieron un veredicto falso
> con los cuatro gates y los 180 tests en verde.

### 4.1 Cómo se mide, para que sea reproducible

El criterio de §2 nombraba magnitudes sin fijar cómo obtenerlas. Queda fijado:

- **Líneas de producción:** `git ls-files` sobre las extensiones del proyecto,
  excluyendo rutas `tests/`, `vendor/`, `node_modules/`, `dist/` y `build/`.
  **Nunca sobre el árbol de trabajo**, que arrastra dependencias de terceros y
  salida de build.
- **CI remoto que ejecuta el gate:** el workflow existe en la rama por defecto
  **hoy**, tiene disparador automático (`push` o `pull_request`, no sólo
  `workflow_dispatch`), invoca el gate copiable, y sus corridas son
  consultables con `gh run list`. Verde no se exige: una corrida en rojo es
  evidencia igual de válida de que el gate se ejecuta.
- **Gate copiable:** `check_sizes.py` byte-idéntico a **alguna versión
  publicada de Skevi**, no necesariamente la última. Sin este ancla la fila
  sería insatisfacible por todos: ninguna copia del ecosistema coincide hoy
  con `main`.

### 4.2 Población real y resultado

Adoptantes con `skevi-gate.json` o gate copiado, medidos el 2026-09-08:

| Adoptante | LOC producción | CI que corre el gate | Variables rotas |
|---|---|---|---|
| `orbitaNova` | 22 634 | **sí** — `push`+`pull_request`, `npm run check:sizes`, corridas consultables | **2** |
| `eduEMD` | 85 967 (PHP) | **lo tuvo** — verde el 2026-09-06 con `check_sizes` y `check_plans`; el workflow ya no está en la rama por defecto | **2 el 06-09; 1 hoy** |
| `entiendomidiabetes` | 339 651 (PHP) | workflow sí, gate no | 1 |
| `an-kla-memory` | 23 281 | no | 1 |
| `escrubery` | 12 150 | sólo `workflow_dispatch` — su `ci.yml` declara el billing agotado y el CI vigente local | 1 |
| `epistates` | 8 562 | workflow sí, gate no | **0** |
| `basanos` | 3 171 | no | 0 |

**`orbitaNova` califica hoy.** Rompe CI remoto con gate y legado grande a la
vez. Es el primer candidato desde que el criterio se escribió.

**`eduEMD` calificó el 2026-09-06** y es el caso más valioso perdido: PHP —otra
familia de lenguaje—, 85 967 líneas, y una corrida verde ejecutando **dos**
gates de Skevi con una copia byte-idéntica a `v1.0.0`. El workflow fue retirado
después; `d31129c`, el commit de esa corrida, sigue siendo ancestro de su HEAD.
Recuperarlo es una decisión de ese proyecto.

### 4.3 Lo que la aplicación reveló del propio criterio

- **La fila de CI no anclaba versión.** «El gate copiable sin modificar» es
  insatisfacible si significa «igual a `main`»: ninguna copia lo está.
  Anclado a «alguna versión publicada» en §4.1.
- **La fila de autoría era decidible y la declaré `inconclusive`.** En
  `epistates` hay dos correos con **el mismo nombre de persona**: es la misma
  persona con dos cuentas, no dos autores. Alta confianza desde Git.
- **La magnitud sin comando es una invitación a medir mal.** Tres cifras de
  siete estaban infladas por no fijar cómo contarlas.

### 4.4 Seguimiento

1. `orbitaNova` es el piloto viable, con la salvedad de la §6 de
   [la deriva del gate](M6-deriva-del-gate-copiable.md): ejecuta una copia de
   377 líneas contra las 690 vigentes.
2. `eduEMD` es el candidato de mayor valor si su CI vuelve. Es decisión suya.
3. Ambos exigen autorización del adoptante: Skevi no muta proyectos ajenos.

## 5. Qué hacer si nunca aparece el adoptante

Que el piloto no se ejecute es un resultado aceptable y debe registrarse
como tal, no quedar como pendiente perpetuo. En ese caso lo honesto es
declarar en el README que el método está validado **dentro de su
monocultivo** y nombrar cuáles son sus cinco variables constantes, en vez de
dejar que la ausencia de piloto se lea como ausencia de límite.
