# ADR-028: Extensión del versionado de MANIFEST a `scripts/`

Estado: aceptado; implementado en `scripts/MANIFEST.json`,
`templates/skevi/scripts-installed.json`, y en la generalización de
`scripts/check_templates.py` y `scripts/check_sizes.py`.

Contexto: ADR-020 dio a `templates/skevi/` un MANIFEST versionado con
comparación de drift consumidor↔fuente. `scripts/` —el único ejecutable
que Skevi distribuye— quedó fuera: se versionó lo que se lee y no lo que
se ejecuta. ADR-027 cerró la mitad pasiva del problema: la propia copia
declara su edad, sin observar el origen. Queda la mitad activa: un
adoptante que sí quiere saber **contra qué versión** está su copia, no
sólo cuántos días tiene.

`scripts/check_templates.py` ya resolvía exactamente ese problema para
plantillas, y su mecanismo —MANIFEST fuente con digests e historial de
saltos, registro de instalación del consumidor, comparación por versión
declarada, nunca por contenido— no depende de que el artefacto sea
documentación. Extenderlo es generalizar dos constantes, no escribir un
segundo comparador.

Decisión: `check_templates.py` reconoce una **segunda familia de esquema**,
aditiva y no disruptiva de la primera:

```text
CONTRATO: skevi/script-manifest v1 (y skevi/script-install v1)
Entrada (MANIFEST fuente, scripts/MANIFEST.json):
  schema:       "skevi/script-manifest/v1" [obligatorio]
  version:      texto "gate/v<n>" [obligatorio] — mismo valor que
                check_sizes.GATE_VERSION (ADR-027); anclado por test,
                no por código compartido
  generated_at: texto con fecha [obligatorio]
  files:        objeto {nombre: "sha256:<hex>"} [obligatorio] — exactamente
                todo archivo regular de scripts/, sin symlinks, sin el
                MANIFEST mismo — mismo criterio que templates/skevi/, sin
                filtro de extensión: hoy son los 4 .py, y un archivo no-.py
                que se añada exige entrar al manifiesto igual que los demás
  history:      lista de {from, to, breaking, changes} [obligatorio]
Entrada (registro del consumidor, .skevi/scripts-installed.json):
  schema:       "skevi/script-install/v1" [obligatorio]
  version, files, installed_at, source, customized — mismos campos y
    reglas que skevi/template-install/v1 (ADR-020)
Salida: idéntica a check_templates.py — OK/aviso/BLOQ según T09
Errores: los de ADR-020 (esquema, versión sin cadena, digest inválido),
  aplicados a esta familia sin cambio de lógica
Invariantes:
  - el comparador (main()/_chain()) es agnóstico a la familia: una
    versión sin cadena hasta la vigente falla cerrado igual que una
    plantilla obsoleta — y comparar un manifiesto de una familia contra un
    registro de la otra falla porque cada `version` —del documento raíz y
    de cada salto de `history`— debe llevar el namespace que su propio
    `schema` implica (`SCHEMA_NAMESPACE`); sin esa atadura, un namespace
    mal declarado podía coincidir por accidente entre familias y dar `OK`
    falso (ronda adversarial, hallazgo HIGH, corregido antes de mergear)
  - la validación interna de check_sizes.py es estricta por artefacto:
    scripts/MANIFEST.json sólo es válido con schema
    "skevi/script-manifest/v1", nunca con el de plantillas
  - el contenido no es la señal de drift: exenciones locales en
    skevi-gate.json son variación esperada, igual que el relleno de una
    plantilla
Compatibilidad:
  - familia aditiva: ningún consumidor de skevi/template-manifest/v1 nota
    el cambio; la clave "scripts" en skevi-gate.json ya estaba reservada
    por check_sizes.py y no se toca aquí
  - cambios de este contrato -> v2, nunca mutación in situ
```

**Formato de versión generalizado, no duplicado.** `VERSION_RE` (en
`check_templates.py`) y `MANIFEST_VERSION_RE` (en `check_sizes.py`, antes
`TEMPLATE_VERSION_RE`) pasan de `^plantillas/v\d+(\.\d+)*$` a
`^[a-z]+/v\d+(\.\d+)*$`: el espacio de nombres lo declara la familia
—`plantillas`, `gate`—, no el regex. `plantillas/v1` sigue siendo válido
sin cambio.

**El namespace de versión está atado al esquema, no sólo reconocido.**
Cada `version` —del documento raíz y de cada salto de `history`— debe
empezar por el namespace que implica su propio `schema`: `plantillas/`
para la familia de ADR-020, `gate/` para la de este ADR. Sin esa atadura,
pertenecer «al conjunto de esquemas reconocidos» no bastaba para saber
que dos documentos hablaban de la misma familia — es el hallazgo HIGH de
la ronda adversarial, corregido antes de mergear.

**Validación estricta por artefacto, laxa entre familias.**
`check_templates.py` (el comparador que corre el consumidor) acepta
cualquiera de las dos familias reconocidas en cualquiera de los dos
argumentos: es agnóstico por diseño, y mezclar familias falla por la
atadura de namespace de arriba, o por "sin cadena de versión" si el
namespace era correcto pero la versión no existe en la historia.
`check_sizes.py` (la
autoverificación de Skevi sobre sí misma) es estricta: cada llamada a
`check_template_manifest` declara su `expected_schema` y sólo acepta ése.
Son responsabilidades distintas — el primero compara dos documentos que le
entrega el usuario; el segundo certifica que el propio repositorio de
Skevi es internamente consistente.

**`scripts/MANIFEST.json` en `gate/v2`, no en `gate/v1`.** Se alinea con
`GATE_VERSION` de `check_sizes.py`, que ya estaba en `v2` cuando ADR-027 lo
introdujo. Un test (`test_manifest_version_equals_gate_version_constant`)
falla si alguien sube `GATE_VERSION` sin regenerar el manifiesto, o al
revés — la única atadura entre los dos es ese test, no código compartido.

**`templates/skevi/` sube a `plantillas/v2`**, no breaking: añade
`scripts-installed.json` como cuarto archivo copiable, con su entrada en
`history` y sin tocar los digests de los tres archivos existentes. Un
consumidor en `plantillas/v1` recibe aviso, nunca fallo.

Alternativas descartadas:

- **Un comparador nuevo para `scripts/`.** `check_templates.py` ya hace
  exactamente esto; duplicarlo violaría el principio 1 del estándar
  (simplicidad) y ADR-006 (no reinventar lo copiable).
- **Reusar literalmente `skevi/template-manifest/v1` para `scripts/`.**
  Estructuralmente idéntico, pero semánticamente falso: un script no es
  una plantilla, y `check_sizes.py`'s validación interna necesita poder
  rechazar un manifiesto de la familia equivocada en el directorio
  equivocado — imposible si comparten un único esquema.
- **Confiar sólo en la ausencia de cadena entre `plantillas/vN` y
  `gate/vN`, sin atar la versión a su esquema.** Es lo que la primera
  versión de este ADR proponía. Una ronda adversarial la refutó: un
  manifiesto con `schema` de una familia y `version` en el namespace de
  la otra pasaba la validación de esquema —está en el conjunto
  reconocido— y, si ese namespace coincidía con el del documento
  comparado, el resultado era `OK` falso en vez de `BLOQ`. La versión
  adoptada ata cada versión a su propio esquema (`SCHEMA_NAMESPACE`), lo
  que cierra el hueco sin necesitar un chequeo de "misma familia"
  separado y adicional al de esquema.
- **Versionar los cuatro scripts por separado.** `check_plans.py` y
  `check_reports.py` ya comparten configuración cerrada con
  `check_sizes.py` (ADR-014, ADR-022) y el pre-push hook los corre juntos;
  tratarlos como una unidad versionada es coherente con eso, no una
  simplificación forzada.

Consecuencias: un adoptante gana una segunda vía, complementaria a la
autocaducidad pasiva de ADR-027 — puede comprobar activamente su copia de
`scripts/` contra el MANIFEST fuente de Skevi, con el mismo comando que ya
usa para plantillas. El defecto verificado en la sesión que originó esta
mejora —doce adoptantes con copias de hasta tres semanas, ninguno con
forma de saberlo— tiene ahora una comprobación tan autoritativa como la que
ya existía para documentación, sin haber escrito un segundo mecanismo.

Verificación: `python3 scripts/check_sizes.py` → `OK`, valida
`scripts/MANIFEST.json` contra los cuatro archivos reales;
`python3 scripts/check_templates.py --manifest scripts/MANIFEST.json --installed <registro>`
funciona con el mismo binario que ya se distribuye;
`python3 -m unittest discover -s tests`: el total lo reporta la suite, no
este texto — copiar una cifra aquí es exactamente lo que ADR-025 punto 4
prohíbe. Cada tanda de generalización tuvo su RED antes del código,
incluida una segunda ronda que ató el namespace de versión también dentro
de `check_sizes.py`, simétrico con `check_templates.py`.

Procedencia: [ADR-020](ADR-020-adopcion-versionado-plantillas.md) (el
mecanismo que se extiende); [ADR-027](ADR-027-identidad-y-caducidad-del-gate-copiable.md)
(la mitad pasiva que esto complementa, y el número de versión que se
comparte); instrucción directa del humano, 2026-09-08 («pieza 2 del método
de aviso de versión»).
Razón: dar comparación autoritativa donde ADR-027 sólo podía dar aviso
pasivo, reusando el mecanismo que ya existía en vez de duplicarlo.
