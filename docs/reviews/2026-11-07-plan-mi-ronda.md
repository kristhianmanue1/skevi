# Ronda adversarial — PLAN MI (mapa de orientación)

Objeto: docs/plans/2026-11-06-mapa-orientacion.md, redactado sobre
`main` `74a4714c074af49b5bd3045f74de3510c2bae3ce` (con PLAN HV y su
registro aún sin commit). Revisó una sesión fresca del mismo proveedor
(GLM), sin contexto de la conversación que redactó el plan; sólo lectura
y comandos de sólo-lectura.

Veredicto: **proceed**. La ronda verificó las ocho filas del mapeo de
especificaciones contra sus fuentes, reprodujo la aritmética exacta de
la ruta (1334 + 286 = 1620/1620, holgura cero) y confirmó que ningún
gate local valida un render mermaid. Halló tres MED y cuatro LOW; los
siete se cerraron en el plan antes de este registro.

## Hallazgos y disposición

1. [MED] El criterio «los tres fences renderizan» no era determinista ni
   ejecutable sin efectos Git (sin herramienta mermaid local). Cerrado:
   grep mecánico de tres fences con pares abrir/cerrar; el render visual
   queda como verificación humana diferida a la primera publicación.
2. [MED] La verificación de MI-3 (`git diff --stat` sin HEAD, sólo cinco
   archivos) dejaba pasar cambios preparados y ediciones en
   `worst_case_of`. Cerrado: `git diff --stat HEAD` sobre los nueve
   archivos de la ruta, y el Produce alineado.
3. [MED] D1/D3 dibujaban ronda y cierre sin los punteros que gobiernan
   su salida (ADR-016 dos capas, ADR-037 registro). Cerrado: añadidos a
   ambos diagramas y a D2 el trinquete (ADR-025).
4. [LOW] Sobrecitación de ADR-044 (commit/tags/releases no son su
   dominio). Cerrado: push/merge por ADR-044; commit/tags/releases por
   AGENTS.md §Autoridad por operación.
5. [LOW] «IDs estables (ADR-015)»: el ADR norma idioma, no estabilidad.
   Cerrado: estabilidad declarada como decisión de este plan.
6. [LOW] DoD decía «cuatro gates» sin vía operativa para check_templates.
   Cerrado: tres gates (sizes, plans, reports) y unittest; check_templates
   declarado no aplicable a v1 (sin cambio de manifiesto).
7. [LOW] Faltaban ADR-043 (D1) y el trinquete (D2) como contexto de
   arranque para agentes. Cerrado: añadidos.

## Capa técnica

```text
id = SKV-MI-RONDA-20261107-01
date = 2026-11-07
time_utc = 06:04:28Z
head_sha = 74a4714c074af49b5bd3045f74de3510c2bae3ce
model = GLM-5.3 zai-coding-plan; revisor fresco (self-declared; not proof)
STATE = OK
GATE = ronda adversarial sobre docs/plans/2026-11-06-mapa-orientacion.md
en 74a4714 con el plan sin commit; 3 MED + 4 LOW, los siete cerrados
en el plan antes de este registro; ningun BLOCKER ni HIGH.
EVIDENCE
- python3 scripts/check_plans.py -> OK; 11 planes; E1-E6 -> pass
- check_plans sobre el archivo explicito de PLAN MI -> OK -> pass
- python3 scripts/check_sizes.py -> OK; ruta de lectura 1620/1620 -> pass
- python3 scripts/check_reports.py -> OK -> pass
- python3 -m unittest discover -s tests -> 296 tests OK -> pass
- ronda de contexto fresco (hallazgos 1-7) -> 0 BLOCKER, 0 HIGH -> pass
- ADR-nnn citados en el plan vs docs/adr/MANIFEST.json -> 0 faltantes -> pass
- correcciones 1-7 aplicadas antes de este registro -> diff revisado -> pass
PENDING = MI-1..MI-3 sin orden de ejecucion; render visual del mapa
diferido a la primera publicacion (hallazgo 1)
DECISION = proceed
OPERATIONS = redaccion de PLAN MI y este registro; ronda de solo
lectura; sin efectos Git
AUTHORITY = Operador 2026-11-06: analizar a fondo la integracion,
mapear especificaciones, realizar plan y ronda adversarial; ejecucion
de MI-1..MI-3 no emitida
RISK = revisor del mismo proveedor y familia que el autor; filesystem
compartido
report_sha256 = bc21eb157f6e0a033d4c221f9b5518233605beb7e32fc3a70a17234f24c065a0
```

Límite declarado: revisor de contexto fresco del mismo proveedor salvo
que el Operador designe otro; la capa técnica lo registra. La ejecución
de MI-1..MI-3 no fue ordenada: cada tarea declara la autoridad que
exige.
