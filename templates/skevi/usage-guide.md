# Uso de Skevi en este proyecto

> Plantilla — reemplaza cada `<...>` con el dato real del proyecto. Borra
> cualquier sección que no aplique; no dejes placeholders sin llenar.

**Proyecto:** <nombre>
**Fase actual:** <F0 | F1 | F2 | F3>
**Procedencia de las plantillas:** registrada en `installed.json`
(esquema `skevi/template-install/v1`), en este mismo directorio (`.skevi/`)
una vez copiado — única fuente de verdad de qué se copió, de dónde y con
qué versión; no la dupliques aquí.

## Qué leer primero

1. `AGENTS.md` (o `CLAUDE.md`) en la raíz — punto de entrada, trae el
   bloque de registro que enlaza a este archivo.
2. `docs/ai-agent-guide/00-INDICE.md` — fases F0→F3 y reglas de aplicación.
3. `docs/estandar-diseno-software-github.md` — capa normativa transversal.

## Desviaciones de este proyecto respecto al estándar por defecto

<lista de límites de tamaño propios, exenciones registradas, o "ninguna">

## Idiomas elegidos

Fuente normativa: estándar §3.1 (ADR-015, precisión ADR-029).
Completa estas elecciones o enlaza su fuente local existente, sin duplicarla:

- Comunicación humana predeterminada: <idioma elegido por el humano>.
- Producto: <idiomas de documentación, interfaz y mensajes; o no aplica>.
- Comentarios/docstrings: <idioma de la prosa del proyecto o elección del equipo>.
- Excepciones a identificadores nuevos en inglés: <contrato o razón; o ninguna>.

La preferencia de conversación no modifica estas elecciones persistentes.
Antes de fijar texto persistente, pregunta si falta la elección necesaria.

## Verificación local

```bash
<comando real de este proyecto, p. ej. python3 scripts/check_sizes.py>
```

## Dónde están los ADRs y specs de F1

<ruta, p. ej. docs/adr/ — o "pendiente: F1 no se ha ejecutado todavía">
