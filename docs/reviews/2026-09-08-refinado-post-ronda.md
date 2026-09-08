# Registro de cierre — refinado tras la ronda sobre las recomendaciones

Plan: [R1-2026-09-08](../plans/2026-09-08-refinado-post-ronda.md).
Rama: `fix/refinado-post-ronda-m6`. Base: `b563279`.

## Capa técnica

```text
id = SKV-R1-20260908-02
date = 2026-09-08
time_utc = 09:35:19Z
head_sha = 52bca34ce11e02d158c1e0838edf24f8b097dab4
model = Claude Opus 5 (self-declared)
STATE = PARTIAL (second fresh round closed one BLOCKER and four HIGH; its own corrections are unreviewed)
GATE = Plan R1 closed except R-T2 step 2; second fresh-context round executed, all its findings closed.
EVIDENCE
- python3 scripts/check_sizes.py -> OK, 113 text files, ruta de lectura 984/1000 -> pass
- python3 scripts/check_plans.py -> OK, 4 plans verified -> pass
- python3 scripts/check_reports.py -> OK, reports verified, 2 exempt -> pass
- python3 -m unittest discover -s tests -> Ran 182 tests, OK -> pass
- BLOCKER pilot verdict was false -> eduEMD ran both gates green on 2026-09-06 with a copy byte-identical to v1.0.0 -> fail
- Production line counts in the first table -> inflated by counting .venv, build and references; epistates 8562 not 22704 -> fail
- escrubery characterised as having real remote CI -> its ci.yml is workflow_dispatch only, billing exhausted -> fail
- ADR-026 prose contradicted its own evidence table and decision -> fail
- Crosswalk still carried six cells reading owner-nobody after ADR-026 declared them out of scope -> fail
- check_plans and check_reports followed symlinks out of the root -> reproduced, then filtered -> pass
- Re-attack of symlink escape after fix -> content outside the root never reaches stdout -> pass
- Previous emission claimed 111 files at commit 37f6b13 -> the real count there is 112 -> fail
- Long prose line of 262 columns introduced while closing one of 126 -> fail
- Ecosystem sweep for adopters -> 18 repositories cite Skevi; 11 carry a copied gate; none current -> pass
- Copies at 380 lines -> byte-identical to each other and to Skevi commit 7bfd759c of 2026-08-20 -> pass
- Stale gate on an unreadable file -> OK exit 0; current gate on the same fixture -> BLOQ exit 1 -> pass
PENDING = Corrections to this round are themselves unreviewed; R-T2 step 2 open; gate drift proposal undecided; push, PR and merge unauthorised.
DECISION = escalate
OPERATIONS = commits on branch fix/refinado-post-ronda-m6; no push, merge, PR, tag or release
AUTHORITY = Human authorised the refined recommendations, the pending items and both fresh reviewers; nothing beyond that
RISK = Five consecutive emissions of the same failure mode: measuring the wrong population or the wrong artefact and stating the conclusion as verified. Gates and tests passed on every one of them. The mode is not contained by the current process.
report_sha256 = 60ca4d6ad9f4035f86610c1c5032ac5fe45ada775726bec394a6a7e8dcac4236
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
