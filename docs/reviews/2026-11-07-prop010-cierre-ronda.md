# Ronda de cierre — PROP-010 §8 (T05–T09)

Objeto: la ejecución completa del plan derivado de PROP-010 sobre la rama
`feat/prop010-t05-t09` (base `d185427`), bajo ADR-047 ya en main. Esta
ronda, con sección por tarea como exige la propuesta, **es también la
ronda de cierre que su T09 ordena registrar**. Revisó una sesión fresca
del mismo proveedor (GLM); sólo lectura.

Veredicto: **fix-and-retry** — los seis hallazgos se cerraron antes del
commit de cierre y se reverificaron (gates y suite en verde).

## Hallazgos y disposición

1. [HIGH] El ejemplo `installed.json` conservaba el digest de
   `usage-guide.md` de v21 — y `check_templates` no lo caza (corta por
   versión). Cerrado: entradas de usage-guide, corpus-installed y
   scripts-installed sincronizadas a reales; la auto-referente queda
   ilustrativa por construcción, como su precedente.
2. [MED] La fila LLM01 citaba `no_ofrece` como fuente de una cesión que
   esa lista no contiene. Cerrado: redactada sin atribución falsa; y
   declarada la condición de plantilla opcional punteada desde `04` §5.1.
3. [MED] `.gitignore` apuntaba a `docs/proposals/externals/` (ruta
   muerta) y el zip movido quedaba sin ignorar. Cerrado: regla a
   `docs/history/externals/`, `check-ignore` verificado.
4. [MED] La fila de `docs/proposals/` del README quedó huérfana — la
   nota que HV-3 preveía. Cerrado: fila y prosa anotan que el directorio
   existe sólo mientras hay deliberación abierta.
5. [LOW] La cláusula de retirada del catálogo omitía el disparador
   «piloto falla». Cerrado: ambos disparadores de §3.5 en el encabezado.
6. [LOW] «cubre» sobre plantilla opcional. Cerrado con el matiz de la
   fila (puntero normativo en `04` §5.1).

Nota del cierre: la observación del revisor sobre «doble commit del
auto-hospedaje» no aplica — ADR-048 ya vive en main y los espejos están
en `@HEAD`; la suite en verde con los cambios sin commit lo demuestra.

## Capa técnica

```text
id = SKV-PROP010-CIERRE-20261107-01
date = 2026-11-07
time_utc = 14:00:59Z
head_sha = d185427429b20ad6bd4f2dbba6ae013ebd62b4bc
model = GLM-5.3 zai-coding-plan; revisor fresco (self-declared; not proof)
STATE = OK
GATE = ronda adversarial de cierre de PROP-010 §8 (T05-T09) con seccion
por tarea, sobre la rama feat/prop010-t05-t09 sin commit; veredicto
fix-and-retry; los seis hallazgos (1 HIGH, 3 MED, 2 LOW) cerrados antes
del commit de cierre y reverificados.
EVIDENCE
- catalogo: 9/9 clases con pregunta y evidencia; sin copia upstream -> pass
- punteros 04 §5.1 y §8 -> +2 lineas netas; ruta 1620/1620 -> pass
- digests internos del ejemplo installed.json -> todos al dia -> pass
- .gitignore -> docs/history/externals/ y zip ignorado -> pass
- fila README de proposals -> nota de convencion anadida -> pass
- fila LLM01 -> cita de no_ofrece retirada; opcional declarado -> pass
- recuento crosswalk -> OWASP 6/1/3 y SSDF 9/7/3 cuadran -> pass
- unittest discover -s tests -> 297 tests OK -> pass
- cuerpos sellados ADR-020/035/036/037 -> diff vacio -> pass
PENDING = piloto de la plantilla (caso real con registro) para salir de
experimental, conforme a PROP-010 §3.5; HV-3 y HV-5 completos con este
cierre; queda el piloto PT del ciclo autonomo, que exige orden expresa
DECISION = fix-and-retry
OPERATIONS = ejecucion de PROP-010 §8 T05-T09; traslados a docs/history;
round de solo lectura; sin efectos Git
AUTHORITY = Operador 2026-11-07: «adelante» sobre los pendientes con
decision A ya confirmada (ADR-047) y sesion de commits activa
RISK = revisor del mismo proveedor y familia que el autor; la entrada
auto-referente del ejemplo installed.json sigue ilustrativa por
construccion, como su precedente
report_sha256 = b0f1d7bd99489e6982c4f7a151a9135736be0202322cab0043396090448a374d
```

Límite declarado: revisor de contexto fresco del mismo proveedor salvo
que el Operador designe otro. El piloto de la plantilla (§3.5) requiere
un caso real con registro de dos capas para sacarla de experimental.
