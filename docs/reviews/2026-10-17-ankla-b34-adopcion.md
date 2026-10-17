# Actualización AN-KLA b28 → b34 (plantilla beta.26 → beta.33)

## Contrato de tarea

TAREA SKV-ANKLA-B34. Clase Bounded: actualización de dependencia con efecto
en archivos del repositorio, por etiqueta exacta (`04` §7). Base:
`29c479c8b0314a8635cccf972a1759df0d0e14f6` (main). Objetivo: instalar
`an-kla-memory` 0.1.0b34 (tag `v0.1.0-beta.34`) en `.venv` y actualizar el
contexto gestionado por el flujo documentado de `AN-KLA.md`. Autorización:
instrucción directa del Operador en la sesión del 2026-10-17 («agrega y
verifica la nueva versión de an-kla»). No commit, no push, no PR.

El paquete b34 trae plantilla de contexto `0.1.0-beta.33` (versionado de
plantilla independiente del paquete). El drift `outside_managed_block`
reportado por el plan era la edición de `AGENTS.md` fuera del bloque ya
documentada en `2026-09-07-t05-adoption.md`; se absorbió a la nueva baseline
con `--confirm-target-drift`, cerrando la advertencia que arrastrábamos desde
el 2026-09-07.

## Cambio resultante

- `AGENTS.md`: 106 → 108 líneas (límite 200). Sólo el marcador begin del
  bloque gestionado y dos líneas nuevas dentro del bloque; nada fuera del
  bloque cambió.
- `AN-KLA.md`: 345 → 478 líneas (límite 800). Nueva «Referencia rápida para
  agentes», tabla de errores con reintento, `write-proposal-v2`, límites de
  `working-state-v2`, y documentación de `budget_too_small_for_resume_snapshot`
  — bloqueo real en este store, verificado antes y después del cambio.
- `.venv`: b28 → b34; store local intacto (revisión 37, verify OK), índice
  FTS5 reconstruido.

## Hallazgos de la ronda adversarial (contexto fresco, subagente)

- [MED] El contrato `skevi/an-kla-integration v1` (05 §6) exige que la
  activación absorba la lectura de `05` y `AN-KLA.md` en el presupuesto de
  ruta de lectura y lo declare en la config del gate; esa declaración no
  existe y este cambio agranda el costo no declarado (345 → 478 líneas).
  Impacto: la ruta declarada (998/1000) mide menos que la ruta obligatoria
  real para trabajo material. Disposición: **abierto como deuda del corpus**;
  predata este cambio (ya faltaba con beta.28), exige decisión propia del
  Operador (subir `reading_path.limit` con su ADR o dejar constancia de por
  qué no se absorbe) y no invalida este diff. Enlaza con el issue #63.
- Sin hallazgos BLOCKER/HIGH/LOW: los dieciséis comandos y flags de la
  referencia rápida existen en el CLI b34; los códigos de error citados
  tienen sitio de `raise` real en el paquete; `AN-KLA.md` regenerado es
  byte-idéntico a la plantilla canónica; el diff no contiene secretos; el
  resto del árbol está intacto.

## Capa técnica

```text
id = SKV-ANKLA-B34-20261017-01
date = 2026-10-17
time_utc = 13:07:55Z
head_sha = 29c479c8b0314a8635cccf972a1759df0d0e14f6
model = GLM-5.3 (self-declared)
STATE = PARTIAL
GATE = AN-KLA b34 upgrade applied by documented protocol; gates, suite and fresh adversarial round closed proceed.
EVIDENCE
- .venv pip install exact tag v0.1.0-beta.34 -> an-kla-memory 0.1.0b34 -> pass
- upgrade inspect --target v0.1.0-beta.34 -> plan_fingerprint c8fb2068, target_drift outside_managed_block true -> pass
- identity status -> complete, no adoption required -> pass
- upgrade apply --confirm-target-drift -> ok true, template 0.1.0-beta.33, drift absorbed into new baseline -> pass
- rebuild-index + context status -> diagnostics [] warnings [] runtime 0.1.0b34 -> pass
- resume --budget 4096 -> budget_too_small_for_resume_snapshot minimum_budget_bytes=5013 -> pass
- resume --budget 8192 -> full snapshot revision 37 returned -> pass
- python3 scripts/check_sizes.py -> OK 145 files, reading path 998/1000 -> pass
- python3 scripts/check_plans.py -> OK 5 planes E1-E5 -> pass
- python3 scripts/check_reports.py -> OK 12 reportes, 2 exentos -> pass
- python3 -m unittest discover -s tests -> Ran 266 tests OK -> pass
- adversarial round fresh-context subagent -> proceed; 1 MED justified-open -> pass
- AN-KLA.md vs package canonical template -> byte-identical, 23764 chars -> pass
- git status --short -> only AGENTS.md and AN-KLA.md modified -> pass
PENDING = commit and PR authorization; Operator decision on preexisting §6 absorption debt (AN-KLA.md now 478 lines outside reading_path).
DECISION = proceed
OPERATIONS = local edits only; commit, push, PR and merge await explicit per-operation authorization.
AUTHORITY = direct human instruction this session (add and verify new an-kla version); drift absorption matches the documented t05 edit.
RISK = reading path at 998/1000 leaves two lines of slack; next template growth turns the gate red.
report_sha256 = 632885b4fd8967bb9f15f072fc251651bb360b3abc82f4a42db01079dca4cf43
```

Hash: UTF-8, LF, sin newline final y sin la línea `report_sha256`.
Partido de PARTIAL, no de OK: el cambio está aplicado y verificado, pero su
commit/publicación exige autorización por operación, y la deuda §6 quedó
escalada al Operador. La revisión con contexto fresco cerró en `proceed`.
