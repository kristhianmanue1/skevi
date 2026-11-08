# PROP-014 — Contrato de coordinación multi-proyecto

**Estado: PROPUESTO — deliberación abierta; nada de este documento es
norma vigente ni autoriza operación alguna.** Fecha: 2026-11-08.

Origen: texto del Operador (contrato v0.2.0, PROPOSED), enmendado en
esta propuesta como **v0.2.1-candidata** con las dos enmiendas ordenadas
el 2026-11-08 — (1) subordinación al canon local de cada proyecto, nueva
Rule A4, y (2) alineación de la atribución de causa en AR5 — y más las
correcciones que la ronda adversarial fresca del mismo día exigió sobre
ese texto nuevo (piso mínimo de A1-A3, definición de «executor», checks
compartidos estricto-de-todos, SR-08). Todo cambio contra la v0.2.0 está
declarado en §12; el revisor difunde contra el original preservado
fuera del repo.

Posición de Skevi frente al contrato (deliberación, no adopción): es
**política de ecosistema**, no canon de Skevi — cubre coordinación entre
repositorios, un plano que Skevi no ofrece (sus gates son per-repo).
Ojo al solapamiento anotado: `project-manifest.yaml` cede «contrato de
tarea ejecutable ni máquina de estados de auditoría» a epistates, y §4
y §8 de este contrato rozan ese plano cedido — punto de deliberación
abierto. Si el Operador lo aprueba, Skevi adoptaría a lo sumo un
puntero condicional (patrón ADR-019), y el adaptador de ejecución
(Herdr) viviría en `docs/orchestration/` como los adaptadores por host,
fechado y caduco. En conflicto dentro de un proyecto, manda su canon
local — es la enmienda 1.

## Preguntas abiertas que esta propuesta NO decide

1. **Hogar canónico del estado de coordinación** (CC/WO/IA/evidencia):
   ¿repo dedicado con su propio skevi, o directorio canónico versionado
   en un proyecto anfitrión? §8 lo exige pero no lo nombra.
2. **Piloto §9**: qué dos proyectos participan y qué IA los une.
3. **Aprobación**: el checklist §10 exige aprobación explícita del
   Operador; esta propuesta no la constituye.
4. **Designación del Cross-Project Coordinator** (hallazgo M5 de la
   ronda): ningún texto lo designa; su autoridad vive sólo en el CC que
   él mismo registra (bootstrap circular). ¿Corrección en 0.2.2 o como
   condición de adopción en §10?
5. **Feedback 0.2.2 para el Operador** (hallazgos H2/L2/L3 de la ronda,
   heredados de v0.2.0; NO se parchean aquí para preservar su texto):
   divergencias diagrama/texto de §4 — el path `blocked →
   adversarial_review → completed` del diagrama WO se salta
   `verification`, y las colaboraciones carecen de `verifying →
   blocked` — y la lectura del diagrama de secuencia («Record agreed
   IA») como escritura del Coordinator en los proyectos.

---

# Multi-Project Agent Coordination Contract

**Status:** PROPOSED  
**Version:** 0.2.1  
**Scope:** Coordination of autonomous agent teams working within and across software projects  
**Implementation:** Technology-neutral; Herdr may be used as an execution adapter  
**Authority:** This document proposes a protocol. It does **not** grant permissions or authorize repository changes, commits, merges, releases, deployments, or persistent governance writes.

## 1. Purpose and non-goals

Enable multiple projects to develop independently while negotiating dependencies, producing compatible deliverables, and verifying cross-project commitments with minimal operator intervention.

**In scope:** role authority, task and contract lifecycles, escalation, acceptance verification, risk-proportionate adversarial review, dependency tracking, traceability, and recovery rules.

**Out of scope (deferred):** operator-advisor agent, speech interface, autonomous release approvals, vendor-specific orchestration, and an organization-wide memory architecture.

## 2. Architecture

A **Project Captain** governs work within an explicitly delegated project scope. A **Cross-Project Coordinator** handles relationships between projects but does not become their superior authority. **Workers** implement bounded work orders. **Verifiers** check evidence against acceptance criteria and conduct risk-proportionate adversarial challenges. A **Deterministic Controller** tracks state, retries, deadlines, and authorized transitions. The **Human Operator** retains strategic authority and reserved approvals.

These are **roles**, not mandatory separate LLM processes. One runtime may implement multiple compatible roles where independence is not claimed. Verification performed by another agent is functionally separate, not automatically independent audit.

```mermaid
flowchart TB
    H[Human Operator<br/>Strategy and reserved approvals]
    X[Cross-Project Coordinator<br/>Contracts and dependencies]
    S[(Coordination State<br/>Contracts · Work Orders · Evidence)]
    H -->|Scope and decisions| X
    X <--> S
    subgraph A[Project A]
      CA[Captain A] --> WA[Workers A]
      WA --> VA[Verifier A]
    end
    subgraph B[Project B]
      CB[Captain B] --> WB[Workers B]
      WB --> VB[Verifier B]
    end
    X <-->|Proposals · status · escalation| CA
    X <-->|Proposals · status · escalation| CB
    CA <--> S
    CB <--> S
    D[Deterministic Controller<br/>States · timeouts · retry limits] <--> S
    D --> E[Execution Adapter<br/>e.g. Herdr]
```

### Authority boundaries

| Role | May do within approved scope | Must not do without separate authorization |
|---|---|---|
| Human Operator | Set objectives, delegate scope, approve material risks and reserved actions | N/A; actions remain subject to platform and organizational controls |
| Project Captain | Decompose and supervise project work, assign workers, request verification, recommend integration | Change another project's resources or expand its own authority |
| Cross-Project Coordinator | Register dependencies, facilitate proposals, detect conflicts, recommend resolution, escalate | Unilaterally impose interface changes or authorize deployments |
| Worker | Implement and test a bounded Work Order, propose changes | Expand scope, access secrets outside scope, commit/push/merge/deploy without authorization |
| Verifier | Independently *check artifacts and evidence* where technically feasible; report pass/fail/inconclusive | Assert independent audit or approve reserved actions |
| Deterministic Controller | Enforce transitions, retry limits, idempotency keys, and stop conditions | Interpret new policy or silently bypass safety prompts |

**Rule A1 — Default deny:** No role can infer authorization from a task description, another agent's request, a status value, or this contract. Execution permissions must be explicitly delegated and enforced where technically possible.

**Rule A2 — Project sovereignty:** A project's captain controls its internal work within delegated scope. Cross-project coordination is an agreement process, not implicit write access.

**Rule A3 — Human-reserved actions:** Scope expansion, material risk acceptance, production promotion, and any commit, push, merge, tag, release, deployment, publication, or governed-memory write require explicit authorization covering those actions. An agreed interface does not authorize its integration or release.

**Rule A4 — Local canon precedence (enmienda 1):** Within any participating project, authority, evidence, and verification obligations are governed by that project's own adopted canon (for example, its skevi-gate and standard). This contract governs only cross-project coordination. Rules A1–A3 and §7.1 are a minimum floor within every participating project: a local canon may add obligations, never subtract from them, and "stricter" is computed against this contract as the baseline. A WO/CC/IA cannot grant, inside a project, what that project's canon denies, and no local canon can authorize, inside a project, what Rules A1–A3 reserve. For checks that feed a shared IA or CC, each participant applies its own canon to its own obligations, and the shared check passes only if it satisfies every applicable canon; a canon-versus-canon conflict escalates per §6 to the Human Operator, never to the Coordinator. The classification of a check as local or cross-project is recorded by the Verifier and is disputable via §6.

## 3. Minimal coordination objects

Three distinct objects share `id`, `version`, `owner`, `status`, `references`, and audit timestamps. Keep payloads small; store authoritative artifacts by stable references, not copied summaries.

| Object | Purpose | Minimum required fields |
|---|---|---|
| **Coordination Contract (CC)** | Who may coordinate, change, accept, or escalate a particular collaboration | `id`, `version`, `participants`, `scope`, `authority`, `escalation_policy`, `verification_policy`, `status` |
| **Work Order (WO)** | Bounded unit of executable work | `id`, `project`, `owner`, `objective`, `allowed_scope`, `excluded_scope`, `dependencies`, `acceptance`, `permissions`, `status` |
| **Interface Agreement (IA)** | Observable technical commitments between provider and consumer projects | `id`, `version`, `provider`, `consumer`, `interface_reference`, `compatibility_policy`, `acceptance_tests`, `status` |

An IA may have multiple consumers, but each consumer's approval and verification status must remain separately identifiable. A WO references the CC/IA it implements; no duplicated policy text is needed.

### Illustrative contract (not an authorization token)

```yaml
coordination_contract:
  id: CC-001
  version: "0.1.0"
  status: proposed
  participants:
    provider_project: project-a
    consumer_project: project-b
  scope:
    objective: "Deliver compatible memory retrieval interface"
    references:
      interface_agreement: IA-001
      work_orders: [WO-A-001, WO-B-001]
  authority:
    project_captains: [propose, plan_within_scope, verify]
    cross_project_coordinator: [track, recommend, escalate]
    human_reserved: [approve_scope_expansion, accept_material_risk, authorize_release]
  escalation_policy:
    unresolved_contract_conflict: human_operator
    unauthorized_action: stop
    newly_discovered_material_risk: stop_and_escalate
  verification_policy:
    required: [provider_contract_tests, consumer_contract_tests, integration_tests]
    evidence: [artifact_versions, commands, exit_codes, environment, findings]
    status_on_missing_evidence: inconclusive
    adversarial_review: risk_proportionate
    review_decisions: [proceed, fix_and_retry, escalate]
```

## 4. Lifecycle and transitions

**Work Order states:** `proposed -> ready -> in_progress -> verification -> adversarial_review -> completed`. A work order may enter `blocked` from `ready`, `in_progress`, or `verification`, and resume to a previously recorded executable state after its blocker is resolved. `cancelled` is terminal. `completed` means required acceptance checks and adversarial gates have passed for the specific reviewed version; it does **not** authorize release or merge.

**Collaboration states:** `proposed -> agreed -> implementing -> verifying -> adversarial_review -> fulfilled`. `blocked` and `revision_required` are recoverable; `rejected` and `cancelled` are terminal. `agreed` requires a bounded pre-agreement consistency challenge (authority, conflicting requirements, feasibility, testability, dependency cycles), recorded acceptance by each designated project representative, and any human approval required by scope; agent assent alone does not create new authority. An interface change creates a **new IA version** and triggers impact review; do not silently mutate an agreed version.

```mermaid
stateDiagram-v2
    [*] --> proposed
    proposed --> ready: validated scope and dependencies
    proposed --> cancelled
    ready --> in_progress: authorized assignment
    ready --> blocked: unmet dependency
    in_progress --> verification: deliverable + evidence
    in_progress --> blocked: obstacle
    verification --> adversarial_review: acceptance checks pass
    verification --> in_progress: corrections required
    verification --> blocked: missing evidence or environment
    adversarial_review --> completed: proceed + closure gate passes
    adversarial_review --> in_progress: fix and retry
    adversarial_review --> blocked: material inconclusive or escalation
    blocked --> ready: resume before execution
    blocked --> in_progress: resume execution
    blocked --> verification: resume verification
    blocked --> adversarial_review: resume scoped review
    ready --> cancelled
    in_progress --> cancelled
    blocked --> cancelled
    completed --> [*]
    cancelled --> [*]
```

```mermaid
stateDiagram-v2
    [*] --> proposed
    proposed --> agreed: consistency gate + authorized agreement
    proposed --> rejected
    agreed --> implementing: bounded Work Orders ready
    implementing --> verifying: both sides deliver evidence
    implementing --> blocked: unresolved dependency
    verifying --> adversarial_review: acceptance and compatibility checks pass
    verifying --> revision_required: incompatibility
    adversarial_review --> fulfilled: proceed + closure gate passes
    adversarial_review --> revision_required: material findings / fix and retry
    adversarial_review --> blocked: material uncertainty / escalation
    revision_required --> implementing: revised plan or new IA version
    blocked --> implementing: obstacle resolved
    blocked --> verifying: evidence restored
    blocked --> adversarial_review: review can resume
    agreed --> cancelled
    implementing --> cancelled
    blocked --> cancelled
    fulfilled --> [*]
    rejected --> [*]
    cancelled --> [*]
```

**Rule L1 — Status separation:** Runtime states (e.g. Herdr `blocked` or `done`) are observations, not canonical Work Order states or proof of success. Map runtime events to candidate transitions only after checking task evidence and policy.

**Rule L2 — Terminal and retry control:** Do not automatically repeat side-effecting actions if their prior outcome is unknown. Inspect the authoritative system first; resume using an idempotency key when supported or escalate.

## 5. Cross-project protocol

```mermaid
sequenceDiagram
    autonumber
    participant O as Human Operator
    participant B as Captain B (Consumer)
    participant C as Cross-Project Coordinator
    participant A as Captain A (Provider)
    participant V as Verification
    B->>C: Propose capability and acceptance criteria
    C->>A: Request feasibility and impact assessment
    A-->>C: Counterproposal / technical constraints
    C-->>B: Proposed IA version and dependency plan
    alt Scope or risk requires reserved approval
        C->>O: Alternatives, evidence, decision needed
        O-->>C: Explicit decision or rejection
    end
    C->>A: Record agreed IA and provider WO
    C->>B: Record agreed IA and consumer WO
    par Parallel development
        A->>A: Implement provider side
    and
        B->>B: Build client against agreed IA
    end
    A->>V: Provider artifacts and evidence
    B->>V: Consumer artifacts and evidence
    V-->>C: Acceptance and compatibility results
    C->>V: Request risk-scoped adversarial challenge
    V-->>C: Findings, evidence, proceed / fix-and-retry / escalate
    alt All closure gates pass
        C-->>A: Mark commitment technically fulfilled
        C-->>B: Mark commitment technically fulfilled
    else Material finding or inconclusive evidence
        C-->>A: Correct affected obligations or escalate
        C-->>B: Recheck impacted dependencies
    end
    Note over O,V: Fulfilled does not imply merge, release, or deployment authorization
```

**Rule P1 — Propose before crossing boundaries:** A consumer asks for an external capability through an IA proposal; it does not dispatch workers into another project's resources.

**Rule P2 — Concurrency:** Projects may work in parallel against an agreed, versioned interface, using mocks or contract fixtures. Shared-file ownership and integration sequencing must be explicit.

**Rule P3 — Dependency graph:** Store directed edges `consumer WO -> required provider artifact/version`. Detect cycles, missing providers, incompatible versions, and transitive impact before advancing dependent work. A cycle MUST be resolved or expressly modeled as an iterative delivery plan with bounded phases and testable intermediary contracts; a plain cyclic dependency MUST NOT be considered ready.

```mermaid
flowchart LR
    A1[Project A<br/>Provider API v2] -->|IA-001| B1[Project B<br/>Consumer client]
    B1 -->|IA-002| C1[Project C<br/>Downstream service]
    A1 -.->|Version change impact| C1
    G[Dependency graph] --- A1
    G --- B1
    G --- C1
```

## 6. Escalation and stop policy

| Condition | First handler | Required behavior |
|---|---|---|
| Local recoverable failure | Worker, then Project Captain | Retry within bounded budget; record attempts |
| Repeated failure or conflicting local priorities | Project Captain | Replan within scope or escalate |
| Cross-project interface conflict | Cross-Project Coordinator | Compare options and impacts; request agreement |
| Contract conflict unresolved or authority insufficient | Human Operator | Present alternatives and consequences; do not presume approval |
| Unknown side-effect outcome, unapproved boundary crossing, material new risk | Controller + responsible Captain | Stop affected action; preserve evidence; escalate when necessary |
| Independent task unaffected by blocked action | Owning Project Captain | Continue if within scope and safe |

**Rule E1:** A `blocked` runtime indication is not automatically a human escalation. Classify its cause and required authority first. Never automatically approve security, permission, or trust prompts.

**Rule E2:** If an operation exceeds authorization or introduces material new risk, stop that operation; unrelated permitted work may continue.

## 7. Verification and evidence

A commitment is `fulfilled` only when its agreed acceptance criteria **and required adversarial review** have evidence linked to **specific versions and environments**, with no unresolved material blockers or uncertainty. At minimum record:

- exact artifact/repository references and revisions;
- acceptance criteria and which test checks each criterion;
- test commands or procedures, timestamps, environment, exit codes, and results;
- incompatibilities, assumptions, untested cases, and open risks;
- identities of implementer, verifier, and approving authority where applicable.

A claim of success by a worker is **not** verification. A SHA alone proves neither deployment nor acceptance. Agent-based review is self/peer review unless operational and organizational independence is actually demonstrated. For negative security or isolation tests, include a positive control to show the probe operates.

```mermaid
flowchart TD
    D[Deliverable submitted] --> A{Required acceptance evidence complete?}
    A -- No --> I[Fail missing required action<br/>or inconclusive external gap]
    A -- Yes --> T{Contract and integration checks pass?}
    T -- No --> R[Fix and retry]
    T -- Yes --> K{Versions and scope match?}
    K -- No --> R
    K -- Yes --> Q[Risk-scoped adversarial review]
    Q --> G{Review disposition}
    G -- Material finding --> R
    G -- Material uncertainty --> E[Escalate or obtain evidence]
    G -- Proceed --> F{All closure gates satisfied?}
    F -- No --> E
    F -- Yes --> H[Technically fulfilled]
    R --> D
    I --> D
    H --> U{Reserved action requested?}
    U -- Yes --> O[Human authorization gate]
    U -- No --> Z[Close coordination commitment]
```

### 7.1. Risk-proportionate adversarial review

**Rule AR0 — Pre-agreement challenge.** Before a material CC or IA enters `agreed`, challenge its authority assumptions, requirement consistency, testability, feasibility, and dependency graph. Record the result with the contract version. This does not duplicate the later implementation review.

**Rule AR1 — Falsification, not endorsement.** Required adversarial review MUST actively seek counterexamples to the claimed result, including untested assumptions, unauthorized changes, false provenance, regressions, and cross-project incompatibilities outside the original acceptance criteria. A reviewer MUST NOT treat a positive summary as sufficient evidence. A round that merely repeats acceptance checks or praises the work does not count as adversarial review.

**Rule AR2 — First broad, then narrower.** For a material change, the **first** adversarial round MUST inspect the affected contract boundary, authority, evidence provenance, key failure modes, and transitive dependency impact. Each **subsequent** round SHOULD focus on unresolved findings, applied fixes, directly affected checks, and plausible regressions introduced by those fixes. Unaffected verified checks MAY be referenced rather than rerun. The reviewer MUST record the scope and reason for narrowing. Avoid repeatedly reopening previously resolved issues without new evidence.

**Rule AR3 — Reopen only on meaningful impact.** A materially changed artifact, contract version, threat assumption, dependency, or newly discovered high-severity risk MUST trigger an impact assessment. Expand the next round only to the changed or plausibly affected areas; restart broad review only if the original assumptions or trust boundaries no longer hold. Narrowing MUST NOT conceal new material risk.

**Rule AR4 — Bounded cost and termination.** Review MUST use predeclared proportional budgets (such as time, attempts, or token/cost ceiling). On budget exhaustion with unresolved material findings or uncertainty, the decision is `escalate`, **not** `proceed`. The default decision set for each round is exactly `proceed | fix-and-retry | escalate`. No unbounded self-review loops are allowed.

**Rule AR5 — Evidence and polarity.** Each required check MUST record a stable ID, claim, reviewed artifact version, result (`pass | fail | inconclusive`), and evidence reference or explicit missing-evidence reason. The aggregate MUST NOT report `pass` if a required material check is `fail` or `inconclusive`. An omitted required check is a **failed evidence obligation**; an external inability to determine a result is `inconclusive`. If cause is uncertain, record `inconclusive` and do not close; do not assume fault. Any material `inconclusive` blocks fulfillment. A failing test is not reclassified as inconclusive merely because no fix is available. Where a participating project's local canon imposes a stricter cause-attribution rule — for example, an impediment caused by the executor itself counts as `fail`, not `inconclusive` — that stricter rule governs that project's checks (Rule A4); this section's no-fault-assumption applies only to genuinely uncertain causes external to the executor. «Executor» means the worker/runtime executing the Work Order under review. Cause attribution is a recorded field of each check (`executor-caused | external-uncertain`, with its basis), classified by the Verifier; a disputed attribution escalates per §6.

**Rule AR6 — Findings.** Each finding MUST include ID, severity, affected claim/contract and versions, concrete counterexample or evidence, corrective action, and status (`open | resolved | accepted_by_authority` when applicable). Unresolved BLOCKER/HIGH findings MUST block technical fulfillment. Agents MUST NOT reduce severity or accept material risk solely to close the gate. The human may make a separately documented risk decision within actual authority; that decision does not retroactively turn a failed check into `pass` or imply technical fulfillment.

**Rule AR7 — Cross-project obligations.** Review the provider and consumer versions together; check version compatibility, agreed interfaces, dependent Work Orders, transitive effects, and whether each designated party has supplied its verification evidence. Passing local project tests alone cannot fulfill an interproject agreement.

**Rule AR8 — Review provenance.** Record implementer, reviewer/process, role separation, evidence origin, commands/results/environment where relevant, reviewed versions, findings, limits, and final disposition. Another LLM does not automatically constitute independent audit. Optional reproducible hashes can bind recorded bytes but do not prove execution, truth, approval, or independence.

**Rule AR9 — Closure.** `completed` or `fulfilled` requires: (a) required acceptance checks `pass`; (b) required adversarial review disposition `proceed`; (c) no unresolved material `fail`, `inconclusive`, BLOCKER, or HIGH; (d) impacted cross-project checks pass; and (e) all applicable authority gates are satisfied. Closure is version-specific; it does not grant commit, merge, publication, or deployment permissions.

#### Review-round record (illustrative)

```yaml
review:
  id: AR-IA-001-R2
  contract_ref: IA-001@2
  round: 2
  scope:
    unresolved_findings: [F-017]
    changed_artifacts: [provider-api@rev-b]
    regression_targets: [consumer-client@rev-c]
    reused_checks:
      - id: CHECK-001
        previous_evidence_ref: evidence/check-001-r1.json
        verified_versions: [provider-api@rev-a]
        reuse_basis: "No change to checked artifact or assumptions"
    narrowing_reason: "Only F-017 and directly affected dependencies remain"
  checks:
    - id: CHECK-017
      claim: "Provider and consumer agree on pagination semantics"
      result: pass
      artifact_versions: [provider-api@rev-b, consumer-client@rev-c]
      evidence_ref: evidence/check-017.json
  findings:
    - id: F-017
      severity: high
      status: resolved
      evidence_ref: evidence/f-017-resolution.json
  disposition: proceed
  review_independence: functional_separation_only
```

A `proceed` in an individual review round does not close the contract if another required gate remains open. Review records are version-bound and must not be reused after a change that invalidates their assumptions.

## 8. Persistence, recovery, and observability

Maintain a canonical record independent of execution sessions. Every state transition should include `event_id`, `object_id`, `prior_state`, `next_state`, `actor`, `reason`, `timestamp`, and evidence/authorization references. Prevent duplicate transitions and support audit replay. Logs and records must minimize secret and personal-data exposure.

At recovery, reconcile unfinished Work Orders against the actual repository, CI, and external systems before reissuing commands. Treat unknown outcomes as `needs_reconciliation`, not automatically failed. The controller may resume only when the intended action is safe, still authorized, and idempotent or demonstrably not yet executed.

**Implementation note:** Herdr can supply agent execution and observed runtime events. It is not the source of truth for contract acceptance, authority, or release state.

## 9. Minimal pilot and falsification criteria

**Pilot:** Two projects, one provider IA, one consumer IA, two project captains, workers, one verifier function, and a lightweight coordinator/controller. Do not add a permanent global LLM unless observed coordination complexity warrants it.

| Hypothesis | Test / counterexample | Evidence of success |
|---|---|---|
| Projects remain autonomous | Block Project A while B has independent work | B continues only authorized independent tasks |
| Contracts prevent silent incompatibility | Introduce a breaking interface version | Coordinator flags affected consumers and prevents false fulfillment |
| Runtime completion is not proof | Worker reports done without test evidence | WO remains unverified/inconclusive |
| Recovery avoids duplicates | Restart after an action with unknown result | No blind replay; reconciliation is logged |
| Authority remains bounded | Request out-of-scope write or release | Affected action stops; valid in-scope positive control still works |

**Pilot exit criteria:** All five scenarios observed with reproducible records, plus an adversarial first round and a focused second round after a seeded defect is fixed; unresolved failures and limitations reported explicitly. This is a local architecture test, not a general safety certification.

## 10. Adoption checklist

- [ ] Operator approves this contract as project policy (proposal alone is not approval).
- [ ] Identify projects, owners, delegated authorities, and excluded resources.
- [ ] Register a CC and versioned IA for the pilot dependency.
- [ ] Create bounded WOs with testable acceptance criteria.
- [ ] Implement controller checks and durable state without bypassing existing controls.
- [ ] Conduct an adversarial first round, then focused rechecks that shrink to surviving issues unless impact warrants expansion.
- [ ] Run the pilot, inspect the actual evidence, and revise this specification.

**Decision pending:** Approval of the contract and any separate implementation actions. No repository, persistent memory, CI, or production resource is changed by this document.

## 11. Self-adversarial review of this specification (0.2.0)

**Review type:** Author self-review of the text of this contract, **not independent audit**. **Evidence:** inspection of this Markdown specification and its internal consistency; no running agent fleet, cross-project protocol, policy enforcement, or end-to-end workflow was exercised. The checks below are design-level only. Findings were challenged against the revised text; their disposition does not certify implementation.

| ID | Counterexample / failure hypothesis | Corrective rule | Design-level disposition |
|---|---|---|---|
| SR-01 | A contract may be agreed with contradictory obligations, even though delivery later passes an acceptance gate. | AR0 adds pre-agreement consistency challenge; `agreed` transition is guarded. | Addressed in text; behavior untested |
| SR-02 | A second review could reuse a green check from an obsolete artifact or assumption. | AR2/AR3 require impact assessment; review example records referenced versions and reuse basis. | Addressed in text; evidence-reuse enforcement untested |
| SR-03 | An agent could narrow review until a newly introduced material regression is ignored. | AR3 requires impact-based expansion; material changed trust boundaries require broad re-review. | Addressed in text; detection coverage untested |
| SR-04 | An agent could exhaust review budget and declare success or loop indefinitely. | AR4 makes budget exhaustion with material uncertainty an escalation, not a pass. | Addressed in text; budget enforcement untested |
| SR-05 | Both projects can pass local checks while an incompatible version breaks their shared agreement. | AR7 requires joint versioned, transitive cross-project checks. | Addressed in text; integration untested |
| SR-06 | A cyclic dependency could be marked ready without any deliverable becoming available. | P3 requires cycle resolution or bounded iterative milestones before readiness. | Addressed in text; graph detection untested |
| SR-07 | A human risk acceptance could be misrepresented as proof that a failed technical check passed. | AR6 and AR9 preserve failed evidence and distinguish risk decisions from fulfillment. | Addressed in text; policy enforcement untested |
| SR-08 | A local canon looser than this contract could displace Rules A1–A3 inside that project. | A4 (0.2.1) sets A1–A3 and §7.1 as a minimum floor, computes "stricter" against this contract as baseline, and routes canon-versus-canon conflicts to the Human Operator. | Addressed in text; behavior untested |

**Residual material limitations:** The contract does not implement authentication, authorization enforcement, reviewer isolation, provenance attestation, a state machine, dependency analysis, or proof that review probes actually ran. A separate implementation must test both negative and positive controls. Review cannot establish the absence of undiscovered defects. No second independent reviewer participated. The normative rules still need validation against a real pilot before adoption. The 0.2.1 amendments (Rule A4 and the AR5 clause) were reviewed on 2026-11-08 by an external fresh-context session (register in skevi `docs/reviews/`); that round's findings on v0.2.0-inherited text — diagram/text divergences in §4 (WO `blocked → adversarial_review` path bypassing `verification`; missing `verifying → blocked` for collaborations) and the sequence diagram's Coordinator-write reading — remain open as 0.2.2 feedback for the Operator.

## 12. Change history

- **0.2.0 (proposed):** Added falsification-oriented, evidence-granular, progressively narrowed adversarial review; amended terminal state gates, diagrams, and pilot criteria. No implementation or authorization implied.
- **0.2.1 (proposed):** Per the Operator's directive of 2026-11-08 and the fresh adversarial round of the same date: added Rule A4 (local canon precedence) with Rules A1–A3 and §7.1 as minimum floor, shared-check strictest-of-all rule and §6 escalation for canon conflicts; added the stricter-local-cause clause of AR5 with the definition of «executor» and recorded cause attribution classified by the Verifier; added SR-08 and the external-review note to §11; updated the Version header. v0.2.0-inherited text is otherwise unchanged. No implementation or authorization implied.
