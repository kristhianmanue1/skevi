# M6 — Deriva del gate copiable en los adoptantes

> **Tipo:** hallazgo con propuesta. **No es norma.** Registra un defecto
> verificado del contrato de adopción y propone una salida; adoptarla exige
> decisión humana.
> **Origen:** al ejercer el criterio del piloto
> ([M6-piloto-fuera-del-monocultivo](M6-piloto-fuera-del-monocultivo.md)) el
> 2026-09-08 se barrió el ecosistema en busca de adoptantes. El barrido
> encontró mucho más de lo que buscaba.

## 1. El corpus no sabía cuántos adoptantes tiene

`grep -ril skevi` sobre cada repositorio de `~/www` y `~/www/aria`, excluyendo
`.git`, `.venv`, `node_modules` y `__pycache__`:

**18 repositorios citan a Skevi.** `basanos` lo cita en 115 archivos — más que
los 85 del propio Skevi. Le siguen `explotumarca` (40), `an-kla-memory` (30),
`eduEMD` (28), `krathos` (24), `agora` (16), `alubia` (14), `cagf-dashboard` (12),
`pinax` (11), `entiendomidiabetes` (10), `skopos` (9), `orbitaNova`,
`glosomata` y `epistates` (8 cada uno), `expertoGobernanza` (6), `escrubery`
(3), `quantoken` y `kratos` (1).

Ninguno de esos números estaba registrado en Skevi. La primera estimación de
esta misma sesión dijo «ningún adoptante», la segunda «dos» y la tercera
«tres», porque las tres midieron la población equivocada: los cinco proyectos
que `project-manifest.yaml` §`no_ofrece` nombra al ceder plano. Adoptar y
recibir una cesión de plano son cosas distintas.

## 2. Once adoptantes copiaron el gate; ninguno está al día

Clasificación reproducible —una copia es derivada de Skevi si contiene su
cadena de salida `archivos de texto dentro de límites`—:

```bash
for f in ~/www/*/scripts/check_sizes.py ~/www/aria/*/scripts/check_sizes.py; do
  grep -q "archivos de texto dentro de límites" "$f" \
    && echo "DERIVADA $f" || echo "propio $f"
done
```

**Once repos tienen copia derivada** (excluido el propio Skevi): `alubia`,
`an-kla-memory`, `basanos`, `cagf-dashboard`, `eduEMD`, `explotumarca`,
`glosomata`, `kratos`, `orbitaNova`, `pinax`, `skopos`. Otros cuatro tienen un
`check_sizes.py` **propio**, no derivado —`escrubery`, `codigocerebro`,
`backupkairos-controller`, `expertoGobernanza`—: no son copias y no sufren
esta deriva. La primera emisión de esta tabla acertó el total por casualidad y
erró el conjunto: incluía `escrubery` y omitía `kratos`.

| Huella | Líneas | Corresponde a | Repos |
|---|---|---|---|
| `f136b7fd` | 380 | `7bfd759c`, 2026-08-20 | 7 |
| `14c66a48` | 377 | `38095fd3`, 2026-08-17 | 2 |
| `92561c09` | 319 | ningún commit de Skevi | `alubia` |
| `4619b730` | 150 | ningún commit de Skevi | `kratos` |

**Cero adoptantes ejecutan el gate vigente**, que al 2026-09-08 tiene 730
líneas. Nueve están congeladas en agosto; dos han bifurcado sin registro
—`alubia` añade búsqueda de llaves privadas que Skevi nunca tuvo—. Ninguna
copia reconoce las claves `reading_path` ni `reports`.

## 3. La consecuencia, verificada

El programa AUDIT-2026-09-07 corrigió que «el gate puede declarar éxito sin
leer un archivo sujeto a control» (REQ-AUD-02 de
[SPEC-AUDIT](../specs/SPEC-AUDIT-2026-09-07-mejoras.md)). Ese arreglo está en
Skevi y en ningún adoptante. Mismo fixture —un `docs/roto.md` con bytes no
válidos como UTF-8— contra los dos gates:

```text
gate de los adoptantes (377-380 líneas):
  OK — 4 archivos de texto dentro de límites; estructura y hogares
  canónicos verificados                                        exit 0

gate vigente de Skevi (730 líneas al 2026-09-08):
  BLOQ — check_sizes encontró incumplimientos
  - docs/roto.md: contenido no válido como UTF-8                exit 1
```

Veredictos opuestos sobre la misma entrada. Los adoptantes que corren el gate
en CI están validando con la versión que dice `OK`: `orbitaNova` vía
`npm run check:sizes`, `cagf-dashboard` vía `python scripts/check_sizes.py`, y
`eduEMD` —que el 2026-09-06 pasó en verde ejecutando `check_sizes` **y**
`check_plans` con una copia byte-idéntica al tag `v1.0.0`, es decir con el gate
anterior a este arreglo—.

## 4. Por qué ADR-020 no lo detecta

El versionado de plantillas (ADR-020) cubre `templates/skevi/`: un manifiesto
con digests, historial de saltos y `check_templates.py` para el drift. Su
alcance es la documentación copiable.

`scripts/` quedó fuera. Es el único **ejecutable** que Skevi distribuye, el
que un adoptante conecta a su CI, y el que decide si un cambio pasa o no — y
no tiene versión, ni manifiesto, ni chequeo de deriva. Se versionó lo que se
lee y se dejó sin versionar lo que se ejecuta.

## 5. Propuesta

Tres piezas, en orden de valor sobre coste:

**Estado 2026-09-08:** implementadas la pieza 1 —identidad visible— y la
pieza 3 —aviso sin bloqueo, aquí como autocaducidad—, en
[ADR-027](../adr/ADR-027-identidad-y-caducidad-del-gate-copiable.md). La
**pieza 2** —extender el manifiesto de ADR-020 a `scripts/`— queda como
trabajo siguiente con su propio ADR.

1. **Versión en el propio script.** Una constante `GATE_VERSION` que
   `check_sizes.py` imprima en su línea de salida. Un adoptante ve en su log
   de CI con qué versión validó. Coste: una línea y su test.
2. **Extender el manifiesto de ADR-020 a `scripts/`.** El mismo mecanismo ya
   construido —digests, historial, bandera de breaking— aplicado al
   directorio que importa. `check_templates.py` ya sabe hacerlo; lo que falta
   es incluir los scripts en el manifiesto y en el registro de instalación.
3. **Aviso de deriva, no bloqueo.** Un adoptante con copia vieja recibe aviso
   con la versión que tiene y la vigente; incompatible sólo si el salto lleva
   bandera de breaking. Fail-closed ante incompatibilidad, como ya hace
   `check_templates.py`.

**Lo que esta propuesta no hace:** actualizar las copias de nadie. Mutar el
repositorio de un adoptante está fuera de alcance de Skevi por declaración
propia —«cualquier ejecutable propio: no instala, no observa y no muta un
proyecto»— y exigiría autorización de cada uno.

## 6. Efecto sobre el criterio del piloto

Dos adoptantes cumplen el criterio de entrada, medidos como fija §4.1 de
[la propuesta de piloto](M6-piloto-fuera-del-monocultivo.md): `orbitaNova`
—CI activo con `push` y `pull_request` que ejecuta el gate, 23 190 líneas— y
`eduEMD`, que lo cumplió el 2026-09-06 con 86 148 líneas de PHP y una corrida
verde de dos gates, antes de que su workflow desapareciera de la rama por
defecto.

Con una salvedad que el propio criterio no anticipaba: **ambos ejecutan
versiones del gate que Skevi ya no reconoce como suyas** —377 líneas `orbitaNova`,
380 `eduEMD`—. Un piloto sobre cualquiera de los dos mediría el
método contra un ejecutor de hace trescientas líneas. Actualizar esa copia es
condición previa, y es decisión del adoptante.

**Actualizar la copia no es gratuito.** Ejecutar el gate vigente sobre el
árbol de tres adoptantes que hoy pasan en verde produce `BLOQ`: `orbitaNova`
por un `.glb` de assets, `eduEMD` por `.docx` y `.mp4` de contenido,
`explotumarca` por un `.docx` en `docs/history/`. No lo introduce esta
propuesta —el gate vigente ya se comporta así— pero es consecuencia directa de
recomendar la actualización, y se resuelve con `exempt_paths` en su
`skevi-gate.json`, que es decisión de cada adoptante.

Y es la razón de que esta propuesta importe más que el piloto: el criterio
buscaba un adoptante que ejercitara el método bajo observación, y lo que el
barrido encontró fue que **quienes ya lo ejercitan lo hacen con un ejecutor
obsoleto que ninguno sabe que lo está**.
