# PROP-009 — Complemento de adopción para árboles congelados

> **Estado:** ACEPTADA con corrección de encuadre (instrucción directa
> del humano, 2026-09-13). Aterrizada en
> [ADR-033](../adr/ADR-033-arboles-congelados.md) y la plantilla
> `templates/skevi/frozen-trees.md` (plantillas/v7).
> **Origen:** [issue #43](https://github.com/kristhianmanue1/skevi/issues/43)
> (adopción flutterFlow @ `2e0f9cf`, 2026-09-12, ronda adversarial de
> contexto fresco) + iniciativa **A-2 de PROP-002**, aceptada el
> 2026-08-15 y sin aterrizar (issue #40 §1). Es la misma carencia vista
> desde dos lados; este documento la cierra desde uno.
> **Fecha:** 2026-09-13.

## 0. Corrección de encuadre de la aceptación

La primera versión de esta propuesta enmarcaba el hueco como «§3.1
presupone código escrito por el equipo». El humano la corrige al
aceptarla: **Skevi no asume que el código está escrito por humanos** —
la mayor parte de los proyectos que Skevi lleva está escrita por
agentes de IA. El eje normativo no es la autoría (humano, agente de IA
o herramienta generadora) sino el **régimen del árbol**: editable
—donde §3.1 aplica por igual a quien lo escriba— frente a
congelado/sellado —donde la regla correcta es la opuesta—. Todo el
artefacto aterrizado usa este encuadre.

## 1. El hueco

La regla «el código nuevo se parece al código que lo rodea» (§3.1)
aplica por igual a código escrito por humanos o por agentes de IA — en
los proyectos que Skevi lleva, la mayoría lo escriben agentes. Lo que
§3.1 no contempla es el **régimen del árbol**: en un workspace con
árboles **congelados o sellados** —un export de herramienta generadora
como FlutterFlow, una entrega de tercero, un baseline de release— la
regla correcta es la opuesta: el código vecino no debe imitarse ni
tocarse sin re-sellar. Para documentos congelados §3.4 sí da norma («un
documento histórico congelado se exenta»); para código congelado no hay
nada: ni ADR, ni guía, ni mención.

Lo que el tercer adoptante tuvo que inventar sin respaldo normativo:

- un gate propio de integridad byte-a-byte sobre el árbol generado
  (baseline + SHA-256 de 1532 archivos, fail-closed ante alta, baja,
  symlink o drift);
- `skip_dirs` del gate skevi sobre las apps, cuya contención de tamaño
  no significa nada;
- documentación del «parche frágil»: los re-exports del generador
  destruyen los parches manuales y hay que reaplicarlos;
- precedencia explícita: trabajar sólo en la copia canónica, nunca
  sobre el export original.

El precedente histórico existe —PROP-002 §2.2: sistema legado en
producción, auditoría byte-a-byte de 31.159 rutas— y es exactamente la
iniciativa A-2 (baseline por derivación: default deny / allowlist /
cuarentena / promoción) aceptada con la regla «cada aceptada produce
ADR antes de modificar norma». Ese ADR no llegó a existir; la deuda es
la de A-2.

## 2. Propuesta

**Un complemento corto de adopción, no norma transversal** — mismo
rango que las plantillas de `.skevi/`: el adoptante con código
generado lo copia; el que no, no lo ve. Tres piezas:

1. **Baseline por derivación y su gate mínimo.** Default deny sobre el
   árbol generado: nada entra ni muta sin estar en la allowlist
   declarada; el baseline es una derivación del estado sellado
   (listado de rutas + SHA-256 por archivo), nunca una edición
   manual; alta, baja, symlink o drift → fallo cerrado. Es la
   materialización del mecanismo que A-2 aceptó y que este documento
   aterriza en su escala mínima: la de un adoptante, no la de un
   pipeline institucional.
2. **Convivencia con §3.1: régimen, no autoría.** En árboles editables,
   la regla §3.1 sigue valiendo para cualquiera que escriba el código
   nuevo — humano o agente de IA. En el árbol congelado la regla es la
   opuesta: no se imita, no se edita en el export; los parches viven en
   la copia canónica y se reaplican tras
   cada re-export (patrón «parche frágil», documentado).
3. **Convivencia con el gate skevi.** `skip_dirs` sobre las apps
   generadas —su contención de tamaño no significa nada— más el gate
   propio de integridad de la pieza 1; quedan fuera del alcance las
   firmas de release y la integridad del artefacto publicado
   (`no_ofrece`, ADR-026): se norma el método con que el adoptante
   protege lo que no escribe, no el artefacto.

### 2.1 Dónde vive (decisión abierta de forma)

| Opción | A favor | En contra |
|---|---|---|
| **A. Nueva plantilla copiable** `templates/skevi/generated-freeze.md` (recomendada) | Viaja con la adopción; entra al MANIFEST de ADR-020 con su propio digest y cadena; opcional de verdad | Quinto archivo en el bundle; exige bump de plantillas |
| B. Sección en `usage-guide.md` | Cero archivos nuevos | Crece una plantilla con límite de 300; obliga a leerla a quien no la necesita |
| C. Documento del canon no copiable | Cero costo de distribución |   No llega al adoptante en el momento del hueco; reproduce el defecto
  que el issue #42 ya documentó para los comandos de drift |

La recomendación es A; la decisión es del humano junto con la
aceptación del contenido.

## 3. Qué no propone

- No norma lenguajes, frameworks ni integridad de releases
  (`project-manifest.yaml` §no_ofrece; ADR-026).
- No modifica el estándar ni la guía: la pieza 2 declara una excepción
  de alcance **en el complemento**, citando §3.1 — si algún día la
  excepción quisiera ser general, eso es otro ADR con su propia
  deliberación.
- No convierte el caso flutterFlow en requisito universal: los tres
  adoptantes son evidencia de que el perfil existe, no de que todo
  adoptante lo tenga (regla 3 del índice).

## 4. Consecuencias si se acepta

- A-2 deja de ser aceptada-sin-aterrizar: este complemento es su
  materialización en escala de adopción, y el ADR que lo acompañe
  cierra la deuda del issue #40 §1 por esa pata.
- El adoptante de código generado deja de inventar el gate mínimo:
  copia el patrón, declara su allowlist y su baseline.
- Costo: una plantilla más que mantener versionada (opción A) y una
  excepción de alcance más que explicar — el complemento debe citar
  por qué §3.1 no aplica a código generado, o se aplicará a medias.

## 5. Verificación de esta propuesta

- Serie local hasta PROP-008; `gh issue list` sin ningún issue que
  reclame PROP-009 → número asignado conforme al esquema de
  AUDIT-proposal-identifiers §2.
- `grep cuarentena|default deny` sobre estándar y guía: cero
  resultados; A-2 `accepted` en
  [`PROP-002-decision-2026-08-15.md` §1](../history/PROP-002-decision-2026-08-15.md)
  → la deuda existe y no está cubierta por ninguna propuesta en trámite
  (seis documentos en `docs/proposals/`, revisados).
- Los tres adoptantes citados provienen del issue #43; no se
  re-verificaron sus repos — se citan como evidencia declarada por el
  issue, no como medición propia.

## 6. Decisión y aterrizaje

1. El humano aceptó contenido y forma el 2026-09-13 — opción A
   (plantilla copiable) — con una corrección de encuadre: el eje es el
   **régimen del árbol** (editable vs congelado), no la autoría del
   código; Skevi no asume que el código está escrito por humanos, pues
   la mayor parte de los proyectos que lleva la escriben agentes de IA
   (§0).
2. Aterrizada en [ADR-033](../adr/ADR-033-arboles-congelados.md) y la
   plantilla `templates/skevi/frozen-trees.md` (plantillas/v7).
