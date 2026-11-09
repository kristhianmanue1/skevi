# Ronda adversarial — afinar o desechar las propuestas 0.3.0 (PROP-014)

Objeto: las once propuestas candidatas (P1-P11) para una hipotética
versión 0.3.0 del contrato de coordinación, materializadas como
afirmaciones neutras fuera del repo, contra
`docs/proposals/PROP-014-contrato-coordinacion-multi-proyecto.md`
(v0.2.1-candidata) sobre `feat/prop014-contrato-coordinacion`
`5bdcfc3a059af13be957561c679f35680b9ea4cb`.

Revisó una sesión fresca del mismo proveedor (GLM), sin contexto de
autoría ni del análisis previo, con mandato de refutar y de sólo
lectura. Su primer informe llegó truncado; la tabla de veredictos se
remitió completa en la misma sesión.

Veredicto global: **fix-and-retry** — el conjunto contiene correcciones
que el contrato necesita, pero tal como venía era defectuoso en
conjunto; con los descartes y recortes aplicados, redacta en ~42 líneas
netas y queda listo.

## Veredictos (afinar o desechar)

| # | Propuesta | Veredicto | Razón esencial |
|---|---|---|---|
| P1 | Dos modalidades (protocolo activable) | **DESECHAR** | Conmutador fail-open autocalificado por la parte interesada; contradice el piso §7.1 de A4 en lectura amplia y es redundante con A2+A4 en lectura estrecha; añade ceremonia de clasificación por cambio. La sobregobernanza de lo trivial la resuelve P5 |
| P2 | Autorización efectiva por operación | **AFINAR** | Hueco real de A1 («enforced where technically possible» no prescribe ante inverificabilidad); exige subordinación del envelope a A4/§6.8 del canon local, semántica de vigencia y revocación (el contrato no tiene ninguna), y cierra el bootstrap del Coordinator: su authorization_ref es la aprobación §10 |
| P3 | Transiciones condicionales (expected_revision) | **POSTERGAR** | Prematuro: el hogar del estado es la pregunta abierta 1 y un único controlador ya serializa; reactivar cuando ambas cosas cambien |
| P4 | Reúso de evidencia con impacto inspeccionable | **AFINAR** | El ejemplo §7.1 modela la conducta prohibida (reúso declarado «No change» mientras revisa rev-b); anclar a los required checks de AR5; declaración desnuda = hipótesis |
| P5 | Tiers de proporcionalidad | **AFINAR** | «risk_proportionate» se usa sin definir; cortar la redundancia verbatim con AR6/AR4; el tier Low debe excluir los documentos que vinculan ejecutores (AGENTS.md, gates: son gobierno ejecutable); clasifica el Verifier con disputa §6; los tiers son baseline que un canon local puede elevar (coherencia con A4) |
| P6 | Escalera de negociación | **DESECHAR** (salvo 1 cláusula) | Duplica la fila de §6 y el diagrama §5; lo nuevo es sólo el presupuesto de negociación (AR4 acota review, no negociación) |
| P7 | Guardas en transiciones peligrosas | **AFINAR** | Tres defectos reales (path que se salta verification; verifying→blocked ausente; Coordinator escribiendo en proyectos); la guardia de reanudación debe discriminar por estado de entrada; el WO lo registra el capitán del proyecto, nunca el Coordinator |
| P8 | Recuperación ante fallos parciales | **AFINAR** (reducido) | Peldaños 1-3 y 5 ya viven en §8/L2; lo nuevo: compensaciones sólo pre-definidas en el CC y autorizadas, y el CC bloqueado si la consistencia no se puede establecer |
| P9 | Tres planos + claims no confiables | **AFINAR** (reducido) | «Una claim no confiere permiso» ya está en A1; el delta real es la exclusividad determinista para decisiones de control — y debe aclarar que la deliberación (rondas) sigue legítima |
| P10 | Métricas de valor | **POSTERGAR** | Material del plan del piloto, no del contrato; tres vías de juego reproducibles (cancelar todo = autonomía 1.0; rubber-stamp = latencia mínima; defect-seeding inflado); crearía un segundo marco competidor con §9 |
| P11 | Invariantes normativos + falsificación | **AFINAR** | La renuncia a revisión de spec necesita guarda: cubre sólo lo enumerado del 0.3.0 y la parametrización del piloto; tocar A1-A5, AR0-AR9 o la semántica de §4 reabre la sección |

## Riesgo de interacción más grave (cerrado con el descarte de P1)

P1×P5×P7: la «modalidad local» permitía que un cambio de autoridad
(editar un gate o un AGENTS.md) se clasificara «interno sin efecto
cross-project» por la parte interesada — el protocolo nunca se activaba,
P5 nunca clasificaba, P7 no aplicaba: el nivel de rigor lo elegía el
revisado. Desechar P1 lo cierra; A2+A4 ya son la modalidad local, con
el piso §7.1 innegociable.

## Nota de honestidad del autor

P1 fue propuesta por el propio ejecutor como «piedra angular
anti-burocracia» en el análisis previo; la ronda la refutó con un
contraejemplo que el análisis no vio. El registro queda como evidencia
del valor de la ronda y del riesgo de los análisis sin contexto fresco.

## Capa técnica

```text
id = SKV-PROP014-AFINADO-RONDA-20261109-01
date = 2026-11-09
time_utc = 12:03:30Z
head_sha = 5bdcfc3a059af13be957561c679f35680b9ea4cb
model = GLM-5.3 zai-coding-plan; revisor fresco (self-declared; not proof)
STATE = OK
GATE = ronda adversarial de solo lectura en sesion fresca sobre las once
  propuestas 0.3.0 (afirmaciones neutras fuera del repo) contra el
  contrato v0.2.1; veredicto por propuesta afinar/desechar/postergar;
  2 desechadas, 2 postergadas, 7 afinadas con texto de correccion.
EVIDENCE
- veredictos P1-P11 emitidos con file:line y contraejemplo por cada una -> pass
- contraejemplo P1 reproducido -> cambio de firma publica clasificado interno; protocolo nunca activa -> pass
- contraejemplo del ejemplo §7.1 -> verified_versions rev-a junto a changed_artifacts rev-b -> pass
- presupuestos de burocracia -> ~42 lineas netas para el paquete refinado; cero objetos nuevos obligatorios -> pass
- primer informe truncado -> tabla remitida completa en la misma sesion -> pass
- python3 scripts/check_sizes.py -> OK; 221 archivos; ruta 1640/1640 -> pass
PENDING = decision del Operador sobre el 0.3.0 refinado (P2/P4/P5/P7/
  P8/P9/P11 con sus textos de correccion; P3 y P10 al plan del piloto);
  preguntas abiertas 1-4 de PROP-014; entrega Git por lote.
DECISION = fix-and-retry
OPERATIONS = ronda de solo lectura via subagente fresco en dos emisiones
  (la primera llego truncada; la tabla se remitio en la misma sesion);
  sin efectos Git; sin edicion del contrato en esta ronda.
AUTHORITY = Operador 2026-11-09, en conversacion: «ronda adversarial
  fresca para afinar o desechar propuestas»; las propuestas no estaban
  adoptadas: la ronda decide su destino, no el ejecutor.
RISK = revisor del mismo proveedor y familia que el autor; las
  correcciones exactas de P2/P4/P5/P7/P8/P9/P11 viajan en el informe y
  en el backlog de la propuesta, sin verificacion contra implementacion
  (que no existe: §11 del contrato).
report_sha256 = 7337a4ea06e87b5f50b439076bfb550a03066816f295250551e726ec1610793c
```
