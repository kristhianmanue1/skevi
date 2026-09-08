# Política de seguridad

Skevi es un cuerpo normativo de documentación y cuatro scripts de
verificación local en Python de la biblioteca estándar (`check_sizes`,
`check_plans`, `check_reports`, `check_templates`). No expone servicios, no procesa
datos de terceros y no publica artefactos ejecutables.

## Qué cuenta como vulnerabilidad aquí

- Un gate que declara `OK` sin haber comprobado lo que dice comprobar
  (fail-open). Es la clase de fallo más grave en este repositorio: un gate
  siempre verde es peor que no tener gate.
- Un script que expone rutas del host, contenido de la configuración o
  cualquier dato del entorno en su diagnóstico. El estándar exige fallo
  controlado en la frontera y prohíbe volcar la excepción cruda
  (`docs/adr/ADR-007-frontera-valida-implica-fallo-controlado.md`).
- Una ruta de configuración que permita leer o escribir fuera de la raíz del
  proyecto que se verifica.
- Una regla del corpus que, aplicada como está escrita, induzca a un ejecutor
  automatizado a ejecutar contenido no confiable o a ampliar su autoridad sin
  autorización.

Un archivo que excede su límite de tamaño, un enlace roto o una cifra
desactualizada **no** son vulnerabilidades: son incumplimientos del gate.
Repórtalos como issue normal.

## Cómo reportar

Abre un aviso privado en
[Security advisories](https://github.com/kristhianmanue1/skevi/security/advisories/new).
Si no puedes, abre un issue **sin incluir el detalle explotable** y pide un
canal privado.

Incluye, en la medida en que apliquen: el comando exacto y su salida real, la
versión de Python (los gates corren sobre la del sistema), y el
`skevi-gate.json` mínimo que reproduce el fallo. Un reporte sin comando
reproducible es difícil de confirmar — la misma regla de evidencia que el
resto del repositorio.

## Qué esperar

Este repositorio lo mantiene una sola persona y no tiene compromiso de
respuesta en un plazo fijo. No hay programa de recompensas. Lo que sí hay:
todo hallazgo confirmado se corrige con un test que falla antes del arreglo
(`docs/ai-agent-guide/04-ejecucion-y-verificacion.md` §3) y se registra con
su procedencia, de modo que la regla que lo evita queda escrita y no sólo el
parche.

## Versiones cubiertas

**Sólo `main`.** Existen tags publicados —`v1.0.0` y `v1.1.0`, comprobables
con `git ls-remote --tags origin`— y hay adoptantes que citan uno de ellos,
pero **no se mantienen como ramas de soporte**: un hallazgo se corrige en
`main` y no se retroporta. Si dependes de un tag, la corrección te llega
actualizando, no parcheando esa versión.

Este repositorio no firma tags ni verifica la integridad de artefactos
publicados: está declarado fuera de alcance en `project-manifest.yaml`
§`no_ofrece` (ADR-026). Un tag no acredita procedencia.
