# Decisiones del Operador — 2026-11-07 (sesión de pendientes)

Registro consultable de tres decisiones emitidas hoy por selección
explícita entre opciones cuyo texto contenía la regla:

1. **HV-3 (deadlock ADR-002↔ADR-040): opción A** — extender a las
   propuestas la doctrina de rutas históricas de ADR-036: el cuerpo
   sellado conserva la ruta de su fecha y sólo el índice actualiza.
   Ejecuta PROP-010 §8 (T01–T09). Se materializa en **ADR-047**, que
   requerirá confirmación literal antes de su commit fuente.
2. **HV-4 (doble commit del auto-hospedaje): opción 2** — eximir el SHA
   de `source` en auto-hospedaje (`@HEAD` simbólico) manteniendo
   versión y digests verificados en el mismo commit. Se materializa en
   **ADR-048** (revisión acotada de ADR-031) más el ajuste del test.
3. **HV-6 (docs/orchestration/): opción C** — re-scoplar como adaptador
   por host sin peso normativo. **Ejecutada en esta entrega**: ambos
   encabezados re-escopiados con la decisión citada y la comprobación de
   versiones de hoy (codex-cli 0.167.0, opencode 2.2.5, tmux 3.6a —
   presencia y versión, sin revalidación funcional).

El lote SKV-LOTE-20261107-03 fue aceptado y ejecutado en el mismo
intercambio (PR #89, merge `a1a32a7`).

## Capa técnica

```text
id = SKV-DECISIONES-20261107-01
date = 2026-11-07
time_utc = 12:09:24Z
head_sha = a1a32a764b2b086314c053342140f1e7ffa74cf0
model = GLM-5.3 zai-coding-plan (ejecutor; self-declared; not proof)
STATE = OK
GATE = registro de tres decisiones del Operador del 2026-11-07 emitidas
por seleccion explicita entre opciones con texto de regla; su ejecucion
se prepara en entregas propias (ADR-047 y ADR-048).
EVIDENCE
- lote 20261107-03 -> aceptado y ejecutado; PR #89 merge a1a32a7 -> pass
- HV-3 deadlock -> opcion A seleccionada (doctrina ADR-036 extendida) -> pass
- HV-4 doble commit -> opcion 2: eximir SHA en auto-hospedaje -> pass
- HV-6 orchestration -> opcion C seleccionada (adaptador por host) -> pass
- encabezados re-escopiados -> versiones hoy; sin revalidacion -> pass
PENDING = ADR-047 (doctrina de rutas historicas para propuestas) y ADR-048
(revision de ADR-031 para auto-hospedaje) requieren redaccion, ronda y
confirmacion literal antes de su efectividad; PROP-010 §8 (T01-T09)
depende de ADR-047
OPERATIONS = re-scopo de dos encabezados de docs/orchestration y este
registro; sin efectos Git
AUTHORITY = Operador 2026-11-07: «Opción A (Recomendado)», «Ambas
recomendaciones (Recomendado)» y «Acepto (Recomendado)» del lote 03,
seleccion explicita sobre opciones con el texto de la regla
RISK = la seleccion de opciones respalda la decision de fondo; los ADR
que la materialicen deben citar este registro y confirmarse por texto
literal antes del commit fuente, conforme al precedente de ADR-045/046
report_sha256 = 068a6f0a95cdd3f00685d16d343310d38ebe2fdf08e3d0a7a77c88968781b570
```

Los ADR-047 y ADR-048 citan este registro como procedencia de la decisión
de fondo; su texto íntegro se confirma por frase literal del Operador
antes del commit que los sella, como en ADR-045 y ADR-046.
