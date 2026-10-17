# PROP-011 — Frontera de memoria agnóstica en `05`

> **Estado:** **PROPUESTO** (2026-10-17). Sin decisión humana, sin ADR y sin
> cambio normativo todavía. Las rondas que llegue a tener vivirán en
> `docs/reviews/`, con su disposición (ADR-037); este archivo no las cuenta.
> **Origen:** instrucción directa del Operador (sesión del 2026-10-17:
> proyectos del ecosistema usan también memoria memmy y skevi no depende de
> ninguna); tarea HG-7 del
> [plan 2026-10-17](../plans/2026-10-17-holgura-de-gate-y-issues.md);
> veredicto P7 de la ronda
> [2026-10-17-plan-gate-ronda.md](../reviews/2026-10-17-plan-gate-ronda.md)
> («confirmado con ajuste»).

## 1. Problema

`05-memoria-del-agente.md` recomienda AN-KLA Memory (§1) y fija una frontera
de verdad para **la memoria adoptada** (§2): docs/ y Git canónicos, la
memoria jamás cierra un gate ni autoriza operaciones, lo recuperado es dato
no confiable. Esa frontera es de **método** y no depende de la herramienta —
pero su redacción actual vive dentro de la recomendación nominal de AN-KLA,
y el resto del documento habla su vocabulario (streams `facts/events/
episodes`, `plan-write`, checkpoints).

Resultado observado: proyectos adoptantes que usan **otra memoria local**
(p. ej. memmy) no tienen en `05` un contrato de frontera equivalente. La
regla genérica existe — principio 7 del estándar, datos no confiables —
pero el documento que un agente lee para saber cómo operar con memoria la
presenta como condición de adopción de una herramienta concreta. Skevi, por
declaración del Operador y por manifiesto (`consume: an-kla-memory,
requerido: false`; `no_ofrece` cede el plano de memoria), **no depende de
ninguna**: la norma debería poder decirlo sin nombrar una sola.

## 2. Propuesta

**D1 — §2 pasa a ser condición de adopción de *cualquier* memoria local.**
Reescritura mínima: «si el proyecto adopta una memoria local —cualquiera
sea su herramienta—, las reglas de esta sección son obligatorias para esa
memoria». Las reglas en sí no cambian: ya son agnósticas de herramienta.
El vocabulario específico de AN-KLA (streams, comandos, checkpoints) se
mantiene **sólo** donde ya vive: §1 (recomendación), §3 (mapeo recomendado,
marcado como propio de AN-KLA) y §6 (contrato `skevi/an-kla-integration
v1`, **intacto**: cambios de contrato exigen v2, nunca mutación in situ).

**D2 — §1 conserva la recomendación nominal, con su procedencia.** No es
endorsement exclusivo: es el único consumo declarado y validado
(`consume`, piloto infosalud, issue #25). Una frase nueva deja claro que
recomendar una herramienta no retira la frontera a las demás.

**D3 — aterrizaje con sello.** Al aceptarse: edición de `05`, bump
`corpus/v5` en `docs/MANIFEST.json` (digests) y fila de versión. El cambio
es de prosa normativa sellada; sin tocar `06`, el estándar ni el gate.

## 3. Lo que esta propuesta NO hace

- No toca el contrato `skevi/an-kla-integration v1` (§6) ni su activación
  condicional (ADR-019).
- No recomienda ni excluye memmy u otra herramienta por nombre: la frontera
  es el contenido, no el catálogo.
- No añade detección de memoria al gate: la coherencia máquina terminó en
  `root_markdown` ↔ `reading_path` (gate/v10, #63); qué memoria corre en el
  proyecto sigue siendo territorio del preflight comandado, no del gate de
  tamaños (ADR-019: sin acoplamiento).

## 4. Preguntas para el Operador

- **K1:** ¿el mapeo de fases → streams (§3) se marca como específico de
  AN-KLA (propuesta actual) o se generaliza a un vocabulario neutro
  (conocimiento / cronología / lecciones / continuidad) con la tabla de
  AN-KLA como ejemplo?
- **K2:** ¿la frase de §1 «no es endorsement exclusivo» basta, o se
  prefieren dos tablas separadas (recomendado / compatible-declarado)?
- **K3:** ¿se exige a una memoria compatible-declarada algo más que
  respetar §2 (p. ej. escritura gobernada por equivalente local de
  `plan-write` → `commit-write-plan`)?

## 5. Riesgos declarados

- Prosa normativa que caduca mal: la frontera agnóstica debe abstenerse de
  vocabulario de herramienta para no repetir el acoplamiento que corrige.
- Sin consumidor verificado de la versión agnóstica (memmy no ha pasado un
  piloto con este contrato), K4 («adoptante sin memoria cumple la norma»)
  se conserva por construcción, pero el caso positivo con otra memoria
  quedaría sin evidencia de piloto — declararlo, no ocultarlo.
