# ADR-026: Precisión de la frontera de autoridad y alcance de artefacto

Estado: aceptado; implementado en `project-manifest.yaml` §`no_ofrece`.
Resuelve PREGUNTA-M6-3 de
[SPEC-M6](../specs/SPEC-M6-2026-09-07-seis-mejoras.md) con la opción A.

Contexto: la línea de `no_ofrece` decía «autoridad, conformidad ni perfiles de
aseguramiento; ese plano es de praxis-dev» — tres cosas en una. Leída
literalmente, la primera cede **toda** la autoridad. Esa lectura es
incompatible con el corpus desde antes de que existiera la pregunta: §4.3 y
§6.2 del estándar, ADR-017, ADR-018 y la excepción local de `AGENTS.md`
norman autoridad en detalle. Si «autoridad» significara el plano completo,
esas cinco fuentes ya lo estarían invadiendo. ADR-023 adoptó la lectura que
hace coherente al corpus —Skevi norma el mecanismo de graduación de permisos;
`praxis-dev` recibe la gobernanza— pero la dejó como interpretación, no como
decisión registrada.

**Evidencia recogida el 2026-09-08.** Antes de precisar la línea se comprobó
el estado real de los cinco planos cedidos por `no_ofrece`:

| Plano cedido a | Manifiesto propio | Skevi en su manifiesto | Skevi en su `AGENTS.md` | `skevi-gate.json` |
|---|---|---|---|---|
| `praxis-dev` | no existe | — | no | no |
| `argos` | sí | no | no | no |
| `an-kla-memory` | no existe | — | **sí** (ADR-0045) | **sí** |
| `epistates` | sí | no | no | no |
| `escrubery` | no existe | — | **sí** (ADR-0001) | no |

**Ningún manifiesto reciproca la cesión**, y ésa es la afirmación exacta que
sostiene esta decisión: la frontera de plano la declara Skevi sola. Pero
**reciprocidad y adopción son cosas distintas**, y confundirlas invierte el
sentido del hallazgo: `escrubery` y `an-kla-memory` adoptan Skevi como
estándar de proceso con ADR propio, y el segundo instala además su
`skevi-gate.json`. La primera redacción de este ADR midió sólo
`project-manifest.yaml` y concluyó «ninguno menciona a Skevi» — falso, y
detectado por la ronda fresca del 2026-09-08. Medir el artefacto equivocado
produjo la conclusión contraria a la real.

Lo que sí se sigue: **precisar la línea no requiere coordinación previa**,
porque ninguna contraparte ha aceptado una frontera que se pudiera
contradecir. Lo que **no** se sigue: que nadie dependa de Skevi. Tres de
estos cinco sí, y dos citan la versión etiquetada `v1.0.0` —`escrubery` en su
ADR-0001 y `an-kla-memory` en su `.skevi/usage-guide.md`—. Un barrido posterior
sobre todo el ecosistema, y no sólo sobre estos cinco, encontró un número de repositorios que citan a Skevi mayor que los cinco de esta
tabla —el barrido completo se retiró de este merge el 2026-09-08 por contener
cifras falsas verificadas en dos rondas adversariales; pendiente de rehacerse.

Decisión, en tres partes:

1. **La línea de autoridad se precisa** a «gobernanza de autoridad,
   conformidad y perfiles de aseguramiento». El mecanismo de graduación de
   permisos —qué operación exige qué autorización, cómo se gradúa, cómo se
   escala— queda explícitamente en Skevi, que es donde ya estaba.
2. **Se declara que las cesiones son decisiones de alcance propias, no
   acuerdos**, con la evidencia de arriba, en las fronteras de confianza —
   distinguiendo reciprocidad de manifiesto (ninguna) de adopción efectiva
   (dos proyectos). Una cesión no acordada no garantiza que alguien cubra ese
   plano.
3. **Se declara fuera de alcance la integridad del artefacto publicado y los
   riesgos propios del modelo**: firma y verificación de releases, archivo de
   componentes, endurecimiento del build, envenenamiento de datos o modelo,
   fuga de system prompt y debilidades de embeddings. Corresponden a los
   controles que `../crosswalk-estandares.md` marca sin cubrir: SSDF PS.2,
   PS.3, PW.6, y OWASP LLM04, LLM07, LLM08. Skevi norma el **método** con que
   se construye software; no norma propiedades del artefacto publicado ni del
   modelo empleado.

Alternativas descartadas:

- **Dejar la línea ambigua** (opción B de la pregunta). Cada regla de
  autoridad futura reabriría la misma discusión, y ADR-023 tendría que
  volver a defenderse cada vez.
- **Coordinar con praxis-dev antes de precisar** (opción C). Se descarta por
  la evidencia: praxis-dev no tiene manifiesto, de modo que no hay lado con
  el que coordinar todavía. Cuando lo tenga, esta línea es exactamente el
  insumo para esa conversación.
- **Cubrir los seis controles del punto 3.** Integridad de artefactos es
  configuración de plataforma más una norma de firma que este estándar no
  tiene; los tres riesgos de modelo son propiedades del producto, no del
  método. Normarlos sin poder verificarlos produciría reglas sin gate, que es
  lo que ADR-014 llama gate vacuo.
- **Callar el punto 3.** Un hueco sin dueño se lee como olvido; una frontera
  declarada se lee como decisión. El cotejo ya los tenía enumerados: no
  declararlos era la única parte que faltaba.

Consecuencias: `no_ofrece` gana precisión donde generaba contradicción y gana
una frontera donde había hueco. El cotejo de estándares deja de tener
controles «sin dueño» **una vez actualizadas sus seis celdas**, cosa que la
primera emisión de este ADR dio por hecha sin hacerla (corregido el
2026-09-08): pasan a estar declarados fuera de alcance, que es información
distinta y verificable. Un adoptante que necesite firma de
releases o defensa contra envenenamiento sabe, por el manifiesto, que no la
va a encontrar aquí. Las cesiones siguen siendo unilaterales y ahora lo dicen.

Verificación: `python3 scripts/check_sizes.py` → `OK`; la línea nueva no
contradice §4.3, §6.2, ADR-017 ni ADR-018, comprobado con `grep -n` sobre
cada fuente; los controles del punto 3 coinciden uno a uno con los marcados
sin cubrir en `../crosswalk-estandares.md`.

Procedencia: PREGUNTA-M6-3 de
[SPEC-M6](../specs/SPEC-M6-2026-09-07-seis-mejoras.md);
[ADR-023](ADR-023-superficie-de-ejecucion.md), cuya interpretación esta
decisión registra; [`crosswalk-estandares.md`](../crosswalk-estandares.md)
(PS.2, PS.3, PW.6, LLM04, LLM07, LLM08); ronda adversarial del 2026-09-08,
que refutó la premisa de coordinar con un proyecto sin manifiesto;
instrucción directa del humano, 2026-09-08.
Razón: convertir una interpretación en decisión, y los huecos sin dueño en
fronteras declaradas.
