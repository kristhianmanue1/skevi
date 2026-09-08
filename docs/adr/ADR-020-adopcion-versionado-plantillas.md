# ADR-020: Adopción del versionado de plantillas (PROP-006@#28) con enmiendas T09

Estado: aceptado

Contexto: las plantillas de adopción (`templates/skevi/`) se copian a mano
y sin versión: relleno legítimo, customización y obsolescencia eran
indistinguibles (medición del 2026-09-02 registrada en el issue). La
propuesta PROP-006@#28 (D1-D4) y las enmiendas T09 ya aceptadas
(`docs/proposals/AUDIT-template-provenance.md`) definían el diseño;
quedaba abierta una sola decisión (#28 D3.2): si el drift incompatible es
fallo o aviso.

Decisión: adoptar D1-D3 con las enmiendas T09. Lado fuente: MANIFEST
(`skevi/template-manifest/v1`) con versión vigente `plantillas/v1`,
digests y `history` por salto con bandera `breaking`. Lado consumidor:
registro `skevi/template-install/v1` con `source`, digests al instalar y
`customized`. Clasificación T09: (A) obsoleto compatible → aviso; (B)
obsoleto incompatible → fallo `template_drift_version`; (C) personalizado
→ anula A/B por archivo declarado; versión sin cadena hasta la vigente →
B (fail-closed). D3.2 se resuelve como **fallo**: la opción que la propia
propuesta argumenta («instalar una versión retirada es improvisar con
material vencido»), consistente con el principio 5 del estándar y
ADR-007. D4 queda resuelto por aterrizaje simultáneo con la promoción a
estable (PROP-005), ya vigente. El chequeo (`scripts/check_templates.py`)
es manual, local, stdlib-only y no muta consumidores; el gate local
valida el MANIFEST sólo cuando existe. La exigencia canónica de Skevi
sobre sí mismo (MANIFEST, registro y script presentes) vive en su propia
`skevi-gate.json` (`required`), no en los valores por defecto del script:
un adoptante con un `templates/skevi/` previo a este cambio que actualice
el gate no se ve bloqueado (ronda adversarial, hallazgo HIGH).

Alternativas descartadas:
  - Statu quo sin versionado: el drift medido quedaba indetectable.
  - Aviso fuerte en vez de fallo: rompe el fail-closed de ADR-007 y
    permite operar con material vencido sin decisión explícita.
  - Comparar bytes de copia contra plantilla: falso positivo permanente,
    porque el relleno es la finalidad de la plantilla (autorevisión del
    propio #28).
  - Chequeo automático, instalado o remoto: contradice las fronteras del
    manifest («no instala, no observa, no muta»).

Consecuencias: cambiar una plantilla exige bump de versión y regenerar el
MANIFEST — el gate local bloquea cualquier otra vía. Los consumidores
declaran su instalación en `.skevi/installed.json` y comprueban drift con
un comando manual; la migración de una copia previa es manual, una vez,
guiada por `history` y digests. Sin registro de instalación, ningún
efecto: adopción progresiva. El MANIFEST es contrato cerrado: campos no
declarados se rechazan.

Procedencia: aprobación humana (2026-09-08, conversación: «adelante
adoptamos propuestas de plantillas»). Deliberación: issue #28 de este
repositorio y [enmiendas T09](../proposals/AUDIT-template-provenance.md).
