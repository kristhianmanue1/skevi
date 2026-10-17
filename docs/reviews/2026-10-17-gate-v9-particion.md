# Ronda adversarial de la partición del gate (ADR-039, gate/v9) y su disposición

Evaluador con contexto fresco (subagente, solo lectura) sobre la rama
`feat/gate-v9-particion-manifiestos` antes de publicarla. Veredicto:
**fix-and-retry** — el refactor sólido, tres correcciones concretas
exigidas. Las tres se aplicaron y los checks afectados se repitieron en
verde; la condición del proceed quedó cumplida.

## Disposición de hallazgos

| Hallazgo | Severidad | Disposición |
|---|---|---|
| `tests/test_reading_path.py` cargaba `check_sizes` sin `scripts/` en `sys.path`: pasaba en discovery por efecto secundario de otro test y **fallaba aislado** (en HEAD pasaba) | HIGH | **Corregido**: `sys.path.insert` con comentario de procedencia; verificado aislado (22 tests OK) y los ocho módulos uno a uno en verde |
| ADR-039 afirmaba «las plantillas no cambian» mientras el cambio las sincronizaba por obligación (tests que custodian el BLOCKER del 2026-09-08 exigen ejemplo == fuente) | MED | **Corregido**: viñeta reescrita — el salto `plantillas/v10 → v11` es obligatorio y no breaking; añadida la nota del retiro de la exención `limits` |
| Exención muerta `"scripts/check_sizes.py": 870` en `skevi-gate.json`: permitía volver a crecer hasta 870 sin rojo, el riesgo que el PR dice cerrar | MED | **Corregido**: clave `limits` retirada; el archivo vuelve al límite por defecto 800 (654 observado). Retirar no exige ADR; crear o subir sí (§3.4) |
| Escisión de identidad de módulos en la suite (dos instancias de `check_templates` por el patrón `spec_from_file_location` de `test_check_templates.py`) | LOW | **Abierto como seguimiento**: trampa pre-existente del patrón, hoy inocua; registrar la copia bajo nombre privado si se toca ese archivo |
| Fallback hardcodeado de `check_plans.py` (sin `exempt_names`) ahora más alcanzable vía `ModuleNotFoundError` | LOW | **Abierto como seguimiento**: hueco pre-existente, no fail-open (check_sizes revienta antes); alinear el fallback o documentarlo |

## Lo que la ronda atacó y no rompió

Paridad mecánica de la sección movida contra HEAD (idéntica salvo docstring
y un plegado de línea); mensajes y códigos de salida; import fraterno desde
cwd ajeno, `check_plans` y el hook `pre-push`; cadena completa de versiones
(`gate/v9` breaking con nota de migración, `plantillas/v11`, `corpus/v4`
intacto) y digests verificados por sha256 independiente; alias públicos sin
consumidores burlados; sin imports ni referencias muertos; cifras y
procedencia del ADR exactas.

## Capa técnica

```text
id = SKV-GATEV9-20261017-01
date = 2026-10-17
time_utc = 13:51:23Z
head_sha = c3584d222dcd7a2fd1f2da3ee772d6dab2357064
model = GLM-5.3 (self-declared)
STATE = PARTIAL
GATE = HG-2 partition implemented (ADR-039, gate/v9); round fix-and-retry, its three fixes applied and affected checks re-run green.
EVIDENCE
- fresh-context subagent round -> fix-and-retry: 1 HIGH, 2 MED, 2 LOW -> pass
- python3 -m unittest tests.test_reading_path isolated after fix -> Ran 22 tests OK -> pass
- each of the eight test modules run in isolation -> all OK -> pass
- python3 -m unittest discover -s tests -> Ran 266 tests OK -> pass
- python3 scripts/check_sizes.py -> OK 151 files, reading path 1592/1600, gate/v9 -> pass
- python3 scripts/check_plans.py -> OK 6 plans -> pass
- python3 scripts/check_reports.py -> OK 14 reports -> pass
- gate from foreign cwd (/tmp) per round -> OK exit 0 -> pass
- mechanical diff of moved section vs HEAD per round -> identical except docstring and one line fold -> pass
- independent sha256 of the four scripts vs scripts/MANIFEST.json per round -> exact match -> pass
- wc -l cluster -> 654 606 647 156 733 771, none over 800 -> pass
- grep limits skevi-gate.json -> 0 matches, dead 870 exemption retired -> pass
PENDING = publication of this branch under standing authorization; HG-3 next.
DECISION = proceed
OPERATIONS = local commit on feat/gate-v9-particion-manifiestos; push, PR and merge next under standing publication authorization.
AUTHORITY = human instruction 2026-10-17 (adelante con recomendaciones y permiso para publicar); round conditioned proceed on the three fixes, all applied and re-verified.
RISK = test_check_templates.py stays at 771/800 (untouched, own concern); check_plans hardcoded fallback predates this change and is now easier to reach (LOW, follow-up).
report_sha256 = 0fe9d24e2daded29f48f64b020cdf37b415f32626e17d8e6990ee90e2988814c
```

Hash: UTF-8, LF, sin newline final y sin la línea `report_sha256`.
Partido de PARTIAL: verificación local completa; publicación inmediata bajo
autorización vigente.
