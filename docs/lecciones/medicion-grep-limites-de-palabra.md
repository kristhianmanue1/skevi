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
  veces inflados frente al conteo con límites (130 archivos resultaron
  ser 2; 81 resultaron 3); el error lo detectó la ronda adversarial
  re-ejecutando comandos, no la relectura, y sobre una de las cifras
  falsas se reavivó una iniciativa previamente rechazada.
Origen = aria-Skevi/medicion-grep-sin-limites-infla-conteos; episodio
  2026-08-15; issue #99 fila 6 (triaje 2026-11-12).
Revisión = docs/reviews/2026-11-13-issue99-lecciones.md (ronda con
  contexto fresco de otra familia).
```
