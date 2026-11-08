# Piloto ADR-043 — bloque B (PT-3): B1 y B2 medidas

Objeto: cierre del bloque B del piloto pre-registrado — tareas B1 y B2
bajo el ciclo autónomo, con su ronda adversarial de bloque — sobre
`feat/piloto-adr-043`, commit `4735904` (bloque A cerrado en
`docs/reviews/2026-11-08-piloto-bloque-a.md`).

## Las dos tareas y sus pasos

**B1 (Bounded scripts) — contención de `test_check_templates.py`.**
Partición exacta: `SalidaDeLaCadenaTests` y `DetalleSaneaTextoAjenoTests`
viajaron byte a byte (verificado por la ronda contra `96ef6ae`) a
`tests/test_check_templates_salida.py` con loader y helpers propios.
Pasos reversibles sin consulta: (1) inspección de la estructura de
clases, (2) corte por script, (3) corrida de la suite — **fallo** de
`MainBlockIsAtTheEndTests` (la guardia estructural del propio fichero
exigía newline final tras el bloque `__main__`, que el corte había
perdido), (4) corrección de una línea, (5) suite en verde. El fallo
interno se resolvió en el paso siguiente sin escalar; es la guardia del
propio archivo trabajando como fue diseñada (no un re-trabajo del host).

**B2 (Bounded scripts) — paridad hook↔CI.** El hook `pre-push` corre
ahora los tres auto-chequeos de `check_templates` bajo guarda
`-f <registro>`: sin registro no hay efecto (ADR-020) y el adoptante
sin `.skevi/` no se bloquea; con registro corrupto, `check_templates`
falla y el hook aborta (verificado por la ronda en sandbox). Pasos
reversibles: (1) escritura del hook, (2) ejecución standalone en verde.

## Métricas del bloque (evidencia del ejecutor; el recomputo es de PT-5)

| Métrica | B1 | B2 | Evidencia |
|---|---|---|---|
| M1 consultas al Operador | 0 | 0 | ninguna pausa durante el bloque |
| M2 pasos reversibles sin consulta | 5 | 2 | enumeración arriba |
| M3 hallazgos HIGH/BLOCKER | 0 | 0 | ronda del bloque: `proceed` |
| M4 re-trabajos por capacidad del host | 0 | 0 | el fallo interno de B1 fue de contenido, no del host |

Disposición de los hallazgos de la ronda (taxonomía ADR-050): los dos
LOW del bloque A y los cuatro de este bloque se registran sin abrir
pase de arreglos — H1 (divergencia hook↔CI ante registro borrado:
decisión consciente del diseño ADR-020, el CI es autoritativo), H2/H3
(cosméticos del módulo nuevo: se pliegan si el fichero se toca de
nuevo), H4 (import sin uso preexistente: fuera de perímetro).

## Capa técnica

```text
id = SKV-PT3-BLOQUE-B-20261108-01
date = 2026-11-08
time_utc = 14:30:00Z
head_sha = 47359046718042eecd0fb386cb5f2b6d64614981
model = GLM-5.3 zai-coding-plan (self-declared; not proof)
STATE = OK
GATE = PT-3 del plan 2026-10-29-piloto-adr-043: dos tareas reales
  (B1 y B2) ejecutadas bajo el ciclo, M1-M4 registrados con evidencia y
  ronda adversarial del bloque con decision.
EVIDENCE
- git show 4735904 --stat -> 3 ficheros (-154/+216/+19); nada mas -> pass
- comparacion byte a byte de las clases movidas contra 96ef6ae -> identicas -> pass
- wc -l -> 620 y 216; deuda 774/800 resuelta; limite 800 respetado -> pass
- conteo de tests -> 44 def test_ conservados (34+10); suite 297 OK -> pass
- sh -n hooks/pre-push -> sintaxis OK; standalone exit 0 (3 gates + 3 checks + suite) -> pass
- sandbox de la ronda: registro corrupto -> BLOQ; registro ausente -> omitido (ADR-020) -> pass
- ronda del bloque (sesion fresca) -> proceed; M3 = 0 HIGH, 0 BLOCKER; 4 LOW -> pass
- M1/M2/M4 por tarea -> 0/5/0 y 0/2/0, self-declared, enumerados arriba -> pass
PENDING = bloque C (C1 plan del programa B; C2 vacio declarado) y PT-5;
  los LOW de los bloques A y B viajan a PT-5 como registro.
OPERATIONS = tareas B1 y B2 en rama feat/piloto-adr-043 sin entrega Git;
  ronda de solo lectura; sin consultas al Operador durante el bloque.
AUTHORITY = Operador 2026-11-08: «Ordeno ejecutar el piloto ADR-043»
  (registrada en el sellado PT-1); bloques pre-registrados desde el
  sellado.
RISK = M1/M2/M4 self-declared; la ronda verifico perimetro y cobertura;
  el recomputo final contra baseline es de PT-5.
report_sha256 = 894bb39b5f0bb283ed47bbe2f9f1e2bd908018d9a03bae7bb7ca269548b3d817
```
