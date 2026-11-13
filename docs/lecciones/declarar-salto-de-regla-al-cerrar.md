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
Evidencia = Omisiones de regla de método con permiso humano quedaron
  silenciadas en cierres previos del ecosistema y se supieron después,
  cuando el registro ya no podía distinguir permiso de descuido.
Origen = aria-Skevi/flag-skipped-method-rules; issue #99 fila 7
  (2026-11-12).
Revisión = docs/reviews/2026-11-13-issue99-lecciones.md (ronda con
  contexto fresco de otra familia).
```
