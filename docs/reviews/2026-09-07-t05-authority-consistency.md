# Registro y dossier — T05, coherencia de autoridad

Plan: [AUDIT-2026-09-07](../plans/2026-09-07-mejoras-auditoria.md).
Contrato y candidatos: [propuesta T05](../proposals/AUDIT-authority-consistency.md).

## Capa técnica

```text
id = SKV-T05-20260907-01
date = 2026-09-07
time_utc = 19:06:21Z
head_sha = 41d40d9a4e1a521e97810b4124e19e7e8431547f
model = Codex (self-declared)
STATE = PARTIAL (proposal prepared; D1 not selected)
GATE = T05 preparation only; no normative adoption.
EVIDENCE
- Authority matrix -> M1-M8 tied to current local sources -> pass
- Candidate scope -> A1-A5 only proposed, normative files unchanged -> pass
- Fresh review -> MED A1 fallback omitted existing AGENTS without hierarchy; corrected with case C9 -> addressed
- Local gates before this record -> 75 text files and 2 plans OK -> pass
- git diff --check -> no output -> pass
- Remote -> target branch absent; base branch at head_sha; main at 17413f150d08e1e65b72f70a858104505950e751 -> pass
- PROP-008 -> f4a478fab5ad6bc0187a358fa8aeb7c87281af448f20f02169c15683dd95b721 unchanged and excluded -> pass
PENDING = Review correction, final artifact gates, authorized commit/push, and human D1.
DECISION = proceed with preparation; publication conditional on final review and gates; no policy adoption
OPERATIONS = Commit proposal, plan and this record; push without force to origin refs/heads/docs/audit-authority-consistency.
AUTHORITY = User authorized commit/push at agent discretion and continuation; no merge, PR, tag or release.
RISK = Publication may be mistaken for ratification; proposal and plan explicitly keep D1 pending.
report_sha256 = e2db6ae1dca36c14866c2a65b3af93e1e96286e9db3f5e5c116861e3b4071506
```

Hash: UTF-8, LF, sin newline final, excluyendo la línea report_sha256.
Registro previo a publicación: sus pendientes no afirman operaciones realizadas.

## Resultado y revisión

Preparados matriz M1-M8, alternativas A/B/C, cinco textos candidatos y nueve
casos documentales. Se recomienda A: remitir la política general al estándar
y explicitar la restricción humana local, sin habilitar delegación en Skevi.

La revisión fresca de /root/review_t05 encontró un MED: A1 omitía AGENTS
existente sin jerarquía declarada en el fallback. Se corrigió preservando su
prioridad y se añadió C9. No hubo BLOCKER/HIGH. La revisión es de contexto
separado; no se atribuye independencia de modelo. La confirmación de la
corrección y los gates del artefacto final preceden al commit.

No se editaron norma, guía, AGENTS, manifest, ADR ni código. RED no aplica a
esta preparación documental. AN-KLA context status y verify resultaron OK,
revisión 19, con el intérprete .venv. No se escribió memoria.

T05 conserva abierto su paso 3: el aceptante elige alternativa antes de una
tarea separada de adopción. Publicar el borrador no cumple ese paso.

## Autoridad y operaciones concretas

Instrucción vigente: «tienes autorizado commit y push segun creas correponda
adelante con siguietne»; retoma: «adelante». El agente concreta la publicación
documental dentro de ese alcance, sin atribuir aprobación de D1 al humano.

Commit acotado a tres archivos: propuesta T05, plan y este registro.
Push normal a origin, refs/heads/docs/audit-authority-consistency, desde la
base 41d40d9. No force, merge, PR, tags, release ni cambios de configuración.
La rama es derivada de fix/audit-gate-read-errors; contiene sus correcciones
previas y no pretende una integración independiente en main.

Verificación remota previa: rama destino ausente, rama base en 41d40d9 y main
en 17413f1. Tras publicar: comparar HEAD con la referencia remota exacta y
comprobar el árbol. PROP-008 permanece sin rastrear, intacta y fuera del commit.
Si el push normal rechaza una actualización concurrente, detener e inspeccionar.

## Evidencia final antes del commit

Revisión afectada: SKV-T05-REVIEW-20260907T190616Z, decisión proceed;
MED A1 cerrado, sin hallazgos restantes. D1 sigue pendiente.
Gates finales: check_sizes OK, 76 archivos; check_plans OK, 2 planes.
Plan: 291 líneas; propuesta: 205. git diff --check sin salida.
Estos resultados posteriores completan los pendientes técnicos de la emisión;
no cambian su hash ni convierten el dictamen en aceptación de política.
