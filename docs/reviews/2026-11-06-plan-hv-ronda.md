# Ronda adversarial — PLAN HV (hoja de ruta verificada)

Objeto: docs/plans/2026-11-06-hoja-de-ruta-verificada.md, redactado sobre
`main` `74a4714c074af49b5bd3045f74de3510c2bae3ce` (árbol limpio más el
plan sin commit). Revisó una sesión fresca del mismo proveedor (GLM), sin
contexto de la conversación que redactó el plan ni del análisis previo;
sólo lectura y comandos de sólo-lectura.

Veredicto: **proceed**. La ronda reprodujo con comandos todos los hechos
verificables de la sección de análisis, refutó la omisión alegada de
planes cerrados bajo E5 (las rutas a proposals en planes viven en líneas
de creación, exentas) y halló dos MED y tres LOW. Los cinco se cerraron
en el plan antes de este registro; HV-7 queda marcado al existir este
registro y reverificar los gates.

## Hallazgos y disposición

1. [MED] El Produce de HV-3 omitía su salto de corpus (v10 o viaje
   conjunto con el v9 de HV-2) y los espejos `.skevi/` que exigen sus
   punteros en `04` (PROP-010 §3.4, T07). Cerrado: el Produce declara
   corpus/v10 —o viaje conjunto— y los espejos.
2. [MED] Steps de HV-7 marcados `[x]` antes de que existiera este
   registro y la reverificación posterior. Cerrado: desmarcados en la
   corrección; se marcan al publicarse este registro con los gates en
   verde.
3. [LOW] «13 referencias en 5 sellados» sin acotar: son 15 ocurrencias
   en 7 sellados contando ADR-003:19 (define el directorio) y ADR-027:89
   (ruta histórica ya rota). Cerrado: la frase del plan acota el
   universo y cita ambas menciones.
4. [LOW] La fila README.md:34 describe `docs/proposals/` como hogar y
   quedaría huérfana tras el traslado de HV-3. Cerrado: HV-3 la declara
   en su Permitido.
5. [LOW] El step 2 de HV-3 verificaba tres de los cuatro gates (sin
   `check_templates`, justo el que detectaría el drift del hallazgo 1).
   Cerrado: el criterio lista los cinco checks.

## Capa técnica

```text
id = SKV-HV-RONDA-20261106-01
date = 2026-11-06
time_utc = 03:39:30Z
head_sha = 74a4714c074af49b5bd3045f74de3510c2bae3ce
model = GLM-5.3 zai-coding-plan; revisor fresco (self-declared; not proof)
STATE = OK
GATE = ronda adversarial sobre docs/plans/2026-11-06-hoja-de-ruta-verificada.md
en 74a4714 con el plan aun sin commit; 2 MED + 3 LOW, los cinco cerrados
en el plan antes de este registro; ningun BLOCKER ni HIGH.
EVIDENCE
- python3 scripts/check_plans.py -> OK; 10 planes; E1-E6 -> pass
- check_plans sobre el archivo explicito de PLAN HV -> OK -> pass
- python3 scripts/check_sizes.py -> OK; ruta de lectura 1620/1620 -> pass
- python3 scripts/check_reports.py -> OK -> pass
- python3 -m unittest discover -s tests -> 296 tests OK -> pass
- ronda de contexto fresco (hallazgos 1-5) -> 0 BLOCKER, 0 HIGH -> pass
- correcciones 1-5 aplicadas antes de este registro -> diff revisado -> pass
PENDING = ejecucion de HV-1..HV-6 sujeta a la autoridad que cada tarea declara
DECISION = proceed
OPERATIONS = redaccion de PLAN HV y este registro; ronda de solo
lectura; sin efectos Git
AUTHORITY = Operador 2026-11-06: tomar contexto del trabajo a medias,
crear plan con analisis y correr ronda adversarial; HV-1..HV-6 sin
orden de ejecucion
RISK = revisor del mismo proveedor y familia que el autor; filesystem
compartido
report_sha256 = d1225c4e1b332383451e968740e147b0bfb585c85ca3b4e25692c18d3682277b
```

Límite declarado: revisor de contexto fresco del mismo proveedor salvo
que el Operador designe otro; la capa técnica lo registra. La ejecución
de HV-1..HV-6 no fue ordenada: cada tarea declara la autoridad que
exige.
