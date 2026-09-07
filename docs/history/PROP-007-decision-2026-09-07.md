# PROP-007 — Autoridad Git graduada: zonas de autonomía, dossier de gate y delegación del gate

> **Estado:** ADOPTADA — D1-D3 aprobadas por el humano (2026-09-07,
> «adelante con recomendación», en conversación). Piloto G1-G5 corrido
> sobre el ciclo del dossier aceptado (folios `SKV-2026-09-07-01`/`-02`:
> rama → commit → push → PR #29 → merge → reporte de cierre); G4-G5 en
> vigilancia hasta que opere un orquestador designado. D4 ejecutada vía
> ADR-017 y el PR de adopción (estándar §6.2/§6.6/§4.3, manifest).
> Registro histórico: evidencia de decisión, no norma vigente.
> **Origen:** instrucción directa del humano (2026-09-07) y análisis en
> conversación. Aplica al dominio Git la graduación por clase de
> operación de ADR-004; el dossier hereda el formato de dos capas de
> PROP-006.

## Contexto

La norma vigente exige autorización humana previa y específica para
cada operación con efecto externo (§1.4, §4.3) y gradúa los permisos
del ejecutor (§6.2: leer no implica escribir; escribir no implica
commit; commit no implica push). En la práctica observada el humano
autoriza en lote («adelante con commit push etc») y los agentes operan
con ramas y commits propios sin fricción. Esta propuesta escribe la
regla que la práctica ya vive: autonomía en lo local y reversible;
dossier y aceptación en lo externo; y un gate que puede delegarse bajo
condiciones duras — §6.6 exige hoy una decisión humana en los bordes,
siempre, sin vía de delegación.

## D1 — Tres zonas de autoridad

**Propuesta:**

- **Z1 — autonomía del ejecutor:** commit y gestión de ramas locales
  propias: crear, cambiar y borrar locales ya fusionadas. La convención
  de nombres de §4.1 aplica igual. Sin propuesta previa: el contrato de
  tarea pre-autoriza Z1.
- **Z2 — gate:** push, merge, borrado de ramas remotas, tags, releases
  y toda operación de §4.3. Requieren dossier (D2) y aceptación
  registrada.
- **Z3 — quién es el gate:** el humano; o un orquestador designado
  conforme a D3.

**Propuesta en lote:** varias operaciones Z2 pueden proponerse juntas,
enumeradas; la aceptación declara qué operaciones del lote quedan
aceptadas y lo no aceptado sigue gateado.

**Alternativa descartada:** mantener la autorización una-por-una sin
graduación — es el statu quo; su coste real es ceremonia en lo
reversible y fricción en cada sesión material, sin ganancia de control
en lo externo.

## D2 — Dossier de gate y aceptación registrada

**Propuesta:** cada operación Z2 lleva un dossier con el formato de dos
capas de PROP-006:

- capa técnica: operación exacta (comando, rama, PR), evidencia
  (gates, tests, `comando → resultado`), riesgos;
- capa humana: razones y recomendación concreta — qué se pide hacer y
  qué alternativa queda si se rechaza.

La aceptación se registra con: quién acepta (humano u orquestador con
su designación citada), cuándo y contra qué folio. **Sin rastro de
aceptación, el permiso no existe** — la misma regla de evidencia del
repo: lo que no queda registrado no pasó.

**Alternativa descartada:** aceptación verbal sin rastro — no auditable
y no verificable después (vuelve G1 y G2 imposibles).

## D3 — Designación de orquestador (delegación del gate)

**Propuesta:** el gate de Z2 puede delegarse en un orquestador agéntico
sólo si la designación cumple todo esto:

1. **Escrita**, con alcance delimitado (tarea, proyecto o clase de
   operación) y **revocable**; nunca implícita, histórica ni
   autodeclarada por el ejecutor.
2. **Independiente del ejecutor**: otra sesión o contexto, idealmente
   otro modelo — el mismo principio del contexto fresco de `04` §5.1;
   la salida del ejecutor nunca es prueba suficiente (§6.3).
3. **Escalado obligatorio**: ante duda, evidencia inconsistente o
   alcance excedido, el orquestador escala al humano; nunca aprueba por
   cercanía ni improvisa autoridad (§6.7).
4. **Fail-closed por defecto**: sin designación vigente, el gate es el
   humano — el estado actual.

La designación vive donde el proyecto la declare (contrato de tarea o
manifest del adoptante); skevi recomienda el patrón y no impone
herramienta. La aceptación del orquestador es procedencia declarada,
nunca prueba criptográfica — el campo `model` de PROP-006 sigue siendo
autodeclarado.

**Alternativas descartadas:** delegación total permanente (borra la
decisión humana de los bordes y traiciona §6.6); orquestador obligatorio
para todo proyecto (ceremonia: la mayoría no lo necesita).

## Criterios de aceptación (falsables)

La propuesta se adopta sólo si un piloto real cumple:

- G1: toda operación Z2 de la sesión tiene dossier previo y aceptación
  registrada, auditable después de cerrada la sesión.
- G2: cero operaciones Z2 ejecutadas sin aceptación — cruzando reflog
  y remoto contra los folios de aceptación.
- G3: cero ceremonia en Z1 — ningún pedido de permiso para commits o
  ramas locales propias.
- G4: toda aceptación de orquestador es atribuible a una designación
  vigente y revocable; aceptación sin designación válida es violación.
- G5: toda duda del orquestador escala al humano y queda registrada
  como escalado, nunca como auto-resolución.

## D4 — Aterrizaje normativo

Si se aprueba: editar el estándar §6.2 (escalera de permisos con Z1
pre-autorizada por contrato), §6.6 (cláusula de delegación con las
condiciones de D3) y §4.3 (formato de dossier y aceptación); añadir la
entrada correspondiente en `project-manifest.yaml`
(`fronteras_de_confianza`); producir el ADR de la decisión y mover esta
PROP a `docs/history/` en el mismo cambio (patrón PROP-004). El piloto
que valida G1-G5 documenta la sesión de adopción reportada en dos capas
— y sirve a la vez como piloto F1-F4 de PROP-006.

## Criterios de decisión aplicados

§8 del estándar: la graduación es lo más simple de entender (tres
zonas, una regla cada una), lo más fácil de revertir (revocar una
designación es un cambio local), reduce la superficie de mantenimiento
(menos autorizaciones que gestionar) y no añade dependencias. La
delegación queda cercada por cuatro condiciones y un default
fail-closed.

## Adopción

D1-D3 quedan aceptadas o rechazadas por el humano en conversación; con
la aprobación, un PR ejecuta D4 con el piloto documentado. Mientras
tanto, este documento no obliga a nada: la norma vigente sigue rigiendo,
incluida la autorización una-por-una de §4.3.
