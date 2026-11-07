# AUDIT-proposal-identifiers — IDs inequívocos para propuestas duplicadas

> **Estado:** RESUELTA — O-A aceptada por el humano (2026-09-07, en
> conversación): espacio de nombres por hogar sin renumerar; la serie
> local conserva el ID desnudo y la propuesta del issue #28 se cita
> `PROP-006@#28`. Sin edición ni comentario en el issue. Este
> documento queda como registro del esquema; inventarios en §1.
> **Origen:** plan AUDIT-2026-09-07, tarea T07 (REQ-AUD-06). Colisión
> detectada el 2026-09-07: el número `PROP-006` designa dos propuestas
> legítimas y distintas. Inventarios en §1; esquema propuesto en §2.

## 1. Inventario (evidencia, 2026-09-07)

### 1.1 Dos propuestas con el mismo número

| | PROP-006 local | PROP-006 del issue #28 |
|---|---|---|
| Título | Reportes de agente en dos capas con bloque de trazabilidad | Versionado de plantillas de adopción y gate anti-drift |
| Hogar | `docs/history/PROP-006-decision-2026-09-07.md` | `github.com/kristhianmanue1/skevi/issues/28` (OPEN) |
| Estado | ADOPTADA (vía ADR-016) | en deliberación |
| Tema | formato de reportes, trazabilidad, folios | MANIFEST de plantillas, registro del consumidor, anti-drift |
| Origen | instrucción directa del humano (2026-09-07) | agente externo (Prime Agent, ronda ~2026-09-02) |

Causa raíz: el issue #28 fue redactado como continuación de la serie
local — su «PROP-005 D1» es la PROP-005 local («Salida de Alpha»,
`docs/history/PROP-005-decision-2026-09-07.md`) — pero la serie local
asignó el 006 (y luego 007 y 008) sin barrer los issues abiertos.

### 1.2 Referencias entrantes a «PROP-006» desnudo (grep, 2026-09-07)

Once referencias entrantes, **todas** del sentido local — verificadas
una a una: `ADR-015:45` (polaridad de capas), `adr/00-INDICE.md:20`
(origen de ADR-016), `ADR-016:7`, `ADR-019:10` (folio), plan `:188`
(dice «PROP-006 local» explícito), `PROP-007` ×4 (dossier, `model`,
piloto F1-F4), `PROP-008` ×2 (folio pendiente). No cuentan como
entrantes el título propio del documento histórico ni las menciones de
esta propuesta. Cero referencias locales al sentido del issue: T07/T09
lo citan como «issue 28», nunca como «PROP-006».

Observación colateral, sin reescritura: `ADR-015:45` dice «PROP-006,
en deliberación» — cierto al escribirse (previo a ADR-016); es
registro histórico y no se toca.

### 1.3 Riesgo si no se resuelve

T09 (reconciliación de plantillas) trabaja sobre la propuesta del
issue; citarla como «PROP-006» chocaría con la adoptada ADR-016 y sus
once referencias. Buscar `PROP-006` hoy devuelve ambos sentidos en
repos remotos y bifurcaciones, aunque no en este árbol.

## 2. Propuesta: espacio de nombres por hogar, sin renumerar

- **Serie local** (respaldada en `docs/history/PROP-NNN-*.md`):
  identificador desnudo `PROP-NNN`. `PROP-006` local conserva el
  número y sus once referencias: **cero reescritura histórica**.
- **Propuestas con hogar en el tracker**: se citan calificadas —
  `PROP-006@#28` para este repo; `PROP-NNN@<owner/repo>#<n>` si el
  hogar es otro repo. Enlace canónico: la URL del issue.
- **Búsqueda sin ambigüedad**: `PROP-006@` encuentra las calificadas;
  la desnuda con frontera (`rg 'PROP-006([^@0-9]|$)'`) encuentra sólo
  la local.
- **Regla hacia adelante**: antes de asignar un `PROP-NNN` local,
  barrer `gh issue list` (una llamada de lectura) y la serie local;
  si un issue reclama el número, la propuesta local toma el siguiente
  libre y el issue conserva el suyo calificado.
- **Alternativas descartadas**: renumerar el issue a PROP-009 (edita
  evidencia externa, exige autorización y siembra la próxima
  colisión); renombrar la serie local (rompe ADR-015/016 y once
  referencias verificadas).

## 3. Aplicación tras decisión

**Decisión registrada:** O-A aceptada por el humano en conversación
(2026-09-07). Este documento queda como registro del esquema y T09
cita `PROP-006@#28`. Sin comentario ni edición en el issue #28; si se
quiere informar al autor externo, será una operación separada con su
autorización específica. Ningún archivo local cambia de nombre.
