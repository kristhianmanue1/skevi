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

## Drift contra el canon

Compara tus copias versionadas contra los manifiestos fuente de Skevi
(señal válida: la versión declarada, nunca el contenido). Para el corpus,
copia también el `docs/MANIFEST.json` del canon junto a estándar y guía:
es tu referencia de versión:

```bash
python3 scripts/check_templates.py --manifest templates/skevi/MANIFEST.json --installed .skevi/installed.json
python3 scripts/check_templates.py --manifest scripts/MANIFEST.json --installed .skevi/scripts-installed.json
python3 scripts/check_templates.py --manifest docs/MANIFEST.json --installed .skevi/corpus-installed.json
```

## Gate de push

La activación es config local, no viaja con el clon — un clon fresco
pierde el gate de push en silencio si no la repites:

```bash
git config core.hooksPath scripts/hooks
```

## Dependencias activas del ecosistema

- **AN-KLA Memory:** <instalada | no instalada>. Si lo está, el contrato
  `skevi/an-kla-integration` (guía `05` §6) hace obligatorias dos
  lecturas más por sesión material (`05` y `AN-KLA.md`): decláralas en
  `reading_path` de `skevi-gate.json` y sube el límite por decisión
  escrita (ADR-021, ADR-025), p. ej. límite 1400 con `05` y `AN-KLA.md`
  añadidas a `files`.
- Otras dependencias: <ninguna declarada>.
