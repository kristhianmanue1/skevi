# AUDIT-publication-dossier — Dossier de publicación del programa

> **Tipo:** dossier de gate (T13, solicitado el 2026-09-07). Formato
> de dos capas (ADR-016; patrón PROP-007 D2). La operación de creación
> de PR fue autorizada en conversación («adelante con pr»); el merge NO
> está autorizado y queda propuesto, no ejecutado.

## Operaciones

| # | Operación | Estado |
|---|---|---|
| 1 | Commits locales del programa (13) y push de la rama `docs/adopt-authority-consistency` a origin | ejecutado y verificado por sesión: remoto = `f7f29e6` |
| 2 | PR `base: main` ← `compare: docs/adopt-authority-consistency` | autorizado («adelante con pr»); creado y verificado en sesión |
| 3 | Merge del PR a `main` | **no autorizado** — queda propuesto, no ejecutado |
| 4 | Tags, releases, borrado de ramas | no propuestos |

## Diff final (base `17413f1` → head `f7f29e6`)

- 13 commits; 28 archivos; +2418/−37; árbol limpio; cero trabajo ajeno
  (todos los commits son del programa AUDIT-2026-09-07 y sus
  adopciones: `git log 17413f1..HEAD`).
- Código: `scripts/check_sizes.py` (fail-closed en lecturas, +81/−),
  `tests/test_check_sizes.py` (+138, 11 pruebas nuevas, suite 62→73),
  `skevi-gate.json` (+3, binarios declarados), `project-manifest.yaml`
  (+7, fronteras PROP-007).
- Norma: ADR-018 y ADR-019 (nuevas), `00-INDICE` de ADRs, guía `00`,
  `04` §7 (upgrades con autoridad separada), `05` §6 (contrato
  `skevi/an-kla-integration v1`), AGENTS.md (remisión ADR-018; bloque
  administrado intacto).
- Registro: SPEC, plan, 7 propuestas, 6 reportes, deliberación T05,
  PROP-008 + decisión en `docs/history/`, closeout del programa.
- `templates/`: sin cambios (verificado: 0 archivos en el diff).

## Evidencia de verificación

- `check_sizes` → OK, 88 archivos; `check_plans` → OK, 2 planes;
  suite → 73 tests OK; hook pre-push en verde en cada push de la rama.
- Revisión fresca del conjunto (closeout): proceed; 0/87 enlaces
  rotos; autoridad humana intacta.
- `git ls-remote` → `main = 17413f150d08e1e65b72f70a858104505950e751`
  (sin cambio), `docs/adopt-authority-consistency = f7f29e6`.

## Riesgos y reversión

- Adoptantes que consuman la guía o el gate verán comportamiento más
  estricto (fail-closed) y el contrato de memoria condicional — cambios
  de interfaz normativa deliberados (closeout §2, compatibilidad).
- El merge es un commit de merge reversible (`git revert -m 1`); la
  rama se preserva; `main` no se fuerza ni se reescribe.

## Decisión solicitada

Merge del PR [#34](https://github.com/kristhianmanue1/skevi/pull/34)
(verificado: OPEN, MERGEABLE, head `f2363cd`) con merge commit (patrón
vigente #31-#33), sin squash ni rebase, sin tag ni release. Sin
aceptación registrada, la operación no existe.
