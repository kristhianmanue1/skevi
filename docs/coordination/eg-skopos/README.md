# Piloto EG↔Skopos — cadena de encendido

Primer vuelo real del contrato de coordinación (familia PROP-014 v0.5.0,
**perfil mínimo S 0.5.0-S.1** de skevi — sin Herdr, sin multi-modelo).
Partes: **expertoGobernanza** (consumidor) ↔ **Skopos** (proveedor).
Disparador real: las políticas de custodia y derivados del bloque IMSS
vencieron el 2026-11-08T00:00:00Z — su propio fail-closed bloquea el
uso; la renovación es trabajo bilateral forzoso, y este piloto la
formaliza.

**Qué es esto:** candidatos de los objetos de coordinación, preparados
en skevi (portador del perfil S) por orden del Operador del 2026-11-09
(«renovamos el bloque Skopos — y lo hacemos ya como piloto del contrato
de coordinación, matando dos pájaros adelante»). Esa orden es el
`authorization_ref` de las designaciones candidatas. Nada aquí obliga a
las partes hasta su encendido.

## Encendido (quién hace qué)

1. **Operador**: aprueba el estado de la colaboración con las
   precondiciones completas de §10/S: **hogar del estado** (dos opciones
   abajo, recomendada la 1), **fuente de tiempo**, **designaciones**
   (coordinator/controller) e **identidad de escritor** del hogar. La
   orden que habilita este kit vive registrada con hash en
   `docs/reviews/2026-11-09-piloto-eg-skopos-ronda.md` (AUTHORITY).
2. **Capitán de Skopos**: registra WO-SK-001 y lo deja listo —
   **registra, no ejecuta**.
3. **Capitán de expertoGobernanza**: registra WO-EG-001 y lo deja
   listo.
4. **Ronda AR0** sobre el CC (la corre el coordinator designado; peldaño
   de la escalera S2 registrado) — sólo tras `proceed` el CC pasa a
   `agreed` y **entonces** las WOs entran en ejecución. Ninguna
   renovación antes del acuerdo: el vencimiento presiona, y el contrato
   no se dobla.
5. **Hogar y controller**: quien resulte designado crea el hogar
   (opción 1: repo `aria/coordination`, por orden del Operador) y el
   script controller mínimo (S3); el registro de eventos viaja allí.
   Transición sólo con identidad de escritor (S3); sin ella, propuesta.

## Objetos

- `CC-EG-SK-001.md` — contrato de coordinación (candidato v0.1.0)
- `IA-REGISTRO.md` — los cinco contratos existentes mapeados a IAs
- `WO-SK-001.md`, `WO-EG-001.md` — órdenes de trabajo de la renovación
- `events.jsonl` — **borrador** del registro (semilla marcada como
  propuesta, no transición); hogar definitivo según §10

Nota de plano: el manifiesto de skevi cede «contrato de tarea ejecutable
ni máquina de estados de auditoría» a epistates; mientras el hogar sea
PENDING este directorio es sólo borrador de candidatos — la opción 1
(repo dedicado) despeja la cesión al primer encendido.

## Escenarios de falsación del piloto (perfil S + corpus)

Los tres del perfil S (peldaño degradado honesto; controller mínimo
arbitrando; piso de auto-certificación) más los del corpus §9 que
apliquen sin infraestructura: revocación en vuelo (S: sin firma →
observación, no transiciones), reúso de evidencia sin fundamento,
reanudación sin saltarse `verification`, y el control positivo de cada
uno. Se ejecutan sobre la renovación real, no en teatro.
