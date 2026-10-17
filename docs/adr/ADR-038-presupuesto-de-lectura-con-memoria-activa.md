# ADR-038: Presupuesto de ruta de lectura con memoria activa

Estado: aceptado; implementado en `skevi-gate.json` clave `reading_path`.

Contexto: el contrato `skevi/an-kla-integration v1` (`05` §6, ADR-019) dice
sin ambigüedad que la activación de la memoria «absorbe la lectura de este
documento y de `AN-KLA.md` en el presupuesto de ruta de lectura del adoptante
(ADR-021) y la declara por escrito en su config de gate». Skevi tiene
detección positiva de AN-KLA desde el 2026-09-07 (PROP-008) y nunca declaró
esa absorción: la clave `reading_path` de `skevi-gate.json` medía
`AGENTS.md` + `00-INDICE` + estándar + el peor caso de `01`–`04`, y nada más.
El issue #63 documentó ese patrón en dos adoptantes — mitigaciones de prosa
que ninguna máquina comprueba, gate en verde midiendo una ruta que ya no es
la obligatoria — y la ronda del upgrade a b34 (2026-10-17) lo dejó como
hallazgo MED abierto: **el tercer afectado es el propio skevi**. Cifras
históricas, fechadas porque caducan (ADR-025 p4): al 2026-10-17, la ruta
declarada daba 998/1000 mientras la ruta obligatoria real para trabajo
material — con `05` (116) y `AN-KLA.md` (478, tras crecer 136 líneas con la
plantilla beta.33) — sumaba **1592**.

Decisión:

1. `reading_path.files` declara, además de la espina actual,
   `docs/ai-agent-guide/05-memoria-del-agente.md` y `AN-KLA.md`, en orden de
   lectura. El gate vuelve a medir la ruta que un ejecutor debe leer de
   verdad para trabajo material en este repositorio.
2. `reading_path.limit` sube de 1000 a **1600**. No es un techo derivado sino
   un trinquete decidido (ADR-025): 1592 observados el 2026-10-17 más una
   holgura mínima deliberada. La holgura pequeña no es un descuido: es lo que
   hace visible cada crecimiento.
3. **El crecimiento de la plantilla de AN-KLA es un evento presupuestario.**
   El bump que agote la holgura exige re-decidir este número con su propio
   ADR, en el mismo cambio del upgrade — nunca un ajuste en silencio, que es
   lo que ADR-030 y ADR-032 rechazaron del trinquete convertido en contador.
4. `06-componentes-con-llm.md` queda **fuera** de la espina por decisión
   propia: es un complemento condicional con lectura por disparador
   (ADR-024), no parte de la ruta obligatoria; que no aparezca aquí es
   deliberado, no una omisión.

Consecuencias:

- La falsa comodidad de #63 desaparece en casa: presupuesto declarado y ruta
  real vuelven a coincidir.
- El chequeo **máquina** de coherencia `root_markdown` ↔ `reading_path` que
  propone #63 queda diferido a la partición del cluster `check_sizes`
  (issue #61: script en 870/870 exactos, `tests/test_check_sizes.py` en
  773/800 y `tests/test_check_templates.py` en 771/800). Mitigación interina:
  el invariante queda escrito aquí y la política de bump (punto 3) convierte
  cada Upgrade en un momento de verificación.
- Un próximo bump de plantilla an-kla que crezca más de ocho líneas pone el
  gate en rojo hasta que su ADR re-decida el presupuesto. Eso es lo que se
  busca: el coste de lectura de la memoria se decide, no se acumula.

Alternativas descartadas:

- **Margen para k bumps (1700–1900).** Compra silencio a cambio de
  visibilidad: el presupuesto deja de apretar justo cuando el driver externo
  (la plantilla) es el que más crece. Es el trinquete convertido en contador.
- **Pagar la deuda sólo con prosa** (dejar la absorción escrita en este ADR
  sin tocar la config). Repite el fallo de #42 que #63 denuncia: mitigación
  sin máquina y sin presupuesto.

Procedencia: `05` §6 y [ADR-019](ADR-019-integracion-ankla-por-contrato.md);
[ADR-021](ADR-021-presupuesto-de-ruta-de-lectura.md);
[ADR-025](ADR-025-trinquete-no-techo-derivado.md);
[issue #63](https://github.com/kristhianmanue1/skevi/issues/63); rondas del
2026-10-17 registradas en
[../reviews/2026-10-17-ankla-b34-adopcion.md](../reviews/2026-10-17-ankla-b34-adopcion.md)
y
[../reviews/2026-10-17-plan-gate-ronda.md](../reviews/2026-10-17-plan-gate-ronda.md).
