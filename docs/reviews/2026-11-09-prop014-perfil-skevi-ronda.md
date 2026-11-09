# Ronda adversarial — PROP-014-S perfil mínimo (sin Herdr, sin multi-modelo)

Objeto: `docs/proposals/PROP-014-perfil-skevi-minimo.md` (0.5.0-S.1),
derivación del Core 0.5.0-C.1 de la familia PROP-014 (adoptada como
política de devHerdrExpert, `dfb7214`), sobre `feat/prop014-contrato-coordinacion`
`85efecb` con cambios sin commit.

Revisó una sesión fresca del mismo proveedor (GLM), sin contexto de
autoría, mandato de refutar, sólo lectura. Cotejó el perfil contra el
Core y el corpus v0.5.0 (respaldados con hash) y contra el canon skevi
(§4.3, §6.8, `04` §5.1/§5.3, mapa Z1-Z3).

Veredicto: **fix-and-retry** — y el reintento se ejecutó: el HIGH y los
dos MED se corrigieron antes de este registro; los cuatro LOW también.
Verificado en positivo: el hash del Core citado reproduce byte a byte,
todas las reglas citadas existen con esos nombres, el mapeo a zonas
Z1/Z2/Z3 es fiel (push skevi sigue gated por folio, sin path), y la
escalera S2 es fiel a `04` §5.1/§5.3 (Rung C vetado justo donde skevi
veta la ronda propia; material sin segundo contexto escala en vez de
auto-cerrar).

## Hallazgos y disposición

1. [HIGH] S3 degradaba la identidad del escritor a «git commit identity
   + protección de rama» exactamente donde S1 declara válido el
   despliegue sin red — el único aflojamiento real del Core (que exige
   firmas o interfaz controlada como precondición). Cerrado: fail-closed
   — sin firma ni interfaz controlada no hay transiciones (sólo
   observación); la identidad de commit git nunca satisface la
   precondición por sí sola; y un evento sin validación del controller
   designado en su commit es propuesta, nunca transición.
2. [MED] «material trigger» indefinido en la bisagra de S2: dejaba un
   path de auto-cierre en Rung C si el agente único clasificaba por
   debajo del piso. Cerrado: definido por referencia — piso mecánico
   §6 del Core más disparadores objetivos de `04` §5.3 para
   participantes skevi vía S4/A4, clasificación registrada y
   disputable.
3. [MED] El controller mínimo no era fail-closed ante validación
   omitida (el agente podía commitear el evento sin correr el checker).
   Cerrado: la cláusula propuesta-nunca-transición del punto 1 lo
   cubre.
4. [LOW] S2 atribuía al Core un mandato de contexto fresco que no
   tiene (es práctica registrada de la familia bajo AR8). Cerrado:
   premisa reformulada — la escalera es adición pura.
5. [LOW] «Model diversity is never required» sin acotar. Cerrado: «by
   this family's floor; a stricter local canon may require it (A4)».
6. [LOW] Cadena de precedencia omitía a la tarjeta. Cerrado: perfil >
   tarjeta (no normativa).
7. [LOW] El registro de esta ronda se citaba antes de existir.
   Cerrado: este registro es el citado; existe con hash antes del
   commit del perfil.

## Capa técnica

```text
id = SKV-PROP014-PERFILS-RONDA-20261109-01
date = 2026-11-09
time_utc = 17:28:28Z
head_sha = 85efecba2f38149c1b6cf4ec74c0a9e3ba1f591a
model = GLM-5.3 zai-coding-plan; revisor fresco (self-declared; not proof)
STATE = OK
GATE = ronda adversarial de solo lectura en sesion fresca sobre el
  perfil minimo 0.5.0-S.1 (derivacion del Core 0.5.0-C.1); 1 HIGH,
  2 MED y 4 LOW; todos corregidos antes de este registro; el perfil
  solo aprieta tras la correccion del HIGH.
EVIDENCE
- shasum del Core de respaldo -> e02190ed613f7665904e50ce7a0ce2a48fa3e01ddb252d7885a26d55eef3e5ed, citado exacto en el perfil -> pass
- citas de reglas L1/L5/L6/E3/E4/AR8/secciones -> existen con esos nombres en Core y corpus -> pass
- mapeo Z1/Z2/Z3 -> push skevi gated por folio, sin path de Tier-1; fiel a §4.3 -> pass
- fidelidad de la escalera S2 -> Rung C vetado en material igual que 04 §5.3; escala en vez de auto-cerrar -> pass
- wc -l del perfil -> 120/800 aprox tras correcciones; limite respetado -> pass
- sin fences mermaid -> nada que validar con parser -> pass
PENDING = aprobacion del perfil por el Operador (§8/§10 de la familia);
  lote de la rama feat/prop014-contrato-coordinacion; hogar canonico
  de la familia confirmado en devHerdrExpert (dfb7214).
DECISION = fix-and-retry
OPERATIONS = ronda de solo lectura via subagente fresco; correcciones
  sobre el perfil antes del commit; sin efectos Git.
AUTHORITY = Operador 2026-11-09, en conversacion: «debes crear tu
  propia version basada en estas propuestas y compatible pero pensando
  en que no siempre se tendra herdr o entornos agenticos
  multi-modelo».
RISK = revisor del mismo proveedor y familia que el autor; el perfil
  no ha corrido piloto: sus tres escenarios S6 son diseno no probado.
report_sha256 = 0422ee471086d69988fa0f3df23b2dc116dc95efa4e99d17572d0d2194e41f90
```
