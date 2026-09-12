# PLAN LANG — Idioma y validación de entradas

Autoriza: instrucción humana del 2026-09-12, «adelante con recomendacion».
Clase Architectural; base y límites en [SPEC-LANG](../specs/SPEC-LANG-2026-09-12.md).
Fuente única del DoD de las tareas de este incremento.

```text
PLAN LANG — Idioma y validación de entradas
Autoriza: SPEC-LANG y autorización humana 2026-09-12
Clase de tarea: Architectural

TAREA LANG-1 — Fallo controlado
  Consumes: `docs/specs/SPEC-LANG-2026-09-12.md` REQ-L1; ADR-007
  Produce: corrección de `scripts/check_templates.py` y `scripts/check_sizes.py`
  Steps:
  - [x] Añadir pruebas de campos ausentes y schema mal tipado en ambas familias
        — verificación: RED observado antes de corregir producción
  - [x] Validar campos y tipos antes del acceso — verificación: tests focales
        en verde, salida BLOQ sin excepción ni traceback

TAREA LANG-2 — Elección humana explícita
  Consumes: `docs/adr/ADR-029-eleccion-de-idioma-humano.md`; REQ-L2
  Produce: estándar, F0/F3 y `templates/skevi/usage-guide.md` alineados
  Steps:
  - [x] Precisar norma y remitir desde F0/F3 — verificación: los cinco casos
        de ADR-029 se resuelven sin contradicción y sin detector de idiomas
  - [x] Registrar valores de adopción — verificación: plantilla distingue
        comunicación, producto y comentarios y permite referencia local

TAREA LANG-3 — Refactorización aislada
  Consumes: REQ-L3; salida verde de LANG-1
  Produce: nombres ingleses en `scripts/check_reports.py` y namespaces
  Steps:
  - [x] Registrar snapshot posterior al fix y antes de renombrar — verificación:
        comparación de tokens demuestra cambio sólo de nombres y referencias
  - [x] Mantener alias importables y actualizar usos internos — verificación:
        búsqueda de consumidores y suite focal verde, salidas sin cambios

TAREA LANG-4 — Versionado y cierre
  Consumes: REQ-L4 y salidas LANG-1..3
  Produce: manifests actualizados y crea `docs/reviews/2026-09-12-language-and-validation.md`
  Steps:
  - [x] Apartar scripts/.DS_Store a un respaldo temporal — verificación:
        bytes y hash conservados, sin cambiar exenciones
  - [x] Actualizar versiones/historial/digests — verificación: gates de
        manifiestos y comparación de copias anteriores compatible
  - [x] Ejecutar gates y suite — verificación: todos OK, lectura <=1000
  - [x] Revisar en contexto fresco — verificación: proceed, sin hallazgos
        bloqueantes, diff y enlaces comprobados
```

DoD: cada paso verificado; reporte técnico con hash reproducible y capa humana.
No commit, push, merge, tags, release ni escrituras de memoria. Parada al
entregar este resultado local, con pendientes de publicación explícitos.
