# Piloto: F0→F3 de punta a punta sobre proyecto nuevo (infosalud)

> Primer ciclo completo F0→F3 sobre un proyecto real desde cero — el
> requisito que el README §Estado exigía para salir de Alpha y que
> `piloto-orbitanova-2.md` dejaba como "siguiente sesión sugerida".
> Documento de evidencia, no norma: si algo aquí contradice el estándar
> o la guía vigentes, ganan ellos (`AGENTS.md` §Prioridad).

## Qué se ejecutó

Proyecto consumidor: `kristhianmanue1/infosalud` (CLI Python stdlib-only
que cataloga fuentes de Infosalud/DIS-DPM-IMSS). Ejecutado el 2026-09-01
en una sola sesión; reportado por el propio ejecutor en el issue #25 de
este repositorio y verificado a distancia (vía `gh api`, sin clonar) el
mismo día — la verificación de este registro es independiente del
reporte.

### Línea de tiempo observada (commits del adoptante)

```text
17:56  3f70f08  cascarón inicial (F2)
17:56  c6d8c4b  análisis F0 y diseño F1 (specs, contratos, ADR-001..006)
18:09  710d3ed  contrato cli-infosalud v1.1 (SPEC-1..3) con correcciones
                de ronda adversarial
18:11  6e5b64d  merge F2+F3 (autorización humana explícita)
18:12  144f7bb  fix validación URL (:8080) + enmienda de contrato
18:14  e459575  alta de 23 fuentes reales (autorización humana)
18:41  5aaf774  adopción AN-KLA Memory beta.19 (ADR-007)
19:04  927d951  guardias de memoria (scripts/mem, hook pre-commit,
                test de fences)
19:09  —        issue #25 publicado en skevi; cerrado 19:27 (opción D,
                PR #26)
19:48+  —       evolución posterior: ADR-008 vigencia, ADR-009
                diccionario, ADR-010 borrador, ADR-011 export CSV/SQLite,
                ADR-012 listados históricos (21:53)
```

### Estado del F0/F1 en disco (verificado)

- `docs/f0-analisis.md` (327 líneas): EV-1…EV-15, REQ-1…REQ-9 con
  criterios, PREGUNTA-1 resuelta por decisión humana (autorización DPM,
  commit `68a2753`).
- `docs/f1-specs.md` (254 líneas): SPEC-1…SPEC-8, 41 bloques
  DADO/CUANDO/ENTONCES.
- `docs/f1-contratos.md` (201 líneas): `cli-infosalud v1.1` con sección
  «Enmiendas 2026-09-01, ronda adversarial F3».
- 12 ADRs al momento de la verificación (7 al cerrarse el issue; los
  ADR-008…012 son posteriores — el proyecto siguió evolucionando).
- Adopción de plantillas: `.skevi/` en la raíz con
  `architecture-overview.md` y `usage-guide.md`.

### Errata del issue #25, anotada

El issue dice «23 evidencias EV-*»; en disco hay **15** (EV-1…15). El 23
es el número de **fuentes de datos** dadas de alta (`e459575`). El resto
de cifras del issue (9 REQ, SPEC-1…3, 7 ADRs al cierre) sí cuadraba con
el estado del momento.

### Ronda adversarial F3

El issue cita 2 BLOCKER: un esquema cerrado que no rechazaba campos
sobrantes y verificaciones pre-cargadas que envenenaban la máquina de
estados. En disco quedan las **correcciones** — enmiendas del contrato
(`710d3ed`, `144f7bb`), guardas de esquema cerrado (`f58f9fe`) — pero no
la transcripción de la ronda (vivió en conversación y memoria del
adoptante). Lección para la guía: la ronda deja rastro obligatorio en un
artefacto, no sólo en la sesión.

### AN-KLA como memoria del agente (ADR-007 del adoptante)

Frontera de verdad declarada: `docs/` y Git canónicos; la memoria guarda
estado de sesión, índices y punteros, nunca copia de documentos
normativos. Wrapper `scripts/mem` que empaqueta `plan-write →
commit-write-plan` con guardias (hook pre-commit + test de fences). La
coexistencia `.skevi/` + bloque gestionado an-kla en `AGENTS.md` corrió
sin conflicto. Este uso conjunto motivó el `05-memoria-del-agente.md` de
skevi (PR #26) y el issue #102 de an-kla-memory.

## Qué validó este piloto y qué no

| Validó | No validó |
|---|---|
| F0→F3 completo de punta a punta sobre proyecto nuevo, con autorizaciones humanas por operación | La promoción Alpha→estable en sí: exige este registro más una deliberación explícita (PROP-005) |
| F2 cascarón desde cero con build/run/test verificable antes de F3 | Clasificación de tarea (Spike/Bounded/Architectural): el proyecto nació completo, no entró a un repo existente |
| Ronda adversarial con contexto fresco encontrando BLOCKER reales con RED→GREEN | Transcripción de la ronda en disco del adoptante (ver lección arriba) |
| Adopción de Skevi como `.skevi/` + guía en el adoptante, con gates locales vía hooks | Ratchet y compactación de memoria: sin ejercitarse |
| Coexistencia de Skevi y AN-KLA en el mismo adoptante sin segunda fuente de norma |  |

## Consecuencias para Skevi

- `docs/proposals/PROP-005-salida-de-alpha-y-cierre-issue-25.md`:
  promoción de versión, resolución formal de los puntos 4 y 5 del #25 y
  degradación de la referencia externa del `05` §4.
- El criterio de salida de Alpha («un piloto F0→F3 completo con
  evidencia») queda cubierto por este registro; la decisión es de la
  deliberación, no de este documento.

## Procedencia

- Reporte del ejecutor: issue #25 de skevi (PR #26 cierra con el
  `05-memoria-del-agente.md`).
- Verificación independiente de este registro: `gh api` sobre
  `kristhianmanue1/infosalud` (contents y commits, 2026-09-01), commits
  citados arriba; sin clonar ni ejecutar nada del adoptante.
- Memoria an-kla de skevi: facts del dogfooding A-4 y adopción PROP-004.
