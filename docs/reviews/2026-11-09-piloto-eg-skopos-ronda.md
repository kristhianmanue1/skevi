# Ronda adversarial — kit del piloto EG↔Skopos (primer vuelo del contrato)

Objeto: `docs/coordination/eg-skopos/` (seis archivos: README, CC
candidato v0.1.0, IA-REGISTRO, WO-SK-001, WO-EG-001, events.jsonl) sobre
`main` `b41ba9dab6a92041fbef23b3055288e49d753ff0` con cambios sin
commit. Primer vuelo real del contrato de coordinación bajo el perfil
mínimo S de skevi, aprobado como política.

Revisó una sesión fresca del mismo proveedor (GLM), sin contexto de
autoría, mandato de refutar, sólo lectura — incluida la lectura de los
cinco contratos bilaterales reales de expertoGobernanza para verificar
la fidelidad del mapeo.

Veredicto: **fix-and-retry** — y el reintento se ejecutó: los cinco HIGH
y los seis MED se corrigieron antes de este registro; los tres LOW
también. La fidelidad del mapeo resistió el ataque (estados,
vencimientos, fail-closed y la distinción forma/fidelidad verificados
contra los originales con file:line por el revisor).

## La orden del Operador (registro durable — H-4)

Esta ronda registra con hash la orden que habilita el kit, citada por
los `authorization_ref` del CC y de la semilla de eventos: **«renovamos
el bloque Skopos — y lo hacemos ya como piloto del contrato de
coordinación, matando dos pájaros adelante»** (Operador, 2026-11-09, en
conversación; aceptación de la opción 1 del análisis inmediato
anterior: renovar como piloto). Este registro con hash es el artefacto
verificable de esa orden.

## Hallazgos y disposición

1. [HIGH] Contradicción de orden en el encendido: los capitanes podían
   ejecutar antes del `agreed`. Cerrado: pasos 2-3 registran y dejan
   listo; la ejecución sólo tras AR0 → `agreed` — «el vencimiento
   presiona, y el contrato no se dobla».
2. [HIGH] Dependencia autocircular en WO-SK-001 (dependía de la IA que
   él mismo produce). Cerrado: movida a `references`; `dependencies`
   apunta a la aprobación §10 del encendido.
3. [HIGH] tier_1 concedía push de pie. Cerrado: tier_1 = commits y
   ramas locales; push y merge según el canon local de cada participante
   (A4/S4 — en skevi, folio).
4. [HIGH] Autorización autorreferencial (la orden sólo se citaba a sí
   misma en el kit). Cerrado: este registro con hash es el artefacto
   durable; los `authorization_ref` repuntados a él.
5. [HIGH] La renovación de derivados se prometía sin vehículo. Cerrado:
   ruta de la política de derivados en `allowed_scope` con criterio
   propio y procedimiento de verificación.
6. [MED] IA-002 omitía su propio vencimiento y la regla de migración no
   cubría su vía. Cerrado: vencimiento anotado y regla extendida a la
   vía 002.
7. [MED] Aceptar derivatives vencido de llegada sería aceptar letra
   muerta. Cerrado: aceptación condicionada a la política renovada.
8. [MED] `time_source` sin marca de bloqueante. Cerrado: bloqueante
   para `agreed`.
9. [MED] Encendido subespecificado. Cerrado: paso 1 enumera las
   precondiciones completas (hogar, tiempo, designaciones, identidad de
   escritor); AR0 con dueño y peldaño; creación del hogar y del
   controller secuenciados.
10. [MED] Falta el borde hacia la política 0500 en WO-EG-001. Cerrado:
    `IA-004@nueva` en dependencies.
11. [MED] EVT-001 presentaba como transición lo que es propuesta (S3).
    Cerrado: `"kind": "proposal"` y README lo llama borrador del
    registro.
12. [LOW] «Igual que IA-003» confundía perfiles independientes (IA-004
    tiene política propia). Cerrado. «Hash del actor cuando exista»
    debilitaba S3: transición sólo con identidad de escritor. Cerrado.
    La cesión del plano a epistates (manifest) ahora declarada; la
    opción de repo dedicado la despeja. Cerrado. Cada criterio de
    aceptación lleva su procedimiento o comando. Cerrado.

## Capa técnica

```text
id = SKV-PILOTO-EG-SKOPOS-RONDA-20261109-01
date = 2026-11-09
time_utc = 18:15:25Z
head_sha = b41ba9dab6a92041fbef23b3055288e49d753ff0
model = GLM-5.3 zai-coding-plan; revisor fresco (self-declared; not proof)
STATE = OK
GATE = ronda adversarial de solo lectura en sesion fresca sobre el kit
  del piloto EG-Skopos (6 archivos, primer vuelo del contrato, perfil
  S); 5 HIGH, 6 MED y 3 LOW; todos corregidos antes de este registro;
  fidelidad del mapeo verificada contra los 5 contratos bilaterales
  reales.
EVIDENCE
- fidelidad del mapeo -> estados/vencimientos/fail-cited verificados con file:line por el revisor -> pass
- autocircularidad H-2 -> grafo sin bucles tras mover IA-001@nueva a references -> pass
- tier_1 sin push de pie -> canon local manda (A4/S4); WOs con push: null -> pass
- orden del Operador -> registrada en este artifacto con hash; authorization_ref repuntados -> pass
- events.jsonl -> kind: proposal (S3); jsonl valido linea a linea -> pass
- python3 scripts/check_sizes.py -> OK; 232 archivos; ruta 1640/1640 -> pass
- python3 scripts/check_plans.py + check_reports -> OK; 13 planes; 55 reportes -> pass
PENDING = encendido: decision del Operador sobre hogar del estado (se
  recomienda repo dedicado aria/coordination), fuente de tiempo y
  designaciones; registro de las WOs por los capitanes; AR0 antes de
  agreed; ejecucion de la renovacion en los repos de las partes;
  entrega Git de este kit por lote.
DECISION = fix-and-retry
OPERATIONS = ronda de solo lectura via subagente fresco; correcciones
  sobre el kit antes del commit; sin efectos Git; sin escritura en los
  repos de las partes (A2/P1).
AUTHORITY = Operador 2026-11-09, en conversacion: «renovamos el bloque
  Skopos — y lo hacemos ya como piloto del contrato de coordinación,
  matando dos pájaros adelante» — aceptación de la opción 1 del análisis
  del bloque Skopos; este registro con hash es su artefacto durable.
RISK = revisor del mismo proveedor y familia que el autor; el kit es
  borrador hasta el encendido (precondiciones §10); la renovación
  ejecuta en repos ajenos bajo capitanes propios.
report_sha256 = 07744be8817eef339e5b0e6cbc7bc7aacad5ab1b6843b5bd677f8a2396345b1a
```
