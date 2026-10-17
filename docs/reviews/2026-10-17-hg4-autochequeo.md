# Ronda adversarial del autochequeo de plantillas (HG-4) y su disposición

Evaluador con contexto fresco (subagente, solo lectura). Veredicto:
**fix-and-retry**; las tres correcciones se aplicaron y los checks
afectados se repitieron en verde. La propia ronda declaró que no se
requiere ronda nueva: mismo alcance, correcciones locales.

## Disposición de hallazgos

| Hallazgo | Severidad | Disposición |
|---|---|---|
| El step de CI sólo fiscaliza drift de **versión** (digest adulterado y lag no-breaking dan exit 0 por diseño); el nombre prometía más | MED | **Corregido**: step renombrado («drift de versión; espejo de digests en unittest») y comentario del workflow reescrito; la evidencia de cierre queda clasificada por clase de drift en este registro |
| La prueba de `source` no verificaba lo que su docstring prometía (HEAD pasaba) | MED | **Corregido**: ahora compara contra `git log -1 --format=%H -- <manifiesto>` por familia — la procedencia ADR-031 por familia quedó sellada |
| Comentario de paridad hook↔CI quedó inexacto («los mismos comandos») | LOW | **Corregido**: comentario reescrito; añadir las tres invocaciones al hook sería triple redundancia (unittest ya muerde el espejo) |
| Primera prueba que exige `.git` (tarball sin metadata fallaría) | LOW | **Aceptado**: el runner canónico corre sobre clones (CI y hook); sin skipUnless hasta que importe |
| `files` de `.skevi/` es espejo declarativo, no copias en disco | LOW | **Aceptado y declarado aquí** para el lector futuro |
| `import subprocess` local + regex duplicada de `SOURCE_RE` | LOW | **Corregido de paso**: la prueba endurecida ya no usa la regex |

## Evidencia por clase de drift (quién muerde qué)

- Edición de artefacto sin bump → `check_sizes` (manifiesto vs disco, preexistente).
- Digest/schema/customized del registro estancados → **unittest** (espejo exacto; verificado en sandbox: FAILED).
- Lag **breaking** de versión → **step de CI** (`check_templates`, BLOQ exit 1; verificado).
- Lag no breaking → aviso compatible exit 0 **por diseño** (señal = versión, no contenido).

## Capa técnica

```text
id = SKV-HG4-20261017-01
date = 2026-10-17
time_utc = 14:19:08Z
head_sha = 35c5b5a6404ca9a989ef5c1f4feedab4bd500de9
model = GLM-5.3 (self-declared)
STATE = PARTIAL
GATE = HG-4 self-check delivered; round fix-and-retry, its three fixes applied and affected checks re-run green.
EVIDENCE
- fresh-context subagent round -> fix-and-retry: 2 MED, 4 LOW, no blockers -> pass
- drift by class (round sandboxes) -> digest tamper: unittest FAILS; non-breaking lag: exit 0 by design; breaking lag: BLOQ exit 1 -> pass
- record==manifest==disk equality per family, recomputed sha256 -> exact, three families -> pass
- git log -1 per manifest -> sources are each family last bump (a6bfa33, a6bfa33, 6f82ce3), not HEAD -> pass
- python3 -m unittest discover -s tests -> Ran 272 tests OK -> pass
- python3 scripts/check_sizes.py -> OK 156 files, reading path 1592/1600, gate/v10 -> pass
- CI step syntax and placement per round -> consistent with sibling steps, before unittest -> pass
PENDING = publication of this branch under standing authorization.
DECISION = proceed
OPERATIONS = local commit on feat/hg4-autochequeo-plantillas; push, PR and merge under standing publication authorization.
AUTHORITY = human instruction 2026-10-17 (adelante con tus recomendaciones; commits, push, PR y merge aprobados para la sesión).
RISK = .skevi/ files are a declarative mirror of source manifests, not copies on disk (documented); installed_at is informative only.
 = 782d3e8b8eb716151b68a8f7396c75510eec8e30640b4f988e76a3bf60189013
report_sha256 = 13e18ac0b7613869b2f329ecd31945dcd34f51a6f8e8dbaa0131ced4630e6f8d
```

Hash: UTF-8, LF, sin newline final y sin la línea `report_sha256`.
Partido de PARTIAL: publicación inmediata bajo autorización vigente.
