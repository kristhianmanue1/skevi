# ADR-040: Familia de manifiesto adr/v1 — los ADRs quedan sellados

Estado: aceptado; implementado en `docs/adr/MANIFEST.json` (adr/v1),
`scripts/check_templates.py` y `scripts/check_sizes.py` (gate/v11).

Contexto: `docs/MANIFEST.json` (corpus, ADR-032) sella sólo 8 archivos —
estándar y guía. Los ~40 ADRs, inmutables por regla del corpus, quedaban
fuera de todo sello: un adoptante que descargue el corpus no puede verificar
que los ADRs que lee son los originales (issue #64 §1). La ronda del
2026-10-17 (P5) descartó la alternativa de «declarar explícitamente qué capa
queda sellada» sin verificador: es la mitigación de prosa que el propio #63
denuncia de #42, y lo que ADR-026 tipifica como regla sin gate. La vía del
campo nuevo en `docs/MANIFEST.json` era inviable sin más código: el esquema
cerrado lo rechaza.

Decisión: cuarta familia de manifiesto, `skevi/adr-manifest/v1` con espacio
de nombres `adr/vN`, sobre `docs/adr/MANIFEST.json` con **listado exacto**
del directorio y digests — `docs/adr/` es plano y los ADRs son inmutables,
así que el contrato de ADR-020 encaja sin enmiendas: cada ADR nuevo exige
entrada nueva y bump, y el gate lo recuerda igual que ya hace con corpus y
plantillas. Registro de instalación: la familia existe para verificar
descargas, no como flujo de adopción; no se define `adr-install/v1` hasta
que un consumidor real lo pida. Diferida con #64 §4, la familia no sella
`docs/history/` ni `docs/reviews/`: sus vidas útiles son otras y el corpus
no promete su inmutabilidad byte a byte.

Consecuencias: el sello del corpus se completa donde más duele su ausencia
(ADRs = decisiones inmutables); el listado exacto añade un paso mecánico a
cada ADR nuevo (entrada + bump `adr/vN`), el mismo precio que ya pagan las
plantillas; `00-INDICE.md` queda dentro del sello.

Procedencia: [issue #64](https://github.com/kristhianmanue1/skevi/issues/64)
§1; tarea HG-5 del
[plan 2026-10-17](../plans/2026-10-17-holgura-de-gate-y-issues.md); veredicto
P5 de la ronda
[2026-10-17-plan-gate-ronda.md](../reviews/2026-10-17-plan-gate-ronda.md);
[ADR-028](ADR-028-manifest-de-scripts.md) y
[ADR-032](ADR-032-manifiesto-de-corpus.md) por el mecanismo de familias.
