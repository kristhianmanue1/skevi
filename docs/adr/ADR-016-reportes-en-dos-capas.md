# ADR-016: reportes de agente en dos capas con bloque de trazabilidad

Estado: aceptado. Implementado en el formato de fase de `00-INDICE.md`,
el reporte adversarial de `04` §5.2 y el §6 del estándar. Implementado
en 442061a (02 §3.3).

Contexto: PROP-006 (instrucción directa del humano, 2026-09-07) propuso
separar los reportes del agente en dos capas — técnica en inglés para
máquinas, humana en el idioma del proyecto para personas — y añadir un
bloque de trazabilidad (folio, fecha, hora, hash, modelo). Los formatos
vigentes mezclaban ambas audiencias en un solo texto. El piloto corrió
sobre la propia sesión de adopción: dos reportes punta a punta (folios
`SKV-2026-09-07-01` y `-02`) con hash reproducible vía `sha256sum`,
folio sin colisión y capa humana derivada de la técnica. Criterios
F1-F4: F3 pass (dos hashes, cero colisiones), F4 pass (revisión de la
propia sesión); F1 pass por esquema cerrado — un parser es trivial
sobre líneas `clave = valor` y líneas `... [pass|fail|inconclusive]` —
quedando la verificación con orquestador externo como seguimiento; F2
pass por operación real (el humano decidió sobre las capas humanas).

Decisión: todo reporte de tarea material lleva capa técnica (inglés,
autoritativa: claves fijas `STATE`, `GATE`, `EVIDENCE` con líneas
`comando -> resultado -> pass|fail|inconclusive`, `PENDING`), capa
humana (idioma del proyecto, proyección sin afirmaciones nuevas; ante
contradicción gana la técnica) y bloque de trazabilidad de esquema
cerrado: `id` folio monótono, `date`, `time_utc`, `head_sha`,
`report_sha256`, `model` (autodeclarado, nunca prueba), `session` si
existe. Tarea trivial: capa humana sola. Forma canónica del hash,
fijada por el piloto y ratificada aquí: UTF-8, LF, sin newline final,
excluida la línea `report_sha256`.

Alternativas descartadas:

- una sola capa bilingüe: más barata, pero obliga a cada público a leer
  el idioma ajeno y a parsear prosa;
- metadata obligatoria en cada mensaje: ceremonia sin riesgo real,
  contra el mínimo necesario;
- firma criptográfica del modelo: imposible; el campo `model` queda
  autodeclarado y el principio 7 prohíbe que eleve confianza.

Consecuencias: los formatos de fase y adversarial ganan las dos capas y
el bloque; un orquestador puede parsear sin leer prosa y el humano
puede supervisar sin leer la pared técnica. El `report_sha256` da
integridad reproducible al reporte. La regla hereda la polaridad de
idioma de ADR-015.
