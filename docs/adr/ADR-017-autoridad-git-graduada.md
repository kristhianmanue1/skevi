# ADR-017: autoridad Git graduada en tres zonas con gate delegable

Estado: aceptado. Implementado en el §6.2, §6.6 y §4.3 del estándar y
en `fronteras_de_confianza` de `project-manifest.yaml`; la referencia
de commit se completa en el cambio que materializa (02 §3.3).

Contexto: PROP-007 (instrucción directa del humano, 2026-09-07). La
norma exigía autorización humana previa por cada operación con efecto
externo (§1.4, §4.3; §6.2: cada escalón se autoriza aparte) y no
contemplaba delegar el gate (§6.6: siempre decisión humana explícita).
La práctica observada autoriza en lote y los agentes operan commits y
ramas propias sin fricción. La sesión de adopción sirvió de piloto: un
dossier de dos capas (folio `SKV-2026-09-07-01`) propuso el ciclo
rama → commit → push → PR → merge; el humano lo aceptó en conversación
y el cierre se reportó con folio propio (`SKV-2026-09-07-02`).
Criterios G1-G5 observados en ese ciclo: dossier previo y aceptación
registrada (G1), ninguna operación Z2 sin aceptación (G2), cero
ceremonia en lo local (G3); G4-G5 quedan en vigilancia hasta que opere
un orquestador designado — sin designación, no son ejercitables.

Decisión: tres zonas. **Z1** — commit y ramas locales propias del
ejecutor (crear, cambiar, borrar locales ya fusionadas),
pre-autorizados por el contrato de tarea, sin propuesta previa. **Z2**
— push, merge, borrado de ramas remotas, tags y releases: dossier
(capa técnica con operación exacta y evidencia; capa humana con
razones, riesgos y recomendación) y aceptación registrada (quién,
cuándo, folio); lotes válidos si la aceptación enumera lo aceptado.
**Z3** — el gate es el humano, o un orquestador designado por escrito,
con alcance delimitado y revocable, independiente del ejecutor (otra
sesión o contexto, idealmente otro modelo) y con escalado obligatorio
al humano ante duda; sin designación vigente, el gate es el humano.

Alternativas descartadas:

- autorización una-por-una sin graduación (statu quo): ceremonia en lo
  reversible sin ganancia de control en lo externo;
- delegación total y permanente del gate: borra la decisión humana de
  los bordes;
- orquestador obligatorio para todo proyecto: ceremonia que la mayoría
  no necesita.

Consecuencias: baja la latencia en lo local y reversible sin tocar el
control de lo externo. La aceptación del orquestador es procedencia
declarada, nunca prueba criptográfica (principio 7). Sin rastro de
aceptación, el permiso no existe. §6.6 deja de decir "siempre humano"
a cambio de las cuatro condiciones de designación y el default
fail-closed.
