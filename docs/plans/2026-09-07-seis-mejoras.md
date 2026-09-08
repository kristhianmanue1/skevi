# PLAN M6-2026-09-07 — Seis mejoras derivadas del análisis crítico

> Artefacto de escala (ADR-010): nueve bloques de tarea, varias sesiones.
> Dueño de los criterios (DoD y steps) frente a cada TAREA que lo referencie
> (`../ai-agent-guide/04-ejecucion-y-verificacion.md` §1).
> Autoriza: [SPEC-M6](../specs/SPEC-M6-2026-09-07-seis-mejoras.md).

```text
PLAN M6-2026-09-07 — Seis mejoras derivadas del análisis crítico
Autoriza: SPEC-M6-2026-09-07 (REQ-M6-01 … REQ-M6-07)
Clase de tarea: Architectural — crear un plan multi-tarea (01 §2, ADR-013)
```

## Restricciones globales (verbatim de la SPEC que autoriza)

- «No adoptar una propuesta por haberla planificado: cada tarea cierra con
  evidencia o con descarte trazable.» — SPEC-M6 §No objetivos
- «No añadir dependencias: todo script nuevo es stdlib de Python, ejecutable
  con el 3.9.6 del sistema (EV-M6-6).» — SPEC-M6 §No objetivos
- «Sin push, merge, PR, tags, releases ni operaciones destructivas.»
  — SPEC-M6 §No objetivos
- «P3 (REQ-M6-03) no se redacta antes de resolver su frontera con
  `praxis-dev`: ver PREGUNTA-M6-1.» — SPEC-M6 §No objetivos

## Orden y dependencias

`T00 → T01 → {T02, T03} → T04 → T06 → T07 → T08`.
`T05` entra en cualquier punto tras la resolución de PREGUNTA-M6-1; si la
respuesta es (B), su salida es una remisión, no una regla. `T07` registra
criterio de entrada; su ejecución depende de PREGUNTA-M6-2 y puede quedar
abierta sin invalidar el resto.

## Tareas

```text
TAREA T00 — Base, rama y SPEC
  Consumes: instrucción humana 2026-09-07; guía `docs/ai-agent-guide/01-analisis-y-requerimientos.md`
  Produce:  crea `docs/specs/SPEC-M6-2026-09-07-seis-mejoras.md`
  Steps:
  - [x] Árbol limpio y commit base fijados — verificación: `git status --short`
        vacío y `git rev-parse HEAD` = b400b85
  - [x] Rama de trabajo aislada (estándar §4.1) — verificación:
        `git branch --show-current` = feat/seis-mejoras-2026-09-07
  - [x] SPEC con REQ-M6-01..07, no objetivos, EV-M6-* y PREGUNTA-M6-1/2 —
        verificación: python3 scripts/check_sizes.py sale OK

TAREA T01 — Plan completo verificable
  Consumes: `docs/specs/SPEC-M6-2026-09-07-seis-mejoras.md`; `templates/plan-de-implementacion.md`
  Produce:  crea `docs/plans/2026-09-07-seis-mejoras.md` (este archivo)
  Steps:
  - [x] Nueve bloques TAREA con Consumes/Produce/Steps y criterio por step —
        verificación: python3 scripts/check_plans.py sale OK
  - [x] Plan bajo el límite de plantilla derivada (300 líneas, estándar §3.4) —
        verificación: wc -l sobre este plan < 300

TAREA T02 — P1: cotejo con estándares de industria nombrados
  Consumes: REQ-M6-01; `docs/estandar-diseno-software-github.md`
  Produce:  crea `docs/crosswalk-estandares.md` — documento informativo,
            sin autoridad normativa nueva
  Steps:
  - [x] Tabla por control de NIST SSDF (PO/PS/PW/RV), OWASP ASVS y OWASP LLM
        Top 10, con columnas cubre / cubre parcialmente / no cubre y la
        sección de Skevi que lo satisface — verificación: cada fila «cubre»
        cita sección existente, comprobado con `grep -n` sobre el estándar
  - [x] Sección «Lo que Skevi no cubre» enumerando los huecos, cada uno con
        su dueño (Skevi, otro proyecto del ecosistema, o nadie) —
        verificación: cada dueño distinto de Skevi resuelve a una línea
        literal de `project-manifest.yaml` §no_ofrece
  - [x] Declarar el documento como evidencia, no norma, y su vida útil
        (caduca al cambiar la versión del estándar externo citado) —
        verificación: encabezado con tipo y versión de cada fuente externa
  - [x] Gate y tamaños — verificación: python3 scripts/check_sizes.py OK

TAREA T03 — P5: presupuesto de ruta de lectura obligatoria
  Consumes: REQ-M6-05; `docs/estandar-diseno-software-github.md` §3.4
  Produce:  crea ADR-021; amplía `scripts/check_sizes.py` y `skevi-gate.json`
  Steps:
  - [x] RED: test que falla porque el gate no mide la ruta acumulada —
        verificación: python3 -m unittest discover -s tests falla con el
        motivo esperado, salida registrada en el reporte
  - [x] GREEN: clave opcional `reading_path` (lista de rutas + límite) en
        `skevi-gate.json`, fail-closed — sin clave no comprueba nada (ADR-006)
        — verificación: suite en verde y python3 scripts/check_sizes.py OK
  - [x] Caso negativo: ruta que excede su límite produce BLOQ con código de
        salida distinto de cero — verificación: test dedicado en `tests/`
  - [x] ADR-021 con alternativas descartadas y checklist de cierre de
        `docs/ai-agent-guide/02-specs-adr-contratos.md` §3.3 —
        verificación: `docs/adr/00-INDICE.md` actualizado y `grep -rn ADR-021`
        resuelve en estándar §3.4, AGENTS.md y README
  - [x] Límite declarado por escrito en el estándar §3.4 (no heredado en
        silencio) — verificación: `grep -n "ruta de lectura"` sobre el estándar

TAREA T04 — P2: gate estructural de reportes de dos capas
  Consumes: REQ-M6-02; `docs/adr/ADR-016-reportes-en-dos-capas.md`
  Produce:  crea `scripts/check_reports.py`, su suite en `tests/` y ADR-022
  Steps:
  - [x] Contrato del gate en el formato de `docs/ai-agent-guide/02-specs-adr-contratos.md`
        §4: entrada, salida, errores, invariantes, compatibilidad —
        verificación: cada campo declarado existe luego en la firma real,
        comprobado con `grep -n` sobre el script (check CONTRATO↔código, 04 §9)
  - [x] RED: suite que falla contra un script inexistente y contra reportes
        malformados (clave ausente, marca inválida, hash irreproducible) —
        verificación: salida del RED registrada en el reporte de la tarea
  - [x] GREEN: comprobar forma de la capa técnica — claves STATE, GATE,
        EVIDENCE, PENDING; bloque de trazabilidad id/date/time_utc/head_sha/
        report_sha256/model; cada línea de evidencia con pass|fail|inconclusive
        — verificación: suite en verde
  - [x] `report_sha256` reproducible en forma canónica (UTF-8, LF, sin newline
        final, excluida la línea del hash) — verificación: test que recalcula
        el hash de un reporte fijo y compara
  - [x] Fail-closed vía clave `reports` en `skevi-gate.json`; sin clave, cero
        comprobaciones; clave con tipo inválido es error (patrón de
        `scripts/check_plans.py`) — verificación: dos tests, uno por rama
  - [x] Declarar explícitamente que el gate comprueba forma y nunca honestidad
        del reporte — verificación: docstring del script y línea en el ADR
  - [x] ADR-022 con alternativas y checklist de cierre —
        verificación: `docs/adr/00-INDICE.md` actualizado; README y AGENTS.md
        listan el comando nuevo; python3 scripts/check_sizes.py OK

TAREA T05 — P3: superficie de herramientas del ejecutor (condicional)
  Consumes: REQ-M6-03; PREGUNTA-M6-1 resuelta; `docs/estandar-diseno-software-github.md` §6
  Produce:  según la decisión — sección nueva del estándar + ADR, o remisión
            escrita en `project-manifest.yaml` §no_ofrece y en §6
  Steps:
  - [x] Registrar la respuesta humana a PREGUNTA-M6-1 con su fecha y opción
        elegida — verificación: la decisión aparece citada en el ADR o en la
        remisión; sin ella la tarea permanece BLOQ y no se redacta nada
  - [x] Si (A) o (C): reglas de allowlist de herramientas, egress de red,
        sandbox, servidores MCP y secretos en ventana de contexto, cada una
        con procedencia y razón — verificación: `grep -n` muestra procedencia
        en cada viñeta nueva; python3 scripts/check_sizes.py OK
  - [x] Si (B): remisión sin regla nueva, en el manifiesto y en §6 —
        verificación: grep -n praxis-dev sobre el manifiesto muestra la
        línea nueva y ninguna regla se añadió al estándar
  - [x] Ronda adversarial de frontera: la salida no invade lo que
        `project-manifest.yaml` §no_ofrece cede a otro proyecto —
        verificación: reporte con decisión proceed | fix-and-retry | escalate

TAREA T06 — P4: componentes con salida no determinista (LLM)
  Consumes: REQ-M6-04; `docs/ai-agent-guide/04-ejecucion-y-verificacion.md` §5.3 disparador 2
  Produce:  crea `docs/ai-agent-guide/06-componentes-con-llm.md` y ADR-023
  Steps:
  - [x] Procedimiento de verificación no determinista: golden set versionado,
        criterio por umbral en vez de igualdad, y qué es RED cuando el test
        no es binario — verificación: cada apartado remite a la regla de
        `docs/ai-agent-guide/04-ejecucion-y-verificacion.md` §3 que precisa,
        sin contradecirla
  - [x] Presupuesto de contexto y coste declarado en el contrato de tarea —
        verificación: el campo nuevo aparece en el bloque TAREA de
        `docs/ai-agent-guide/04-ejecucion-y-verificacion.md` §1 o se declara
        opcional por escrito
  - [x] Salida del modelo tratada como dato no confiable en la frontera
        (estándar §2.4 y principio 7) — verificación: `grep -n` muestra la
        remisión al principio, no una copia parafraseada
  - [x] Alta en `docs/ai-agent-guide/00-INDICE.md` (tabla de archivos y orden
        de lectura) sin romper el presupuesto de T03 — verificación:
        python3 scripts/check_sizes.py OK con la clave `reading_path` activa
  - [x] ADR-023 con alternativas y checklist de cierre — verificación:
        `docs/adr/00-INDICE.md` actualizado

TAREA T07 — P6: criterio de entrada del piloto fuera del monocultivo
  Consumes: REQ-M6-06; `docs/history/piloto-infosalud.md`; `project-manifest.yaml`
  Produce:  crea `docs/proposals/M6-piloto-fuera-del-monocultivo.md`
  Steps:
  - [x] Enunciar las variables del monocultivo actual con evidencia por
        piloto — verificación: cada fila cita un archivo real de
        `docs/history/` comprobado con `wc -l`
  - [x] Criterio de entrada: al menos dos variables rotas a la vez (otro
        autor humano, CI remoto real, lenguaje compilado, legacy grande) —
        verificación: criterio escrito en forma falsable, no en adjetivos
  - [x] Declarar qué afirmación del corpus quedaría respaldada al ejecutarse
        y cuál seguiría sin respaldo — verificación: cita literal de la línea
        de `project-manifest.yaml` §fronteras_de_confianza que limita hoy
  - [x] Registrar como propuesta, no como norma, y anotar PREGUNTA-M6-2 como
        bloqueo externo — verificación: el archivo vive en `docs/proposals/`
        y ninguna regla del estándar o la guía lo referencia como obligatorio

TAREA T08 — Cierre: ronda fresca, gates y transferencia
  Consumes: salidas de T02..T07
  Produce:  crea `docs/reviews/2026-09-08-seis-mejoras.md`
  Steps:
  - [x] Ronda adversarial en contexto fresco sobre el conjunto (disparador 4
        de `docs/ai-agent-guide/04-ejecucion-y-verificacion.md` §5.3: gate
        copiable con consumidores no controlados) — verificación: reporte con
        hallazgos, verificaciones y decisión proceed | fix-and-retry | escalate
  - [x] BLOCKER y HIGH corregidos; MED corregido o justificado por escrito —
        verificación: cada hallazgo con estado cerrado | abierto | aceptado
  - [x] Gates y suite completos tras las correcciones — verificación:
        python3 scripts/check_sizes.py; python3 scripts/check_plans.py;
        python3 -m unittest discover -s tests los tres OK
  - [x] Enlaces internos verificados tras mover o crear archivos —
        verificación: cada ruta relativa nueva resuelve; python3 scripts/check_plans.py OK
  - [x] Conciliación por tarea con evidencia, decisión o descarte, y lista de
        seguimiento abierto — verificación: T00..T07 aparecen todas, ninguna
        cerrada por checkbox sin evidencia
  - [x] Reglas del método saltadas, declaradas al cierre — verificación:
        sección propia en el reporte, o la frase «ninguna» con su razón
```

## DoD del plan

- Cada tarea T00–T08 ejecutada o descartada por decisión trazable; ningún
  cierre por checkbox sin evidencia de comando.
- python3 scripts/check_sizes.py, python3 scripts/check_plans.py y
  python3 -m unittest discover -s tests: los tres OK al cierre.
- Ronda adversarial de cierre con decisión `proceed` o `escalate`.
- Cero operaciones de autoridad separada sin autorización explícita y
  específica del humano (REQ-M6-07).
- T05 y T07 pueden cerrar como BLOQ por pregunta abierta sin invalidar el
  resto: su bloqueo es exógeno al ejecutor y se reporta como tal.
