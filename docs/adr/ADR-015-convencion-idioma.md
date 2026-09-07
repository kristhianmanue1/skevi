# ADR-015: convención de idioma — código en inglés, cara al usuario en el idioma del proyecto

Estado: aceptado. Implementado en a0bcc6b — el commit que añade la
viñeta de convención de idioma al estándar §3.1 (02 §3.3).

Contexto: la instrucción directa del humano del 7 de septiembre de 2026
llegó como hipótesis, mejorada en conversación hasta forma falsable:
skevi funciona mejor si norma una convención bilingüe — identificadores
y nombres estructurales del código en inglés; contenido de cara al
usuario en el idioma del proyecto, que puede ser el nativo del equipo.
Skevi ya vivía la regla sin escribirla: los scripts usan identificadores
en inglés con comentarios en español, ADR-003 fijó los directorios en
inglés, el §3.5 exige claves de registro en inglés y el §4.1 usa
ejemplos de rama en inglés. El estándar §3.1 mencionaba "idiomas
estructurales del proyecto" sin definirlos: la regla nueva precisa ese
hueco.

Decisión: añadir al §3.1 del estándar la convención de idioma — en
código nuevo, identificadores y nombres estructurales (variables,
funciones, clases, ramas, claves de configuración) en inglés; los
comentarios siguen el idioma de la prosa del proyecto; documentación,
mensajes de interfaz y textos visibles en el idioma del proyecto, que
puede ser el nativo del equipo. La viñeta precisa y gana sobre la
lectura genérica de "el código nuevo se parece al código que lo
rodea". La regla fija convención para código nuevo; no ordena migrar
legado.

Alternativas descartadas:

- todo el proyecto en un solo idioma: uniforme, pero pelea con la
  práctica real de equipos hispanohablantes y con ADR-003, que ya
  separó estructura (inglés) de prosa (español);
- dejar que cada proyecto decida sin norma: es el statu quo; la regla
  existe porque la mezcla sin criterio escrito es lo que la guía
  prohíbe en todo lo demás;
- inglés también en la documentación de cara al usuario: maximiza
  reutilización, pero degrada la legibilidad para el público nativo y
  contradice la práctica de skevi, cuya prosa normativa es español.

Consecuencias: la capa técnica de los proyectos (código, claves, ramas,
identificadores) queda en inglés; los comentarios y el contenido de
cara al usuario, en el idioma que el proyecto declare. Renombrar
legado es una refactorización aparte
(§3.3), nunca un efecto colateral de esta regla. Los reportes de agente
en dos capas (PROP-006, en deliberación) heredan esta polaridad: capa
técnica en inglés, capa humana en idioma del proyecto. La regla es
transversal y no viola la frontera `no_ofrece` del manifest (no es una
regla específica de un lenguaje de programación).
