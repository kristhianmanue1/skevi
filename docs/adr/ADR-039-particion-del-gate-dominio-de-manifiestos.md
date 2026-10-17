# ADR-039: El dominio de manifiestos vive en check_templates; check_sizes delega

Estado: aceptado; implementado en `scripts/check_sizes.py` y
`scripts/check_templates.py` (gate/v9).

Contexto: el issue #61 dejó registrado que `scripts/check_sizes.py` llegó a
**870/870** líneas — holgura cero — haciendo cinco cosas: tamaños, archivos
canónicos, ruta de lectura, manifiestos e identidad del gate. La ronda
adversarial del 2026-10-17 (P2) precisó que el cuello de botella es un
**cluster**: `tests/test_check_sizes.py` en 773/800 y
`tests/test_check_templates.py` en 771/800. ADR-032 ya anticipó por escrito
que «la siguiente adición estructural obliga a partir el archivo o a
re-decidir»; HG-3 (el chequeo máquina del issue #63) necesita ese espacio.

El dominio de manifiestos estaba partida en dos: `check_templates.py` era el
dueño temático — esquemas, namespaces y drift contra el registro del
consumidor — pero la validación estructural y el cotejo contra el disco de
los manifiestos fuente (las tres familias de ADR-020/028/032) vivían en
`check_sizes.py`, duplicando conjuntos de claves y expresiones de digest.

Decisión:

1. La validación estructural de manifiestos y su cotejo contra el disco
   (`check_template_manifest`, `check_corpus_manifest` y sus apoyos) se
   mueven a `check_templates.py`, su hogar por materia. Conservan el modelo
   de fallo de lista agregable que `check_sizes.main()` consume.
2. `check_sizes.py` queda con tamaños, archivos canónicos, ruta de lectura e
   identidad del gate, y **delega** mediante import. La unidad de copia del
   adoptante pasa a ser, de forma declarada, **los cuatro scripts juntos**:
   ya lo era de facto — `check_plans.py` importa `CONFIG_KEYS` de
   `check_sizes` desde antes de este ADR y `scripts/MANIFEST.json` versiona
   los cuatro como una familia con una sola versión `gate/vN`.
3. El salto es **gate/v8 → gate/v9, breaking**: quien re-copie sólo
   `check_sizes.py` obtiene un `ImportError` al arrancar. La nota de
   migración del manifiesto lo dice: re-copiar `check_sizes.py` y
   `check_templates.py` juntos. Fallar al empezar es fail-closed; fallar a
   medias con un gate que no valida manifiestos sería fail-open.

Alternativas descartadas:

- **Paquete `scripts/skevi_gate/` con módulos.** ADR-028 deja fuera del
  MANIFEST de scripts todo subdirectorio: el código movido quedaría sin
  cotejo contra la fuente — un agujero de sellado creado justo al arreglar
  la holgura. Además agranda la superficie de adopción más que el corte por
  materia.
- **Un tercer script `check_manifests.py` de nivel superior.** Mismo
  acoplamiento de import que la opción elegida, pero con un archivo nuevo
  que duplica el hogar temático que ya existía.
- **Subir el límite a 900-950 con ADR.** Salida legítima según #61, pero
  compra holgura sin resolver la duplicación del dominio ni liberar espacio
  en las suites del cluster.

Consecuencias:

- `check_sizes.py` queda en ~650/800 — cabe HG-3 (coherencia
  `root_markdown` ↔ `reading_path`, issue #63) sin otro ADR de límite.
  La exención `limits` de `skevi-gate.json` para este archivo (870) se
  retira con el mismo cambio: retirar una exención no exige ADR;
  subirla o crearla sí (estándar §3.4).
- `check_templates.py` crece a ~600/800: asume su dominio completo.
- Las pruebas del dominio se mueven a `tests/test_check_manifests.py`,
  aliviando `tests/test_check_sizes.py` (~645/800); `test_check_templates.py`
  no se toca. Los archivos de test nuevos no escalan la clase de la tarea
  (ADR-012).
- Las plantillas de ejemplo cambian por obligación, no por gusto: los
  registros `scripts-installed.json` e `installed.json` deben coincidir con
  la versión de su manifiesto fuente al publicarse — un adoptante nuevo que
  sólo llena los placeholders recibiría BLOQ en su primera ejecución si no
  (BLOCKER de la ronda 2026-09-08, custodiado por tests). El salto de este
  cambio es `plantillas/v10 → v11`, no breaking: sólo sincronizan los dos
  ejemplos.
- El comportamiento observable del gate no cambia: mismos mensajes, mismo
  código de salida, misma config. Lo que cambia es dónde vive el código y
  qué debe copiar el adoptante.

Procedencia: [issue #61](https://github.com/kristhianmanue1/skevi/issues/61);
tarea HG-2 de [../plans/2026-10-17-holgura-de-gate-y-issues.md](../plans/2026-10-17-holgura-de-gate-y-issues.md);
ronda adversarial P2/P8 de
[../reviews/2026-10-17-plan-gate-ronda.md](../reviews/2026-10-17-plan-gate-ronda.md);
[ADR-028](ADR-028-manifest-de-scripts.md),
[ADR-032](ADR-032-manifiesto-de-corpus.md),
[ADR-006](ADR-006-gate-configurable-por-proyecto.md).
