# Ronda adversarial del chequeo de coherencia (HG-3, gate/v10) y su disposición

Evaluador con contexto fresco (subagente, solo lectura) sobre el diff de
HG-3 antes de publicarlo. Veredicto: **fix-and-retry**; las dos correcciones
exigidas se aplicaron y los checks se repitieron en verde. La tercera
devolución es una pregunta de alcance, escalada al Operador.

## Disposición de hallazgos

| Hallazgo | Severidad | Disposición |
|---|---|---|
| El remedio «quítalo de root_markdown» era un callejón circular: el mismo gate BLOQuea el Markdown de raíz no declarado («suelto en raíz») — dos mensajes se contradecían y un ejecutor automatizado haría ping-pong | MED | **Corregido**: la rama alternativa del mensaje y de la nota de migración v9→v10 ahora dicen «muévelo fuera de la raíz del proyecto» |
| Falso negativo simétrico en el conjunto intrínseco: `CLAUDE.md`/`AGENTS.md` existentes en raíz y ausentes de un presupuesto activo quedan sin señal — la misma falsa comodidad de #63 | MED | **Escalado al Operador**: extender el requisito a los intrínsecos es decisión de alcance normativo, no de este chequeo; la exclusión queda declarada en el comentario del código como deliberada y pendiente |
| La generalización a CONTRIBUTING.md/SECURITY.md no es exceso: el propio issue la avala («o existe como markdown de raíz») | LOW | **Aceptado por diseño**, registrado en la ronda |
| Sin test de la vía `worst_case_of` | LOW | **Corregido**: test añadido — un Markdown de raíz es lectura siempre, no alternativa de fase; BLOQ verificado |
| Acoplamiento del «1400» del mensaje con la prosa de `usage-guide.md` | LOW | **Aceptado como riesgo documentado**: es un ejemplo citado «como ejemplo»; sin chequeo de drift de prosa |
| La sugerencia opcional (2) de #63 (aviso en el placeholder de la plantilla) sigue sin adoptarse | LOW | **Abierto**: se decide al cerrar el issue |
| Cambios sin commitear sobre main | LOW | **Corregido**: rama `feat/gate-v10-coherencia-root-markdown` creada antes de commitear |

## Lo que la ronda atacó y no rompió

El RED es real y lo reprodujo de forma independiente; los tres tests cubren
los casos que dicen cubrir; la cadena de versiones y digests íntegra
(`gate/v10` breaking con migración, `plantillas/v12`, `corpus/v4` intacto);
el mensaje del gate dice la verdad sobre la plantilla (usage-guide L117);
ningún documento declara v9 como vigente (ADR-039 es inmutable y describe
su fecha, correcto).

## Capa técnica

```text
id = SKV-GATEV10-20261017-01
date = 2026-10-17
time_utc = 14:03:27Z
head_sha = 1a4f7a8f7b36e7eada0c7f5950d9c60d5e8e54d0
model = GLM-5.3 (self-declared)
STATE = PARTIAL
GATE = HG-3 machine check for #63 implemented (gate/v10); round fix-and-retry, its two fixes applied, scope question escalated.
EVIDENCE
- fresh-context subagent round -> fix-and-retry: 2 MED, 4 LOW -> pass
- RED observed and independently reproduced by the round -> AssertionError 0 != 1 on the exact new test -> pass
- python3 -m unittest discover -s tests -> Ran 270 tests OK -> pass
- each of the eight test modules in isolation -> all OK -> pass
- python3 scripts/check_sizes.py -> OK 152 files, reading path 1592/1600, gate/v10 -> pass
- extra declared only in worst_case_of (sandbox) -> BLOQ, not an escape route -> pass
- digests of the three manifest families vs disk per round -> all match; corpus/v4 intact -> pass
- grep 1400 usage-guide -> line 117 documents the case the message cites -> pass
PENDING = publication of this branch under standing authorization; Operator scope decision on intrinsic AGENTS/CLAUDE requirement.
DECISION = proceed
OPERATIONS = local commit on feat/gate-v10-coherencia-root-markdown; push, PR and merge under standing publication authorization.
AUTHORITY = human instruction 2026-10-17 (adelante con recomendaciones y permiso para publicar); scope escalation preferred over silent broadening.
RISK = the 1400 example in the gate message is coupled to usage-guide.md prose (accepted, documented); #63 optional item 2 still undecided.
 = 17c1eca152d9dd9ca72db8f3254201788703fec286da26c10397e38ab5c55d20
report_sha256 = 2bdee64dbb42d55f141736ee27837f734a71685928ce02251d15d93c39abfada
```

Hash: UTF-8, LF, sin newline final y sin la línea `report_sha256`.
Partido de PARTIAL: verificación local completa; publicación inmediata bajo
autorización vigente; decisión de alcance pendiente del Operador.
