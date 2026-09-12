# LANG — Idioma explícito y errores controlados

## Capa humana

Implementación local en `fix/language-policy-and-validation`, sobre `ffc7252`.
La norma conserva inglés estructural y pide declarar idioma de comunicación,
producto y comentarios. Una preferencia de conversación no cambia los
artefactos persistentes. ADR-029 registra la precisión; F0/F3 y la plantilla
la hacen operativa, sin detector automático de idiomas.

Los validadores rechazan campos ausentes y tipos incorrectos de schema sin
excepción cruda. RED: 34 errores antes del fix; GREEN: pruebas nuevas y
suite de 230 tests en verde. El refactor de reportes conserva imports y
argumentos públicos anteriores; su lógica ejecutable normalizada coincide
con la anterior. Los saltos a gate/v3 y plantillas/v3 son compatibles.

Los gates pasan con ruta de lectura 993/1000. Se conservó el metadato que
bloqueaba tamaños en un respaldo, sin añadir exenciones. Los cambios previos
de AN-KLA en AGENTS.md/AN-KLA.md no forman parte de este incremento.

Revisión fresca independiente: proceed, sin hallazgos bloqueantes.
Sin commit, push ni publicación.

## Capa técnica

```text
id = SKV-LANG-20260912-01
date = 2026-09-12
time_utc = 12:43:44Z
head_sha = ffc72520be5ffc50142969f6dc2f614bddac598c
model = GPT-6 (self-declared)
session = /root
STATE = OK (local implementation verified)
GATE = SPEC-LANG REQ-L1..L4 and PLAN LANG; local changes only, no publication.
EVIDENCE
- Baseline unittest discovery -> 224 tests passed -> pass
- RED: test_manifest_inputs before production fix -> 5 tests, 34 subtest errors (KeyError/TypeError), exit 1 -> pass
- GREEN: test_manifest_inputs after required-key/type checks -> 5 tests passed -> pass
- Compatibility: existing comparator tests -> 30 tests passed -> pass
- Refactor: normalized executable AST against post-fix snapshot -> identical except documented compatibility adapters -> pass
- Report imports: English entrypoint and legacy keyword calls -> identical results for valid, bad-hash and missing-layer inputs; aliases retained -> pass
- Full unittest discovery after fixes -> 230 tests passed -> pass
- Gate age test after version/date bump -> initially failed on a moving production date; fixed with explicit 2026-09-08 fixture, threshold unchanged -> pass
- Standard 3.1, F0, F3 and adoption template -> explicit human/product/comment choices; conversation preference does not mutate persistent policy -> pass
- ADR-029 cases 1..5 -> conversation override, stable error code, missing choice, external contract and Spanish comments resolved by standard 3.1 -> pass
- Previous HEAD installation records against new manifests -> exit 0, compatible notices for gate/v2 to v3 and plantillas/v2 to v3 -> pass
- check_sizes -> OK, reading path 993/1000, gate/v3; all manifests and file limits verified -> pass
- check_plans -> 5 plans verified -> pass
- check_reports including this record -> 6 reports verified, 2 exempt -> pass
- scripts/.DS_Store -> moved to recoverable temporary backup, SHA256 c747d7bbe83ae09333d3463e3b507cb2044b875a103fef4ed9cb81cf5dbce270 unchanged -> pass
- git diff --check -> exit 0 -> pass
- Independent fresh review -> proceed; no BLOCKER, HIGH or MED findings; legacy signatures and four CLI cases unchanged -> pass
PENDING = No work pending within local implementation scope. Commit, push, merge, tags, release and adopter migration are not authorized; no memory writes.
DECISION = proceed
RISK = Legacy public Spanish names remain as compatibility adapters; other legacy scripts are outside the rename scope. Gates validate structure, not language or truth. No LLM performance claim.
report_sha256 = a9710f6efba11a4c7fa6365931327d2a3287094b51a5ceee7146d83c181e9c1c
```

## Ronda adversarial

Revisor: `/root/review_language_final`, contexto fresco y solo lectura.
Hallazgos BLOCKER/HIGH/MED: ninguno. Se verificaron firmas legadas, salidas
de reportes existentes, cuatro casos CLI, compatibilidad de manifests y los
cinco casos de idioma. Decisión: proceed para el incremento local.
Límite residual: siete líneas libres de ruta; no se amplió el presupuesto.

## Evidencia auxiliar y límites

- Snapshot posterior al fix y anterior al refactor:
  `/private/tmp/skevi-lang-refactor-fvti0g0t/` (efímero).
- Respaldo recuperable del metadato:
  `/private/tmp/skevi-metadata-backup-wquf9ogt/.DS_Store` (efímero).
- La evidencia RED se observó antes de modificar producción; no se infiere
  de un test añadido después. La corrección simétrica de check_sizes se
  incluyó al reproducir el mismo acceso a campos ausentes durante la lectura.
- No se certifica cumplimiento de todos los adoptantes ni salud del remoto.
