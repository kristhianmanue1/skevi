# SPEC-M6-2026-09-07 — Seis mejoras derivadas del análisis crítico

## F0 — Problema, resultado y autoridad

Problema: se sostuvo la hipótesis «Skevi no requiere mejoras: ya contiene lo
suficiente para llevar proyectos con agentes de IA con los mejores estándares
de la industria». El análisis crítico del 2026-09-07 la refutó con evidencia
del propio repositorio: (a) el manifiesto declara en `no_ofrece` que adoptarlo
no garantiza mejora y que los pilotos no generalizan; (b) no existe ningún
cotejo con un estándar de industria nombrado — NIST SSDF aparece una vez, en
un plan, rotulado «sin autoridad normativa nueva»; (c) las cuatro reglas de
mayor valor (ronda adversarial, RED, clase de tarea, autoridad por operación)
sólo las verifica el autorreporte del ejecutor, que §6.3 del estándar declara
prueba insuficiente; (d) hay huecos de contenido específicos de desarrollo con
agentes — evals, superficie de herramientas, presupuesto de contexto.

Resultado observable: seis mejoras con salida, dependencia y criterio de
entrada propios, ejecutadas o descartadas por decisión trazable; ninguna
adoptada por el solo hecho de haber sido planificada.

Fuente de habilitación: instrucción directa del humano del 2026-09-07
(«realiza plan para las 6 mejoras e inicia»). Habilita documentos, código
local y sus pruebas; **no** implica push, merge, PR, tags ni release.

Clase: **Architectural** — crear un plan multi-tarea es disparador por sí
solo (guía `01` §2, ADR-013). Base:
`b400b85c164827ecfb107363a2194c5c6635a9c7`; rama `feat/seis-mejoras-2026-09-07`;
árbol limpio verificado con `git status --short` (salida vacía).

Plan: [tareas, dependencias y aceptación](../plans/2026-09-07-seis-mejoras.md).

### Evidencia de entrada

```text
EV-M6-1: gates y suite en verde en la base | python3 scripts/check_sizes.py;
  check_plans.py; python3 -m unittest discover -s tests → OK; OK; 110 tests OK [pass]
EV-M6-2: cero cotejo normativo con estándares de industria | sobre la base
  b400b85, grep -rE '\b(OWASP|SLSA|SBOM|MCP|DORA)\b' sobre docs/ excluyendo
  docs/history/ (no normativo, AGENTS.md) → 0 coincidencias; sin excluirlo, 1
  —una mención de MCP en PROP-001, registro histórico— [pass]
  Corregido el 2026-09-08: la primera redacción declaraba un comando sin la
  exclusión, que no reproducía el resultado. Hallazgo de la ronda fresca;
  una evidencia que no se puede repetir deja de ser evidencia (§3.4).
EV-M6-3: NIST SSDF sólo informativo | grep -n NIST docs/plans/*.md →
  1 hit, bajo «Referencias informativas, sin autoridad normativa nueva» [pass]
EV-M6-4: sin método para salida no determinista | grep -rE '\bevals?\b' docs/
  → 0 (los hits son el verbo español «evalúa») [pass]
EV-M6-5: ruta de lectura obligatoria al 92% de 1000 líneas | wc -l AGENTS.md
  00-INDICE.md estandar-*.md 04-*.md → 923 [pass]
EV-M6-6: runtime del gate | python3 --version → Python 3.9.6 [pass]
```

### Requisitos

```text
REQ-M6-01 [funcional] [fuente: humano 2026-09-07; EV-M6-2, EV-M6-3]
Enunciado: existe un cotejo explícito entre el corpus y estándares de industria
nombrados, que declara también lo que NO cubre.
Criterio de aceptación: ver T02 del plan.
Prioridad: imprescindible

REQ-M6-02 [funcional] [fuente: humano 2026-09-07; estándar §6.3; manifiesto no_ofrece]
Enunciado: la forma del reporte de dos capas (ADR-016) se comprueba con un gate
ejecutable, no con el autorreporte del ejecutor.
Criterio de aceptación: ver T04 del plan.
Prioridad: imprescindible

REQ-M6-03 [funcional] [fuente: humano 2026-09-07; estándar §6.2]
Enunciado: la autoridad por operación se extiende a la superficie de
herramientas del ejecutor, o se remite por escrito al proyecto que la posee.
Criterio de aceptación: ver T05 del plan; decisión de frontera previa.
Prioridad: imprescindible (la decisión); condicionada (la redacción)

REQ-M6-04 [funcional] [fuente: humano 2026-09-07; EV-M6-4; guía 04 §5.3 disparador 2]
Enunciado: existe procedimiento para componentes cuya salida no es determinista
por depender de un LLM.
Criterio de aceptación: ver T06 del plan.
Prioridad: imprescindible

REQ-M6-05 [funcional] [fuente: humano 2026-09-07; estándar §3.4; EV-M6-5]
Enunciado: la ruta de lectura obligatoria tiene límite escrito y verificado por
el gate, igual que cada archivo individual.
Criterio de aceptación: ver T03 del plan.
Prioridad: imprescindible

REQ-M6-06 [no-funcional] [fuente: humano 2026-09-07; manifiesto fronteras_de_confianza]
Enunciado: la generalización del método más allá del monocultivo actual tiene
criterio de entrada declarado y pendiente registrado.
Criterio de aceptación: ver T08 del plan.
Prioridad: deseable — depende de un adoptante externo, fuera del control local

REQ-M6-07 [restricción] [fuente: AGENTS.md §Autoridad por operación; ADR-018]
Enunciado: ninguna operación de autoridad separada se ejecuta en este trabajo.
Criterio de aceptación: ver T09; cero push, merge, PR, tag, release o
instalación de dependencias.
Prioridad: imprescindible
```

### No objetivos y restricciones

- No adoptar una propuesta por haberla planificado: cada tarea cierra con
  evidencia o con descarte trazable.
- No tocar `project-manifest.yaml` salvo que una tarea resuelva un ítem de
  `pospuesto`, y sólo en la misma tarea que lo resuelve (guía `02` §3.3).
- No modificar plantillas de adopción (`templates/skevi/`): cambiarlas
  dispara el protocolo de versionado de ADR-020 y no está en alcance.
- No añadir dependencias: todo script nuevo es stdlib de Python, ejecutable
  con el 3.9.6 del sistema (EV-M6-6).
- No añadir GitHub Actions (ADR-001 vigente); el gate sigue local.
- No reescribir `AGENTS.md`/`CLAUDE.md` fuera del bloque que cada tarea
  necesite (estándar §3.5, «creación, no retrofit»).
- Sin push, merge, PR, tags, releases ni operaciones destructivas.
- P3 (REQ-M6-03) no se redacta antes de resolver su frontera con `praxis-dev`:
  ver PREGUNTA-M6-1.

### Preguntas abiertas

```text
PREGUNTA-M6-1: ¿la superficie de herramientas del ejecutor (allowlist de
  shell, egress de red, sandbox, servidores MCP, secretos en ventana de
  contexto) pertenece a Skevi o al plano de praxis-dev?
Por qué importa: el manifiesto cede a praxis-dev «autoridad, conformidad y
  perfiles de aseguramiento». Escribirla aquí sin decidir invade una frontera
  declarada; omitirla deja el hueco más grande del corpus sin dueño.
Opciones: (A) Skevi la norma, por continuidad con §4.3/§6.2 que ya gradúan
  autoridad de Git — recomendada, con la remisión de conformidad intacta;
  (B) remisión escrita a praxis-dev en el manifiesto y en §6, sin regla nueva;
  (C) partir: mecanismo en Skevi, perfiles de aseguramiento en praxis-dev.
RESUELTA 2026-09-07: opción (A), por instrucción directa del humano.
  Materializada en el §6.8 del estándar y en ADR-023; la remisión de
  conformidad y perfiles de aseguramiento a praxis-dev queda intacta.

PREGUNTA-M6-3: la línea de `project-manifest.yaml` §no_ofrece cede a
  praxis-dev «autoridad, conformidad ni perfiles de aseguramiento». ¿Debe
  precisarse para distinguir el mecanismo de graduación de permisos —que
  §4.3, §6.2, ADR-017 y ADR-018 ya norman— del plano de gobernanza cedido?
Por qué importa: leída literalmente, la línea la invadirían esas cuatro
  fuentes preexistentes y también el §6.8 nuevo. La tensión no la crea
  ADR-023; la hace visible. Sin precisión, cada regla de autoridad futura
  reabre la misma discusión.
Opciones: (A) precisar la línea a «gobernanza de autoridad, conformidad y
  perfiles de aseguramiento», dejando el mecanismo en Skevi — recomendada,
  es la lectura que ya hace coherente al corpus; (B) dejarla como está y
  aceptar la ambigüedad; (C) coordinar con praxis-dev antes de tocarla.
Estado: abierta. Modificar `no_ofrece` es decisión de política del humano;
  el ejecutor no la resuelve por su cuenta (fail-closed, principio 5).

PREGUNTA-M6-2: ¿hay un adoptante externo disponible para el piloto de
  REQ-M6-06 (otro autor humano, CI remoto real, lenguaje compilado o repo
  legacy grande — al menos dos variables rotas a la vez)?
Por qué importa: sin él, la palabra «industria» sigue sin respaldo empírico y
  T08 sólo puede registrar el criterio, no ejecutarlo.
Opciones: registrar el criterio de entrada ahora y ejecutar cuando exista.
```

## F1 — Conducta de diseño

- Toda regla normativa nueva declara procedencia y razón en su propia línea
  (AGENTS.md §Convenciones de edición). Regla sin fuente no es aplicable.
- Toda decisión con alternativas reales se registra en un ADR nuevo e
  inmutable, con su checklist de cierre de `02` §3.3 completo.
- Todo script nuevo con lógica no trivial lleva su suite en `tests/`, y todo
  cambio de comportamiento sigue RED-GREEN-REFACTOR con la salida del RED
  registrada (ADR-011).
- Todo gate nuevo es fail-closed vía `skevi-gate.json` y copiable sin editar
  el script (ADR-006): sin su clave, no comprueba nada.
- El cierre del programa lleva ronda adversarial en contexto fresco: aplica el
  disparador 4 de `04` §5.3 — los gates son interfaz para consumidores no
  controlados por el mismo autor.

## F1 — CONTRATO del gate de reportes (T04)

Formato de `02` §4. Cada campo se comprobó contra la firma real del código
con `grep -n`, no de memoria (check CONTRATO↔código de `04` §9).

```text
CONTRATO: skevi/check-reports v1
Entrada:
  skevi-gate.json.reports: objeto [opcional] — ausente = gate inactivo
    .dir:    texto [obligatorio] ruta relativa a un directorio existente
    .exempt: lista de texto [opcional] rutas relativas exentas, con motivo
             escrito fuera de la config (JSON no admite comentarios)
  archivos: <dir>/*.md; sólo los que contienen un fence ```text con
            report_sha256 se tratan como capa técnica
Salida:
  stdout: una línea "OK — <n> reporte(s)…" o "BLOQ — …" con un fallo por línea
  código de salida: 0 si OK o inactivo; 1 si BLOQ
Errores:
  config no objeto | subcampo desconocido | dir ausente o inexistente |
    exempt mal tipada -> BLOQ por configuración, gate no corre
  archivo no UTF-8 | ilegible -> BLOQ por archivo; nunca vuelca la excepción
    (ADR-007): un fallo de lectura no acredita conformidad
  capa incompleta | STATE o DECISION fuera de conjunto | fecha, hora o
    head_sha mal formados | EVIDENCE ausente o vacía | línea sin "->" |
    marca de una palabra fuera de {pass, fail, inconclusive} |
    report_sha256 que no reproduce -> BLOQ por reporte
Invariantes:
  - comprueba forma, nunca honestidad: pasar no prueba que la evidencia sea
    cierta ni que la ronda adversarial se ejecutara
  - se validan todas las capas técnicas del archivo, no sólo la primera
  - una línea de evidencia sin marca es válida (transición de ADR-005)
  - la forma canónica del hash es la de ADR-016 y no se redefine aquí
  - un archivo exento no se valida, pero se cuenta y se reporta como exento
Compatibilidad:
  - sin la clave `reports`, el gate es inactivo y sale 0: el adoptante que
    no la declara no percibe el cambio
  - la clave vive en el conjunto cerrado compartido con check_sizes.py y
    check_plans.py: copiar un solo script produce BLOQ, no un fallo silencioso
  - cambios del contrato -> v2, nunca mutación in situ
```
