# Cotejo HV-6 — docs/orchestration/ contra el canon vigente

**Qué se cotejó.** La guía (`orquestacion-codex-opencode-tmux.md`, 728
líneas) y su runbook (165 líneas), verificados por última vez el
2026-08-12 contra `codex-cli 0.147.0`, `opencode 1.18.16` y `tmux 3.6a`,
contra el canon vigente a corpus/v9.

| Desfase | Evidencia | Estado |
|---|---|---|
| Reportes en dos capas (ADR-016) | 0 menciones en ambos archivos | ausente |
| Lote con folio (ADR-044) | 0 menciones de lote, folio o ADR-044 | ausente |
| Superficie (ADR-023) | 0 menciones | ausente |
| Ronda adversarial | 3; sin dos capas ni registro (ADR-037) | parcial |
| Caducidad | verificada 2026-08-12 (87 días); caduca con las tools | vencida |

Lo que la guía sí tiene y el canon respeta: separación controlador/ejecutor
con retiro del supervisor, señal `AGENT_DONE`, visibilidad tmux, y su propia
adversarial histórica en `docs/history/`. No contradice el canon: lo precede.

**Recomendación — opción C (re-scoplar como adaptador por host).** La guía
no es norma caduca sino el **adaptador por host** que la neutralidad de
proveedor exige mantener fuera del canon: cambiar su encabezado de «guía
técnica reutilizable» a «adaptador por host, fecha de verificación, sin
peso normativo», re-verificarla contra las versiones vigentes de las tres
herramientas (o declararla sin re-verificar) y conservarla en
`docs/orchestration/`, cuya fila del README ya dice «caduca con ellas».
La alternativa (archivo en `docs/history/`) pierde un mecanismo que el
ecosistema sigue usando y que el contraste con la propuesta externa
(valoró su §9) confirmó vivo.

## Capa técnica

```text
id = SKV-HV6-COTEJO-20261107-01
date = 2026-11-07
time_utc = 11:52:08Z
head_sha = 52d0482b4b9a03ea83baf3cc8fa65d0f3d02f96a
model = GLM-5.3 zai-coding-plan (ejecutor; self-declared; not proof)
STATE = PARTIAL
GATE = cotejo HV-6 de docs/orchestration/ contra el canon vigente; guia
de 728 lineas + runbook de 165, verificada por ultima vez 2026-08-12
(87 dias); recomendacion emitida, decision del Operador pendiente.
EVIDENCE
- grep -c «dos capas|ADR-016» en guia y runbook -> 0 y 0 -> pass
- grep -c «lote|folio|ADR-044» en la guia -> 0 -> pass
- grep «superficie|ADR-023» en la guia -> 0 coincidencias -> pass
- grep «ronda adversarial» -> 3 menciones sin dos capas ni registro -> pass
- encabezado de la guia -> verificacion 2026-08-12, tres tools -> pass
PENDING = decision del Operador: re-scoplar como adaptador por host
(recomendado) o trasladar a docs/history/
OPERATIONS = redaccion del cotejo; sin efectos Git
AUTHORITY = orden del Operador 2026-11-07 «adelante con pendientes»
sobre la tarea HV-6 del plan ya entregado
RISK = cotejo por grep dirigido, no lectura linea a linea de 728 lineas;
los huecos encontrados son ausencias verificables, no interpretaciones
report_sha256 = 37d5fde3004dab9bbcfdfdf8160ff605f7f66dd9f3e746935807393c93b91f5a
```

La decisión es del Operador. Este cotejo no cierra HV-6: su step 2
(recomendar con decisión registrada) queda pendiente de esa decisión.
