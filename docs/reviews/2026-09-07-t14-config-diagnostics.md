# Registro y dossier — T14, diagnóstico de configuración

Plan: [AUDIT-2026-09-07](../plans/2026-09-07-mejoras-auditoria.md).
Contrato: [SPEC-AUD-02](../specs/SPEC-AUDIT-2026-09-07-mejoras.md).

## Capa técnica

```text
id = SKV-T14-20260907-01
date = 2026-09-07
time_utc = 18:45:31Z
head_sha = 5a3a3af4477cdac76adacd2404537805ca2d28aa
model = GPT-6 (self-declared)
STATE = OK (T14 local gate only)
GATE = T14 local tests and fresh code/artifact reviews pass; MED-01 closed for check_sizes configuration.
EVIDENCE
- Initial increment commit -> 5a3a3af4477cdac76adacd2404537805ca2d28aa; six reviewed files only -> pass
- RED before T14 production change -> 50 focal tests; 8 failures including subtests -> pass
- RED causes -> 7 payload exposures and 1 missing controlled JSON diagnostic -> pass
- GREEN -> 50 focal tests and 73 full-suite tests OK -> pass
- Config diagnostics -> controlled fields/reasons, JSON line/column, no echoed caller text for covered failures -> pass
- Final gates -> 74 text files and 2 plans OK; plan within 300 lines; links and technical hash verified -> pass
- git diff --check -> no output -> pass
- Remote inspection -> main at 17413f150d08e1e65b72f70a858104505950e751; target branch absent -> pass
- PROP-008 -> f4a478fab5ad6bc0187a358fa8aeb7c87281af448f20f02169c15683dd95b721 unchanged and excluded -> pass
PENDING = Authorized T14 commit and branch push; next task T05. T05-T13 remain outside this increment.
DECISION = proceed (T14 local gate and publication dossier only)
OPERATIONS = commit T14 files; git push -u origin HEAD:refs/heads/fix/audit-gate-read-errors
AUTHORITY = Current user explicitly authorized commit and push at agent discretion; no merge, PR, tag or release.
RISK = Diagnostic wording changes; unknown keys/values are withheld. No claim of sanitizing other commands or all runtime failures.
report_sha256 = 4f411469cadd42e3c6ae97439505d46a774502875b9a690dfa888ab1fad2cf70
```

Hash: UTF-8, LF, sin newline final, excluyendo la línea report_sha256.
Las marcas describen el momento de emisión; no prueban aceptación ni identidad.

## Resultado y evidencia

T14 está verificada localmente con revisión fresca proceed. Las excepciones de
lectura/decodificación ya no se imprimen; los errores JSON conservan línea y
columna; la validación indica campo y motivo sin copiar claves/valores recibidos.
La subclase interna de ValueError permite mostrar sólo mensajes controlados,
sin cambiar el esquema aceptado ni las excepciones capturadas como ValueError.

Antes de cambiar producción se ejecutó:

```bash
python3 -B -m unittest discover -s tests -p test_check_sizes.py
```

Resultado RED: `Ran 50 tests`, `FAILED (failures=8)`. Cinco métodos nuevos;
los ocho fallos incluyen subtests. Siete verifican payload visible: decoder,
lectura, ValueError inesperado, clave desconocida, required, exempt_paths y
nombre de límite. El octavo comprueba que el JSON mal formado carecía del
diagnóstico controlado con nombre de archivo. Son fixtures y mocks sintéticos.
GREEN del mismo comando: 50 pruebas OK. Suite completa: 73 pruebas OK.

```bash
python3 -B -m unittest discover -s tests
python3 -B scripts/check_sizes.py
python3 -B scripts/check_plans.py
git diff --check
```

Gates antes de este registro: 73 archivos, 2 planes, ambos OK; gates finales:
74 archivos y 2 planes OK. El reporte del primer incremento se conserva como
evidencia histórica: MED-01 era pendiente entonces; T14 lo cierra para check_sizes.
No se atribuye este saneamiento a check_plans ni a todos los errores de runtime.

Revisión fresca: /root/review_t14, folio SKV-T14-REVIEW-20260907-01,
proceed sobre diff; comprobó 50 focales, 73 totales, compatibilidad de ValueError
y CONFIG_KEYS sin cambios. Segunda pasada: dossier, SPEC, plan, enlaces y hash
conformes; sin hallazgos nuevos. No se atribuye independencia de modelo.
El RED y la consulta remota son evidencia del ejecutor, no reproducción del
revisor. La siguiente tarea es T05; publicación aún prevista a esta emisión.

## Autoridad vigente y operaciones concretas

El humano indicó el 2026-09-07: «tienes autorizado commit y push segun creas
correponda adelante con siguietne». La autorización precede a este dossier;
el ejecutor concreta aquí sus operaciones bajo esa delegación de criterio.
No se afirma una aprobación humana posterior de un folio que aún no existía.

Primera operación realizada: commit 5a3a3af del incremento T00-T04, seis
archivos revisados, con 68 pruebas y gates verdes; PROP-008 excluida.
Segunda operación prevista: commit de script, tests, SPEC, plan y este reporte
para T14, sólo tras revisión fresca. Tercera: push de ambas confirmaciones a
origin, rama fix/audit-gate-read-errors, sin force. El remoto comprobado fue
https://github.com/kristhianmanue1/skevi.git y no tenía la rama de destino.
Una creación concurrente incompatible hará fallar el push normal; no forzarlo.

Riesgo: cambia el texto de diagnóstico; se retiene campo/motivo y se ocultan
datos de entrada. No se modifican main, política GitHub, CI, consumidores,
memoria ni PROP-008. Merge, PR, tag y release no forman parte de estas operaciones.
Verificación posterior: comparar git rev-parse HEAD con git ls-remote para la
rama exacta y revisar git status. La aceptación del push se reporta sólo cuando
esa comprobación termine; este dossier previo no afirma que ya ocurrió.
