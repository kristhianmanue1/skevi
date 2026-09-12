# ADR-029 — Elección explícita del idioma humano

Estado: aceptado por instrucción humana, 2026-09-12; implementación local
en estándar §3.1, F0 §3.2, F3 §4 y `plantillas/v3`. Sin commit
ni publicación de este incremento.

Contexto: ADR-015 ya obliga a usar inglés para identificadores nuevos y
permite idioma humano declarado. F0 y la plantilla no piden registrarlo
expresamente; «idioma del proyecto» agrupa conversación y producto aunque
puedan tener públicos distintos. Cubre REQ-L2 de
[SPEC-LANG](../specs/SPEC-LANG-2026-09-12.md).

Decisión: conservar inglés estructural; declarar en el contexto de adopción
el idioma humano predeterminado, los idiomas del producto y de comentarios.
La preferencia expresa del interlocutor cambia la respuesta, no la política
persistente ni los contratos. Esta precisión desarrolla ADR-015; para la
capa humana de ADR-016 y del estándar §6.9 también aplica la preferencia del
interlocutor. La capa técnica mantiene su formato e idioma ingleses.

En proyectos nuevos o al adoptar esta precisión, registrar la elección en
`.skevi/usage-guide.md`; si ya hay una fuente local, enlazarla sin duplicar.
Si no se ha declarado, preguntar antes de fijar texto persistente; se puede
continuar el trabajo que no dependa de esa elección. El idioma nativo se
elige, no se deduce de nacionalidad, ubicación o idioma de los identificadores.

Conservar términos de dominio, nombres propios y contratos externos que
exijan un nombre exacto; registrar la razón de esas excepciones. Código
generado conserva el contrato de su generador. No renombrar legado como
efecto colateral ni inferir una mejora de rendimiento del LLM por el idioma.

Alternativas descartadas:

- Todo en inglés: impone al humano un idioma no elegido.
- Traducir todo según la conversación: rompe estabilidad de interfaces y
  confunde preferencia temporal con política del producto.
- Un detector automático de inglés: no distingue nombres propios,
  abreviaturas ni contratos; excede los gates estructurales de Skevi.
- Copiar la regla en cada guía: multiplica versiones. Las guías remiten al
  estándar, la plantilla registra valores del adoptante.

Consecuencias: revisión explícita de identificadores nuevos y elecciones
humanas, sin nuevo gate ni nueva clave JSON. Plantilla `plantillas/v3`:
cambio aditivo compatible para consumidores existentes; completar los campos
al adoptar esta precisión. No se exige migración automática de copias.

Casos de aceptación documental:

1. Proyecto español, petición de respuesta en inglés: responder en inglés;
   no cambiar documentación o interfaz española.
2. Código `appointment_not_found`, producto español: mantener el código y
   traducir sólo su explicación humana.
3. Idioma no declarado: preguntar para los artefactos persistentes; no
   deducirlo del país del usuario ni inventar una política.
4. Contrato externo con nombres españoles: conservarlos y citar su contrato.
5. Comentarios españoles: válidos si así se declararon; no traducirlos por
   confundirlos con identificadores.

Procedencia y razón: instrucción humana «adelante con recomendacion» tras
el análisis local del 2026-09-12; hacer operativa la elección contemplada
por ADR-015 sin cambiar compatibilidad, alcance ni autoridad.
