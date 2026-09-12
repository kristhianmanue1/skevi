# Dossier de publicación — ADR-028 y política de idioma

## Capa humana

El humano autorizó en conversación: «para skevi verifica si tenemos tree
limpio de lo contaro raliza commit, push, merge segun convenga para llear todo
main y dejar tree limpio y naliza release».

La publicación propuesta cubre todo lo acumulado desde `v1.1.0`, no sólo la
rama actual. Incluye M6 (presupuesto de lectura, gate de reportes, superficie
de ejecución, componentes con LLM y cotejo de estándares), sus refinamientos
ADR-025..027, ADR-028, la actualización documental de AN-KLA beta.28 y LANG.
Se recomienda `v1.2.0`: añade capacidades compatibles —versionado de scripts,
validación fail-closed y reglas normativas— sin retirar interfaces anteriores.
No hay un cambio incompatible que justifique una versión mayor.

Operaciones aceptadas en este folio: commits locales atómicos; push de
`fix/language-policy-and-validation`; PR hacia `main`; merge del PR sin
force-push; tag anotado `v1.2.0`; release GitHub desde ese tag. Se excluyen
borrado de ramas, force-push, migración de adoptantes y escritura de memoria.

Riesgos: los manifiestos mal formados fallan ahora de forma controlada; los
adoptantes no se actualizan automáticamente. Skevi declara fuera de alcance
la firma de releases. Si el PR no es mergeable o los checks fallan, se detiene
antes del merge. La reversión del código sería un nuevo `git revert` del merge;
el tag y la release quedan como historia publicada y no se reescriben.

## Capa técnica

```text
id = SKV-REL-20260912-01
date = 2026-09-12
time_utc = 13:32:15Z
head_sha = ffc72520be5ffc50142969f6dc2f614bddac598c
model = GPT-5 (self-declared)
STATE = PARTIAL (publication authorized; execution and final verification pending)
GATE = Publish every change since v1.1.0 to main, then release v1.2.0.
EVIDENCE
- Human instruction in current conversation -> commit, push, merge and release explicitly authorized -> pass
- git fetch origin; rev-parse origin/main -> 0c97249a9f7812e44356387f19135a177f692ff1 -> pass
- git log v1.1.0..HEAD -> 27 committed changes before local commits, including M6, ADR-025..028 and their fixes -> pass
- unittest discovery -> 230 tests passed -> pass
- Hidden regular file regression -> RED omitted .hidden-gate; GREEN rejects it as unlisted -> pass
- check_sizes after dossier -> 122 files; reading path 993/1000; gate/v3 -> pass
- check_plans -> 5 plans verified -> pass
- check_reports after dossier -> 7 technical reports verified; 2 exempt -> pass
- Fresh adversarial release review after fixes -> proceed; no open BLOCKER, HIGH or MED -> pass
- GitHub branch protection -> main protected; PR path available -> pass
- GitHub releases and remote tags -> v1.1.0 latest; v1.2.0 absent -> pass
PENDING = Atomic commits; push; PR; merge; post-merge gates; tag and GitHub release.
DECISION = proceed
RISK = Stricter manifest rejection is intentional; adopters are not migrated. Release signing remains outside Skevi scope.
report_sha256 = edf96dcb2902366a34049e81c2e3cb502e4f399d33e9d89fc8eeaa654cb38bdb
```

## Parada

Detener ante hallazgos BLOCKER/HIGH, cambios concurrentes, SHA remoto distinto,
PR no mergeable, gate rojo o tag `v1.2.0` ya existente. El cierre exige que
`main`, el tag y la release resuelvan al SHA de merge y que el árbol local
quede limpio.
