# Registro de cierre — programa M6, seis mejoras

Plan: [M6-2026-09-07](../plans/2026-09-07-seis-mejoras.md).
Autoriza: [SPEC-M6](../specs/SPEC-M6-2026-09-07-seis-mejoras.md).
Rama: `feat/seis-mejoras-2026-09-07`. Base: `b400b85`.

> **Segunda emisión.** La primera (`SKV-M6-20260908-01`) declaró `PARTIAL`
> porque la ronda en contexto fresco no podía ejecutarse. El humano la
> autorizó, se ejecutó, y su reporte encontró que **tres líneas de esa
> emisión marcadas `pass` eran falsas**. Esta emisión las corrige y las
> conserva marcadas `fail` en la evidencia: borrarlas habría ocultado el
> fallo en vez de registrarlo.

## Capa técnica

```text
id = SKV-M6-20260908-02
date = 2026-09-08
time_utc = 03:52:26Z
head_sha = b400b85c164827ecfb107363a2194c5c6635a9c7
model = Claude Opus 5 (self-declared)
STATE = OK (six improvements delivered; fresh-context round executed, findings closed)
GATE = Plan M6 T00-T08 closed with evidence; fresh-context adversarial round ran and its BLOCKER, HIGH and cheap MED findings are corrected.
EVIDENCE
- python3 scripts/check_sizes.py -> OK, 107 text files within limits -> pass
- python3 scripts/check_plans.py -> OK, 3 plans verified (E1-E5) -> pass
- python3 scripts/check_reports.py -> OK, reports verified, 2 exempt -> pass
- python3 -m unittest discover -s tests -> Ran 175 tests, OK -> pass
- Test count chain -> 110 base, 122 after T03, 160 after T04, 163 after F-3, 175 after this round -> pass
- Standalone run matches discover -> sizes 62/62, plans 26/26, reports 50/50 -> pass
- sh scripts/hooks/pre-push -> all four gates green -> pass
- BLOCKER absolute reports.dir -> reproduced as ValueError traceback leaking host paths, then fixed -> pass
- HIGH technical layer in plain fence -> reproduced as OK with exit 0, then fixed -> pass
- HIGH command-output fence rejected -> reproduced as BLOQ on a valid trivial record, then fixed -> pass
- Re-attack of the three after fix -> controlled BLOQ, BLOQ, OK exit 0 respectively -> pass
- Crosswalk labels recounted against rows by script -> SSDF 9/6/4, OWASP 5/2/3, totals 19 and 10 -> pass
- Crosswalk prior emission -> declared 7/6/6 and 5/2/3, correct sums over false cells; corrected -> fail
- LLM03 relabelled no-cubre to parcial -> 04 section 7 already authorised dependency changes and was not cited -> fail
- EV-M6-2 as first written -> command did not reproduce; rewritten with the exclusion actually used -> fail
- F-3 in check_plans -> RED on two cases returning 0, then BLOQ with exit 1 -> pass
- Reading path budget -> 982 of 1000 lines -> pass
- Broken relative links across the corpus -> 0 -> pass
- git diff --check -> no output -> pass
- Fresh-context adversarial round -> executed by an independent reviewer agent authorised by the human -> pass
- Reviewer decision -> fix-and-retry; all BLOCKER and HIGH findings closed and re-verified -> pass
PENDING = PREGUNTA-M6-2 external pilot; PREGUNTA-M6-3 precision of the no_ofrece authority line; two LOW findings accepted as risk; a second fresh round was not run after these corrections.
DECISION = proceed
OPERATIONS = commit of the M6 change on branch feat/seis-mejoras-2026-09-07, authorised by the human; no push, merge, PR, tag or release
AUTHORITY = Human authorised planning, execution of the six improvements, option A of PREGUNTA-M6-1, the fresh-context reviewer, the F-3 fix and the commit; nothing beyond that
RISK = Corrections were made after the fresh round and were not themselves reviewed in fresh context. Two exempt records remain uncorrected by design. Three claims in the previous emission of this record were false and are marked fail above rather than removed.
report_sha256 = 66a051965e1e5de402f7cce2da431d041c823fbde5a51bd2c04dc84e0db8d57c
```

Hash: UTF-8, LF, sin newline final, excluyendo la línea `report_sha256` —
la forma canónica de ADR-016, comprobada por `scripts/check_reports.py`
sobre este mismo archivo.

## Capa humana

Las seis mejoras se entregaron. Cuatro crearon norma con su ADR —021 a 024—,
una produjo un documento de evidencia sin autoridad normativa y la sexta
quedó como propuesta con criterio de entrada, bloqueada por un factor
externo. Una ronda adversarial independiente encontró un BLOCKER, siete HIGH
y siete MED reales; todos los BLOCKER y HIGH están cerrados y reverificados.

## Conciliación por tarea

- **T00/T01** — SPEC con REQ-M6-01..07, evidencia EV-M6-1..6 y tres preguntas
  abiertas; plan de nueve bloques que pasa el gate de planes.
- **T02 (P1)** — [`crosswalk-estandares.md`](../crosswalk-estandares.md): 29
  controles contra NIST SSDF v1.1 y OWASP LLM Top 10 2025, con las versiones
  leídas de la fuente. Hoy: 14 cubiertos, 8 parciales, 7 sin cubrir.
- **T03 (P5)** — ADR-021: clave `reading_path`, espina sumada y alternativas
  por su máximo. 923 de 1000 al medirla; 982 al cerrar el programa.
- **T04 (P2)** — ADR-022: `check_reports.py`. Su primera corrida encontró dos
  desviaciones reales en registros vigentes; la ronda fresca encontró tres
  defectos en el gate mismo.
- **T05 (P3)** — ADR-023: §6.8 del estándar, superficie de ejecución
  declarada, más el campo `Superficie:` del contrato de tarea, su alta en la
  lista cerrada de §4.3 y en `04` §7, y la checklist §7.
- **T06 (P4)** — ADR-024: complemento `06-componentes-con-llm.md` y campo
  `Presupuesto:`.
- **T07 (P6)** — [propuesta con criterio de entrada](../proposals/M6-piloto-fuera-del-monocultivo.md).
- **T08** — esta emisión.

## Ronda adversarial en contexto fresco

Ejecutada el 2026-09-08 por un revisor independiente, sin el contexto del
ejecutor, autorizado explícitamente por el humano. Decisión del revisor:
`fix-and-retry`. Estado de cada hallazgo tras las correcciones:

| # | Sev. | Hallazgo | Estado |
|---|---|---|---|
| 1 | BLOCKER | `reports.dir` absoluto producía traceback con rutas del host | **cerrado** — `_ruta_contenida`, reataque verificado |
| 2 | HIGH | capa técnica en fence liso no se comprobaba (fail-open) | **cerrado** — la capa se ancla en `report_sha256` |
| 3 | HIGH | registro trivial con fence de salida rechazado (falso positivo) | **cerrado** — mismo anclaje |
| 4 | HIGH | el registro decía F-3 abierto; el diff lo corregía | **cerrado** — declarado cerrado aquí |
| 5 | HIGH | la tabla resumen del crosswalk no cuadraba con sus filas | **cerrado** — recuento por script |
| 6 | HIGH | conteo de tests falso (160 declarados, 163 reales) | **cerrado** — cifras retiradas de los ADR |
| 7 | HIGH | §6.8 obligaba sin sitio donde cumplirse ni forma de comprobarlo | **cerrado** — campo, §4.3, `04` §7 y checklist |
| 8 | MED | test de lectura fallida pasaba por la razón equivocada | **cerrado** — parche selectivo y aserción concreta |
| 9 | MED | `test_hash_is_canonical_form` era un duplicado | **cerrado** — tres tests que rompen la forma |
| 10 | MED | 15 tests no corrían con el archivo suelto | **cerrado** — `__main__` al final |
| 11 | MED | `dir` relativo que escapa la raíz | **cerrado** — misma frontera que el BLOCKER |
| 12 | MED | evidencia declarada que no reproducía (ADR-024, EV-M6-2) | **cerrado** |
| 13 | MED | LLM03 marcado «no cubre» siendo parcial | **cerrado** |
| 14 | MED | la frontera con praxis-dev no abordaba la palabra «autoridad» | **cerrado** — lectura explícita en ADR-023 y PREGUNTA-M6-3 |
| 15 | LOW | claves opcionales sin procedencia normativa | **cerrado** — declarado como límite en ADR-022 |
| 16 | LOW | claves duplicadas: ganaba la última | **cerrado** — detección |
| 17 | LOW | `Produce` de T08 con la fecha equivocada | **cerrado** |
| 18 | LOW | el hash se excluía por prefijo, no por clave exacta | **cerrado** |

Dos verificaciones del revisor quedaron `inconclusive` por causa exógena a
él: no tenía red para comprobar las fuentes externas del crosswalk, y las
salidas RED son históricas y no reejecutables desde el árbol actual. Ambas
las había ejecutado el ejecutor y están en la evidencia de la primera
emisión.

## Reglas del método que no se cumplieron

Una. **Las correcciones de esta ronda no se revisaron en contexto fresco.**
`04` §5.3 dice que tras corregir un hallazgo se repite la ronda si el cambio
fue material, y estas correcciones lo son: tocan el gate copiable. Se
repitieron los checks afectados y se reatacaron los tres hallazgos
principales con sus comandos, pero por el mismo ejecutor. Queda como riesgo
declarado, no como cumplimiento.

## Seguimiento abierto

1. Segunda ronda fresca sobre las correcciones, si el humano la considera
   necesaria.
2. PREGUNTA-M6-3: precisar la línea de `no_ofrece` sobre «autoridad».
3. PREGUNTA-M6-2: adoptante para el piloto fuera del monocultivo.
4. Presupuesto de ruta de lectura en 982 de 1000: quedan 18 líneas.
5. Los dos registros exentos de `check_reports`.
