# ADR-044: push y merge propuestos por avance con autoridad condicional

Estado: aceptado el 2026-10-28; implementado en `AGENTS.md`,
`project-manifest.yaml` y `corpus/v6`. La publicación requiere su propio gate.

Contexto: [ADR-018](ADR-018-coherencia-de-autoridad.md) mantuvo en Skevi
autorización humana una por una para push y merge, restringiendo el gate
delegable general del estándar §6.6. El Operador aprobó la continuación
autónoma de ADR-043 y precisó: «por instruciones del humano o configuracion
futura el agente puede realizar push y merge, y agnete debe de proponer de
acurdo avance estas operaciones» (conversación, 2026-10-28). La
[SPEC-AGENTIC](../specs/SPEC-AGENTIC-2026-10-28.md) C11-C17 distingue
propuesta, permiso y ejecución. Esta entrega no identifica un gate futuro
adoptado y operativo.

Decisión: al llegar a hitos verificables, el agente prepara y presenta al
gate el dossier en dos capas de push ordinario o merge exactos, con folio,
destino, commit, evidencia, riesgos y recomendación. Ejecuta sólo si la
operación está enumerada y cubierta por (a) aceptación humana previa,
explícita, vigente y registrada contra el folio del dossier, o (b)
configuración futura adoptada expresamente por humano y verificada por un
gate independiente real, que registre aceptación equivalente. Un lote puede
cubrir dossiers y operaciones enumerados y condicionados sin nueva consulta
en cada paso; cada operación se revalida inmediatamente antes de su efecto.

La vía (b) exige emisor y custodia verificables, alcance y destinos
cerrados, usos deduplicables, caducidad y revocación, comprobación del commit
y estado remoto, y reconciliación tras timeout. El ejecutor no puede
activar o ampliar su propia autoridad editando configuración, ADR, manifest,
memoria, skill o plugin. Si no hay gate designado, operativo y verificable,
el humano sigue siendo el gate. Esta decisión no instala tal gate ni
autoriza push/merge de la rama actual.

Alternativas descartadas:

- Exigir aprobación humana nueva tras cada hito aunque exista un lote
  vigente: repite una decisión ya delimitada y frena la continuidad.
- Dejar que el agente decida por progreso o por un campo `allow`: confunde
  evidencia con autoridad y permite auto-otorgamiento.
- Activar ahora un archivo de configuración en Skevi: el repositorio no
  tiene runtime, custodia ni gate externo que lo haga exigible.

Consecuencias: sustituye **sólo** la exigencia humana una por una de
ADR-018 y `AGENTS.md` para push ordinario y merge. Conserva su jerarquía,
separación de memoria y compatibilidad de adoptantes. `force-push`, rebase
de historia compartida, reset destructivo, borrado remoto, tags, releases,
despliegue y demás destructivas siguen bajo autorización humana explícita
por operación. Una restricción más fuerte de un adoptante prevalece; nadie
se actualiza automáticamente. La capa general del estándar §4.3/§6.6 ya
permite dossier, lote explícito y gate designado, por lo que no se modifica.

Procedencia y razón: instrucción del Operador citada arriba; estándar §1.4,
§4.3, §6.6 y §6.8; SPEC-AGENTIC C11-C17. Separar la propuesta oportuna del
permiso efectivo reduce esperas sin convertir un artefacto autodeclarado en
autorización. Un `proceed`, CI verde o SHA no acreditan esa autorización.
