# WO-EG-001 — Aceptación formal y revisiones v0.3 (consumidor)

**Estado: `proposed`** — se registra al encender el CC. Proyecto:
**expertoGobernanza** (capitán: agente de expertoGobernanza). Perfil S.

```yaml
work_order:
  id: WO-EG-001
  version: "0.1.0"
  status: proposed
  project: expertoGobernanza
  owner: <capitan-de-expertoGobernanza>
  objective: "Formalizar lo pendiente del bloque bilateral: (a) la
    aceptación formal de skopos-document-derivatives v0.1 que quedó en
    propuesta desde el 8-oct; (b) las revisiones contractuales v0.3 de
    custodia y funciones locales enlazando la política nueva de
    WO-SK-001."
  allowed_scope:
    - docs/contratos/          # revisiones v0.3 y estado de aceptación
    - docs/evidencia/          # corridas bilaterales de la renovación
  excluded_scope:
    - cualquier archivo de skopos      # A2/P1
    - corpus/                          # nada de esto entra al corpus
  dependencies:
    - {interface_agreement: IA-001@nueva}   # requiere WO-SK-001 listo
    - {interface_agreement: IA-004@nueva}   # política 0500 renovada
    - {interface_agreement: IA-002}         # la aceptación colgada
  acceptance:
    - "skopos-document-derivatives pasa de propuesta a aceptado en su
       forma, CONDICIONADO a la política de derivados renovada por
       WO-SK-001 (aceptar la forma vencida sería aceptar letra muerta);
       fidelidad del contenido sigue SIN aceptarse — texto explícito en
       la revisión — procedimiento: estado del contrato + policy_sha256
       nuevo citado"
    - "revisiones v0.3 citan el policy_sha256 nuevo por manual —
       procedimiento: grep del hash en docs/contratos/*.md"
    - "evidencia bilateral de cada corrida enlazada en docs/evidencia/ —
       procedimiento: enlace presente en la revisión v0.3"
  permissions: {commit: agent/wo-eg-001, push: null}
  authorization_ref: <cc-eg-sk-001-authority-block>
  correction_budget: {unit: correction_cycles, limit: 2}
```

Notas: la aceptación de IA-002 exige su reto AR0 (consistencia previa
al acuerdo) con registro. La regla de cita no cambia: cada cita nueva
sigue exigiendo cotejo de página y fragmento contra el PDF custodiado.
