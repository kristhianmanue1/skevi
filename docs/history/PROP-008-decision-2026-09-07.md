# PROP-008 — Decisión de adopción y piloto K1-K4

> Registro histórico: evidencia de decisión, no norma vigente.
> Norma vigente: [ADR-019](../adr/ADR-019-integracion-ankla-por-contrato.md)
> y [05 §6](../ai-agent-guide/05-memoria-del-agente.md).

## Decisión

D1 (contrato `skevi/an-kla-integration v1`) y D2 (reglas derivadas:
folio, attest, hueco de upgrades) quedan aprobadas por el humano en
conversación, 2026-09-07: «estan aprobados D1/D2 para que procedas en
cuanto puedas». D3 se ejecutó en la misma sesión de adopción, rama
`docs/adopt-authority-consistency`: contrato en `05` §6, regla de
upgrades en `04` §7, ADR-019 y traslado de esta PROP a `docs/history/`
en el mismo cambio (patrón PROP-004).

## Piloto K1-K4 sobre la propia sesión de adopción

- **K1** (detección positiva → efecto por comando) — **pass**: la
  sesión de adopción arrancó con preflight: `context status` →
  `ok: true`, revisión 20; `verify` → `ok: true`. El efecto
  contractual se observa por comando:
  `grep -n "an-kla-integration" docs/ai-agent-guide/05-memoria-del-agente.md`
  → líneas 67 y 74 (sección obligatoria-para-memoria-adoptada).
- **K2** (un diagnóstico → una acción; cero auto-reparación) —
  **pass**: por inspección, la tabla de errores del contrato mapea
  cada diagnóstico a una sola acción y no declara ninguna ruta de
  auto-reparación. Evidencia de la práctica general (diagnóstico
  fuera de la tabla del contrato, que v1 no mapea): el aviso
  `context_target_changed_outside_managed_block` de T05-A fue
  reportado y no reparado
  ([revisión T05-A](../reviews/2026-09-07-t05-adoption.md)).
  El ejercicio de casos negativos de la propia tabla queda para T08.
- **K3** (checkpoint = punteros) — **pass**: `checkpoint show` de la
  revisión 20 (2026-09-07): las decisiones `d-t05` y `d-boundaries`
  contienen punteros (ruta de ADR, reporte de revisión, estado de
  PROP-008), no re-enunciado de normas.
- **K4** (adoptante sin AN-KLA cumple la norma) — **pass**: barrido
  de la norma obligatoria con
  `grep -rn -i "an-kla" AGENTS.md docs/estandar-diseno-software-github.md docs/ai-agent-guide/0{0,1,2,3,4}-*.md`
  → única aparición: el bloque administrado de `AGENTS.md` (líneas
  94-104), insertado por la propia adopción de AN-KLA. Un adoptante
  sin memoria no tiene ese bloque ni ninguna otra referencia; la
  totalidad de la norma le aplica sin ella.

## Comprobaciones del aterrizaje

- `python3 -B scripts/check_sizes.py` → OK (ver detalle en el reporte
  de la sesión) [pass]
- `python3 -B scripts/check_plans.py` → OK [pass]
- Referencias entrantes a `docs/proposals/PROP-008-*` revisadas: las
  menciones restantes son registros históricos (SPEC, plan, reviews,
  deliberación T05) que describen estados pasados; no se reescriben.
- Ronda adversarial en contexto fresco sobre el diff: `fix-and-retry`
  con tres MED corregidos; reporte en
  [2026-09-07-prop008-aterrizaje](../reviews/2026-09-07-prop008-aterrizaje.md).
