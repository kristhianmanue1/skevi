# Verificación de procedencia upstream — PROP-010 §1.1

## Capa humana

PROP-010 afirmaba que la copia local del plugin Engineering 1.2.0 coincide
exactamente con una revisión pública concreta, que la licencia es Apache-2.0,
que no hay `NOTICE` y que `engineering/` no se movió después. Ninguna ronda
pudo comprobarlo: las tres lo dejaron `inconclusive` porque el material vivía
fuera del alcance de lectura. El Operador aportó el bundle dentro del
repositorio el 2026-09-18 y autorizó consultar GitHub oficial.

Los catorce archivos coinciden por SHA-256, uno a uno, con el árbol
`engineering/` de la revisión declarada. La licencia existe y es Apache-2.0;
no hay `NOTICE`. Nueve commits tocaron ese directorio y el último es
precisamente la revisión copiada: no hay nada posterior.

**Esto acredita procedencia, no dependencia.** Skevi no copia código de ese
plugin ni lo sigue: destila criterios y los reescribe con sus propias
garantías. La comprobación sirve para que §3.1 pueda atribuir con exactitud de
dónde se leyó, no para cumplir obligación alguna de redistribución — no hay
redistribución. El bundle **no se versiona** en este repositorio: hacerlo sí
sería redistribuir material de terceros, y además vendorizaría una dependencia
en un corpus que declara no tener ninguna.

## Capa técnica

```text
id = SKV-PROV-PROP010-20260918-01
date = 2026-09-18
time_utc = 12:03:45Z
head_sha = fc58b5838d88802c418960c55e73567f769e4c9d
model = Claude Opus 5 (self-declared)
STATE = OK (provenance verified against the upstream repository)
GATE = Close limit 1 of PROP-010 7: verify the upstream provenance claims of 1.1 with reproducible evidence.
EVIDENCE
- Local bundle docs/proposals/externals/Engineering-1.2.0-v38.zip, extracted outside the repository -> 14 files, matching the file list claimed in 1.1 -> pass
- gh api repos/anthropics/knowledge-work-plugins/git/trees/58da91d19dac075bc4d6dc2071500eeba3178c4b?recursive=1 -> engineering/ holds exactly those same 14 paths -> pass
- Per-file SHA-256 of the local bundle against the upstream blob contents at that revision -> 14 match, 0 differ -> pass
- LICENSE at that revision -> present at repository root, Apache License, 212 lines, with unrelated text appended at the end, as 1.1 described -> pass
- NOTICE at that revision -> absent, so Apache-2.0 4(d) does not apply -> pass
- gh api repos/anthropics/knowledge-work-plugins/commits?path=engineering -> 9 commits; the newest is 58da91d (2026-05-19); none afterwards as of today -> pass
- Cadence start date -> first commit is 2026-02-24 by committer date; PROP-010 1.1 says 2026-02-23 -> fail
- Redistribution -> none: the bundle is not versioned here and the distillation copies no code -> pass
PENDING = Correct the 2026-02-23 date in PROP-010 1.1. Nothing else within this record.
DECISION = proceed
RISK = Verification is of the bundle supplied by the Operator against the public repository today; it does not prove how that bundle was obtained. GitHub was read over the network with the Operator's authorization.
report_sha256 = fd1dfa4893b02dcd3260f731d584a34eb084948b4510688bef2bba7a8bce5bbd
```
