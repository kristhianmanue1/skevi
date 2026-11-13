# Ronda adversarial del cambio del issue #99 — lecciones y calibración

Registro de la ronda que ataca el cambio entregado en la rama
`docs/issue99-lecciones-metodo` (issue #99: 9 lecciones de método; filas
1-2 a la guía 04, filas 6-8 a `docs/lecciones/` bajo ADR-053, filas
3/4/5/9 verificadas ya cubiertas). Revisor: subagente de contexto fresco
de otra familia de modelo que el autor (autor GLM/zai; revisor
Qwen `qwen3:8b` local vía Ollama). Disposiciones por tres pilas (ADR-050).

Contexto de la elección de revisor: los tres proveedores de modelos
grandes con acceso ese día quedaron fuera (Anthropic sin saldo, OpenAI sin
créditos, Alibaba con token inválido); se usó el revisor local de otra
familia disponible, con las verificaciones mecánicas (digests, gates,
conteos) cubiertas por verificación determinista del ejecutor.

## Capa técnica

```text
id = SKV-2026-11-13-01-RONDA
date = 2026-11-13
time_utc = 15:01:40Z
head_sha = ff9b6c54e22b5ca85b03a26948dd1229fbecc418
model = GLM-5.3 zai-coding-plan; revisor fresco de otra familia:
  Qwen qwen3:8b Ollama local (self-declared; not proof)
STATE = OK
GATE = ronda adversarial con contexto fresco real de otra familia sobre el
  diff 7d7d06b..ff9b6c5: condensación neta cero sin pérdida en guía 04
  (306 líneas; ruta 1640/1640), cascada corpus/v12 + plantillas/v24 +
  adr/v11 con digests reproducibles, ADR-053 coherente, lecciones sin
  duplicar norma ni sobreafirmar su origen, plan E1-E6 fiel a lo
  ejecutado; hallazgo LOW corregido y hallazgo refutado con cita;
  disposiciones por tres pilas antes de commitear.
EVIDENCE
- Ronda parte 1, diff de guia 04 (revisor) -> hallazgo LOW: referencia `06-componentes-con-llm.md` abreviada; corregido en ff9b6c5 [pass]
- Segundo hallazgo de la parte 1 -> refutado: «superpowers executing-plans» sigue presente en el texto nuevo, cita verificada [pass]
- Ronda parte 2, lecciones y README (revisor) -> lecciones honestas, sin sobreafirmar su origen; README con precedencia y promocion [pass]
- Veredicto consolidado del revisor (salida transcrita) -> proceed, con hallazgo LOW corregido y parte 2 sin hallazgos [pass]
- Suite ejecutada por el propio revisor -> 297 tests OK en 0.713 s [pass]
- Digests de la cascada en 5 registros (docs/, templates/, .skevi/) -> 88 digests recomputados contra disco, 0 inconsistencias [pass]
- Gates del ejecutor en ff9b6c5 -> check_sizes OK con 240 archivos y ruta 1640/1640; check_plans 14 planes; check_reports 57 reportes [pass]
- Tres check_templates contra .skevi/ -> al dia en plantillas/v24, gate/v14 y corpus/v12 [pass]
PENDING = ninguno material abierto. Nota registrada: el revisor escribió un
  archivo de trabajo (decision.txt) pese a su restricción de sólo lectura;
  retirado de inmediato, sin cambios en el árbol (git status limpio).
DECISION = proceed
OPERATIONS = dentro del lote SKV-LOTE-20261112-01: commits locales de la
  rama docs/issue99-lecciones-metodo (9fb332f, 5740a9d, 39dbdb3, ff9b6c5);
  siguen push de rama, PR, CI en verde, revisión final de cabeza como
  comentario del PR, merge fijado al SHA revisado y respuesta al issue
  #99. Sin squash, force-push, tags, releases ni borrado de ramas.
AUTHORITY = Operador 2026-11-13, aceptación textual: «acepto publicar :
  publicar 95aeb5d y el lote SKV-LOTE-20261112-01 para el #99.» y «se
  aplican tus recomendaciones» (decisiones D1-D4 del informe de contexto).
RISK = revisor de otra familia pero de capacidad limitada (qwen3:8b
  local): dos degradaciones de formato durante la ronda (respuesta no
  solicitada y archivo fuera de restricción); mitigado con verificación
  determinista del ejecutor (digests por script, gates, conteos) y la
  suite; la ronda de otra familia con modelo grande queda como mejora
  pendiente cuando haya saldo.
report_sha256 = 2a34ec6ea75c6c9f393e75007446c752677fe536f61da317057608a25b2a7020
```

## Capa humana

La ronda revisó el cambio completo del issue #99 con un revisor
independiente de otra familia (Qwen local). Su único hallazgo real (abreviar
la referencia `06-componentes-con-llm.md`) se corrigió y reverificó; su
segundo hallazgo se refutó con cita textual; las lecciones resultaron
honestas respecto de su origen. Veredicto: **proceed**. El límite de
capacidad del revisor quedó declarado en RISK y compensado con las
verificaciones mecánicas; la capa técnica manda ante contradicción.

> **Nota (2026-11-13, r1):** la revisión posterior de contexto fresco
> (Sonnet r1, registro `2026-11-13-issue99-r1-fix.md`) **reabre la
> disposición de esta ronda**: sin acceso a las notas de origen, este
> revisor no podía contrastar la evidencia de las lecciones cuando afirmó
> su honestidad. La r1 verificó contra las notas y corrigió dos
> Evidencias (filas 7 y 8).
