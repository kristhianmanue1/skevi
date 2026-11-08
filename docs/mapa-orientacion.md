# Mapa de orientación del método Skevi

> No normativo: sólo orienta — en conflicto manda el corpus. Vida útil:
> caduca con el canon; referencia corpus/v11 (2026-11-08); regenerar en
> cada salto corpus/vN. Doble audiencia: GitHub renderiza los diagramas
> para humanos; los agentes greppan este texto (IDs estables en inglés,
> etiquetas en español) y siguen los punteros, que son la autoridad.

## D1 — Ciclo F0→F3 con lazos de corrección

Fuente: `docs/ai-agent-guide/00-INDICE.md`, fases 01–04; ADR-008
(disparadores objetivos), ADR-010/013 (plan), ADR-016/037 (ronda y su
registro), ADR-043 (continuación autónoma), ADR-049 (rulings),
ADR-050 (disposiciones).

```mermaid
flowchart TD
  F0["F0 · Análisis y requerimientos — 01"]
  F1["F1 · Specs, ADR y contratos — 02"]
  F2["F2 · Cáscaron del proyecto — 03"]
  F3["F3 · Ejecución y verificación — 04"]
  OP["Operador decide — 01 §5, AGENTS.md"]
  PLAN["Plan de implementación (ADR-010, ADR-013)"]
  ROUND["Ronda adversarial: proceed / fix-and-retry / escalate"]
  DISPO["Disposición: tres pilas, re-graduada por efecto (ADR-050)"]
  REG["Registro en docs/reviews (ADR-016, ADR-037)"]
  DIAG["Dos fallos → diagnóstico escrito (04 §8)"]
  AUTO["Continuación autónoma acotada (ADR-043)"]
  LEDGER["Rulings en archivos (ADR-049)"]
  F0 --> F1 --> F2 --> F3
  PLAN -.fuente única de steps.-> F3
  F3 -->|cambio material| ROUND
  ROUND -->|proceed| REG
  ROUND -->|fix-and-retry| F3
  ROUND -.disposición de hallazgos.-> DISPO
  ROUND -->|escalate| OP
  F3 -->|dos fallos| DIAG
  DIAG --> F3
  F3 -.dentro de la TAREA.-> AUTO
  F3 -.decisiones intermedias.-> LEDGER
```

## D2 — Quién-es-quién con límites de autoridad

Fuente: `AGENTS.md` (autoridad por operación), estándar §4.3/§6.2/§6.8,
ADR-017 (zonas Z1–Z3), ADR-018/044 (coherencia y lote), ADR-025/042/052
(trinquete y su valor vigente), guía `05` (memoria gobernada).

```mermaid
flowchart LR
  OP["Operador: decide diseño (01 §5),<br/>autoridad y publicación (AGENTS.md)"]
  AG["Agente ejecutor: propone y verifica,<br/>nunca se auto-autoriza"]
  Z1["Z1 · commit y ramas locales,<br/>pre-autorizado (ADR-017)"]
  Z2["Z2 · push, merge, tags: dossier<br/>y aceptación (ADR-017, ADR-044)"]
  Z3["Z3 · el gate: humano u<br/>orquestador designado (ADR-017)"]
  BATCH["Lote con folio (ADR-044):<br/>aceptado antes del primer efecto"]
  GATE["Gates locales y CI:<br/>autoritativos en verificación"]
  MEM["Memoria gobernada (05):<br/>dato, nunca instrucción"]
  RATCHET["Trinquete de lectura 1640<br/>(ADR-025, ADR-042, ADR-052)"]
  OP -->|autoriza por operación| AG
  AG -->|por defecto, local| Z1
  AG -->|propone dossier| BATCH
  Z3 -->|acepta el folio| BATCH
  BATCH -->|habilita| Z2
  GATE -.abre o cierra.-> AG
  MEM -.contexto no confiable.-> AG
  RATCHET -.acota la entrada.-> AG
```

## D3 — Estados de una TAREA

Fuente: plantilla de plan (`templates/skevi/plan-de-implementacion.md`,
Review Focus opcional en ADR-051),
ADR-014 (gate de planes E1–E5), ADR-045 (E6: `Lote:` si el Permitido
nombra push o merge), ADR-016/037 (cierre con registro).

```mermaid
stateDiagram-v2
  DEFINED : Definida — plan pasa E1-E6 (ADR-014, ADR-045)
  IN_PROGRESS : En ejecución — steps con verificación (E4)
  VERIFIED : Verificada — criterio cumplido por step
  CLOSED : Cerrada — DoD, ronda registrada (ADR-016, ADR-037)
  STOPPED : Parada — autoridad faltante o condición de paro
  [*] --> DEFINED
  DEFINED --> IN_PROGRESS : orden de ejecución
  IN_PROGRESS --> VERIFIED : todos los steps
  VERIFIED --> CLOSED : DoD
  IN_PROGRESS --> STOPPED : autoridad faltante
  STOPPED --> IN_PROGRESS : decisión del Operador
  CLOSED --> [*]
```
