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
Evidencia = Barridos del ecosistema corregidos caso a caso conservaron
  cifras falsas en las filas no señaladas; la segunda ronda con el
  patrón corregido cambió conteos que el parche puntual dejó intactos.
Origen = aria-Skevi/rehacer-el-barrido-no-parchear-el-caso; issue #99
  fila 8 (2026-11-12).
Revisión = docs/reviews/2026-11-13-issue99-lecciones.md (ronda con
  contexto fresco de otra familia).
```
