# ADR-030: El gate mide el disco, no el índice de Git

Estado: aceptado; implementado en `scripts/check_sizes.py` (gate/v4).

Contexto: `discover()` recorre el sistema de archivos (`ROOT.rglob("*")`),
no `git ls-files`. La fricción está documentada dos veces en el propio
auto-hospedaje — BLOQ por `.DS_Store` resuelto con `exempt_paths`
(SPEC-AUDIT-2026-09-07; reviews/2026-09-07-mejoras-auditoria.md) y el
apartado a /tmp «sin añadir exenciones» (SPEC-LANG-2026-09-12) — y un
adoptante real (flutterFlow @ `2e0f9cf`, 2026-09-12) tuvo que declarar
`skip_dirs` y tres `exempt_paths` para archivos que Git ni versiona, tras
observar que dos clones del mismo commit pueden fallar distinto. La
pregunta quedaba abierta: ¿el gate mide lo que el agente lee (on-disk,
estado de la máquina) o lo que el repo es (rastreado, reproducible)?

Decisión: **on-disk, por diseño y por escrito.** La razón es el propósito
de §3.4: un archivo que no cabe en una lectura se aplica a medias, y el
ejecutor lee el disco, no el índice de Git. Medir el disco es medir el
riesgo real; la reproducibilidad entre clones no se abandona: se obtiene
por **política declarada de ignorados** — `skip_dirs`, `exempt_paths` y,
desde esta decisión, `exempt_names` —, no por mecanismo.

`exempt_names` añade la exención que faltaba: por nombre exacto de
archivo, para la basura que Git no versiona (`.DS_Store`, `.dart_tool`,
`Thumbs.db`) sin declarar su ruta directorio por directorio.

```text
CONTRATO: skevi-gate.json clave «exempt_names» v1
Entrada:
  exempt_names: lista de texto [opcional] — nombres de archivo sin ruta.
Salida: los archivos cuyo nombre está en la lista quedan exentos del
  límite de tamaño, igual que «exempt_paths».
Errores:
  nombre con «/» o «\», vacío, «.» o «..» → BLOQ con mensaje que remite a
  «exempt_paths» (fallo accionable, ADR-007).
Invariantes:
  - se añade a los valores de Skevi, no los reemplaza (misma semántica
    aditiva que «exempt_paths»).
  - un nombre exento no se lee: el gate no abre el archivo (misma
    propiedad que las demás exenciones).
Compatibilidad: clave aditiva; un gate viejo la rechaza como desconocida
  (fail-closed, nunca la ignora). Cambios de formato -> v2.
```

Alternativas descartadas:

- **Medir sólo `git ls-files`.** Reproducibilidad total entre clones, pero
  punto ciego pre-commit: un archivo nuevo sin `git add` es invisible
  hasta commitearse, exactamente cuando el gate debe verlo. Añade además
  una dependencia de Git a la lógica del gate (stdlib-only hoy) y deja de
  medir en un árbol sin `.git`.
- **Respetar `.gitignore`.** Semántica no trivial — negaciones, anidación,
  precedencia de directorios — que en stdlib es un proyecto en sí,
  contra el principio 1 y la regla 3 del índice.
- **Dejar el comportamiento sin ADR.** Es el estado actual: una decisión
  de diseño vigente que ningún documento declara, sostenida sólo por el
  código. El issue que la reporta pide precisamente escribirla.

Consecuencias: dos clones con la misma `skevi-gate.json` producen el
mismo resultado salvo por archivos cuya basura no esté cubierta por la
política declarada — y ese hueco queda explícito en la config del
adoptante, no escondido en el código. Skevi no cambia su propia config:
sus dos `exempt_paths` de `.DS_Store` siguen válidos; migrarlos a
`exempt_names` es opcional y no perseguida aquí (diff mínimo).

**Ajuste de límite para `scripts/check_sizes.py`, declarado.** El gate
estaba al 99 % de su presupuesto (794/800) antes de esta decisión; la
clave nueva lo llevó a 814 líneas. Las salidas de §3.4 se recorrieron en
orden: no hay código muerto que borrar; la vida útil del archivo es una;
partirlo rompe «copiable sin edición» (ADR-006) y crearía un quinto
archivo distribuido sólo por contabilidad interna; y no está congelado,
 así que la exención no procede. Queda el ajuste que §3.4 permite
explícitamente: límite por archivo fijado por escrito — 830 en
`skevi-gate.json` (`limits`), con este párrafo como decisión. 830 deja
margen para una edición menor sin nueva decisión; la siguiente adición
estructural obliga a partir el archivo o a re-decidir. La ventana de
lectura de un ejecutor (del orden de 2000 líneas) no se agota con 830.

Verificación: `python3 scripts/check_sizes.py` → salida real registrada
en el reporte de la tarea; la suite (`python3 -m unittest discover -s
tests`) cubre fusión aditiva, rechazo de rutas/puntos/vacío, restauración
por `reset_to_skevi_defaults` y no-lectura del archivo exento. El total
lo reporta la suite, no este texto.

Procedencia: issue #41 del repo (adopción flutterFlow @ `2e0f9cf`,
ronda adversarial de contexto fresco, 2026-09-12); fricción previa en
`docs/specs/SPEC-AUDIT-2026-09-07-mejoras.md` y
`docs/specs/SPEC-LANG-2026-09-12.md`; decisión del humano en
conversación, 2026-09-13.
Razón: escribir la decisión de diseño que regía de facto sin estar
declarada, y dar la exención por nombre que cerraba la fricción
observada en tres adopciones.
