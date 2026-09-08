#!/usr/bin/env python3
"""Gate estructural de reportes de dos capas (ADR-016, ADR-022).

Comprueba **forma**, nunca honestidad. Que un reporte pase este gate no
prueba que su evidencia sea cierta, que la ronda adversarial se ejecutara ni
que el trabajo esté hecho: prueba que el reporte está completo y que su hash
reproduce. La verificación de que una regla se cumplió de verdad sigue fuera
del alcance de Skevi (`project-manifest.yaml` §no_ofrece).

Qué se valida de la capa técnica: fence ```text presente; claves obligatorias
del bloque de trazabilidad y del reporte; polaridad cerrada sobre las claves;
`STATE` y `DECISION` dentro de su conjunto; al menos una línea de EVIDENCE con
la forma `- <qué> -> <resultado>`; marca válida cuando el último segmento es
una sola palabra; y `report_sha256` reproducible en forma canónica.

Marcas y transición (ADR-005): el validador acepta la línea **con marca y sin
ella**. Una línea cuyo último segmento tiene varias palabras es prosa sin
marca y pasa; una de una sola palabra ocupa el lugar de la marca y debe ser
`pass`, `fail` o `inconclusive` — así se atrapan `passed`, `ok` o `addressed`
sin romper la transición.

Fail-closed (ADR-006): sin clave `reports` en skevi-gate.json no comprueba
nada — inactivo, nunca error; clave presente con tipo inválido sí es error.

Uso:
  python3 scripts/check_reports.py [--root DIR]
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG_NAME = "skevi-gate.json"
CONFIG_KEY = "reports"

# Capa técnica de ADR-016: las obligatorias son las que ese ADR enumera.
# `session` es opcional por el propio ADR y `DECISION` la exige `04` §5.2 para
# una ronda adversarial (no para un reporte de fase), de ahí que sea opcional
# aquí. `OPERATIONS`, `AUTHORITY` y `RISK` **no tienen fuente normativa**: son
# práctica heredada de los registros vigentes. Se admiten para no rechazar
# esos registros, y esa ausencia de fuente está declarada en ADR-022 como
# límite conocido — una clave sin regla que la respalde no se convierte en
# regla por estar en esta lista (AGENTS.md §Convenciones de edición).
REQUIRED_KEYS = {
    "id", "date", "time_utc", "head_sha", "model",
    "STATE", "GATE", "PENDING", "report_sha256",
}
OPTIONAL_KEYS = {"session", "DECISION", "OPERATIONS", "AUTHORITY", "RISK"}
MARKS = {"pass", "fail", "inconclusive"}
STATES = {"OK", "PARTIAL", "BLOCKED"}
DECISIONS = {"proceed", "fix-and-retry", "escalate"}

# Cualquier bloque cercado, no sólo ```text: una capa técnica en un fence
# liso no puede escapar al gate. La capa se ancla en `report_sha256`, que
# es lo que ADR-016 hace obligatorio, no en el lenguaje del fence.
FENCE_RE = re.compile(r"```[A-Za-z0-9_+-]*\n(.*?)\n```", re.S)
HASH_KEY = "report_sha256"
KEY_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.*)$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
TIME_RE = re.compile(r"^\d{2}:\d{2}:\d{2}Z$")
SHA1_RE = re.compile(r"^[0-9a-f]{40}$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


class _ConfigError(ValueError):
    """Diagnóstico con campos conocidos, nunca payload del usuario (ADR-007)."""


def _es_linea_del_hash(linea: str) -> bool:
    """La línea que se excluye del canon es la de la clave exacta, no la de
    cualquier clave con ese prefijo (`report_sha256_prev` no se excluye)."""
    match = KEY_RE.match(linea)
    return match is not None and match.group(1) == HASH_KEY


def _primer_token(valor: str) -> str:
    return valor.split("(")[0].split(";")[0].strip().split(" ")[0]


def comprobar_reporte(relativo: str, texto: str) -> list[str]:
    """Fallos de forma de un reporte. Lista vacía = capas técnicas válidas.

    Un archivo puede llevar más de una capa técnica (dos emisiones en el
    mismo registro): se validan todas, no sólo la primera. Un fence ```text
    que no declara `report_sha256` es salida de comando transcrita, no una
    capa técnica, y se ignora — el gate ancla la capa, no todo bloque
    preformateado.
    """
    capas = [
        m.group(1) for m in FENCE_RE.finditer(texto)
        if any(l.startswith(HASH_KEY) for l in m.group(1).split("\n"))
    ]
    if not capas:
        return [f"{relativo}: sin capa técnica (ningún bloque declara {HASH_KEY})"]
    fallos: list[str] = []
    for capa in capas:
        fallos.extend(_comprobar_capa(relativo, capa, texto))
    return fallos


def _comprobar_capa(relativo: str, capa: str, texto: str) -> list[str]:
    fallos: list[str] = []
    lineas = capa.split("\n")
    claves: dict[str, str] = {}
    evidencia: list[str] = []
    en_evidencia = False
    for linea in lineas:
        if linea.strip() == "EVIDENCE":
            en_evidencia = True
            continue
        match = KEY_RE.match(linea)
        if match:
            en_evidencia = False
            nombre = match.group(1)
            if nombre in claves:
                # Sin esto, la última repetición ganaba en silencio y
                # `STATE = BLOCKED` seguido de `STATE = OK` pasaba el gate.
                fallos.append(f"{relativo}: clave duplicada en la capa: {nombre}")
            claves[nombre] = match.group(2).strip()
        elif en_evidencia and linea.strip():
            evidencia.append(linea)

    faltan = sorted(REQUIRED_KEYS - set(claves))
    for clave in faltan:
        fallos.append(f"{relativo}: falta la clave obligatoria {clave}")
    for clave in sorted(set(claves) - REQUIRED_KEYS - OPTIONAL_KEYS):
        fallos.append(f"{relativo}: clave desconocida en la capa técnica: {clave}")

    if "STATE" in claves and _primer_token(claves["STATE"]) not in STATES:
        fallos.append(
            f"{relativo}: STATE debe empezar por uno de "
            f"{', '.join(sorted(STATES))}"
        )
    if "DECISION" in claves and _primer_token(claves["DECISION"]) not in DECISIONS:
        fallos.append(
            f"{relativo}: DECISION debe empezar por uno de "
            f"{', '.join(sorted(DECISIONS))}"
        )
    if "date" in claves and not DATE_RE.match(claves["date"]):
        fallos.append(f"{relativo}: date debe ser AAAA-MM-DD")
    if "time_utc" in claves and not TIME_RE.match(claves["time_utc"]):
        fallos.append(f"{relativo}: time_utc debe ser HH:MM:SSZ")
    if "head_sha" in claves and not SHA1_RE.match(claves["head_sha"]):
        fallos.append(f"{relativo}: head_sha debe ser 40 hexadecimales")

    if not any(l.strip() == "EVIDENCE" for l in lineas):
        fallos.append(f"{relativo}: sin sección EVIDENCE")
    elif not evidencia:
        fallos.append(f"{relativo}: EVIDENCE sin ninguna línea")
    for linea in evidencia:
        cuerpo = linea.strip()
        if not cuerpo.startswith("- "):
            fallos.append(f"{relativo}: línea de EVIDENCE sin viñeta: {cuerpo[:40]}")
            continue
        if "->" not in cuerpo:
            fallos.append(
                f"{relativo}: línea de EVIDENCE sin '->' que separe fuente de "
                f"resultado: {cuerpo[:40]}"
            )
            continue
        ultimo = cuerpo.rsplit("->", 1)[1].strip()
        if ultimo and " " not in ultimo and ultimo not in MARKS:
            fallos.append(
                f"{relativo}: marca inválida «{ultimo}»; ADR-005 sólo admite "
                f"{', '.join(sorted(MARKS))} (o línea sin marca)"
            )

    if "report_sha256" in claves:
        declarado = claves["report_sha256"]
        if not SHA256_RE.match(declarado):
            fallos.append(f"{relativo}: report_sha256 debe ser 64 hexadecimales")
        else:
            canon = "\n".join(l for l in lineas if not _es_linea_del_hash(l))
            obtenido = hashlib.sha256(canon.encode("utf-8")).hexdigest()
            if obtenido != declarado:
                fallos.append(
                    f"{relativo}: report_sha256 no reproduce en forma canónica "
                    "(UTF-8, LF, sin newline final, excluida su propia línea)"
                )
    return fallos


def _ruta_contenida(root: Path, valor: str) -> Path | None:
    """Resuelve `valor` contra `root`; None si es absoluta, empieza por `~`
    o escapa de la raíz tras `.resolve()` (cierra también el symlink)."""
    if valor.startswith("/") or valor.startswith("~"):
        return None
    candidato = (root / valor).resolve()
    try:
        candidato.relative_to(root.resolve())
    except ValueError:
        return None
    return candidato


def cargar_config(root: Path) -> dict:
    ruta = root / CONFIG_NAME
    if not ruta.is_file():
        return {}
    data = json.loads(ruta.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise _ConfigError(f"{CONFIG_NAME}: la raíz debe ser un objeto")
    return data


def reportes_declarados(root: Path) -> tuple[list[Path], set[str]] | None:
    """Archivos a comprobar y rutas exentas. None = inactivo (sin la clave)."""
    config = cargar_config(root)
    if CONFIG_KEY not in config:
        return None
    valor = config[CONFIG_KEY]
    if not isinstance(valor, dict):
        raise _ConfigError(
            f"{CONFIG_NAME}: «{CONFIG_KEY}» debe ser un objeto con «dir» "
            "y, opcionalmente, «exempt»"
        )
    desconocidas = sorted(set(valor) - {"dir", "exempt"})
    if desconocidas:
        raise _ConfigError(
            f"{CONFIG_NAME}: «{CONFIG_KEY}» sólo admite «dir» y «exempt»"
        )
    directorio = valor.get("dir")
    if not isinstance(directorio, str) or not directorio.strip():
        raise _ConfigError(f"{CONFIG_NAME}: «{CONFIG_KEY}.dir» debe ser texto")
    # `dir` es entrada no confiable: misma frontera que `_safe_relative_paths`
    # en check_sizes.py. Sin esto, una ruta absoluta o un `..` hacían que el
    # gate leyera fuera del repo y reventara con traceback, filtrando rutas
    # del host — justo lo que ADR-007 prohíbe y este script promete no hacer.
    destino = _ruta_contenida(root, directorio)
    if destino is None:
        raise _ConfigError(
            f"{CONFIG_NAME}: «{CONFIG_KEY}.dir» debe ser una ruta relativa "
            "contenida en la raíz del proyecto"
        )
    if not destino.is_dir():
        raise _ConfigError(
            f"{CONFIG_NAME}: «{CONFIG_KEY}.dir» declarado pero el directorio "
            f"no existe: {directorio}"
        )
    exentos = valor.get("exempt", [])
    if not isinstance(exentos, list) or not all(isinstance(e, str) for e in exentos):
        raise _ConfigError(
            f"{CONFIG_NAME}: «{CONFIG_KEY}.exempt» debe ser una lista de rutas"
        )
    return sorted(destino.glob("*.md")), set(exentos)


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    root = ROOT
    # La línea de comandos también es una frontera: se valida contra un
    # esquema cerrado y falla controlado (§2.4, ADR-007). Un IndexError o un
    # argumento ignorado en silencio serían los dos fallos que este mismo
    # script le reprocha al resto del corpus.
    if argv:
        if argv[0] != "--root" or len(argv) != 2:
            print("BLOQ — check_reports recibió argumentos inválidos")
            print("- uso: check_reports.py [--root DIR]")
            return 1
        root = Path(argv[1]).resolve()
        if not root.is_dir():
            print("BLOQ — check_reports no encontró la raíz indicada")
            print("- «--root» debe apuntar a un directorio existente")
            return 1

    try:
        declarados = reportes_declarados(root)
    except _ConfigError as exc:
        print("BLOQ — check_reports encontró configuración inválida")
        print(f"- {exc}")
        return 1
    except json.JSONDecodeError as exc:
        print("BLOQ — check_reports encontró configuración inválida")
        print(f"- {CONFIG_NAME}: JSON inválido (línea {exc.lineno}, columna {exc.colno})")
        return 1
    except (OSError, UnicodeDecodeError):
        print("BLOQ — check_reports encontró configuración inválida")
        print(f"- {CONFIG_NAME}: no se pudo leer la configuración")
        return 1

    if declarados is None:
        print(f"OK — inactivo: sin clave «{CONFIG_KEY}» en {CONFIG_NAME}")
        return 0

    archivos, exentos = declarados
    fallos: list[str] = []
    revisados = 0
    saltados = 0
    for archivo in archivos:
        relativo = archivo.relative_to(root).as_posix()
        if relativo in exentos:
            saltados += 1
            continue
        try:
            texto = archivo.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            fallos.append(f"{relativo}: contenido no válido como UTF-8")
            continue
        except OSError:
            # Nunca volcar la excepción: puede llevar rutas del host (ADR-007).
            fallos.append(f"{relativo}: no se pudo leer el archivo")
            continue
        # docs/reviews/ también aloja prosa de cierre sin capa técnica: sólo
        # se validan los archivos que declaran una, y «declarar una» significa
        # tener `report_sha256`, no tener un fence ```text — un registro
        # trivial puede transcribir salida de comando (00-INDICE: «tarea
        # trivial: capa humana sola»).
        if HASH_KEY not in texto:
            continue
        revisados += 1
        fallos.extend(comprobar_reporte(relativo, texto))

    if fallos:
        print("BLOQ — check_reports encontró incumplimientos")
        for fallo in fallos:
            print(f"- {fallo}")
        return 1
    print(
        f"OK — {revisados} reporte(s) con capa técnica verificada"
        + (f"; {saltados} exento(s)" if saltados else "")
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
