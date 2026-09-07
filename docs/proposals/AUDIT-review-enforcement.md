# AUDIT-review-enforcement — Revisión exigible en GitHub frente al gate local

> **Estado:** RESUELTA — O0 aceptada por el humano (2026-09-07, en
> conversación): el statu quo queda documentado como excepción
> compensada y no se modifica ninguna configuración de GitHub. Las
> secciones 1-3 registran la evidencia y el análisis que sustentan la
> decisión; §3 fija los disparadores de reevaluación.
> **Origen:** plan AUDIT-2026-09-07, tarea T06 (REQ-AUD-06). Base
> normativa: ADR-001 y ADR-018. Evidencia remota de sólo lectura
> obtenida el 2026-09-07 (§1); ningún ajuste fue modificado.

## Contexto

ADR-001 movió el gate de estructura y tamaños a un hook local de Git:
no hay checks de CI en GitHub. Sus consecuencias declaradas — un push
sin hook instalado pierde el gate, y no hay verificación visible en
la interfaz de PRs — se compensan hoy con dos capas que GitHub no
verifica: la política de autoridad por operación (AGENTS.md; ADR-018)
y la práctica de revisión fresca en contexto distinto del ejecutor
(`04` §5.1). La pregunta de T06: ¿debe GitHub exigir revisión humana
en `main`, y qué parte de la excepción local queda declarada como tal?

## 1. Configuración remota vigente (sólo lectura, 2026-09-07)

Observado con `gh api repos/kristhianmanue1/skevi/...`; `main` en
`17413f150d08e1e65b72f70a858104505950e751` (verificado por
`git ls-remote` en la misma sesión):

| Ajuste | Valor observado |
|---|---|
| `protected` | true |
| `required_pull_request_reviews` | presente: PR requerido para fusionar |
| `required_approving_review_count` | 0 |
| `dismiss_stale_reviews` | false |
| `require_code_owner_reviews` | false (repo sin CODEOWNERS) |
| `require_last_push_approval` | false |
| `enforce_admins` | true — el admin tampoco bypasea |
| `required_status_checks` | ninguno (coherente con ADR-001) |
| `required_signatures` | false; commits recientes sin firmar (`%G?` = N) |
| `required_linear_history` | false; `main` tiene merge commits (#32, #33, por `git log`) |
| `required_conversation_resolution` | false |
| `allow_force_pushes` / `allow_deletions` | false / false |
| rulesets | ninguno |
| colaboradores | uno: kristhianmanue1 (admin) |

Lectura conjunta: GitHub exige PR para fusionar, pero con cero
aprobaciones exigidas. Ninguna revisión es verificada por la
plataforma; la protección remota efectiva se reduce a PR obligatorio,
no force-push y no borrado.

## 2. Revisión exigida vs excepción compensada local

La excepción de ADR-001 cubre contenido (gate local), no proceso
(revisión). El hueco exacto: fusionar un PR sin aprobación alguna es
válido para GitHub; sólo la política escrita lo impide. Opciones,
cada una con riesgo y coste:

- **O0 — statu quo documentado como excepción compensada.** Registrar
  aquí la excepción: gate local + política AGENTS + revisión fresca
  documentada (precedente T05-A). Coste: cero. Riesgo: el admin puede
  fusionar sin revisión; la compensación es procedural, no técnica.
  Evidencia: ADR-001 (consecuencias), ADR-018 (exigencia humana
  local), cierre T05-A (práctica de revisión fresca).
- **O1 — exigir 1 aprobación.** Inaplicable hoy: el único colaborador
  es el admin (§1) y `enforce_admins` le aplica; nadie más puede
  aprobar. Exigiría una segunda cuenta humana. Coste: alto. Riesgo:
  bloquea el flujo vigente de rama → PR → merge.
- **O2 — refuerzos que dependen de aprobaciones**
  (`dismiss_stale_reviews`, `require_last_push_approval`): sin
  `count >= 1` carecen de efecto. Mismo bloqueo que O1.
- **O3 — exigir firmas** (`required_signatures`): los commits de la
  práctica actual no están firmados (§1); activarlo rompe el push
  hasta configurar firma en cada entorno. Protege integridad, no
  revisión. Coste: medio.
- **O4 — `required_conversation_resolution` y/o
  `required_linear_history`:** baratos de activar; el segundo obliga a
  squash/rebase y rompe el patrón de merge commits vigente. Ninguno
  exige revisión. Coste: bajo/medio; valor: bajo para este hueco.

## 3. Recomendación y criterios de decisión

O0: es lo más simple, lo más reversible y no añade superficie (§8 del
estándar); exigir revisión sin un segundo revisor real añade bloqueo
sin garantía. Disparadores de reevaluación: segundo colaborador,
cambio de cuota de CI o decisión de firmar commits. No se añade
ningún workflow de Actions por omisión (ADR-001).

## Adopción

**Decisión registrada:** O0 aceptada por el humano en conversación
(2026-09-07). No se configura nada en GitHub; la excepción queda
documentada en §1-§3, con los disparadores de reevaluación allí
fijados. El cambio de configuración de GitHub seguiría siendo
operación con autoridad separada si un disparador la activa.
