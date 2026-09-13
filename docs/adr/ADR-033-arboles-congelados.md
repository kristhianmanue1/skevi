# ADR-033: Complemento de adopción para árboles congelados (aterriza A-2)

Estado: aceptado; implementado en `templates/skevi/frozen-trees.md`
(plantillas/v7).

Contexto: dos deudas convergen en el mismo hueco. **A-2 de PROP-002**
(baseline por derivación: default deny / allowlist / cuarentena /
promoción) fue aceptada el 2026-08-15 con la regla «cada aceptada
produce ADR antes de modificar norma», y ese ADR nunca llegó a existir
(issue #40 §1). **Issue #43** documenta al tercer adoptante del perfil
de apps móviles (flutterFlow @ `2e0f9cf`, 2026-09-12) que tuvo que
inventarse sin respaldo normativo un gate de integridad byte-a-byte
sobre su árbol generado, exclusiones del gate de tamaños y la
documentación del «parche frágil». [PROP-009](../history/PROP-009-codigo-generado-congelado.md)
propuso el vehículo para cerrar ambas deudas con un solo artefacto y el
humano la aceptó el 2026-09-13 con una corrección de encuadre.

**Encuadre corregido por el humano:** Skevi no asume que el código
está escrito por humanos — la mayor parte de los proyectos que Skevi
lleva está escrita por agentes de IA. El eje normativo no es la autoría
(humano, agente de IA o herramienta generadora) sino el **régimen del
árbol**: editable, donde §3.1 aplica por igual a quien lo escriba, o
congelado/sellado, donde la regla correcta es la opuesta.

Decisión: **complemento corto de adopción, no norma transversal** —
`templates/skevi/frozen-trees.md`, mismo rango que las plantillas de
`.skevi/`, que se copia sólo si el proyecto tiene árboles congelados.
Tres piezas, según PROP-009 §2 con el encuadre corregido:

1. **Baseline por derivación y su gate mínimo** — la materialización de
   A-2 en escala de adopción: default deny sobre el árbol congelado,
   baseline derivado por comando (listado de rutas + SHA-256 por
   archivo, nunca editado a mano), allowlist explícita, cuarentena y
   promoción para los cambios permitidos, fallo cerrado ante alta,
   baja, symlink o drift.
2. **Régimen, no autoría.** En árboles editables §3.1 sigue valiendo
   para cualquiera que escriba código nuevo — humano o agente de IA.
   En el árbol congelado la regla es la opuesta: no se imita al
   vecino, no se edita en el export; los parches viven en la copia
   canónica y se reaplican tras cada re-export (patrón «parche
   frágil», documentado).
3. **Convivencia con el gate skevi:** `skip_dirs` sobre el árbol
   congelado —su contención de tamaño no significa nada— más el gate
   de integridad propio de la pieza 1, ambos declarados en la
   `skevi-gate.json` del adoptante.

Alternativas descartadas:

- **Norma transversal.** Modificaría §3.1 del estándar para todos los
  adoptantes, con o sin árboles congelados; contradice la regla 3 del
  índice (mínimo necesario) y la frontera de ADR-026: lo que se norma
  es el método con que el adoptante protege lo que no edita, no el
  artefacto ni la herramienta que lo genera.
- **Sección en `usage-guide.md`.** Engorda una plantilla de 300 líneas
  para adoptantes que no la necesitan; el complemento opcional es
  opcional de verdad.
- **Diferir A-2 otra vez.** El argumento de ADR-006 para diferir A-6
  («nadie había reportado fricción») ya no existe: tres adoptantes del
  perfil documentaron fricción real. Diferir sería ignorar evidencia.
- **Registrar el complemento como excepción de §3.1 en el estándar.**
  La excepción vive en el complemento, citando §3.1; si algún día
  quisiera ser general, eso exige su propia deliberación.

Consecuencias: A-2 deja de ser aceptada-sin-aterrizar — su mecanismo
queda materializado en escala de adopción y el ADR cierra la deuda del
issue #40 §1 por esa pata. El adoptante con árboles congelados deja de
inventar el gate mínimo. Costo: una plantilla más en el bundle
(plantillas/v7), opcional de copiar; la plantilla declara su
procedencia y su alcance para no aplicarse a medias.

Verificación: `python3 scripts/check_sizes.py` → salida real registrada
en el reporte de la tarea; la plantilla entra al MANIFEST de
`templates/skevi/` (plantillas/v7) con su digest y salto en `history`,
y al `required` de `skevi-gate.json`.

Procedencia: [PROP-009](../history/PROP-009-codigo-generado-congelado.md)
(aceptada con corrección de encuadre); [PROP-002 §A-2,
decisión 2026-08-15](../history/PROP-002-decision-2026-08-15.md);
issues #43 y #40; instrucción directa del humano, 2026-09-13 («Skevi no
debe asumir que el código está escrito por humanos: la mayor parte de
los proyectos que lleva Skevi la escriben agentes de IA»).
Razón: aterrizar una iniciativa aceptada sin dueño y dar norma al
perfil de adopción real que tres proyectos ya reportaron, con el eje en
el régimen del árbol y no en la autoría del código.
