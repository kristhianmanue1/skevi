# ADR-048: exención de SHA literal en el auto-hospedaje del registro

Estado: aceptado (confirmación literal del Operador, 2026-11-07:
«Confirmo ADR-048», con el texto de la regla delante).

## Contexto

ADR-031 fijó la procedencia cerrada del registro de instalación: el campo
`source` de `*-installed.json` carga `<origen>@<sha>` — el SHA del último
commit que tocó el manifiesto de su familia, sellado por
`SelfInstalledRecordsStayInSyncTests::test_sources_point_to_the_last_bump_of_each_family`
(tests/test_check_manifests.py). En el repositorio fuente esa exigencia
es matemáticamente insatisfiable en un solo commit: un commit no puede
contener su propio SHA, de modo que cada salto de versión obliga a un
segundo commit que sólo re-escribe los espejos. Precedentes: `df1b4e0` →
`329e2b6` (gate/v13) y `a82a4dd` → `52d0482` (corpus/v9, documentado en
`docs/reviews/2026-11-07-hv4-dossier-doble-commit.md`).

## Decisión

Sólo para el auto-hospedaje —cuando el origen declarado es el propio
repositorio— el campo `source` acepta la referencia simbólica `@HEAD`. La
procedencia no se debilita en lo que importa: la igualdad de versión y de
todos los digests SHA-256 por archivo entre espejo y manifiesto fuente
sigue siendo obligatoria dentro del mismo commit
(`test_versions_and_digests_track_their_source_manifests`), y el CI
coteja los tres espejos en cada corrida.

Para todo adoptante —origen externo— la procedencia cerrada de ADR-031
queda intacta: SHA literal del último bump de la familia.

## Consecuencias

- Un solo commit por salto de versión en el repo fuente; desaparece el
  commit doble.
- El dogfood de CI se conserva íntegro (los tres pasos de
  `check_templates` de `skevi-gate.yml`).
- El espejo pierde el SHA-ancla legible; la trazabilidad del bump queda
  en el historial Git del manifiesto fuente, que el test sigue
  consultando.
- El test del último bump se ajusta: exige SHA literal exacto sólo
  cuando el origen no es el propio repositorio; `@HEAD` se acepta
  únicamente en auto-hospedaje, y `check_templates` lo rechaza cuando el
  origen declarado no coincide con el remote de este repositorio
  (fail-closed sin Git).
- Coste: `check_templates` y la suite deben distinguir auto-hospedaje de
  adopción externa por el origen declarado.

## Procedencia

Decisión del Operador del 2026-11-07 (opción 2 del dossier HV-4,
presentada con el texto de la regla; registro
`docs/reviews/2026-11-07-decisiones-operador.md`).
