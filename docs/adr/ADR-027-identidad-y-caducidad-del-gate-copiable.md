# ADR-027: Identidad y autocaducidad del gate copiable

Estado: aceptado; implementado en `scripts/check_sizes.py`
(`GATE_VERSION`, `GATE_GENERATED_AT`, `GATE_STALE_AFTER_DAYS`,
`gate_staleness`).

Contexto: un barrido del ecosistema el 2026-09-08 encontró **18 repositorios
que citan a Skevi** y **once con `scripts/check_sizes.py` copiado**. Ninguna
copia estaba al día: nueve son byte-idénticas al commit `7bfd759c` del
2026-08-20, dos a `38095fd3` del 2026-08-17. Cero adaptación —las copias son
idénticas entre sí, y la variación por proyecto vive donde ADR-006 la manda,
en `skevi-gate.json`— y por tanto es congelamiento puro, no divergencia.

La consecuencia está verificada. El programa AUDIT-2026-09-07 corrigió que el
gate podía declarar éxito sin leer un archivo sujeto a control. Mismo fixture
—un `.md` con bytes no válidos como UTF-8— contra ambos: la copia de los
adoptantes responde `OK` con código 0; el gate vigente responde `BLOQ` con
código 1. `orbitaNova` y `eduEMD` han validado en CI con la versión que dice
`OK`.

**El defecto del mecanismo existente** no es que falte comprobación, sino
dónde vive: `check_templates.py` (ADR-020) es un script aparte que hay que
acordarse de ejecutar apuntando a un checkout de Skevi. Nadie ejecuta una
comprobación cuya existencia desconoce, y su alcance además es
`templates/skevi/` — la documentación copiable—, no `scripts/`. Se versionó lo
que se lee y quedó sin versionar lo que se ejecuta.

Decisión: la señal va **dentro del gate que el adoptante ya ejecuta**, en dos
piezas mínimas y sin red:

1. **Identidad visible.** `GATE_VERSION` y `GATE_GENERATED_AT` se imprimen en
   la línea de salida, en `OK` y en `BLOQ`. No informan de que exista algo
   nuevo; hacen que lo viejo sea **visible** en cada log de CI. Quien compare
   dos repos lo nota sin herramienta.
2. **Autocaducidad.** Cumplidos `GATE_STALE_AFTER_DAYS` desde
   `GATE_GENERATED_AT` —el día 90, no el 91—, el gate añade un aviso con su edad en días. Dice
   «soy vieja», nunca «existe una nueva»: lo segundo exigiría observar el
   origen, y `project-manifest.yaml` §`no_ofrece` cede ese plano —«no
   instala, **no observa** y no muta un proyecto»—.

**Aviso, nunca `BLOQ`.** Romper el CI de un adoptante porque exista algo más
reciente sería cambiarle el comportamiento sin su permiso. Hereda la
polaridad de ADR-020: obsoleto pero compatible → aviso.

**El aviso no altera el código de salida** y un `GATE_GENERATED_AT` mal
editado al copiar devuelve `None` en vez de fallar: la identidad de la copia
no es una frontera de seguridad y no debe poder tumbar un gate ajeno.

Alternativas descartadas:

- **Consulta de red desde el gate.** Rompe ADR-001 en espíritu —gates locales,
  sin dependencia de infraestructura remota—, añade una dependencia y un modo
  de fallo nuevo, y convierte una comprobación de tamaños en un cliente HTTP.
  Si alguien quiere red, que sea un comando aparte y explícito.
- **Que Skevi barra el ecosistema y reporte quién está desactualizado.** Es lo
  que se hizo a mano para llegar hasta aquí, y es útil — pero es observación
  de corpus, cedida a `argos` por el manifiesto. Si esa herramienta debe
  existir, vive allí.
- **Sólo extender el manifiesto de ADR-020 a `scripts/`.** Es la comparación
  autoritativa y sigue siendo deseable, pero por sí sola no resuelve el
  problema observado: responde «¿estoy al día?» a quien pregunta, y el
  problema es que nadie preguntaba. Queda como trabajo siguiente, con su
  propio ADR, sobre esta base.
- **Versión en los cuatro scripts a la vez.** `check_sizes.py` es el que once
  adoptantes copiaron y el que demostró la deriva. Los demás la adoptan cuando
  se observe el mismo caso, no por simetría anticipada (regla 3 de
  `00-INDICE.md`: mínimo necesario).

Consecuencias: cada corrida de CI de un adoptante deja constancia de con qué
versión validó. Un adoptante que copie hoy y no vuelva recibirá, al cumplirse los noventa días, un aviso en su propia salida sin que Skevi haya mirado su repositorio.
Al cambiar el comportamiento del gate hay que subir `GATE_VERSION` y poner la
fecha: es una obligación nueva del mantenedor, y su olvido produce una copia
que miente sobre su edad — riesgo aceptado, porque la alternativa es no tener
identidad ninguna.

**Lo que esta decisión no hace:** no actualiza la copia de nadie, no detecta
si la copia fue modificada, y no compara contra el origen. Para eso está el
trabajo siguiente sobre el manifiesto.

Verificación: `python3 scripts/check_sizes.py` → la identidad aparece en la
línea `OK` **y en la de `BLOQ`**, ambas con test; la primera emisión sólo la
imprimía en `OK`, que es el log que nadie lee cuando todo va bien. Los tests
de identidad viven en `tests/test_reading_path.py` y cubren el umbral en su
frontera exacta —89 días sin aviso, 90 con él—, reloj anterior a la
generación, constante mal editada de cualquier tipo (formato roto o comillas
borradas), y que el aviso **no** afirme la existencia de una versión más
nueva. El total vigente de la suite lo reporta la suite.

Procedencia: [`M6-deriva-del-gate-copiable`](../proposals/M6-deriva-del-gate-copiable.md)
(el barrido, los hashes y el fixture); [ADR-020](ADR-020-adopcion-versionado-plantillas.md)
(la polaridad de aviso y el mecanismo que no llegaba a `scripts/`);
[ADR-006](ADR-006-gate-configurable-por-proyecto.md) (el script se copia sin
modificar, la variación va en la config); instrucción directa del humano,
2026-09-08.
Razón: poner la señal de vejez dentro de lo que el adoptante ya ejecuta, que
es lo único que alcanza a quien no sabe que tiene un problema.
