# PLAN HG — Holgura del gate y salida a los issues 61, 63 y 64

Autoriza: instrucción humana del 2026-10-17, «corre ronda adversarial para
tus propuestas y afinar el plan e inicia». Clase Architectural (ADR-013).
Fuente única del DoD de las tareas. Las rondas y la disposición de cada
veredicto viven en
[../reviews/2026-10-17-plan-gate-ronda.md](../reviews/2026-10-17-plan-gate-ronda.md),
no aquí (ADR-037).

```text
PLAN HG — Holgura del gate y salida a los issues 61, 63 y 64
Autoriza: instrucción humana 2026-10-17; ronda adversarial P1-P8 Proceed
Clase de tarea: Architectural (ADR-013)
Base: rama docs/plan-gate-holgura, sobre ADR-038 ya aplicado (HG-1)

TAREA HG-1 — Deuda §6 de ruta de lectura (cerrada hoy)
  Consumes: ADR-038; deuda §6 de `docs/ai-agent-guide/05-memoria-del-agente.md`
  Produce: `skevi-gate.json` con 05 y AN-KLA.md en reading_path, limite 1600
  Steps:
  - [x] Declarar espina y limite con ADR propio — verificación: gate OK con
        ruta 1592/1600 en el commit 815fe9a; fila nueva en el indice de ADRs

TAREA HG-2 — Partir el cluster de check_sizes (#61)
  Consumes: issue #61; ADR-027 (identidad del gate); ADR-032 (partición
    anticipada por escrito); suite `tests/test_check_sizes.py` en 773/800 y
    `tests/test_check_templates.py` en 771/800
  Produce: gate repartido por responsabilidad sin perder la copia única del
    adoptante, con gate/v9
  Steps:
  - [x] Decidir el corte (paquete scripts/ frente a módulos) y su ADR —
        verificación: ADR-039 declara el corte por materia (dominio de
        manifiestos a check_templates) y por qué no rompe ADR-006
  - [x] Partir tamaños, canónicos, ruta, manifiestos e identidad —
        verificación: 266 tests OK (aislados y en discovery) y ningún
        archivo del cluster sobre 800: 654/606/647/156/733/771
  - [x] Subir gate/v9 con fecha regenerada — verificación: sin aviso de
        vejez (2026-10-17) y `scripts/MANIFEST.json` con digests vigentes
        verificados por test y por sha256 independiente (ronda)

TAREA HG-3 — Chequeo de coherencia root_markdown ↔ reading_path (#63)
  Consumes: salida de HG-2; issue #63; ejemplo 1400 del adoptante lalia-akuo
  Produce: BLOQ con remedio cuando AN-KLA.md esté en root_markdown y falte
    del presupuesto de lectura
  Steps:
  - [x] Test RED: root_markdown declara un markdown de raíz ausente de la
        espina — verificación: fallo observado por la razón correcta
        (exit 0 != 1) antes de tocar producción
  - [x] Implementar el chequeo con mensaje que cite el remedio —
        verificación: test en verde (25 en el módulo, 269 en la suite) y
        skevi mismo pasa (1592/1600, gate/v10 breaking con migración)

TAREA HG-4 — Autochequeo de plantillas en casa (#64.2)
  Consumes: issue #64 §2; ADR-020 (registro en el consumidor); ADR-031
    (formato cerrado de source); ADR-034 (workflow como gate autoritativo)
  Produce: crea `.skevi/installed.json` con digests reales y step de
    `scripts/check_templates.py` en el workflow de CI
  Steps:
  - [x] Crear el registro con source apuntando a la revisión de la última
        actualización de plantillas, no al HEAD — verificación: invocación
        canónica del gate en verde contra templates/skevi
  - [x] Añadir el step al workflow — verificación: CI en verde con el
        chequeo corriendo y fallando ante un drift introducido a propósito

TAREA HG-5 — Familia adr/v1 de manifiesto (#64.1)
  Consumes: salida de HG-2; issue #64 §1; ADR-028 (familias); ADR-032
  Produce: crea docs/adr/MANIFEST.json con listado exacto y digests de los
    ADRs inmutables
  Steps:
  - [x] Generar el manifiesto y registrarlo en el gate — verificación: BLOQ
        ante un ADR editado y OK con el listado exacto del directorio
  - [x] Documentar la capa sellada frente a la no sellada — verificación:
        el manifiesto declara qué protege y history/reviews quedan fuera
        por vida útil, no por olvido

TAREA HG-6 — Claims legibles por máquinas: frontera primero (#64.4)
  Consumes: issue #64 §4; project-manifest.yaml no_ofrece (cesión de claims
    a argos); ADR-026 como precedente de precisión de frontera
  Produce: decisión escrita entre precisar la cesión o descartar la idea
  Steps:
  - [x] Deliberar la frontera con argos antes que la mecánica —
        verificación: la decisión cita la cesión exacta y dice qué haría
        skevi que hoy no hace (nada de extracción de evidencia)
  - [x] Sólo si procede: NO procede — wontfix por frontera con argos
        verificación: cifras fechadas, no copiadas (ADR-025 p4), y gate
        en verde

TAREA HG-7 — Frontera de memoria agnóstica (P7)
  Consumes: ronda P7 confirmada; ADR-019 intacto; sello corpus/v4 vigente
  Produce: §2 de 05 como condición de adopción para cualquier memoria
    local, con bump corpus/v5
  Steps:
  - [x] Redactar la PROP con §2 como condición y §1 como recomendación —
        verificación: la PROP no toca el contrato v1 de §6 (cambios, v2)
  - [ ] Tras aceptación: aplicar el cambio y sellar — verificación:
        digests nuevos en docs/MANIFEST.json y K4 sigue en pie (adoptante
        sin memoria cumple la norma completa)
```

DoD: cada paso verificado con su comando; rondas de contexto fresco por
tarea (disparador 4 de `04` §5.3: plantillas, manifiestos y gate son
interfaz hacia el adoptante); reporte técnico con hash reproducible por
cierre de tarea. Parada: cerradas HG-2..HG-7 o decisión del Operador de
recortar; ninguna tarea autoriza push, merge o release por sí misma.
