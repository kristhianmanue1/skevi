# WO-SK-001 — Renovar las políticas de custodia y derivados (proveedor)

**Estado: `proposed`** — se registra al encender el CC. Proyecto:
**Skopos** (capitán: agente de Skopos). Perfil S.

```yaml
work_order:
  id: WO-SK-001
  version: "0.1.0"
  status: proposed
  project: skopos
  owner: <capitan-de-skopos>
  objective: "Renovar las políticas vencidas del bloque IMSS —custodia
    de ambos manuales y derivados del 2000-002-001— con nueva vigencia
    acotada, sin ampliar alcance, y entregar los hashes de las políticas
    nuevas como evidencia."
  allowed_scope:
    - runs/pdf-document-imss-pilot-v1/   # política custodia 2000-002-001
    - runs/pdf-imss-0500-pilot-v1/       # política custodia 0500-002-001
    - runs/pdf-document-imss-pilot-v1/derivatives  # política de derivados
  excluded_scope:
    - cualquier archivo de expertoGobernanza   # A2/P1: nadie cruza
  references: [{implements: IA-001@nueva}]     # lo produce este WO
  dependencies: [{approval: section-10-ignition}]
  acceptance:
    - "describe_capabilities anuncia policy_sha256 nuevos y vigencia
       futura (recomendado: 2027-05-08T00:00:00Z, seis meses) —
       procedimiento: describe_capabilities por host y cotejo del hash"
    - "política de derivados renovada con su propio hash — procedimiento:
       digest del archivo de política nuevo vs el anunciado"
    - "el vencimiento viejo NO se extiende editándolo: política nueva
       versionada, la vieja expira y queda como historia — procedimiento:
       git log del archivo de política"
    - "recibos de una corrida bilateral por manual con la política nueva
       — procedimiento: corrida documentada en docs/evidencia/ de EG"
  permissions: {commit: agent/wo-sk-001, push: null}   # push por folio
                                                       # del canon local
  authorization_ref: <cc-eg-sk-001-authority-block>
  correction_budget: {unit: correction_cycles, limit: 2}
```

Notas: la renovación es un acto acotado del proveedor («el retiro o
renovación exige revisión explícita» — sus propios contratos). No
cambia modalidades, páginas ni límites: sólo vigencia. La evidencia
(recibos, hashes) se enlaza al registro de eventos del CC.
