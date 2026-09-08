#!/usr/bin/env python3
"""Chequeo de drift de plantillas de adopción (PROP-006@#28 D3 + enmiendas T09).

Compara el MANIFEST fuente de Skevi (templates/skevi/MANIFEST.json, esquema
`skevi/template-manifest/v1`) contra el registro de instalación del
consumidor (`.skevi/installed.json`, esquema `skevi/template-install/v1`).
El señal válido de drift es la versión declarada, nunca el contenido: las
copias se rellenan por diseño y difieren en bytes de su fuente.

Clasificación T09: (A) obsoleto pero compatible → aviso; (B) obsoleto
incompatible → fallo `template_drift_version` (#28 D3.2 resuelta como fallo);
(C) personalizado → anula A/B por archivo declarado. Versión sin cadena
hasta la vigente → B (fail-closed). Copiable sin edición: stdlib-only, sin
red, no muta archivos.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

MANIFEST_SCHEMA = "skevi/template-manifest/v1"
INSTALL_SCHEMA = "skevi/template-install/v1"
MANIFEST_KEYS = {"schema", "version", "generated_at", "files", "history"}
INSTALL_KEYS = {"schema", "version", "files", "installed_at", "source",
                "customized"}
HISTORY_KEYS = {"from", "to", "breaking", "changes"}
DIGEST_RE = re.compile(r"^sha256:[0-9a-f]{64}$")
VERSION_RE = re.compile(r"^plantillas/v\d+(\.\d+)*$")
DRIFT_REASON = "template_drift_version"


class _InputError(ValueError):
    """Entrada inválida con motivo fijo; nunca payload ni rutas del host."""


def _require(condition, message):
    if not condition:
        raise _InputError(message)


def _check_digest(value, where):
    _require(isinstance(value, str) and DIGEST_RE.match(value),
             f"{where} no es un digest con formato sha256:<hex>")


def _check_common(data, schema, keys, label):
    _require(isinstance(data, dict), f"{label}: la raíz debe ser un objeto")
    _require(data.get("schema") == schema,
             f"{label}: schema desconocido (se espera {schema})")
    unknown = sorted(set(data) - keys)
    _require(not unknown,
             f"{label}: campo desconocido: {', '.join(unknown)}")


def _load_manifest(path: Path) -> dict:
    label = "manifest"
    try:
        raw = path.read_text(encoding="utf-8")
    except OSError:
        raise _InputError(f"{label}: no se pudo leer el archivo")
    except UnicodeDecodeError:
        raise _InputError(f"{label}: contenido no válido como UTF-8")
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise _InputError(
            f"{label}: JSON inválido (línea {exc.lineno}, columna {exc.colno})"
        )
    except RecursionError:
        raise _InputError(f"{label}: JSON inválido o demasiado anidado")
    _check_common(data, MANIFEST_SCHEMA, MANIFEST_KEYS, label)
    _require(isinstance(data["version"], str)
             and VERSION_RE.match(data["version"]),
             f"{label}: version no coincide con plantillas/v<n>")
    _require(isinstance(data["generated_at"], str) and data["generated_at"],
             f"{label}: generated_at debe ser texto con fecha")
    _require(isinstance(data["files"], dict) and data["files"],
             f"{label}: files debe ser un objeto con entradas")
    for name, digest in data["files"].items():
        _check_digest(digest, f"{label}: files.{name}")
    _require(isinstance(data["history"], list),
             f"{label}: history debe ser una lista")
    for index, jump in enumerate(data["history"]):
        where = f"{label}: history[{index}]"
        _require(isinstance(jump, dict), f"{where} debe ser un objeto")
        _require(set(jump) == HISTORY_KEYS,
                 f"{where} debe tener exactamente from/to/breaking/changes")
        _require(jump["from"] is None
                 or (isinstance(jump["from"], str)
                     and VERSION_RE.match(jump["from"])),
                 f"{where}.from no es una versión válida")
        _require(isinstance(jump["to"], str)
                 and VERSION_RE.match(jump["to"]),
                 f"{where}.to no es una versión válida")
        _require(isinstance(jump["breaking"], bool),
                 f"{where}.breaking debe ser booleano")
        _require(isinstance(jump["changes"], dict),
                 f"{where}.changes debe ser un objeto")
        for name, summary in jump["changes"].items():
            _require(isinstance(summary, str),
                     f"{where}.changes.{name} debe ser texto")
    return data


def _load_install(path: Path) -> dict:
    label = "installed"
    try:
        raw = path.read_text(encoding="utf-8")
    except OSError:
        raise _InputError(f"{label}: no se pudo leer el archivo")
    except UnicodeDecodeError:
        raise _InputError(f"{label}: contenido no válido como UTF-8")
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise _InputError(
            f"{label}: JSON inválido (línea {exc.lineno}, columna {exc.colno})"
        )
    except RecursionError:
        raise _InputError(f"{label}: JSON inválido o demasiado anidado")
    _check_common(data, INSTALL_SCHEMA, INSTALL_KEYS, label)
    _require(isinstance(data["version"], str)
             and VERSION_RE.match(data["version"]),
             f"{label}: version no coincide con plantillas/v<n>")
    _require(isinstance(data["files"], dict) and data["files"],
             f"{label}: files debe ser un objeto con entradas")
    for name, digest in data["files"].items():
        _check_digest(digest, f"{label}: files.{name}")
    _require(isinstance(data["installed_at"], str) and data["installed_at"],
             f"{label}: installed_at debe ser texto con fecha")
    _require(isinstance(data["source"], str) and data["source"],
             f"{label}: source debe ser texto")
    _require(isinstance(data["customized"], list)
             and all(isinstance(v, str) for v in data["customized"]),
             f"{label}: customized debe ser una lista de nombres de archivo")
    outside = sorted(set(data["customized"]) - set(data["files"]))
    _require(not outside,
             f"{label}: customized declara un archivo ausente de files: "
             + ", ".join(outside))
    return data


def _chain(history, start: str, current: str):
    """Devuelve (saltos, None) de start a current, o (None, motivo)."""
    jumps = []
    seen = {start}
    node = start
    while node != current:
        edges = [h for h in history if h["from"] == node]
        if len(edges) > 1:
            return None, (f"history ambigua para {node} "
                          "(varios saltos desde la misma versión)")
        if not edges:
            return None, (f"versión instalada {start} sin cadena hasta la "
                          "vigente: se trata como incompatible (fail-closed)")
        edge = edges[0]
        jumps.append(edge)
        node = edge["to"]
        if node in seen:
            return None, f"history con ciclo en {node}"
        seen.add(node)
    return jumps, None


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Chequeo de drift de plantillas (#28 D3 + T09)."
    )
    parser.add_argument("--manifest", required=True,
                        help="MANIFEST fuente (skevi/template-manifest/v1)")
    parser.add_argument("--installed", required=True,
                        help="registro del consumidor (template-install/v1)")
    args = parser.parse_args(argv)

    try:
        manifest = _load_manifest(Path(args.manifest))
        installed = _load_install(Path(args.installed))
    except _InputError as exc:
        print(f"BLOQ — {exc}")
        return 1

    current = manifest["version"]
    start = installed["version"]
    customized = set(installed["customized"])
    if start == current:
        print(f"OK — plantillas al día: versión vigente {current}")
        return 0

    jumps, error = _chain(manifest["history"], start, current)
    if error is not None:
        print(f"BLOQ — {DRIFT_REASON}: {error}")
        return 1

    affected: set[str] = set()
    for jump in jumps:
        affected.update(jump["changes"])
    # Customizados a anunciar: los afectados declarados, o todos los
    # declarados si la cadena no registra cambios por archivo.
    custom = sorted(affected & customized) if affected else sorted(customized)
    breaking = [j for j in jumps if j["breaking"]]

    if breaking:
        # Con saltos breaking y sin registro por archivo, el fallo es
        # conservador: todos los archivos instalados cuentan como afectados
        # salvo los declarados customized (T09, bandera conservadora).
        stale = sorted((affected or set(installed["files"])) - customized)
        if stale:
            print(f"BLOQ — {DRIFT_REASON}: copia obsoleta incompatible "
                  f"respecto de {current}")
            for jump in breaking:
                print(f"- salto breaking: {jump['from']} -> {jump['to']}")
            for name in stale:
                print(f"- afectado sin customized declarado: {name}")
            for name in custom:
                print(f"- customized (re-copia bajo responsabilidad del "
                      f"consumidor): {name}")
            return 1

    print(f"OK — copia obsoleta pero compatible: sin saltos breaking "
          f"aplicables hasta {current}")
    if not affected:
        print("- aviso: la cadena no registra cambios por archivo; "
              "re-copia opcional")
    else:
        for name in sorted(affected - customized):
            print(f"- aviso: re-copia opcional; cambia en la cadena: {name}")
    for name in custom:
        print(f"- aviso: customized — re-copia bajo responsabilidad del "
              f"consumidor: {name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
