# Dossier HV-4 — El doble commit del auto-hospedaje

**El problema, con evidencia de hoy mismo.** Cada salto de versión de una
familia obliga a dos commits: el commit fuente no puede contener su propio
SHA, y `test_sources_point_to_the_last_bump_of_each_family`
(tests/test_check_manifests.py:186-205) exige que `source` de
`.skevi/*-installed.json` cargue el SHA del último commit que tocó el
manifiesto. Hoy volvió a pasar: fuente `a82a4dd` → espejos `52d0482`. El
precedente histórico es `df1b4e0` → `329e2b6`.

**Opción 1 — Retirar los espejos del repo fuente.** Borrar
`.skevi/installed.json`, `.skevi/corpus-installed.json` y
`.skevi/scripts-installed.json`; se conserva `templates/skevi/*-installed.json`
(invariante ADR-039) y `TemplateExamplesStayCurrentTests`. Puntos de
contacto: `.github/workflows/skevi-gate.yml:51-56` (los tres pasos de
`check_templates` del CI), `README.md:67-68` (el dogfood declarado) y
`SelfInstalledRecordsStayInSyncTests` (tests/test_check_manifests.py:155-205).
Coste: ADR nuevo que revise el dogfood de ADR-034 (issue #64), edición de CI,
README y tests. Riesgo: el mecanismo de espejo deja de ejercitarse en el
propio repo — la señal de drift sólo la vería el adoptante, tarde.

**Opción 2 — Eximir el SHA en auto-hospedaje (recomendada).** Mantener
los espejos y el CI intactos; aceptar en
`test_sources_point_to_the_last_bump_of_each_family` que, cuando el origen
es el propio repo, `source` cargue `@HEAD` simbólico, porque la igualdad
de versión y de todos los digests ya la custodia
`test_versions_and_digests_match_source_manifests` en el mismo commit.
Coste: ADR nuevo que revise ADR-031 para este caso acotado y la edición del
test. Riesgo: debilita la procedencia cerrada exactamente en el caso en que
menos importa (el origen es el repo que se acaba de verificar), pero es una
excepción que hay que mantener acotada y declarada.

**M1 (aceptación verificable), integrable en cualquiera.** La aceptación
por folio puede registrarse como comentario del PR contra el SHA clavado
—ya ocurrió así en #87 y #88— y la protección de rama la vuelve
verificable. No exige elegir entre 1 y 2; puede adoptarse sola.

**Recomendación:** opción 2, por ser quirúrgica, conservar el dogfood en
CI y eliminar el segundo commit; M1 como práctica estándar independiente.

## Capa técnica

```text
id = SKV-HV4-DOSSIER-20261107-01
date = 2026-11-07
time_utc = 11:52:08Z
head_sha = 52d0482b4b9a03ea83baf3cc8fa65d0f3d02f96a
model = GLM-5.3 zai-coding-plan (ejecutor; self-declared; not proof)
STATE = PARTIAL
GATE = dossier de opciones HV-4: doble commit del auto-hospedaje; dos
opciones con puntos de contacto y recomendacion; decision del Operador
pendiente. Evidencia fresca: el propio salto de hoy repitio el patron
(fuente a82a4dd -> espejos 52d0482).
EVIDENCE
- git log del salto de hoy -> fuente a82a4dd, espejos 52d0482 -> pass
- precedente historico df1b4e0 -> 329e2b6 -> mismo patron -> pass
- tests/test_check_manifests.py:186-205 -> source = ultimo bump -> pass
- .github/workflows/skevi-gate.yml:51-56 -> check_templates x3 -> pass
- README.md:67-68 -> registro .skevi y CI como dogfood -> pass
PENDING = decision del Operador: opcion 1 (retirar espejos) u opcion 2
(eximir SHA en auto-hospedaje con ADR que revise ADR-031); integracion
de M1 (aceptacion por folio verificable en el PR) segun eleccion
OPERATIONS = redaccion del dossier; sin efectos Git
AUTHORITY = orden del Operador 2026-11-07 «adelante con pendientes»
sobre la tarea HV-4 del plan ya entregado
RISK = dossier de ejecutor que recomienda; la decision es del Operador
report_sha256 = 81f68afbe13369d0d649babf16c8b2795ca88417c5f827638de3cf4d8c1ac850
```

La decisión es del Operador. Este dossier no cierra HV-4: su step 2
(registrar la decisión) queda pendiente.
