# ADR-032: Manifiesto de corpus — el canon normativo versionado

Estado: aceptado; implementado en `scripts/check_sizes.py` y
`scripts/check_templates.py` (gate/v6), `docs/MANIFEST.json`
(corpus/v1) y `templates/skevi/corpus-installed.json` (plantillas/v6).

Contexto: el estándar (501 líneas) y la guía (7 archivos) se copian al
adoptante **sin digests ni versión**: su envejecimiento es indetectable
— el adoptante no tiene forma de saber qué revisión del canon sigue.
El pendiente estaba registrado en
`docs/history/PROP-002-correcciones-desde-adoptantes.md` §4 (adoptante
anclado a commit) y lo reabrió el issue #40 §2 (adopción flutterFlow @
`2e0f9cf`, 2026-09-12). ADR-020 y ADR-028 versionan plantillas y
scripts; el corpus normativo —lo que el adoptante realmente ejecuta al
leer— era el único payload sin manifiesto.

Decisión: **tercera familia de manifiesto**, con el mismo mecanismo de
comparación por versión de ADR-020/028 (el comparador
`check_templates.py` gana la familia, no un segundo comparador):

```text
CONTRATO: skevi/corpus-manifest/v1 (y skevi/corpus-install/v1)
Entrada (docs/MANIFEST.json, fuente):
  schema:       "skevi/corpus-manifest/v1" [obligatorio]
  version:      "corpus/v<n>" [obligatorio]
  generated_at: texto con fecha [obligatorio]
  files:        objeto {ruta-relativa-a-docs/: "sha256:<hex>"}
                [obligatorio] — el canon declarado: estándar + guía.
                Rutas relativas al directorio del manifiesto; pueden
                anidar subdirectorios; nunca escapan de la raíz.
  history:      lista de {from, to, breaking, changes} [obligatorio]
Entrada (.skevi/corpus-installed.json, adoptante): mismos campos y
  reglas que las familias previas; `source` con el formato cerrado de
  ADR-031.
Salida: OK/aviso/BLOQ por versión, idéntico a las demás familias.
Errores: archivo ausente → fallo, nunca omisión (ADR-007); digest
  desactualizado → fallo por archivo; ruta que escapa la raíz → fallo.
Invariantes:
  - validación condicional a la existencia de docs/MANIFEST.json, como
    ya hacía el gate con templates/ y scripts/ (regla 3 del índice).
  - SIN listado de directorio: docs/ anida subdirectorios y el
    listado exacto y plano es contrato de ADR-020 para plantillas —
    lo que se protege aquí es el corpus declarado, no un inventario
    del árbol. Añadir un documento al canon exige editarlo en el
    manifiesto: es lista cerrada, no descubrimiento.
Compatibilidad:
  - familia aditiva: ningún consumidor de las familias previas nota el
    cambio; gate/v6 sube por los cambios de código en los dos scripts.
  - cambios de este contrato -> v2, nunca mutación in situ.
```

**Ajuste de límite de `scripts/check_sizes.py`, re-decidido.** La
cláusula de ADR-030 («la siguiente adición estructural obliga a partir
el archivo o a re-decidir») se ejecuta aquí por la segunda vía: el
límite pasa de 830 a 870, escrito en `skevi-gate.json` (`limits`) y
justificado en este ADR. La partida se re-siembra como movimiento
futuro si el archivo crece otra vez (ver descartadas).

Alternativas descartadas:

- **Partir el subsistema de manifiestos en un módulo nuevo.** Rompería
  «copiable sin edición» (ADR-006) —quinto archivo distribuido—,
  añadiría mecánica de imports frágil para los tests que cargan el gate
  por ruta, y es un refactor que §3.3 prohibe mezclar con un cambio de
  comportamiento. Queda anotado como la partida a ejecutar si el
  archivo vuelve a tocar su techo.
- **Listado recursivo del directorio en la familia corpus.** Cambiaría
  el contrato de ADR-020 para todas las familias y convertiría el
  manifiesto en inventario automático: un archivo colado en `docs/`
  entraría al canon sin decisión — polaridad cerrada al revés.
- **Clave nueva en `skevi-gate.json` con los digests.** La config del
  gate es del adoptante, no del canon: los digests fuente no pueden
  vivir en un archivo que cada proyecto edita. La fuente de verdad del
  canon es un manifiesto publicado junto a lo que declara.

Consecuencias: el adoptante puede responder «¿qué revisión del canon
sigo?» con un comando — la misma pregunta que ADR-031 hizo posible para
«¿de dónde lo copié?». El costo: un sexto archivo en el bundle de
adopción (plantillas/v6) y un manifiesto más que regenerar al tocar el
canon — el gate lo recuerda con su BLOQ si se olvida.

Verificación: `python3 scripts/check_sizes.py` → salida real registrada
en el reporte de la tarea; la suite cubre familia aceptada por el
comparador, atadura de namespace `corpus`, digest viejo por archivo,
ruta que escapa la raíz, archivo ausente como fallo, digests reales del
repo contra su manifiesto y la plantilla recién llenada pasando el
comparador. El total lo reporta la suite, no este texto.

Procedencia: issue #40 §2 (deuda detectada, 2026-09-12);
`docs/history/PROP-002-correcciones-desde-adoptantes.md` §4 (pendiente
original); decisión del humano en conversación, 2026-09-13.
Razón: cerrar el único payload de adopción que viajaba sin versión ni
digests, reusando el mecanismo de ADR-020/028 en vez de duplicarlo.
