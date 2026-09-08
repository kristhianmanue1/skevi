# Aterrizaje PROP-008 (D3) y propuesta T06 — contrato y evidencia

## Contexto de la sesión

Tarea doble en la rama `docs/adopt-authority-consistency`, base
`42156e40be4832d601ca20df6eca958c695e58e2`. (1) Con la aprobación
humana de D1/D2 de PROP-008 (2026-09-07, en conversación), aterrizaje
D3: contrato `skevi/an-kla-integration v1` en `05` §6, regla de
upgrades en `04` §7, ADR-019 e índice, PROP-008 trasladada a
`docs/history/` con cabecera ADOPTADA, registro de decisión con
piloto K1-K4. (2) T06 pasos 1-2: inspección read-only de la
protección de `main` y propuesta
[AUDIT-review-enforcement](../proposals/AUDIT-review-enforcement.md)
(O0-O4, en deliberación). Ronda adversarial fresca (subagente
independiente): `fix-and-retry` — tres MED corregidos (plan T08/T13/R4
actualizado con ediciones compensadas, remisión a este reporte,
«PR de adopción» sustituido por «cambio de adopción») y tres LOW
atendidos (K2 reformulado, término unificado en `04`, variante de
formato declarada en `05` §6). Sin commit: la autorización de
commit/push se pide aparte, por operación.

```text
id = SKV-T06-PROP008-20260907-01
date = 2026-09-07
time_utc = 19:22:00Z
head_sha = 42156e40be4832d601ca20df6eca958c695e58e2
model = GLM (self-declared)
STATE = PARCIAL
GATE = D3 landing and T06 steps 1-2 verified with gates and fresh adversarial round; T06 step 3 awaits human decision; no commit/push authorization yet
EVIDENCE
- D1/D2 approval -> human instruction in conversation, 2026-09-07 -> pass
- grep -rn -i an-kla (AGENTS + standard + guide 00-04) -> only AGENTS.md managed block, lines 94-104 -> pass
- grep -n an-kla-integration docs/ai-agent-guide/05-memoria-del-agente.md -> lines 67 and 74 -> pass
- python3 -B scripts/check_sizes.py -> OK, 81 text files within limits -> pass
- python3 -B scripts/check_plans.py -> OK, 2 plans verified -> pass
- python3 -B -m unittest discover -s tests -> 73 tests OK -> pass
- wc -l docs/plans/2026-09-07-mejoras-auditoria.md -> 300 lines, limit <=300 -> pass
- fresh adversarial round -> fix-and-retry; 3 MED fixed, 3 LOW addressed -> pass
- git ls-remote origin refs/heads/main -> 17413f150d08e1e65b72f70a858104505950e751 unchanged -> pass
- gh api repos/kristhianmanue1/skevi/branches/main/protection (read-only) -> PR required, 0 approvals, enforce_admins true, no checks/signatures -> pass
PENDING = T06 step 3 human decision (O0-O4 of AUDIT-review-enforcement); commit/push/PR authorization; T08 continues on the landed contract
DECISION = proceed to publication-ready state; no commit, push or PR before explicit authorization
OPERATIONS = local edits only; no external operations executed this session
AUTHORITY = human D1/D2 approval (2026-09-07, conversation); no Git external authority claimed
RISK = normative interface change for adopters; conditional activation limits blast radius; local an-kla-memory package 0.1.0b17 vs repo beta.24 upgrade still requires separate authorization
report_sha256 = b80b2b883948f26d2774c5728064f65706fb273c6de8af140b35a22b3b8ff6ed
```

Hash: UTF-8, LF, sin newline final y sin la línea `report_sha256`,
calculado sobre el bloque técnico en forma canónica. Emisión previa al
commit: resultados posteriores se añaden sin reescribirla.

Esfuerzo observado: una sesión; sin dependencias nuevas ni coste de
infraestructura. El gate de tamaños no verifica el contrato de
integración: su frontera es forma/tamaño; la verificación es el
preflight comandado (05 §6).

Posterior a la emisión del bloque: el humano aceptó O0 de
[AUDIT-review-enforcement](../proposals/AUDIT-review-enforcement.md)
(2026-09-07, en conversación); T06 queda cerrado sin cambiar
configuración de GitHub, y se autorizó commit y push de este cambio.
