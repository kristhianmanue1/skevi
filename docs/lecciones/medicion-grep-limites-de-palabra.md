# Medir adopción con grep con límites de palabra y repetir el conteo

```text
id = skevi/medicion-grep-limites
Regla = Antes de usar un conteo de adopción o de citas como argumento,
  mídelo con límites de palabra (grep -rlE "\b…\b") y repítelo; reporta
  el comando exacto y las dos corridas.
Cómo aplicarla = Encierra el término entre \b en el patrón; corre el
  mismo comando dos veces; si las corridas difieren, investiga la causa
  antes de citar la cifra; nunca reportes un número sin el comando que
  lo produjo.
Evidencia = Conteos de adopción sin límites de palabra salieron 18 a 65
  veces inflados frente al conteo con límites; el error se descubrió al
  repetir la medición con el patrón corregido, no al leer el primer
  resultado.
Origen = aria-Skevi/medicion-grep-sin-limites-infla-conteos; issue #99
  fila 6 (2026-11-12).
Revisión = docs/reviews/2026-11-13-issue99-lecciones.md (ronda con
  contexto fresco de otra familia).
```
