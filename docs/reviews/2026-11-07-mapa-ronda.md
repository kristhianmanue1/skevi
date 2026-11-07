# Ronda adversarial — mapa de orientación (MI-1 ejecutada)

Objeto: docs/mapa-orientacion.md (nuevo) y dos diff de `README.md` (fila
de la tabla de hogares, línea 34; corrección de la deriva de
`reading_path`, HV-1), sobre `main` `4277454` con cambios sin commit.
Revisó una sesión fresca del mismo proveedor (GLM), sin contexto de
autoría; sólo lectura, con validación de sintaxis mediante el parser real
de mermaid v11 en directorio temporal fuera del repo.

Veredicto: **fix-and-retry** — y el reintento se ejecutó: los cinco
hallazgos se corregiron y se reverificaron antes de este registro,
incluido el control positivo del render (los tres fences VALID con el
parser real).

## Hallazgos y disposición

1. [BLOCKER] Un punto y coma en la descripción del estado `CERRADA`
   rompía el render de `stateDiagram-v2` (separador de sentencias).
   Cerrado: sustituido por coma; fences 1–3 VALID con parser real.
2. [HIGH] Las glosas Z1/Z2/Z3 invertían ADR-017 (Z1 no es lectura ni Z3
   integración: Z1 es commit/ramas locales, Z2 push/merge/tags con
   dossier, Z3 quién ejerce el gate). Cerrado: etiquetas fieles al ADR y
   arista del lote corregida (Z3 acepta el folio; el lote habilita Z2).
3. [MED] La cifra 1620 se atribuía sólo a ADR-025, cuyo texto fija 1000.
   Cerrado: el nodo cita ADR-025 y ADR-042, y la fuente de D2 también.
4. [LOW] IDs en español pese al contrato declarado. Cerrado: BATCH,
   DEFINED, IN_PROGRESS, VERIFIED, CLOSED, STOPPED.
5. [LOW] Punteros parciales (01 §1-2, E1-E6 sin ADR-045, OP sin
   AGENTS.md). Cerrado: «— 01» a secas; (ADR-014, ADR-045);
   (01 §5, AGENTS.md).

## Capa técnica

```text
id = SKV-MAPA-RONDA-20261107-01
date = 2026-11-07
time_utc = 06:25:52Z
head_sha = 4277454aec56b17b90d295792da8e1844ad6db1f
model = GLM-5.3 zai-coding-plan; revisor fresco (self-declared; not proof)
STATE = OK
GATE = ronda adversarial sobre docs/mapa-orientacion.md y los diff de
README.md en 4277454 con cambios sin commit; 1 BLOCKER, 1 HIGH, 1 MED
y 2 LOW; los cinco corregidos y reverificados antes de este registro
(fences 1-3 VALID con parser mermaid v11 real).
EVIDENCE
- parser mermaid v11 antes de la correccion -> fence 3 INVALID por ; -> pass
- parser mermaid v11 tras la correccion -> fences 1, 2 y 3 VALID -> pass
- grep de ADR-nnn del mapa vs docs/adr/MANIFEST.json -> 0 faltantes -> pass
- grep ^TAREA y conteo de fences en el mapa -> 0 y 3 pares -> pass
- grep «1000 líneas» en README.md tras HV-1 -> 0 coincidencias -> pass
- wc -l README.md -> 176 (techo 300) -> pass
- git diff --stat HEAD sobre los 9 de la ruta de lectura -> vacío -> pass
- python3 scripts/check_plans.py -> OK; 11 planes; E1-E6 -> pass
- python3 scripts/check_sizes.py -> OK; ruta de lectura 1620/1620 -> pass
- python3 -m unittest discover -s tests -> 296 tests OK -> pass
PENDING = render visual en GitHub diferido al primer push del PR
(verificación humana en publicación, como declara MI-1)
DECISION = fix-and-retry
OPERATIONS = ejecución de MI-1..MI-3 y HV-1 (orden del Operador); ronda
de solo lectura; validación con mermaid+jsdom instalados en directorio
temporal fuera del repo; sin efectos Git
AUTHORITY = Operador 2026-11-07: lote SKV-LOTE-20261107-01 aceptado y
ejecutado (PR #87, merge 4277454); orden «MI-1..MI-3 + HV-1 (Recomendado)»
RISK = revisor del mismo proveedor y familia que el autor; filesystem
compartido; el render final sólo es verificable en GitHub
report_sha256 = 0c40c5d098bb07de66433ff2171ba0775e8a6a1b0ba226ce80e0444489f0a28e
```

Límite declarado: revisor de contexto fresco del mismo proveedor salvo
que el Operador designe otro. El render visual en GitHub queda como
verificación humana diferida al primer push, como declara MI-1.
