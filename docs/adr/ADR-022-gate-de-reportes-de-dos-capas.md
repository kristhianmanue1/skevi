# ADR-022: Gate estructural de reportes de dos capas

Estado: aceptado; implementado en `scripts/check_reports.py`, con la clave
`reports` de `skevi-gate.json` y su suite en `tests/test_check_reports.py`.

Contexto: el corpus norma contra el autorreporte —«la salida del ejecutor
nunca es prueba suficiente» (estándar §6.3)— y a la vez dependía del
autorreporte para sus cuatro reglas de mayor valor: ronda adversarial
ejecutada, salida del RED registrada, clase de tarea bien asignada y
autoridad concedida por operación. El gate cubría tamaños (ADR-006),
estructura de planes (ADR-014) y drift de plantillas (ADR-020); la forma de
los reportes de ADR-016 no la comprobaba nadie. El propio manifiesto lo
declara: «no ofrece verificación de que una regla se cumplió de verdad; el
gate comprueba forma y tamaño». Este ADR no cambia esa frontera: la ocupa
hasta donde llega la forma.

Decisión: `scripts/check_reports.py`, separado de `check_sizes.py` por el
mismo criterio que ADR-014 separó `check_plans.py` —forma de un reporte ≠
tamaño de un archivo—, con configuración compartida y una clave nueva
`reports`, objeto de dos campos: `dir` (directorio de registros) y `exempt`
(rutas con exención escrita). Comprueba, por cada capa técnica del archivo:
fence ```text presente; claves obligatorias `id`, `date`, `time_utc`,
`head_sha`, `model`, `STATE`, `GATE`, `PENDING`, `report_sha256`; polaridad
cerrada sobre las claves, con `session`, `DECISION`, `OPERATIONS`,
`AUTHORITY` y `RISK` como opcionales declaradas; `STATE` dentro de
`{OK, PARTIAL, BLOCKED}` y `DECISION` dentro de
`{proceed, fix-and-retry, escalate}`; al menos una línea de `EVIDENCE` con
la forma `- <qué> -> <resultado>`; y `report_sha256` **reproducible** en la
forma canónica que fijó ADR-016 (UTF-8, LF, sin newline final, excluida su
propia línea). **Fail-closed** como `plans`: sin la clave no comprueba nada;
con la clave mal tipada, con subcampo desconocido o con `dir` inexistente,
es `BLOQ`.

**Marcas y transición.** ADR-005 exige que un validador «acepte la línea con
marca y sin ella» mientras dure la transición. La regla implementada respeta
esa exigencia sin renunciar a detectar errores: si el último segmento tras
`->` tiene varias palabras, es prosa y pasa; si es **una sola palabra**,
ocupa el lugar de la marca y debe ser `pass`, `fail` o `inconclusive`. Así
se atrapan `passed`, `ok` o `addressed` sin bloquear las líneas que aún no
llevan marca.

**Más de una capa por archivo.** Un registro puede transcribir dos
emisiones; validar sólo la primera dejaría la segunda sin gate. Se validan
todas. Un fence ```text sin `report_sha256` es salida de comando transcrita,
no una capa técnica, y se ignora: el gate ancla la capa, no todo bloque
preformateado.

Alternativas descartadas:

- **Extender `check_sizes.py`.** Mismo argumento de ADR-014: mezcla
  responsabilidades y su nombre mentiría. La config compartida ya evita la
  divergencia que justificaría juntarlos.
- **Validar el contenido y no sólo la forma** —que la evidencia sea cierta,
  que la ronda existiera—. Es el plano de `epistates` («contrato de tarea
  ejecutable ni máquina de estados de auditoría»), y comprobarlo desde aquí
  invadiría una frontera declarada.
- **Reescribir los dos registros históricos que fallan** en vez de
  exentarlos. Su `report_sha256` cubre su propio texto: editarlos lo
  invalidaría y destruiría justo la propiedad que este gate protege. Una
  evidencia que deja de reproducirse deja de ser evidencia (§3.4, «al partir
  un archivo ya verificado»).
- **No construir el gate.** Deja el hueco que el manifiesto ya declaraba y
  que el análisis crítico del 2026-09-07 identificó como el mayor
  desequilibrio del corpus: las reglas más fuertes con la ejecución más
  débil.

**Hallazgos de la primera corrida** (evidencia de que el gate no es vacuo —
el anti-patrón que ADR-014 bloqueó). Sobre los cinco registros de
`docs/reviews/`, tres pasan y dos fallan por desviaciones reales:

- `2026-09-07-prop008-aterrizaje.md`: `STATE = PARCIAL`, en español. ADR-016
  fija la capa técnica en inglés autoritativo; el valor correcto era
  `PARTIAL`.
- `2026-09-07-t05-authority-consistency.md`: una línea de evidencia marcada
  `-> addressed`, fuera del conjunto cerrado de tres marcas de ADR-005.

Ambos quedan **exentos con este motivo escrito**, no corregidos, por la
razón de la tercera alternativa descartada. La exención es del archivo
concreto, no de la regla: cualquier registro nuevo en `docs/reviews/` se
valida completo. Que dos de cinco registros vigentes se desviaran es la
medida del hueco que este ADR cierra.

**Correcciones de la ronda fresca del 2026-09-08.** Un revisor en contexto
fresco encontró tres defectos en la primera versión de este gate, todos
reproducidos con comandos antes de corregirse: (1) `reports.dir` no se
validaba, de modo que una ruta absoluta producía traceback con rutas del
host —violando el ADR-007 que el propio docstring del script invoca—; (2) el
filtro de `main()` anclaba en el fence ```` ```text ```` mientras
`comprobar_reporte` anclaba en `report_sha256`, y esa asimetría dejaba pasar
sin comprobar una capa técnica escrita en un fence liso —fail-open— y a la
vez rechazaba un registro trivial que sólo transcribía salida de comando
—falso positivo contra el propio CONTRATO y contra «tarea trivial: capa
humana sola» de `00-INDICE.md`—. Ambos ejes se cerraron anclando la capa en
`report_sha256` y validando `dir` con la frontera de `_ruta_contenida`. Se
añadieron además detección de claves duplicadas —`STATE = BLOCKED` seguido
de `STATE = OK` pasaba— y exclusión del hash por clave exacta en vez de por
prefijo.

**Vigencia de la exención** — aclaración de alcance, no decisión nueva: precisa hasta cuándo rige la exención que este mismo ADR ya decidió, sin cambiarla. Una decisión distinta exigiría un ADR propio (`02` §3.2). Las dos exenciones **no caducan**. El
`report_sha256` de esos registros cubre su propio texto y es permanente:
mientras existan, corregirlos seguirá invalidando su hash. No hay disparador
de archivado que las retire —`docs/reviews/` no tiene política de antigüedad,
comprobado con `grep -rn` sobre ADR-002, `AGENTS.md` y `README.md`—, y no se
inventa uno: una caducidad sin proceso que la ejecute es una nota que nadie
lee. Si alguna vez se crea esa política, la exención se revisa entonces.

**Límite declarado.** De las claves opcionales, `session` la fija ADR-016 y
`DECISION` la exige `04` §5.2 para una ronda adversarial. `OPERATIONS`,
`AUTHORITY` y `RISK` **no tienen fuente normativa**: son práctica heredada de
los registros vigentes, admitidas para no rechazarlos. Que el gate las acepte
no las convierte en regla —una regla sin fuente no es aplicable (`AGENTS.md`
§Convenciones de edición)—; darles fuente, o retirarlas, es trabajo aparte.

Consecuencias: un reporte incompleto o con hash que no reproduce deja de
poder cerrarse como `OK`. La integridad reproducible que ADR-016 prometió
pasa de propiedad declarada a propiedad comprobada. Para el adoptante el
cambio es inerte salvo que declare la clave. Copiar `check_reports.py` sin
actualizar `check_sizes.py` produce `BLOQ` por clave desconocida —efecto
buscado y anclado en `tests/test_check_reports.py`—: los tres scripts de
gate comparten un único conjunto cerrado de claves.

Verificación: `python3 scripts/check_reports.py` → `OK`, con 2 registros
exentos por el motivo escrito de arriba. La suite creció de 122 tests a 175
en el programa M6; los de este gate viven en `tests/test_check_reports.py` y
se ejecutaron en RED antes de que el script existiera, antes de la
corrección de capas múltiples y antes de cada hallazgo de la ronda fresca
del 2026-09-08. Las cifras vigentes las reporta la suite, no este texto: un
conteo copiado en un ADR envejece con el primer test que se añada — y este
mismo párrafo ya declaró 157 cuando eran 163.

Procedencia: [ADR-016](ADR-016-reportes-en-dos-capas.md) (la forma que este
gate ancla); [ADR-005](ADR-005-resultado-por-linea-de-evidencia.md) (marcas
y transición); [ADR-014](ADR-014-gate-de-planes-chequeo-estructural.md) (el
patrón de gate separado con config compartida);
[SPEC-M6](../specs/SPEC-M6-2026-09-07-seis-mejoras.md) REQ-M6-02 y T04 del
[plan M6](../plans/2026-09-07-seis-mejoras.md).
Razón: dejar de verificar con autorreporte lo que puede verificarse por
forma, sin cruzar a la verificación de contenido que es de otro proyecto.
