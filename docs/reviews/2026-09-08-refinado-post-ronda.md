# Registro de cierre — refinado tras la ronda sobre las recomendaciones

Plan: [R1-2026-09-08](../plans/2026-09-08-refinado-post-ronda.md).
Rama: `fix/refinado-post-ronda-m6`. Base: `b563279`.

## Capa técnica

```text
id = SKV-R1-20260908-01
date = 2026-09-08
time_utc = 04:40:29Z
head_sha = b563279791c37041f47ef998c075596d17fdd1ef
model = Claude Opus 5 (self-declared)
STATE = OK (five refinements applied; fresh-context round executed by file, all findings closed)
GATE = Plan R1 R-T1..R-T6 closed with evidence, except R-T2 step 2 which is explicitly marked unmet.
EVIDENCE
- python3 scripts/check_sizes.py -> OK, 111 text files, ruta de lectura 984/1000 -> pass
- python3 scripts/check_plans.py -> OK, 4 plans verified -> pass
- python3 scripts/check_reports.py -> OK, reports verified, 2 exempt -> pass
- python3 -m unittest discover -s tests -> Ran 180 tests, OK -> pass
- git diff --check -> no output -> pass
- Fresh reviewer verified 9 prior closures by file, not by commit range -> 8 closed, 1 closed only halfway -> pass
- BLOCKER check_plans plans key unvalidated -> reproduced as traceback leaking host paths, then fixed -> pass
- Re-attack with absolute and with ../ escape -> controlled BLOQ both, no host paths -> pass
- HIGH ADR-025 broke its own rule 4 -> it quoted live occupancy figures including one already stale -> fail
- HIGH norm delegated occupancy to a gate that never printed it -> gate now prints it on the OK line -> pass
- HIGH non-reciprocity claim was inverted -> escrubery and an-kla-memory adopt Skevi by ADR; the latter installs skevi-gate.json -> fail
- HIGH SECURITY.md claimed no releases -> git ls-remote --tags origin returns v1.0.0 and v1.1.0 -> fail
- Occupancy after all changes -> 984 of 1000, up from 982 at base -> fail
- Long prose lines outside table rows in touched files -> none remain -> pass
- Occupancy figures copied into normative documents -> none remain -> pass
PENDING = Corrections made after this round were not themselves reviewed in fresh context; R-T2 step 2 unmet and left open; PREGUNTA-M6-2 external pilot; push, PR and merge unauthorised for this change.
DECISION = proceed
OPERATIONS = commit on branch fix/refinado-post-ronda-m6; no push, merge, PR, tag or release
AUTHORITY = Human authorised the refined recommendations and the fresh reviewer; the M6 authorisation for push, PR and merge does not extend to this change (04 section 7)
RISK = Three of the four HIGH findings were false statements written by this executor into normative documents, and one inverted the meaning of its own evidence by measuring the wrong artefact. The same failure mode may persist in claims this round did not test.
report_sha256 = 088095e56f9711f3d8ee99572514161a97af0967c52789e638c554274bfbcc0a
```

Hash: UTF-8, LF, sin newline final, excluyendo la línea `report_sha256`.

## Capa humana

Cinco refinamientos aplicados sobre el seguimiento abierto del programa M6.
La ronda fresca esta vez tuvo dos encargos: verificar los cierres del programa
anterior —por archivo y por hallazgo, porque el rango de commits que yo había
propuesto no aislaba nada— y revisar el cambio nuevo. Encontró un BLOCKER,
cuatro HIGH, cuatro MED y dos LOW. Todos cerrados.

## Conciliación por tarea

- **R-T1** — ADR-025. Se pidió derivar el techo del presupuesto de lectura y
  no se derivó: **no existe derivación honesta** desde este repositorio, porque
  la ventana útil depende del modelo, del trabajo en curso y de la herramienta.
  Se declara lo que el límite realmente es —un trinquete sobre lo observado— y
  se fija su asimetría: subirlo exige ADR con razón escrita, bajarlo tras
  comprimir no. El techo sigue en 1000.
- **R-T2** — `AGENTS.md` pasa de reenunciar cuatro reglas transversales a
  citarlas. **Su segundo step no se cumplió** y está marcado así en el plan: la
  ruta sube de 982 a 984, porque la política que R-T1 añade al §3.4 cuesta más
  de lo que la compresión libera. Forzar el número comprimiendo más habría sido
  degradar texto por una cifra.
- **R-T3** — ADR-026. Precisa la línea de autoridad de `no_ofrece` a
  gobernanza, declara fuera de alcance la integridad de artefactos y los
  riesgos de modelo, y registra que ningún manifiesto reciproca la cesión.
- **R-T4** — `.github/SECURITY.md`, no en la raíz, donde el gate lo rechaza.
  RV.1 pasa de «no cubre» a «parcial»: hay canal, no hay vigilancia continua.
- **R-T5** — la exención de ADR-022 no caduca, y se retira el disparador de
  archivado que yo había inventado.
- **R-T6** — esta emisión.

## Ronda adversarial en contexto fresco

| # | Sev. | Hallazgo | Estado |
|---|---|---|---|
| 1 | BLOCKER | `check_plans.py` no validaba la clave `plans`: leía fuera de la raíz y volcaba rutas del host | **cerrado** — `_dir_contenido` y `relative_to` protegido |
| 2 | HIGH | ADR-025 violaba su propia regla 4 citando ocupaciones vivas, una ya obsoleta | **cerrado** — cifras retiradas, regla precisada |
| 3 | HIGH | la norma delegaba la ocupación a un gate que no la emitía al pasar | **cerrado** — el gate la publica en su línea OK |
| 4 | HIGH | la evidencia de no-reciprocidad estaba invertida | **cerrado** — ver abajo |
| 5 | HIGH | `SECURITY.md` afirmaba que no hay releases; hay dos tags | **cerrado** |
| 6 | MED | frase residual contradictoria en el cotejo | **cerrado** |
| 7 | MED | `SECURITY.md` decía tres scripts; son cuatro | **cerrado** |
| 8 | MED | el step de R-T2 declaraba una verificación que no se cumple | **cerrado** — marcado no cumplido |
| 9 | MED | editar ADR-022 rozaba la inmutabilidad de `02` §3.2 | **cerrado** — declarado aclaración de alcance |
| 10 | LOW | el Estado de ADR-021 usaba un valor fuera del vocabulario | **cerrado** |
| 11 | LOW | línea de 126 columnas en prosa | **cerrado** |

El revisor también verificó los nueve cierres del programa M6: ocho cerrados
de verdad —comprobados por mutación del código, no por lectura— y uno cerrado
a medias, que resultó ser el BLOCKER de arriba.

## El hallazgo que importa

El HIGH-4 no fue un descuido de redacción: **medí el artefacto equivocado y
concluí lo contrario de la verdad**. Comprobé `project-manifest.yaml` en los
cinco proyectos y escribí «ninguno menciona a Skevi». Dos lo adoptan
formalmente —`escrubery` con su ADR-0001, `an-kla-memory` con su ADR-0045 y su
propio `skevi-gate.json`— y uno cita una versión etiquetada. La afirmación
correcta es la estrecha: ningún **manifiesto** reciproca la cesión. La que
escribí decía que nadie depende de Skevi, cuando hay adoptantes reales.

Tres de los cuatro HIGH fueron afirmaciones falsas escritas por mí dentro de
documentos normativos nuevos, en el mismo programa cuyo propósito era que las
reglas se verificaran por comando y no por autorreporte. Los cuatro gates y
los 180 tests pasaban con las cuatro afirmaciones falsas dentro.

## Reglas del método que no se cumplieron

Una, la misma que en la emisión anterior: **las correcciones de esta ronda no
se revisaron en contexto fresco**. Se repitieron los checks y se reatacaron el
BLOCKER y los cuatro HIGH con sus comandos, pero por el mismo ejecutor. El
riesgo está declarado en la capa técnica, no compensado.

## Seguimiento abierto

1. Ronda fresca sobre estas correcciones, si se considera necesaria.
2. R-T2 step 2: la ruta de lectura subió en vez de bajar; queda en 984 de 1000.
3. PREGUNTA-M6-2: adoptante para el piloto fuera del monocultivo — con el
   matiz de que ya hay dos adoptantes reales del método, aunque ninguno rompe
   dos variables del monocultivo a la vez.
4. `push`, PR y merge de este cambio: sin autorizar.
