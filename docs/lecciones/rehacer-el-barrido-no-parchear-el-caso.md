# Rehacer el barrido completo, no parchear el caso señalado

```text
id = skevi/rehacer-el-barrido
Regla = Si una afirmación de barrido («quién adopta o cita X») resulta
  falsa en un caso, se rehace el barrido completo con el patrón
  corregido; arreglar sólo el caso señalado deja el resto del barrido
  igual de falso.
Cómo aplicarla = Corrige el patrón de medición (con límites de palabra:
  ver skevi/medicion-grep-limites), re-corre el barrido entero sobre el
  universo original, reporta las dos corridas y re-valida cada
  conclusión derivada del barrido anterior.
Evidencia = El 2026-09-08, al afirmar quién adopta Skevi en el
  ecosistema, una medición sobre un solo artefacto (project-manifest.yaml)
  concluyó «ninguno lo menciona». La ronda fresca señaló dos adoptantes;
  la corrección a dos (mirando además AGENTS.md) siguió mal: eran tres,
  porque epistates documenta su adopción en docs/architecture/ y ninguna
  de las dos mediciones miraba ahí. El patrón siguió: nueve emisiones
  falsas en cinco rondas; la salida no fue otra corrección, sino retirar
  del merge los documentos donde vivía el censo.
Origen = aria-Skevi/rehacer-el-barrido-no-parchear-el-caso; episodios
  2026-09-08; issue #99 fila 8 (triaje 2026-11-12).
Revisión = docs/reviews/2026-11-13-issue99-lecciones.md (ronda con
  contexto fresco de otra familia).
```
