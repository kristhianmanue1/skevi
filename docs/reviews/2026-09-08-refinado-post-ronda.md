# Registro de cierre — refinado tras la ronda sobre las recomendaciones

Plan: [R1-2026-09-08](../plans/2026-09-08-refinado-post-ronda.md).
Rama: `fix/refinado-post-ronda-m6`. Base: `b563279`.

> **Quinta emisión.** Cuatro rondas adversariales anteriores en esta misma
> rama encontraron ocho afirmaciones falsas, todas sobre el censo de
> adopción del ecosistema — nunca en el código, la norma o los ADR. Una
> quinta ronda encontró una novena. Decisión humana: **retirar los dos
> documentos de censo de este merge** en vez de pedirle a este mismo
> ejecutor que se corrija una vez más. Lo demás —tres gates, siete ADR
> (021–027), estándar, `AGENTS.md`— pasó la quinta ronda sin un solo
> hallazgo nuevo y se mergea.

## Capa técnica

```text
id = SKV-R1-20260908-04
date = 2026-09-08
time_utc = 15:25:57Z
head_sha = 81c9f5cd9ba8dc66b90eddb856411dc43a60c145
model = Claude Sonnet 5 (self-declared)
STATE = OK (normative work merges; ecosystem census withdrawn by human decision)
GATE = check_sizes, check_plans, check_reports and the suite green; fourth fresh round on the ecosystem docs found a ninth false claim, so those two documents are excluded from this merge instead of re-certified by this executor.
EVIDENCE
- python3 scripts/check_sizes.py -> OK, 113 text files, ruta de lectura 984/1000 -> pass
- python3 scripts/check_plans.py -> OK, 4 plans verified -> pass
- python3 scripts/check_reports.py -> OK, reports verified, 2 exempt -> pass
- python3 -m unittest discover -s tests -> Ran 194 tests, OK -> pass
- git diff --check -> no output -> pass
- Fourth fresh-context round on code, ADR-021..027, standard, AGENTS.md, manifest, crosswalk -> zero new findings after 5 consecutive rounds -> pass
- Same round on the two ecosystem documents -> two BLOCKER (unversioned cagf-dashboard workflow claimed as CI; adopter count 18 omitting emd, real count >=22) plus five HIGH -> fail
- cagf-dashboard workflow versioned -> git ls-files .github/ on that repo returns empty -> fail
- emd cites Skevi with formal .skevi installations -> 24 files, two .skevi directories confirmed -> fail
- Decision to withdraw rather than re-correct -> nine consecutive false claims across five rounds on the same failure mode -> pass
- ADR-026 and ADR-027 references to the withdrawn documents -> replaced with explicit withdrawal notes, no broken backtick paths remain -> pass
- Remaining cross-reference in docs/plans/2026-09-07-seis-mejoras.md (already on main, out of this branch) -> exempt from E5 by its own "crea" wording, unaffected -> pass
PENDING = Ecosystem adoption census (who adopts Skevi, with what CI, at what scale) remains open; to be redone with a repo list confirmed by the human, or by an executor other than this one. Second-emission drift-and-pilot documents recoverable from this branch's history if resumed.
DECISION = proceed (normative scope only)
OPERATIONS = commit on branch fix/refinado-post-ronda-m6; push, PR and merge to main authorised by the human for this scope
AUTHORITY = Human explicitly authorised push, PR and merge for the branch as scoped by this withdrawal; the ecosystem census was explicitly excluded from that authorisation
RISK = The withdrawn documents' correct claims (11 derivative gate copies, the four hash lineages, the 7 reproducible LOC figures, symlink closure) are also lost from the merged tree along with the false ones, since they lived in the same two files. Recoverable from git history on this branch, not re-published here.
report_sha256 = 8d42444ccf5d0c2a7d73cf653564792b62153713ff0d5ec9be97a18657b9dc9e
```

Hash: UTF-8, LF, sin newline final, excluyendo la línea `report_sha256`.

## Capa humana

Cinco refinamientos del programa M6 original, más el trabajo de esta rama:
ADR-021 (presupuesto de lectura), ADR-022 (gate de reportes), ADR-023
(superficie de ejecución), ADR-024 (componentes con LLM), ADR-025 (el
presupuesto es trinquete, no techo derivado), ADR-026 (frontera de
autoridad y alcance de artefacto) y ADR-027 (identidad y autocaducidad del
gate copiable). Cuatro gates de código: `check_sizes.py`, `check_plans.py`
y `check_reports.py` con fronteras de symlink cerradas en los tres.

## Por qué se retira en vez de corregirse

El patrón, con evidencia:

| Ronda | Hallazgo sobre el ecosistema |
|---|---|
| 1 | Contar `.venv/` y `build/` como código de producción |
| 2 | Buscar adoptantes sólo en `project-manifest.yaml` |
| 3 | «Ninguno califica» — población incompleta |
| 3 | Cifras de LOC infladas hasta 2,6× |
| 4 | Partición de copias falsa (nueve/dos → siete/dos/dos bifurcadas) |
| 4 | Membresía de «once copias» incluía `escrubery` (script propio) |
| 5 (self) | `agora` cita Skevi en 16 archivos, no 5 |
| 6 | `cagf-dashboard` «corre el gate en CI» — workflow no versionado |
| 6 | «18 repos citan Skevi» — son al menos 22, falta `emd` |

Nueve emisiones falsas sobre el mismo tipo de afirmación, corregidas una a
una durante cinco rondas, sin que el proceso las contuviera. El código y la
norma no comparten ese patrón: la quinta ronda los atacó explícitamente por
mutación y coherencia cruzada y no encontró nada. La distinción no es
casualidad — es evidencia de que el problema es específico de censar el
ecosistema, no del método de verificación en general.

## Qué se pierde con el retiro

Los dos documentos también contenían afirmaciones correctas y verificadas:
las 11 copias derivadas del gate con su lista nominal, las cuatro huellas y
su linaje exacto, las 7 cifras de LOC reproducibles con el comando
publicado, y el cierre de las cuatro formas de escape por symlink. Se
pierden del árbol mergeado junto con lo falso, porque vivían en los mismos
archivos. Quedan recuperables del historial de esta rama.

## Seguimiento abierto

1. Rehacer el censo de adopción, con una lista de repos confirmada por el
   humano o por un ejecutor distinto de éste.
2. `entiendomidiabetes` tiene el mismo defecto que `cagf-dashboard` —workflow
   no versionado— y decidía parte del veredicto de un piloto que ya no está
   en el árbol; se hereda como antecedente para el censo futuro.
3. La pieza 2 del método de aviso de versión —extender el manifiesto de
   ADR-020 a `scripts/`— sigue pendiente, sin depender de los documentos
   retirados.
