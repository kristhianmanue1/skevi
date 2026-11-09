# PROP-014-S — Perfil mínimo del contrato de coordinación (sin Herdr, sin multi-modelo)

**Estado: PROPUESTO — derivado de la familia PROP-014 v0.5.0; nada de
este documento es norma vigente ni autoriza operación alguna.**
Versión: 0.5.0-S.1 (2026-11-09).

Origen: Core `PROP-014-core-contrato-coordinacion.md` 0.5.0-C.1 (sha256
`e02190ed613f7665904e50ce7a0ce2a48fa3e01ddb252d7885a26d55eef3e5ed`,
copia local verificada de la familia adoptada como política de
devHerdrExpert, commit `dfb7214`, 2026-11-09). La cadena completa —
corpus v0.5.0, Core, tarjeta — vive en ese repo; skevi conserva la
cadena de origen v0.2.0→v0.3.1 con sus registros.

Propósito: el mismo contrato, utilizable donde **no hay Herdr** y donde
**no hay varios modelos de IA** — un solo agente en una sola sesión con
un solo modelo debe poder coordinarse bajo esta ley. El perfil sólo
**aprieta o aclara**; nunca afloja: en silencio, omisión o conflicto,
manda el corpus v0.5.0 y luego el Core. Precedencia: corpus > Core >
este perfil > tarjeta (no normativa). Compatibilidad: objetos CC/WO/IA
idénticos — un participante con este perfil coopera con participantes
Core sin traducción.

---

# Coordination Contract — Minimal Profile (S)

**Status:** PROPOSED · **Version:** 0.5.0-S.1 (profile of PROP-014 v0.5.0)
**Scope:** same as the family; deltas only — the Core remains the law
**Authority:** proposes a protocol; grants no permissions.

## S1. Execution plane — never normative

The execution plane is environment-defined and carries no normative
weight: a single agent session, subagents, a terminal multiplexer, or a
tool such as Herdr — any, none, or several. No rule of the family
requires a specific runtime; runtime states are observations (L1). An
environment without Herdr, without subagents, and without network is a
valid deployment of this profile.

## S2. Independence ladder — recorded, never assumed

The family's recorded practice (AR8) is fresh-context separation for
adversarial review; this profile fixes the ladder of available rungs
and makes the rung **a recorded field** of the review record — a pure
addition on top of the Core's independence-recording requirement:

1. **Rung A — separate context, other model family** (best): another
   provider's model in a fresh session or subagent.
2. **Rung B — separate context, same model**: a fresh session or
   subagent of the same family.
3. **Rung C — simulated freshness**: no second context exists; the
   review examines only the diff and the specs, without relying on the
   author's memory of intent, and is recorded as degraded.

No rung is ever recorded as independence it does not have (AR8). «Material»
is defined by reference: the §6 tier floor of the Core (mechanically
High triggers), plus — for skevi-canon participants via S4/A4 — the
objective triggers of `04` §5.3; the classification is recorded and
disputable like a tier. Rung C is acceptable only when no material
trigger fires — a material change under Rung C MUST escalate the
closure decision to the Human Operator with that fact stated (E4).
Model diversity is never required *by this family's floor*; a stricter
local canon may require it (A4). The irreducible floor is the family's
three planes: no deliberative actor self-certifies a control decision,
whatever the number of models.

## S3. Minimal Deterministic Controller and state home

The Deterministic Controller may be as small as a script over a
version-controlled directory: a git-tracked `coordination/` directory
(with CC/WO/IA as JSON or YAML files and an append-only event log) plus
a checker that validates transitions against `prior_state` (L5
compare-and-set by file+commit), budgets (L6, E3), and the §6 tier
floor. Default minimal state home: the same git repository of the
provider project or a dedicated coordination repository — designation
and `state_home_ref` remain §8/§10 preconditions.

Writer identity is fail-closed (per the Core's §7/§8 precondition): a
write requires signed commits **or** a controlled write interface.
Where neither exists, the coordination state accepts **no
transitions** — an offline or credential-less deployment is valid for
observation and review only, never for state writes; git's commit
identity alone never satisfies the precondition. Likewise, an event
whose commit lacks approved validation by the designated controller is
a **proposal, never a transition**: it is recorded and not applied.

## S4. Tier mapping for skevi-canon participants (A4 application)

For a participant whose local canon is skevi, the local canon tightens
the tiers exactly as A4 provides: Tier 1 standing authorization applies
only where the local canon allows (in skevi, `push` remains a Z2
operation gated by lote and folio — the profile never waives it); Tier 2
main-line merges are Z2 (dossier + acceptance by folio before the
effect); Tier 3 is reserved to the Operator (release, deployment,
publication). Nothing in this profile loosens Tier 3 in any
participant, ever.

## S5. Deltas against the Core

| Tema | Core | Este perfil |
|---|---|---|
| Adaptador de ejecución | «Herdr may serve as execution adapter» | plano de ejecución no normativo; Herdr opcional entre otros (S1) |
| Separación de contexto | implícita en AR8/§6 | escalera A/B/C con peldaño registrado; Rung C material escala a humano (S2) |
| Controller / estado | designado, `state_home_ref` | implementación mínima declarada: script + directorio git + log de eventos (S3) |
| Identidad del escritor | firmas o interfaz controlada | fail-closed: sin firma ni interfaz controlada no hay transiciones — sólo observación; evento sin validación del controller designado es propuesta, no transición (S3) |
| Tiers vs canon local | A4 genérico | mapeo explícito a zonas Z1/Z2/Z3 para participantes skevi (S4) |

Todo lo demás del Core se incorpora por referencia sin cambio.

## S6. Falsification additions for this profile

| Hypothesis | Test | Evidence of success |
|---|---|---|
| Degraded rung is honest (S2) | Run a material review with no second context available | The record shows Rung C; closure escalates to the Operator with the degradation stated; a Rung-B run records B, never A |
| Minimal controller arbitrates (S3) | Two conflicting event-file commits against the same `prior_state` | Only one lands; the other is rejected with an event; no Herdr involved |
| Single-agent floor holds (S2/S4) | One session, one model, material change, asks its own closure | Self-certification denied; the decision escalates (E4) with recommendation |

## Procedencia y cambio

- Derivado del Core 0.5.0-C.1 (sha arriba citado) por orden del
  Operador del 2026-11-09 («crea tu propia versión… compatible…
  pensando en que no siempre se tendrá Herdr o entornos agénticos
  multi-modelo»). Cadena: corpus v0.5.0 → Core 0.5.0-C.1 → este
  perfil 0.5.0-S.1. Familia adoptada en devHerdrExpert (`dfb7214`).
- Ronda adversarial fresca de esta derivación:
  `docs/reviews/2026-11-09-prop014-perfil-skevi-ronda.md` (hash en el
  registro). Nada de este perfil se adopta sin la aprobación §8/§10
  del Operador.
