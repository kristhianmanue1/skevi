# ADR-034: el gate corre en CI remoto; el hook local queda como verificación rápida

Estado: aceptado (instrucción directa del Operador, 2026-09-17). Sustituye a
[ADR-001](ADR-001-gate-local-sin-ci.md). Implementado en
`.github/workflows/skevi-gate.yml`; el check requerido en `main` es una
operación de configuración separada que se registra al aplicarse.

Contexto: ADR-001 llevó el gate a un hook local porque la cuenta tenía
minutos de GitHub Actions limitados, y fijó su propia condición de revisión:
«si en el futuro cambian los límites de minutos de la cuenta, esta decisión
se reevalúa explícitamente con un ADR nuevo». `AUDIT-review-enforcement`
(O0, 2026-09-07) incluyó «cambio de cuota de CI» entre sus disparadores.
Observado el 2026-09-17: el repositorio es público (`gh repo view`), y la
documentación de GitHub declara gratuito el uso de runners estándar alojados
por GitHub en repositorios públicos. La premisa de ADR-001 no aplica hoy; no
se afirma que fuera falsa cuando se decidió. Sus consecuencias declaradas
seguían abiertas: un push sin `core.hooksPath` pierde el gate, `--no-verify`
lo omite y los PRs no muestran verificación.

Decisión: un workflow de GitHub Actions ejecuta en cada PR y push a `main` los
mismos comandos que `scripts/hooks/pre-push` —`check_sizes`, `check_plans`,
`check_reports` y `unittest`— con Python 3.9 y 3.12. El CI es el gate
autoritativo; el hook se conserva como verificación local rápida. Controles:
sólo `pull_request` (nunca `pull_request_target`), `permissions: contents:
read`, sin secretos, `persist-credentials: false`, acciones fijadas por SHA y
tiempo máximo acotado. Exigir el check en `main` y exigir fijación por SHA son
cambios de configuración con autoridad separada (estándar §4.3), aplicados
sólo tras un control positivo que demuestre que el check falla ante una
violación deliberada.

Alternativas descartadas:
  - Workflow informativo sin check requerido: deja abierto el mismo bypass que
    motivó el cambio; un gate que sólo advierte no es un gate (estándar §3.4).
  - Mantener ADR-001 con otra justificación: la razón escrita dejó de aplicar
    y no se identificó otra real.
  - Sólo el Python del runner: el hook local corre en 3.9 y ninguna fuente
    declaraba versión mínima; una sola versión no detecta la divergencia.

Consecuencias: 3.9 queda como versión mínima verificada de los scripts. Un
workflow roto bloquea merges una vez exigido el check (`enforce_admins`
activo); la reversión es quitar el check requerido y revertir el workflow. El
gate sigue comprobando forma, no verdad (`project-manifest.yaml`
§`no_ofrece`). No cambia la política de aprobaciones de `main` decidida en
`AUDIT-review-enforcement` (O0). Para adoptantes nada cambia: el estándar
§3.4 ya permite conectar el gate al CI o a un comando local; esta decisión es
propia del repositorio fuente. Si el repositorio deja de ser público o cambia
la política de facturación de GitHub, se reevalúa con un ADR nuevo.
