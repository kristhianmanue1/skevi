# CC-EG-SK-001 — Contrato de coordinación expertoGobernanza ↔ Skopos

**Estado: `proposed`** — candidato v0.1.0 bajo el perfil mínimo S
(0.5.0-S.1) del contrato de coordinación PROP-014. Preparado en skevi
por orden del Operador (2026-11-09); sin encendido no obliga.

```yaml
coordination_contract:
  id: CC-EG-SK-001
  version: "0.1.0"
  status: proposed
  profile: skevi/PROP-014-S@0.5.0-S.1
  state_home_ref: PENDING   # bloqueante para agreed (§10/S3)
  time_source: PENDING      # bloqueante para agreed (precondición §10)
  participants:
    provider_project: skopos          # /Users/krisnova/www/aria/skopos
    consumer_project: expertoGobernanza  # /Users/krisnova/www/expertoGobernanza
  scope:
    objective: "Renovar el bloque bilateral IMSS (custodia + derivados)
      vencido el 2026-11-08 y formalizar las aceptaciones pendientes,
      como primer vuelo real del contrato de coordinación."
    references:
      interface_agreements: [IA-001, IA-002, IA-003, IA-004]
      work_orders: [WO-SK-001, WO-EG-001]
  authority:
    tier_1_standing: "Commits y gestión de ramas locales propias en
      cada repo; nada cruza fronteras (A2/P1)."
    tier_2_attribution: "Push y merge según el canon local de cada
      participante (A4/S4): en skevi, dossier y folio (Z2); en las
      partes, sus propios gates. Merge a la línea principal: su capitán,
      con gates locales en verde y ronda 'proceed'."
    tier_3_operator: "Publication/release de cualquiera de los dos
      repos; ampliación de alcance; aceptación de riesgo material."
    coordinator_designation:
      agent_ref: skevi-session-2026-11-09
      scope: "Preparación de candidatos y registro; sin autoridad sobre
        recursos de las partes."
      authorization_ref: "docs/reviews/2026-11-09-piloto-eg-skopos-ronda.md (orden del Operador 2026-11-09 registrada con hash)"
      note: CANDIDATO — cada capitán registra su designación al encender
    controller_designation:
      implementation_ref: "Script mínimo sobre events.jsonl (S3):
        validación prior_state (L5), presupuestos (L6/E3), piso de tier"
      authorization_ref: "docs/reviews/2026-11-09-piloto-eg-skopos-ronda.md (misma orden registrada; una sola aprobación puede designar a ambos — A5)"
      note: CANDIDATO
  negotiation_budget: {unit: rounds, limit: 3}
  escalation_policy:
    unresolved_contract_conflict: human_operator
    unauthorized_action: stop
    newly_discovered_material_risk: stop_and_escalate
  verification_policy:
    required: [provider_receipt_hashes, consumer_contract_revisions,
               bilateral_evidence_links]
    evidence: [policy_sha256, command_outputs, exit_codes, findings]
    status_on_missing_evidence: inconclusive
    adversarial_review: risk_proportionate   # piso: High (§7.2 — toca
                                             # contratos compartidos)
    review_decisions: [proceed, fix_and_retry, escalate]
```

## Hogar del estado (designado 2026-11-09)

**`aria/coordination`** (repo dedicado) es el hogar canónico, designado
por el Operador al aceptar la opción recomendada junto al lote
SKV-LOTE-20261109-02. La copia canónica del CC (v0.2.0, con
`state_home_ref` y `time_source` llenos), los WOs, el IA-REGISTRO y el
registro de eventos viven allí, con el controller mínimo (S3) ya
operativo; este directorio de skevi queda como borrador de origen y
señalética.
