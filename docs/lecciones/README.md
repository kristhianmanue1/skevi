# Lecciones de método de skevi

> **Tipo:** registro de lecciones de método con su evidencia; no son norma.
> En conflicto manda el corpus (estándar, guía, ADRs). **Vida útil:** por
> lección; cada una caduca al promoverse a guía. Decidido en
> [ADR-053](../adr/ADR-053-hogar-de-lecciones-de-metodo.md); origen:
> [issue #99](https://github.com/kristhianmanue1/skevi/issues/99)
> (CC desde devHerdrExpert, 2026-11-13).

## Formato

Cada lección es un archivo corto en este directorio, versionado en Git,
con un fence `text` de claves fijas:

- `id` — estable, en inglés, grep-able (`skevi/<slug>`); el nombre del
  archivo va en el idioma de la lección;
- `Regla` — una oración operativa;
- `Cómo aplicarla` — pasos concretos, con el comando exacto si aplica;
- `Evidencia` — el episodio real que la produjo, con ruta o referencia;
- `Origen` — proyecto/nota y fecha;
- `Revisión` — registro de la ronda que la admitió (una lección entra
  sólo tras revisión con contexto fresco: ADR-053).

## Relación con el corpus

- **Precedencia: corpus > lecciones.** Una lección nunca modifica ni
  interpreta norma; si choca con el corpus, el corpus manda y la lección
  se corrige o se retira.
- **Promoción, no duplicación:** una lección que demuestra ser regla
  recurrente viaja a la guía en un salto `corpus/vN` y deja de ser
  lección; nunca se mantienen dos versiones de la misma regla.
- **Canónico sin memoria:** este registro vive en `docs/` y Git para
  valer sin ninguna memoria instalada (guía `05` §2, K4); la memoria de
  un agente puede indexarlo, nunca sustituirlo.

## Servicio externo

Un lector de mandatos de otro repositorio puede servir estas lecciones
con `--repo <checkout de skevi>`, sin copiarlas: el formato es
autocontenido y agnóstico de proveedor (misma doctrina de neutralización
que ADR-035). Skevi no depende de ese lector: sin él, las lecciones se
leen como archivos.
