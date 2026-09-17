# Skevi

Cuerpo normativo para diseñar software y para operar agentes de IA que crean y
mantienen proyectos. Dos capas: un **estándar** atemporal e independiente de
herramientas, y una **guía por fases** escrita para que la ejecute un agente.

**Nombre.** Del griego σκεύη (*skeví*, plural de σκεῦος/*skevos*: vasija,
utensilio, instrumento, equipamiento, arnés, aparejo) — un conjunto de
herramientas, no una sola. También se lee como forma corta de Παρασκευή
(*Paraskeví*, "preparación"): la fase F0 de la guía es, literalmente, eso.

**Audiencia primaria.** Este corpus está escrito para que lo ejecute un
agente de IA, no para que lo lea un humano de principio a fin. `AGENTS.md`
y `docs/ai-agent-guide/` asumen un ejecutor automatizado como lector. Las
secciones de revisión existen para que una persona audite el resultado, no
para que sea la vía principal de lectura.

No depende de ningún lenguaje, framework ni proveedor. Sólo asume Git y un
hospedaje tipo GitHub.

## Estructura

Por directorio y vida útil, sin enumerar archivos: cada carpeta tiene su
fuente de verdad, que es la que se consulta para el contenido vigente.

| Ruta | Contenido | Vida útil | Fuente de verdad |
|---|---|---|---|
| `AGENTS.md` | Entrada para ejecutores automatizados | Estable | — |
| `project-manifest.yaml` | Qué ofrece y qué no, frente al ecosistema | Por release | — |
| `docs/estandar-diseno-software-github.md` | Capa normativa transversal | Cambia poco | `docs/MANIFEST.json` |
| `docs/ai-agent-guide/` | Guía por fases F0→F3 y complementos | Cambia con la práctica | `00-INDICE.md` |
| `docs/adr/` | Decisiones estructurales inmutables | Sólo crece | `00-INDICE.md` |
| `docs/crosswalk-estandares.md` | Cotejo con NIST SSDF y OWASP LLM | Caduca con sus fuentes | Tabla de versiones del archivo |
| `docs/proposals/` | Cambios bajo deliberación, no normativos | Hasta decidir | Encabezado de cada archivo |
| `docs/specs/`, `docs/plans/` | F0/F1 y planes de programas de mejora | Por programa | Encabezado; planes: `check_plans` |
| `docs/reviews/` | Rondas y cierres de programa | Congelado al cerrar | `skevi-gate.json` clave `reports` |
| `docs/history/` | Registro de procedencia, no normativo | No cambia | — |
| `docs/orchestration/` | Método concreto, acoplado a herramientas | Caduca con ellas | Fecha de verificación del archivo |
| `templates/skevi/` | Plantillas de adopción versionadas | Versionado | `templates/skevi/MANIFEST.json` |
| `templates/` (raíz) | Formatos copiables | Sin versionar (issue #48) | — |
| `scripts/` | Gates copiables y hooks de Git | Versionado | `scripts/MANIFEST.json` |
| `tests/` | Suites de los scripts | Con los scripts | `python3 -m unittest discover -s tests` |

La separación no es estética: cada carpeta tiene una **vida útil distinta**.
El estándar cambia poco, la guía cambia con la práctica, `orchestration/`
caduca cuando cambian las herramientas, `proposals/` vive mientras se delibera
un cambio y `history/` no debería cambiar nunca. Mezclarlas en un archivo obliga
a revisar lo estable cada vez que se mueve lo volátil.

## Cómo se usa

**Un agente que empieza un proyecto** lee `AGENTS.md`, luego
`docs/ai-agent-guide/00-INDICE.md`, y avanza por fases: análisis (F0) →
specs/ADRs/contratos (F1) → cascarón (F2) → ejecución y verificación (F3).
Cada fase tiene un gate que se cierra con evidencia, no con una declaración.

**Una persona que revisa trabajo** usa el checklist de cumplimiento del
estándar (§7) y el formato de ronda adversarial de la guía (`04` §5).

**Un proyecto que adopta el método** copia el estándar y la guía, fija sus
propios límites de tamaño por escrito, e instala el gate en su CI. Si su
estructura de directorios difiere de la de Skevi — otros nombres de ADR,
guía o plantillas, o ninguno de ellos —, declara `skevi-gate.json` en su raíz
en vez de editar `scripts/check_sizes.py`: el script se copia sin
modificación (ADR-006).

**Las plantillas de adopción están versionadas** (ADR-020): el
`templates/skevi/MANIFEST.json` declara la versión vigente y el historial de
saltos, cada uno con su bandera de breaking. Al copiar, el consumidor crea
`.skevi/installed.json` (a partir de la plantilla del mismo directorio)
declarando qué instaló, de dónde y qué personalizó. Para comprobar si una
copia quedó obsoleta:

```bash
python3 <ruta-a-skevi>/scripts/check_templates.py \
  --manifest <ruta-a-skevi>/templates/skevi/MANIFEST.json \
  --installed .skevi/installed.json
```

Copia antigua pero compatible → aviso; incompatible → fallo; archivos
declarados en `customized` → re-copia bajo responsabilidad del consumidor.
Sin registro de instalación no hay efecto alguno. Migración de copias
previas: crear el registro una vez, a mano, con la guía del propio
registro.

**El mismo mecanismo cubre `scripts/`** (ADR-028): `scripts/MANIFEST.json`
declara la versión vigente de los cuatro gates, con el mismo formato y el
mismo comando, cambiando sólo el par manifest/instalado:

```bash
python3 <ruta-a-skevi>/scripts/check_templates.py \
  --manifest <ruta-a-skevi>/scripts/MANIFEST.json \
  --installed .skevi/scripts-installed.json
```

La versión de `scripts/MANIFEST.json` (`gate/vN`) es la misma que
`check_sizes.py` imprime en su propia salida (ADR-027): un adoptante que
sólo mira su log de CI ya sabe que su copia envejece; quien quiere saber
**contra qué versión** usa este comando.

**Y cubre el corpus normativo** (ADR-032): `docs/MANIFEST.json` declara
la versión vigente del estándar y de la guía, con la misma mecánica:

```bash
python3 <ruta-a-skevi>/scripts/check_templates.py \
  --manifest <ruta-a-skevi>/docs/MANIFEST.json \
  --installed .skevi/corpus-installed.json
```

## Verificación

```bash
python3 scripts/check_sizes.py
python3 scripts/check_plans.py
python3 scripts/check_reports.py
```

`check_sizes` comprueba que existen los archivos canónicos, que no hay
Markdown operativo suelto en la raíz, que ningún archivo de texto excede su
límite y que la ruta de lectura obligatoria cabe en su presupuesto — clave
`reading_path`, 1000 líneas en este repo (ADR-021). `check_plans` verifica la
estructura de los planes de implementación de `docs/plans/` (ADR-014) — cada tarea con Consumes/Produce/Steps, cada step
con criterio de verificación, cada ruta referenciada existente —; es
opcional y fail-closed: sin clave `plans` en `skevi-gate.json`, no comprueba
nada. `check_reports` (ADR-022) verifica la forma de la capa técnica de los
reportes de dos capas de `docs/reviews/` —claves, `STATE`, marcas y hash
canónico reproducible—, también fail-closed vía la clave `reports`. Los tres
dan `OK` o `BLOQ` con código de salida distinto de cero.

Comprueban **forma**: que un reporte pase no prueba que su evidencia sea
cierta. Esa verificación sigue fuera del alcance de Skevi.

`check_sizes` imprime además su propia versión y, al cumplirse noventa días
desde que se generó, avisa de su edad (ADR-027). No consulta la red ni
observa el repositorio de origen: dice cuántos días tiene, no si existe una
versión más reciente. Es la señal que un adoptante ve en su log de CI sin
tener que ejecutar nada aparte.

```bash
python3 -m unittest discover -s tests
```

Corre las suites de `tests/` sobre los scripts del proyecto — sus cuatro
artefactos ejecutables: `check_sizes.py`, `check_plans.py` (ADR-014),
`check_reports.py` (ADR-022) y `check_templates.py` (ADR-020, ADR-028).

**Gate en CI, hook local como verificación rápida** (ADR-034, sustituye a
ADR-001). El workflow `.github/workflows/skevi-gate.yml` ejecuta los tres
gates y los tests en cada PR y push a `main`, con Python 3.9 y 3.12. El hook
(`git config core.hooksPath scripts/hooks`) corre lo mismo antes del push para
detectar fallos sin esperar al CI; no sustituye al CI, que es el autoritativo.

## Principios que lo sostienen

Ver `docs/estandar-diseno-software-github.md` §1 — fuente única. No se
resumen ni se parafrasean aquí: una paráfrasis es una segunda copia con otras
palabras, y envejece igual de mal que una copia literal.

## Estado

**Estable.** El criterio de salida de Alpha — «un piloto F0→F3 completo
con evidencia» — se cumplió el 2026-09-01 con el piloto infosalud
(`docs/history/piloto-infosalud.md`). El gate se verifica en CI y, como
paso previo opcional, con el hook local (ADR-034).

`docs/history/` conserva los registros de los pilotos que originaron
estas reglas, incluida la ronda adversarial que corrigió el protocolo de
orquestación. Ese material es evidencia de procedencia, no norma vigente.
