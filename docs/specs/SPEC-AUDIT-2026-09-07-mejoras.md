# SPEC-AUDIT-2026-09-07 — Mejora de Skevi tras revisión fresca

## F0 — Problema, resultado y autoridad

Problema: el gate puede declarar éxito sin leer un archivo sujeto a control;
el corpus también contiene diferencias de autoridad y referencias ambiguas.
Resultado: convertir el diagnóstico revisado en trabajo trazable y comenzar
por una corrección comprobable del gate, conservando las fronteras de Skevi.

Fuente de habilitación: instrucción del humano del 2026-09-07 de persistir
un plan detallado con tareas y fases e iniciar su ejecución. La revisión
fresca anterior aceptó el análisis corregido, no ratificó nuevas políticas.
La instrucción habilita documentos y la corrección local; no implica publicar.

Clase: Architectural por crear un plan multi-tarea (guía F0 §2, ADR-013).
El incremento de código conserva interfaces y dependencias existentes.
La revisión fresca de cierre aplica al gate copiable con consumidores externos
(guía F3 §5.3). El plan contiene los steps y DoD; esta SPEC define conducta.

Plan: [tareas, dependencias y aceptación](../plans/2026-09-07-mejoras-auditoria.md).

### Requisitos

```text
REQ-AUD-01 [funcional] [fuente: humano, 2026-09-07]
Enunciado: persistir el itinerario completo de mejoras y comenzar su ejecución.
Criterio de aceptación: ver T00, T01 y T02-T04 del plan.
Prioridad: imprescindible

REQ-AUD-02 [funcional] [fuente: estándar §3.4; reproducción adversarial]
Enunciado: un archivo no exento que no pueda leerse no equivale a verificado.
Criterio de aceptación: ver T02-T03 del plan y casos C1-C4 de SPEC-AUD-01.
Prioridad: imprescindible

REQ-AUD-03 [restricción] [fuente: estándar §2.4; ADR-007]
Enunciado: los errores de lectura producen diagnóstico controlado y saneado.
Criterio de aceptación: ver T02-T03; C1-C4 no filtran traceback ni payload.
Prioridad: imprescindible

REQ-AUD-04 [restricción] [fuente: ADR-006; estándar §3.4]
Enunciado: se conserva el contrato de configuración, exenciones y límites.
Criterio de aceptación: ver T03; casos C5-C6 y suite previa en verde.
Prioridad: imprescindible

REQ-AUD-05 [restricción] [fuente: AGENTS.md; humano, alcance de inicio]
Enunciado: las operaciones externas y decisiones de política mantienen su gate.
Criterio de aceptación: ver T00, T04 y T13; sin operación no autorizada.
Prioridad: imprescindible

REQ-AUD-06 [funcional] [fuente: análisis corregido; humano, plan completo]
Enunciado: cada mejora restante tiene salida, dependencia y decisión de entrada.
Criterio de aceptación: ver T05-T13; ningún cierre por checkbox sin evidencia.
Prioridad: imprescindible para planificar; ejecución posterior condicionada
```

### No objetivos y restricciones

- No modificar PROP-008 preexistente durante el primer incremento.
- No adoptar propuestas por el solo hecho de planificarlas.
- No escribir memoria ni checkpoints; la persistencia solicitada es Markdown.
- No modificar GitHub, consumidores, hooks, dependencias ni política de CI.
- Sin commit, push, merge, tags ni releases en este incremento.
- Sin escaneo exhaustivo de seguridad, certificación PMI ni conformidad.
- Sin refactor general del gate, garantía de snapshot ni soporte de otra
  codificación; entradas no exentas se verifican como UTF-8.

Excepción local identificada durante GREEN: `file .DS_Store docs/.DS_Store`
clasifica ambas rutas como Apple Desktop Services Store; git check-ignore -v
confirma .gitignore:1 y git ls-files confirma que no están rastreadas.
Se añaden sólo esas rutas a exempt_paths de skevi-gate.json: son metadatos
binarios de Finder, no documentos sujetos a lectura. Fuente: exención explícita
del estándar §3.4. No se altera el lector, patrón global ni política de límites.
Esta corrección incorpora skevi-gate.json al alcance local de T03-T04.

Entorno comprobado: Python del sistema 3.9.6 para gates; entorno virtual
3.12.12 para AN-KLA; dependencia de implementación exclusivamente stdlib.
Base: `17413f150d08e1e65b72f70a858104505950e751`; rama de trabajo
`fix/audit-gate-read-errors`. Estado inicial: PROP-008 no rastreada, ajena
al incremento. Se conserva sin cambio. AN-KLA: contexto válido, revisión 19.

Preguntas de entrada del primer incremento: ninguna. Se usa UTF-8 y el
contrato existente de exenciones. Elegir autoridades delegadas, política de
revisiones remotas, folios distribuidos o adopción PMI pertenece a tareas
posteriores del plan; ninguna respuesta es necesaria para corregir lecturas.

## F1 — SPEC-AUD-01 [cubre: REQ-AUD-02, REQ-AUD-03, REQ-AUD-04]

Comportamiento: el comando local agrega un incumplimiento si la lectura de
un archivo descubierto y no exento falla. Continúa comprobando los demás
archivos, muestra BLOQ y devuelve 1. Ningún error de lectura equivale a None.

Entradas: árbol y configuración actuales; contenido UTF-8 para archivos no
exentos. Salidas: CLI existente, texto en español, códigos 0/1 existentes.
Errores: ruta relativa del archivo y motivo controlado; no reproducir la
excepción cruda, sus bytes ni rutas absolutas que pueda incluir.

Casos:

- C1: DADO README existente, CUANDO su lectura lanza PermissionError,
  ENTONCES BLOQ, salida 1 y diagnóstico de README sin excepción cruda.
- C2: DADO un Markdown no canónico descubierto, CUANDO falla su lectura con
  OSError, ENTONCES también bloquea; la regla no se limita a REQUIRED.
- C3: DADO README con bytes no UTF-8, CUANDO se ejecuta el CLI,
  ENTONCES BLOQ, salida 1 y motivo UTF-8, sin volcar contenido.
- C4: DADO un host de registro leído para el conteo, CUANDO su segunda
  lectura falla, ENTONCES BLOQ controlado; no termina con traceback.
- C5: DADO un archivo explícitamente exento por ruta o extensión, CUANDO
  el gate recorre el árbol, ENTONCES no intenta leerlo ni lo bloquea.
- C6: DADO árbol válido, CUANDO se ejecuta el gate, ENTONCES mantiene OK/0;
  un exceso de tamaño sigue produciendo BLOQ/1 con el límite vigente.

Invariantes: None representa solamente una exención; los errores de lectura
no producen éxito; el gate sigue sin demostrar corrección semántica.
Una segunda lectura exitosa no prueba un snapshot consistente: esa propiedad
no se añade ni se atribuye a este arreglo.
El diagnóstico de load_config anterior al recorrido no queda saneado por
este incremento; la revisión detectó exposición de excepción cruda allí.
Su tratamiento se agenda como T14, sin reclamar saneamiento universal del CLI.

### Diseño y compatibilidad

Conservar `count_text_lines(relative)` y su resultado para lectura válida y
exención; dejar propagar OSError/UnicodeDecodeError al coordinador `main()`.
Capturar ambos alrededor de las lecturas de cada archivo, incluida la del
registro, y agregar diagnóstico con motivo fijo. La excepción no se imprime.
No ampliar los patrones de exención ni añadir detección heurística de binarios.

Contrato CLI existente: invocación sin nuevos flags; salida OK/0 o BLOQ/1.
El cambio observable es que un árbol no verificable deja de pasar. Adoptantes
con archivos binarios no exentos deben declarar una exención justificada;
no se considera UTF-8 inválido una prueba automática de que algo es binario.

Alternativas: capturar sólo en el helper no cubre la segunda lectura; envolver
todo el proceso y abortar al primer fallo pierde la lista de incumplimientos;
un nuevo tipo de resultado o lector compartido añade cambios innecesarios.
La corrección deriva de ADR-007 y §3.4; no decide nueva arquitectura ni precisa
un ADR adicional para repetir una decisión ya aceptada.

F2: reutilizar estructura y runner existentes; no crear cascarón de aplicación.
Los documentos nuevos viven en specs, plans y reviews según su propósito.

## Evidencia previa de entrada

EV-01: git status/rev-parse → base y rama indicadas; PROP-008 preexistente.
EV-02: gates previos → OK, 70 archivos y 1 plan; suite → 62 pruebas OK.
EV-03: mock selectivo de lectura de README, llamando main completo → OK/0
con 69 archivos ante PermissionError y UnicodeDecodeError (defecto confirmado).
EV-04: .venv/bin/python -m an_kla, con update check desactivado → context y
verify OK, revisión 19. No hubo escritura de memoria.

F0: OK para T00-T04; requisitos con fuente, límites y entorno comprobados.
F1: OK para SPEC-AUD-01; casos, errores y compatibilidad definidos.
Estas marcas habilitan la ejecución local inicial, no cierran F3 ni las
decisiones posteriores. Evidencia RED/GREEN y revisión: se crea el registro
en docs/reviews/2026-09-07-mejoras-auditoria.md al cerrar el incremento.
