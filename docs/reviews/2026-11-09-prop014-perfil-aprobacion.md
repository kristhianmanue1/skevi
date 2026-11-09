# Aprobación del Operador — PROP-014-S como política de coordinación de skevi

El Operador aprobó el perfil mínimo del contrato de coordinación
(`docs/proposals/PROP-014-perfil-skevi-minimo.md`, 0.5.0-S.1) como
política de coordinación de skevi, con la orden literal del 2026-11-09:
«adelante para comists push merges y aprovacion de perfil» — aceptada
en selección estructural que nombra las cuatro partes (commits, push,
merges, aprobación del perfil).

Alcance exacto de la aprobación: el perfil (derivación del Core
0.5.0-C.1 de la familia PROP-014, adoptada como política de
devHerdrExpert en `dfb7214`) queda aprobado **como política de skevi**
para coordinación multi-proyecto — el mismo plano que skevi declara no
ofecer en su manifiesto, ahora cubierto por perfil propio. No es
adopción de canon: el corpus de skevi no cambia; en conflicto dentro de
un proyecto participante manda su canon local (Rule A4; para skevi, sus
zonas Z1/Z2/Z3 siguen mandando — S4 del perfil). Las precondiciones
§8/§10 de la familia (hogar del estado con `state_home_ref`, identidad
autenticada del escritor, `time_source`, designaciones de Coordinator y
Controller) quedan pendientes para la primera colaboración real, igual
que el piloto de escenarios.

Procedencia de la cadena: corpus v0.5.0 → Core 0.5.0-C.1 (sha256
`e02190ed613f7665904e50ce7a0ce2a48fa3e01ddb252d7885a26d55eef3e5ed`) →
perfil 0.5.0-S.1, rondado en fresco antes de esta aprobación
(`2026-11-09-prop014-perfil-skevi-ronda.md`,
`report_sha256 = 0422ee471086d69988fa0f3df23b2dc116dc95efa4e99d17572d0d2194e41f90`).

## Capa técnica

```text
id = SKV-PROP014-PERFIL-APROBACION-20261109-01
date = 2026-11-09
time_utc = 17:40:02Z
head_sha = 617e62e6cc92b149cff55e952f2af4fb51286be8
model = GLM-5.3 zai-coding-plan (self-declared; not proof)
STATE = OK
GATE = registro de decision del Operador: aprobacion del perfil
  0.5.0-S.1 como politica de coordinacion de skevi, con alcance
  declarado y precondiciones §8/§10 pendientes para el primer uso.
EVIDENCE
- orden literal del Operador -> «adelante para comists push merges y aprovacion de perfil» -> pass
- seleccion estructural aceptada -> nombra las cuatro partes de la orden -> pass
- ronda previa del perfil cerrada -> 0422ee471086d69988fa0f3df23b2dc116dc95efa4e99d17572d0d2194e41f90 -> pass
- sha256 del Core de la cadena -> e02190ed613f7665904e50ce7a0ce2a48fa3e01ddb252d7885a26d55eef3e5ed (verificado en la ronda) -> pass
- python3 scripts/check_sizes.py -> OK; 225 archivos; ruta 1640/1640 -> pass
- python3 scripts/check_reports.py -> OK; 54 reportes + este registro -> pass
PENDING = precondiciones §8/§10 para la primera colaboracion real;
  lote de entrega de la rama feat/prop014-contrato-coordinacion.
OPERATIONS = registro de decision de solo escritura documental; sin
  efectos Git en si mismo.
AUTHORITY = Operador 2026-11-09, en conversacion (orden citada arriba);
  la aprobacion es de politica, no de canon — el corpus skevi no cambia.
RISK = la orden llega con erratas de tipeo («comists», «aprovacion»):
  el alcance se tomo de las cuatro partes nombradas, interpretable sin
  ambiguedad material.
report_sha256 = 4aea88db150452bd918e4de395a41f7f205999ac268b9dba2b43428d2f35739e
```
