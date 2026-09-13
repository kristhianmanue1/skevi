# ADR-031: Procedencia cerrada del registro de instalación

Estado: aceptado; implementado en `scripts/check_templates.py` (gate/v5)
y en las plantillas de `templates/skevi/` (plantillas/v5).

Contexto: la decisión de PROP-002 (2026-08-15) aceptó la iniciativa
**A-7 — declaración de adopción con procedencia fijada** con esta
evidencia exigida: «dado un repo adoptante, un agente responde qué
versión sigue y qué dejó, leyendo un archivo». La tabla de la decisión
despachó A-7 a ADR-006, pero ADR-006 aterriza sólo §A-6 (gate
configurable): la procedencia quedó sin dueño. Hoy el campo `source` de
`.skevi/installed.json` y `.skevi/scripts-installed.json` es **texto
libre**: la validación sólo exige que sea string
(`scripts/check_templates.py`, `_load_install`). Un campo que dice «la
copié de otro proyecto» no responde qué versión se sigue — la evidencia
exigida no la produce el formato vigente. Detectado como deuda
normativa en el issue #40 (adopción flutterFlow @ `2e0f9cf`,
2026-09-12); sin ninguna propuesta en trámite que la cubra.

Decisión: `source` adopta un **formato cerrado** — se acepta lo
declarado, se rechaza lo demás:

```text
CONTRATO: campo source de skevi/template-install/v1 y
          skevi/script-install/v1 (mismas reglas, ADR-028) v1
Entrada:
  source: texto [obligatorio] — <origen>@<revisión>
    origen: sin «@» ni espacios — URL del repo o ruta relativa al
      espejo local de donde se copió.
    revisión: hex minúsculas de 7 a 64 dígitos — sha de Git corto o
      completo, incluido SHA-256 de repo.
Salida: sin cambio — el comparador no imprime `source`.
Errores:
  texto libre sin «@revisión» → BLOQ: «source debe ser
  <origen>@<revisión>» con un ejemplo.
Invariantes:
  - aplica a ambas familias de instalación; sus reglas ya eran comunes
    (ADR-028).
  - la revisión es la que el humano tiene en `git log`: no exige
    cómputo adicional ni herramientas fuera del flujo.
Compatibilidad:
  - un adoptante con `source` libre recibe BLOQ en su primer chequeo:
    migración = reescribir el campo con su URL@sha real. El fallo es
    el mecanismo de aviso, no un daño (el chequeo es manual y opcional).
  - cambio de formato -> v2, nunca mutación in situ.
```

Las plantillas de ejemplo (`installed.json`, `scripts-installed.json`)
migran su placeholder a `<url-o-ruta-del-origen>@<sha-del-commit>` para
que un adoptante nuevo llene el formato correcto desde el primer día y
su primera ejecución pase (guardia: el test que simula ese llenado).

Alternativas descartadas:

- **Exigir URL completa con esquema.** Un fork local o un espejo sin
  red —caso real del propio adoptante que motivó el issue— no encaja;
  el valor procedimental está en la revisión anclada, no en el
  esquema de la URL.
- **Mantener texto libre con convención documentada.** Es el estado
  actual: la convención no se valida, y lo no validado se degrada — la
  evidencia que A-7 exigía quedaba en manos de la disciplina.
- **Hash del árbol o digest propio.** Exige computar algo que Git ya
  da; el sha del commit es la moneda que todos los participantes ya
  manejan (simplicidad primero, criterios de decisión §8).

Consecuencias: el registro de instalación responde por sí solo qué
versión sigue una copia y de dónde vino, que era la evidencia que la
aceptación de A-7 exigía. El costo es una migración trivial para los
adoptantes existentes, anunciada por el propio BLOQ con el formato
esperado en el mensaje. Este ADR no crea el mecanismo de instalación
(ADR-020) ni lo extiende a otros artefactos (ADR-028): sólo cierra el
formato de un campo que ya existía.

Verificación: `python3 scripts/check_sizes.py` → salida real registrada
en el reporte de la tarea; la suite cubre el regex (acepta sha corto,
40 y 64; rechaza texto libre, mayúsculas, 6 dígitos, doble @, espacio)
y el BLOQ de extremo a extremo con mensaje accionable. El total lo
reporta la suite, no este texto.

Procedencia: [PROP-002 §A-7,
decisión 2026-08-15](../history/PROP-002-decision-2026-08-15.md) — la
aceptada sin aterrizar; issue #40 (deuda detectada, 2026-09-12);
decisión del humano en conversación, 2026-09-13.
Razón: aterrizar una iniciativa aceptada cuya regla era «cada aceptada
produce ADR antes de modificar norma», cerrando el campo sin formato
que la evidencia exigida dejaba inservible.
