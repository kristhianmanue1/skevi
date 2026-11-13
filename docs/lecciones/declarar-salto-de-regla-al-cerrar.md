# Declarar el salto de una regla de método al cerrar, aun con permiso

```text
id = skevi/declarar-salto-de-regla
Regla = Si en una tarea se saltó una regla del método —ronda adversarial,
  ADR antes que código, RED primero—, el salto se declara en el reporte
  de cierre aunque el humano lo haya permitido: el permiso dispensa la
  regla, no su declaración.
Cómo aplicarla = El reporte de cierre incluye una línea por cada regla
  omitida: cuál, quién la dispensó y con qué autorización; sin esa
  línea, el cierre declara un cumplimiento que no ocurrió.
Evidencia = El 2026-08-15 se mergeó un fix sin la ronda adversarial que
  exigía practicas-ingenieria.md §1; al señalarlo en el cierre, el
  Operador respondió «muy bien que lo viste» y explicó que a un humano se
  le pasa y un agente puede sostener esa vigilancia. Se señaló en el
  momento, sin convertirlo en objeción bloqueante; la decisión siguió
  siendo del maintainer.
Origen = aria-Skevi/flag-skipped-method-rules; episodio 2026-08-15;
  issue #99 fila 7 (triaje 2026-11-12).
Revisión = docs/reviews/2026-11-13-issue99-lecciones.md (ronda con
  contexto fresco de otra familia).
```
