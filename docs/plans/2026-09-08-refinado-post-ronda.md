# PLAN R1-2026-09-08 — Refinado tras la ronda sobre las recomendaciones

> Artefacto de escala (ADR-010): seis bloques de tarea sobre el seguimiento
> abierto del [registro de cierre M6](../reviews/2026-09-08-seis-mejoras.md).
> Autoriza: instrucción directa del humano del 2026-09-08 («adelante con
> recomendaciones refinadas»), tras una ronda adversarial que refutó cuatro de
> las siete recomendaciones originales con comandos.

```text
PLAN R1-2026-09-08 — Refinado tras la ronda sobre las recomendaciones
Autoriza: instrucción directa del humano, 2026-09-08
Clase de tarea: Architectural — crea un plan multi-tarea (01 §2, ADR-013)
```

## Restricciones globales

- Ninguna operación de autoridad separada sin autorización nueva: la del
  programa M6 cubrió su push, PR y merge, y no se extiende a este trabajo
  (`../ai-agent-guide/04-ejecucion-y-verificacion.md` §7).
- No se tocan `templates/skevi/`: cambiarlas dispara ADR-020.
- Sin dependencias nuevas; stdlib de Python.
- Los ADR son inmutables: una decisión que cambia produce un ADR nuevo, no
  una edición del anterior (`../ai-agent-guide/02-specs-adr-contratos.md` §3.2).

## Tareas

```text
TAREA R-T1 — Honestidad del presupuesto de lectura
  Consumes: `docs/adr/ADR-021-presupuesto-de-ruta-de-lectura.md`; estándar §3.4
  Produce:  crea ADR-025; actualiza el Estado de ADR-021 y el texto de §3.4
  Steps:
  - [x] Declarar que el techo de 1000 es un trinquete sobre lo observado y no
        una derivación, con la evidencia de que §3.4 sí deriva su 800 —
        verificación: grep -n "del orden de 2000" sobre el estándar devuelve la
        línea de la derivación existente, y ADR-021 no tiene ninguna equivalente
  - [x] Fijar la política de ajuste: subir el techo exige razón escrita y ADR
        nuevo, nunca una edición silenciosa — verificación: la regla aparece en
        §3.4 y el ADR la cita como procedencia
  - [x] Actualizar el Estado de ADR-021 a sustituido en su cláusula de techo,
        conservando su mecanismo — verificación: grep -n Estado sobre ADR-021
        muestra la referencia a ADR-025 y `docs/adr/00-INDICE.md` la registra
  - [x] Gate y suite — verificación: python3 scripts/check_sizes.py sale OK

TAREA R-T2 — AGENTS.md: punteros en vez de reenunciados
  Consumes: `AGENTS.md`; estándar §1 y §3.4
  Produce:  AGENTS.md con las reglas transversales citadas, no copiadas
  Steps:
  - [x] Sustituir por punteros los reenunciados de fail-closed, datos no
        confiables, evidencia y contención de tamaño, conservando la excepción
        local de autoridad, que sí es propia — verificación: cada viñeta
        conservada cita la sección del estándar que la contiene
  - [ ] NO CUMPLIDO, con decisión registrada — la ruta sube de 982 a 984: la
        compresión de AGENTS.md libera 4 líneas y la política que R-T1 añade a
        §3.4 consume 5. Buscado un segundo candidato el 2026-09-08: el único
        de tamaño en la ruta es §5.3-5.4 de 04 (63 líneas), que mezcla norma
        —«cada hallazgo lleva cuatro campos»— con ilustración; separarlas bien
        es tarea propia y hacerlo deprisa por veinte líneas arriesga perder
        reglas. Se deja abierto: el trinquete de ADR-025 hace su trabajo y
        el gate publica el margen vigente — verificación: python3 scripts/check_sizes.py
        publica la ocupación en su línea OK
  - [x] Gate — verificación: python3 scripts/check_sizes.py sale OK

TAREA R-T3 — Fronteras del manifiesto
  Consumes: `project-manifest.yaml`; PREGUNTA-M6-3 de `docs/specs/SPEC-M6-2026-09-07-seis-mejoras.md`
  Produce:  no_ofrece precisado; PREGUNTA-M6-3 resuelta; ADR-026
  Steps:
  - [x] Precisar la línea de autoridad a gobernanza, conformidad y perfiles de
        aseguramiento, dejando el mecanismo en Skevi — verificación: la línea
        nueva no contradice §4.3, §6.2, ADR-017 ni ADR-018, comprobado con grep
  - [x] Registrar que ninguno de los cinco planos cedidos reciproca, con la
        evidencia por proyecto — verificación: la evidencia distingue manifiesto
        ausente de manifiesto presente que no menciona a Skevi
  - [x] Declarar como frontera la integridad de artefactos publicados y los
        riesgos de modelo, hoy huecos sin dueño — verificación: los controles
        citados coinciden con los marcados sin cubrir en `docs/crosswalk-estandares.md`
  - [x] Marcar PREGUNTA-M6-3 resuelta con su opción y fecha — verificación:
        grep -n PREGUNTA-M6-3 sobre la SPEC muestra la resolución

TAREA R-T4 — Canal de reporte de vulnerabilidades
  Consumes: `docs/crosswalk-estandares.md` (RV.1 sin cubrir)
  Produce:  crea `.github/SECURITY.md`
  Steps:
  - [x] Escribirlo en .github/ y no en la raíz — verificación: en raíz el gate
        da BLOQ por Markdown suelto; en .github/ sale OK
  - [x] Actualizar la fila RV.1 del cotejo — verificación: la fila cita el
        archivo nuevo y el resumen se recuenta contra las filas

TAREA R-T5 — Exención de registros sin caducidad inventada
  Consumes: `docs/adr/ADR-022-gate-de-reportes-de-dos-capas.md`
  Produce:  ADR-022 con la vigencia de la exención declarada
  Steps:
  - [x] Declarar que la exención no caduca porque el hash de esos registros es
        permanente, y retirar cualquier disparador de archivado inexistente —
        verificación: grep -rn sobre el repo no muestra política de archivado
        de docs/reviews que respalde una caducidad

TAREA R-T7 — Identidad y autocaducidad del gate copiable
  Consumes: el barrido de adoptantes de esa sesión (documento retirado del merge); ADR-006; ADR-020
  Produce:  crea ADR-027; amplía `scripts/check_sizes.py`
  Steps:
  - [x] RED de identidad y umbral antes del código — verificación: los tests
        de identidad fallan por constantes inexistentes, y el de la línea BLOQ
        falla contra la primera implementación, que sólo la imprimía en OK
  - [x] GATE_VERSION y GATE_GENERATED_AT en las dos líneas de salida —
        verificación: python3 scripts/check_sizes.py muestra la identidad al
        pasar y al fallar
  - [x] Aviso de edad que no afirme la existencia de una versión nueva, sin
        red y sin alterar el código de salida — verificación: test dedicado
        que falla si el texto del aviso lo insinúa
  - [x] Umbral anclado en su frontera y constante mal editada tolerada —
        verificación: mutar GATE_STALE_AFTER_DAYS rompe la suite
  - [x] ADR-027 con alternativas y checklist de cierre — verificación:
        `docs/adr/00-INDICE.md`, `project-manifest.yaml` y `README.md`
        actualizados

TAREA R-T6 — Ronda fresca por archivo y cierre
  Consumes: salidas de R-T1..R-T5
  Produce:  crea `docs/reviews/2026-09-08-refinado-post-ronda.md`
  Steps:
  - [x] Ronda en contexto fresco acotada a los cierres del programa M6, por
        archivo y por hallazgo, no por rango de commits — verificación: el
        encargo nombra los archivos y los hallazgos, y el reporte responde
        cierre por cierre
  - [x] BLOCKER y HIGH corregidos; MED corregido o justificado — verificación:
        cada hallazgo con estado cerrado, abierto o aceptado
  - [x] Gates y suite completos — verificación: check_sizes, check_plans,
        check_reports y python3 -m unittest discover -s tests, los cuatro OK.
        check_templates queda fuera: exige --manifest y --installed
  - [x] Reglas del método saltadas, declaradas — verificación: sección propia
        en el reporte o la frase ninguna con su razón
```

## DoD del plan

- R-T1..R-T6 ejecutadas o descartadas por decisión trazable.
- `check_sizes`, `check_plans` y `check_reports` en verde, más la suite.
  `check_templates` exige `--manifest` y `--installed` y no se ejecuta sin
  argumentos: no forma parte del gate por omisión (ADR-020).
- Ronda fresca con decisión `proceed` o `escalate`.
- Cero operaciones de autoridad separada sin autorización nueva y específica.
- Los dos documentos de barrido del ecosistema (`M6-deriva-del-gate-copiable.md`, `M6-piloto-fuera-del-monocultivo.md`) se retiran de este merge, decisión humana 2026-09-08: nueve afirmaciones falsas en cinco rondas adversariales sobre el mismo modo de fallo. ADR-027 no depende de ellos y queda vigente; el censo de adopción queda pendiente, a rehacerse fuera de este ejecutor o con la lista de repos que el humano confirme.
