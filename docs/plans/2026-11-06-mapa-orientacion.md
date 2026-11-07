# PLAN MI — Mapa de orientación de doble audiencia (humanos y agentes)

Fuente: orden del Operador (2026-11-06): integrar a Skevi los mapas
mermaid ya validados en el ecosistema (práctica del 2026-11-05), con un
alcance expandido —no sólo para que un controlador humano entienda el
proceso, sino para que **agentes tomen contexto de arranque junto con
ADRs y especificaciones**—, mapeando primero las especificaciones de
Skevi que gobiernan la integración, luego este plan y su ronda. La orden
cubre redacción y ronda; la ejecución de MI-1..MI-3 no fue emitida.

## Mapeo de especificaciones (entrada obligada de este plan)

- **Hogar y vida útil** — ADR-002 y la tabla de hogares del README;
  precedente `docs/crosswalk-estandares.md` (raíz de `docs/`, sin
  sellar, con fila en README). Consecuencia: el mapa vive en la raíz de
  `docs/`, como el crosswalk — no en `docs/orchestration/` (mermaid es
  texto neutral, no método acoplado a herramientas) ni en
  `templates/skevi/`.
- **No normativo** — AGENTS.md (un documento = un propósito) y la regla
  anti-duplicación. Consecuencia: el mapa **sólo apunta, nunca
  restituye**: cada nodo cita su fuente (ADR-nnn, §, archivo); el
  encabezado declara «en conflicto manda el corpus»; no re-dibuja la
  tabla de hogares del README, la cita.
- **Doble audiencia** — ADR-016 (dos capas) por analogía; requerimiento
  del Operador del 2026-09-07 (capa técnica para agentes + capa humana).
  Consecuencia: un artefacto, dos consumos — GitHub renderiza para
  humanos; el texto fuente es greppable para agentes; IDs de nodo en
  inglés (ADR-015) y estables por decisión de este plan (contrato de
  grep), etiquetas en español (ADR-029).
- **Presupuesto de lectura** — ADR-021/025/038/041/042; ruta 1620/1620.
  Consecuencia: el mapa no entra a `reading_path` ni recibe puntero
  desde AGENTS.md o `00-INDICE.md` en v1 (ruta agotada); el puntero para
  agentes queda diferido a la holgura de HV-2 (MI-3); v1 se descubre
  desde README (fuera de la ruta).
- **Caducidad** — patrón crosswalk («caduca con sus fuentes»).
  Consecuencia: vida útil «caduca con el canon»: el encabezado cita la
  versión de referencia (corpus/v8) y se regenera en cada salto
  corpus/vN.
- **Gates** — `check_plans` sólo parsea `docs/plans/`; `check_reports`
  ancla sus capas en `report_sha256`; `check_sizes` mide tamaño y
  hogares. Consecuencia: fences mermaid en la raíz de `docs/` no activan
  ningún gate; verificación mecánica propia: todo ADR-nnn citado existe
  en `docs/adr/MANIFEST.json`.
- **Frontera de oferta** — `project-manifest.yaml`; precedente crosswalk
  sin línea en `ofrece`. Consecuencia: sin cambios de manifiesto en v1;
  template para adoptantes fuera de alcance — primero dogfood y, si se
  prueba, PROP aparte con plantillas/vN.
- **Mermaid en la casa** — `docs/history/supervision-agente-externo.md`
  (dos fences). Consecuencia: precedente de formato; nada nuevo que
  normar.

## Diseño de los tres diagramas (especificación atacable)

D1 — Ciclo F0→F3 con lazos de corrección. Nodos: F0 análisis y
requerimientos, F1 specs/ADR/contratos, F2 cascaron, F3 ejecución y
verificación (con continuación autónoma acotada). Lazos: ronda
adversarial con veredictos (proceed/fix-and-retry/escalate) que se
registra en docs/reviews (ADR-037) como reporte de dos capas (ADR-016);
dos fallos → diagnóstico escrito antes del tercero; plan como artefacto
de escala. Punteros: `00-INDICE.md`, 01–04, ADR-008, ADR-010, ADR-013,
ADR-016, ADR-037, ADR-043.

D2 — Quién-es-quién con límites de autoridad (el de mayor valor para
agentes). Nodos: Operador (decide diseño, autoridad, riesgo,
publicación), agente ejecutor (propone y verifica, nunca se
auto-autoriza), gate local y CI (autoritativo en verificación), lote con
folio (ADR-044), zonas Z1–Z3 (ADR-017), memoria gobernada (05), trinquete
de lectura (ADR-025). Punteros: AGENTS.md, estándar §4.3/§6.2/§6.8,
ADR-017, ADR-018, ADR-025, ADR-044, ADR-045.

D3 — Estados de una TAREA. Nodos: definida (plan con E1–E6), en
ejecución (steps con verificación), verificada (criterio por step),
cerrada (DoD, con la ronda registrada en su reporte de dos capas);
aristas de parada (Parada, autoridad faltante). Punteros: plantilla de
plan, ADR-014, ADR-016, ADR-037, ADR-045.

```text
PLAN MI — Mapa de orientación de doble audiencia
Autoriza: Operador 2026-11-06 (mapear especificaciones, redactar plan,
  correr ronda)
Clase de tarea: Architectural (ADR-013: este plan existe)
Base: 74a4714c074af49b5bd3045f74de3510c2bae3ce (main; más PLAN HV sin
  commit)
Rama: sin rama; este plan no produce efectos Git.

Restricciones globales:
- Ningún efecto Git: push y merge exigen lote aceptado por el Operador
  antes del primer efecto (ADR-044); commit, tags y releases exigen
  autorización humana por operación (AGENTS.md §Autoridad por operación).
- El mapa no norma, no duplica y no entra a la ruta de lectura: en
  conflicto manda el corpus; su techo es el anti-duplicado de AGENTS.md.
- Ningún archivo de reading_path se modifica en v1 (ruta 1620/1620;
  ADR-025 p2, ADR-038 p3). El puntero canónico para agentes espera la
  holgura de HV-2 y no se cuelga de este plan como condición.
- La disposición de docs/orchestration/ sigue siendo HV-6: este plan no
  la resuelve ni la bloquea.
- La ronda y su disposición se registran en docs/reviews (ADR-037).

TAREAS:
TAREA MI-1 — Crear el mapa
  Permitido: crea docs/mapa-orientacion.md con los diagramas D1-D3 del
    diseño especificado, encabezado no-normativo con versión de
    referencia (corpus/v8), vida útil «caduca con el canon» y contrato de
    grep para agentes (IDs en inglés (ADR-015) y estables por diseño de
    este plan, etiquetas en español, puntero a fuente por nodo).
  Prohibido: restituir reglas del corpus (sólo punteros); modificar
    archivos sellados o de la ruta de lectura; efectos Git.
  Consumes: mapeo de especificaciones de este plan; diseño D1-D3;
    precedente crosswalk
  Produce: docs/mapa-orientacion.md con tres fences mermaid
  Steps:
  - [x] Redactar el mapa según el diseño — verificación: todo ADR-nnn
        citado existe en docs/adr/MANIFEST.json (grep mecánico) y tres
        fences mermaid con pares abrir/cerrar contados por grep; el
        render visual queda como verificación humana diferida a la
        primera publicación, declarada en la ronda
  - [x] Declarar caducidad y no-normatividad en el encabezado —
        verificación: el encabezado cita corpus/v8 y «en conflicto manda
        el corpus»

TAREA MI-2 — Descubrimiento desde README
  Permitido: una fila en la tabla de hogares de README.md y su enlace.
  Prohibido: tocar otros archivos; exceder el techo de README (300).
  Consumes: patrón de la fila de docs/crosswalk-estandares.md (línea 33)
  Produce: fila «docs/mapa-orientacion.md | Orientación visual y
    greppable del método | Caduca con el canon | Encabezado del archivo»
  Steps:
  - [x] Añadir la fila con el patrón crosswalk — verificación: grep del
        enlace en README.md, wc -l README.md <= 300 y check_sizes OK

TAREA MI-3 — Frontera de ruta declarada (puntero para agentes diferido)
  Permitido: la nota de dependencia ya registrada en este plan; ninguna
    edición de archivos de la ruta en v1.
  Prohibido: editar AGENTS.md, docs/ai-agent-guide/00-INDICE.md,
    docs/estandar-diseno-software-github.md, docs/ai-agent-guide/
    05-memoria-del-agente.md ni AN-KLA.md.
  Consumes: ADR-025 p2/ADR-038 p3 (ruta agotada); HV-2 (holgura futura)
  Produce: ausencia verificada contra HEAD de cambios en los nueve
    archivos de la ruta (cinco de files, cuatro de worst_case_of);
    dependencia declarada para v2 (una línea de puntero cuando HV-2
    libere holgura)
  Steps:
  - [x] Verificar la frontera — verificación: git diff --stat HEAD vacío
        sobre los nueve archivos de la ruta declarados en
        skevi-gate.json

TAREA MI-4 — Ronda adversarial sobre el mapa y este plan
  Permitido: ronda de contexto fresco sobre este plan y, si MI-1 ya
    corrió, sobre docs/mapa-orientacion.md; registro en docs/reviews.
  Prohibido: que la ronda active tareas, cree autoridad o edite
    archivos.
  Consumes: este plan; verificación de contexto del 2026-11-06
  Produce: crea docs/reviews/2026-11-07-plan-mi-ronda.md con la decisión
  Steps:
  - [x] Ronda de contexto fresco — verificación: registro con decisión
        y sin HIGH/BLOCKER abiertos
  - [x] Incorporar hallazgos y reverificar — verificación: check_sizes,
        check_plans, check_reports y unittest OK tras la corrección

DoD: mapeo de especificaciones citado y verificado; mapa diseñado como
punteros con caducidad declarada; ruta de lectura intacta; README con
su fila y dentro de techo; rondas registradas; tres gates (sizes, plans,
reports) y unittest en verde — check_templates no aplica a v1 porque no
hay cambio de manifiesto.
Parada: hallazgo HIGH o BLOCKER abierto, base cambiada, o autoridad del
Operador denegada o vencida.
```

Límite declarado: la ronda de MI-4 la ejecuta una sesión fresca del
mismo proveedor salvo que el Operador designe otro revisor; el registro
lo declara. La template para adoptantes (mapa como oferta versionada)
requiere PROP aparte si el dogfood lo justifica: este plan no la
preautoriza.
