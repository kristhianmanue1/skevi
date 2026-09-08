# AUDIT-ankla-contract-review — Revisión del contrato AN-KLA aterrizado

> **Estado:** RESUELTA — D1-D3 aceptadas por el humano (2026-09-07, en
> conversación) como detalle operativo registrado del contrato v1, sin
> editar `05` §6. Lo estrictamente nuevo queda disponible para una
> futura v2 (ver Adopción).
> **Origen:** plan AUDIT-2026-09-07, tarea T08 (REQ-AUD-06). Revisa el
> contrato `skevi/an-kla-integration v1` ([05 §6](../ai-agent-guide/05-memoria-del-agente.md),
> [ADR-019](../adr/ADR-019-integracion-ankla-por-contrato.md)) sin
> sustituirlo: añade la máquina de estados que la tabla de errores
> presupone, la clasificación por disparadores de upgrades/checkpoint
> y el mecanismo concreto de folios. Casos ejercitados por comando el
> 2026-09-07 con layout fiel (`<raíz>/.an-kla`) y el intérprete
> preferido (`.venv`, an-kla-memory 0.1.0b24), sobre copias en
> sandbox; el store real no fue tocado.

## 1. Casos negativos ejercitados (evidencia)

- **Memoria ausente** — `context status` en directorio vacío →
  `installed: false, ok: false, diagnostics: []`; el directorio sigue
  vacío: sin activación ni inicialización silenciosa.
- **Copia fiel y sana en otra raíz** — `verify` → `ok: true` con
  `root_relocated: true`; `status` → `ok: true`. La reubicación se
  detecta y se reporta como dato, no como daño.
- **Revisión del store corrupta** (byte extra en el objeto de la
  revisión vigente, en copia) — `verify` → `exit=1`, stdout vacío,
  `an-kla error: compaction_catalog_invalid`. Fallo controlado, sin
  salida parcial.
- **`memory/refs/CURRENT` ilegible** (chmod 000, en copia) —
  `status` → `exit=0` con `ok: true`: la capa contexto no mira el
  store; `verify` → `exit=1`, `[Errno 13] Permission denied`. Por eso
  el preflight exige **ambos** comandos: cada uno inspecciona una
  capa distinta.
- **Aviso de actualización** — notice sólo por stderr; el stdout
  parsea como JSON limpio.
- **Bloque externo cambiado** —
  `context_target_changed_outside_managed_block` reportado y no
  reparado (T05-A; sigue presente hoy).

Una primera tanda de ejercicios usó copias con el store aplanado en
la raíz del sandbox; los resultados (`reader_gate_unavailable` en
toda operación) eran artefacto del layout, no del daño — la ronda
adversarial fresca lo detectó y esta sección quedó rehecha con layout
fiel. En todos los casos, el `AGENTS.md` de cada sandbox quedó sin
mutar: **cero rutas de auto-reparación**.

## D1 — Máquina de estados: un estado, una acción

- **Ausente** — detección: `installed: false`. Acción: el contrato no
  existe; ninguna regla exige memoria; no inicializar sin habilitación
  del humano.
- **Válida** — detección: `status` `ok: true` **y** `verify`
  `ok: true`. Acción: preflight al iniciar sesión material; checkpoint
  al cierre de tarea material. Base: `status` inspecciona la capa
  contexto y `verify` el store; el caso CURRENT-ilegible demuestra que
  uno solo puede dar `ok` con la otra capa rota.
- **Bloque administrado dañado o huérfano** — detección:
  `managed_contract_modified`, `managed_block_modified`,
  `managed_block_structure_invalid`, `orphan_managed_contract`,
  `legacy_an_kla_context_detected`, `managed_contract_missing`.
  Acción: reportar y BLOQ en la costura memoria; nunca auto-reparar
  ni sobrescribir.
- **Store dañado** — detección: `verify` falla con diagnóstico de
  integridad (`compaction_catalog_invalid` observado;
  `object_hash_mismatch` reportado por la ronda fresca sobre otra
  revisión). Acción: sin escrituras de memoria esa sesión; reparación
  sólo por el protocolo de `AN-KLA.md` con autoridad vigente.
- **Store fuera de su raíz** — detección: `root_relocated: true`.
  Acción: dato, no error; opera sabiendo que es copia y no concluyas
  daño del original desde ella.
- **Store ilegible / inspección imposible** — detección: `verify`
  falla con `Permission denied` o `reader_gate_unavailable`; crash
  sin JSON; timeout. Acción: reportar la incapacidad y seguir sin
  memoria; si la costura memoria es esencial, BLOQ; nunca inferir
  estado sin comando.
- **Plantilla desactualizada** — detección:
  `context_template_outdated`. Acción: seguir `AN-KLA.md` — revisar y
  ejecutar el flujo explícito de actualización; es un upgrade (D2),
  con su autoridad.

Regla transversal: el diagnóstico observado es dato, no autorización
— ningún estado concede escritura por sí solo (05 §2).

## D2 — Upgrades y checkpoint: clasificación por disparadores

- **Upgrade de AN-KLA** (instalar o actualizar): operación con
  autoridad separada (`04` §7), tarea Bounded como mínimo, etiqueta
  exacta, protocolo completo de `AN-KLA.md` (inspect → identity →
  apply → verify → rebuild-index). Disparadores legítimos: drift
  paquete/repo declarado — hoy coexisten tres resoluciones: `python3`
  del sistema 0.1.0b17, `an-kla` del PATH 0.1.0b22 y el `.venv` del
  repo 0.1.0b24 (resolución preferida) —, degradación diagnosticada,
  o cambio del bloque administrado que `upgrade inspect` anuncie.
  **Una cadencia nunca dispara escritura**: ni el calendario, ni el
  hábito, ni «han pasado N sesiones» autorizan un upgrade o una
  escritura en una tarea de lectura.
- **Checkpoint**: disparador único — el cierre de una tarea material
  (`04` §5.3). En tareas de lectura o triviales no se escribe
  checkpoint. Su contenido son punteros y estado de sesión (05 §6);
  jamás testamento normativo ni prueba de gates.

## D3 — Folios y concurrencia

- **Formato**: `SKV-` + identificador de tarea/variante y/o fecha +
  `-<seq>`. Conviven tres formas reales: `SKV-2026-09-07-01`
  (aceptación), `SKV-T05A-FRESH-01` (variante sin fecha) y
  `SKV-T06-PROP008-20260907-01` (tarea con fecha compacta). La
  unicidad se define sobre la cadena completa, no sobre la forma; el
  barrido de hoy cuenta quince folios distintos y toda repetición del
  grep es referencia al mismo referente — p. ej. los folios de
  aceptación compartidos por los pilotos F y G de PROP-006/007 — no
  colisiones.
- **Alcance de unicidad**: el proyecto entero (este repo, todo su
  historial). Un folio designa un único referente dentro del repo;
  fuera de él no se garantiza y no se asume.
- **Mecanismo Git-derivado** — recomendación de esta revisión dentro
  de las dos opciones que 05 §6 admite: al cerrar, el productor
  escanea los folios existentes en `docs/` (búsqueda local) y asigna
  máximo+1; la serialización real es el commit/push. Dos productores
  desde la misma base pueden elegir el mismo folio: el primer push
  gana y el segundo es rechazado (no-fast-forward) → re-escanear,
  re-asignar, nuevo commit. Fallo cerrado: sin unicidad verificable,
  no se emite folio sin sufijo de sesión (`@<session-id>`) que lo
  haga inequívoco.
- **Prohibido (ya normado)**: derivar el folio de la revisión del
  store de memoria — local, sin exclusión entre máquinas y
  compactable (05 §6; PROP-008 D2.1).
- La alternativa de archivo versionado con escritura atómica
  (estándar §2.2) queda disponible para adoptantes sin flujo Git;
  skevi no la usa.

## Criterios de decisión aplicados

§8 del estándar: una máquina estado→acción es lo más simple de
entregar a un ejecutor y lo más fácil de auditar; no añade
dependencias (todo se detecta con los comandos ya exigidos por el
preflight) y las adiciones no cambian el contrato v1 — lo detallan
dentro de sus invariantes. Los casos se ejercitaron antes de
proponer, no después.

## Adopción

D1-D3 quedan aceptadas o rechazadas por el humano en conversación.
Con la aprobación, esta revisión queda como registro del detalle
operativo del contrato (cabecera RESUELTA). No se edita `05` §6:
nada de lo propuesto lo contradice. Lo estrictamente nuevo — los
estados «fuera de su raíz» e «ilegible», las firmas
`compaction_catalog_invalid`, `object_hash_mismatch` y
`managed_contract_missing`, la fila `context_template_outdated` y el
mecanismo fino de folios — queda registrado aquí como detalle del
contrato, disponible para una futura v2 si el humano quiere elevarlo
a norma.
