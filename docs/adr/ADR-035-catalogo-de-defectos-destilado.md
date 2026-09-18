# ADR-035: Catálogo de clases de defecto, destilado de material ajeno

Estado: aceptado el 2026-09-18 (folio `SKV-ACC-PROP010-20260918-01`);
implementado por el plan de `docs/plans/` que deriva de
[PROP-010](../proposals/PROP-010-destilacion-engineering.md) §8.

Contexto: la ronda adversarial de `04` §5 exige atacar el trabajo propio, y
`04` §8 exige diagnóstico escrito tras dos intentos fallidos. Ninguno de los
dos dice **contra qué** atacar: el ejecutor improvisa las clases de defecto
que busca, y las improvisa distintas cada vez. El plugin Engineering 1.2.0 de
Anthropic ofrece criterios de revisión y diagnóstico que llenan ese hueco, y
el Operador autorizó destilarlos.

Decisión: **una plantilla, `templates/skevi/review-defect-catalog.md`**, con
clases de defecto agnósticas de lenguaje y plataforma —entrada no confiable e
inyección, autorización, secretos, concurrencia, recursos no liberados,
trabajo no acotado, errores silenciados, contrato roto, y test que no prueba
el requisito—, cada una con su pregunta de ataque y la evidencia que se
espera; más la sección que da forma al diagnóstico escrito de `04` §8:
reproducción, aislamiento, hipótesis con su prueba, y causa raíz separada del
síntoma.

Consecuencias:

- **Se destila, no se copia ni se depende.** La procedencia está verificada
  contra `anthropics/knowledge-work-plugins@58da91d` —catorce archivos por
  SHA-256, licencia Apache-2.0, sin `NOTICE`, sin commit posterior— y
  registrada en `../reviews/2026-09-18-prop010-procedencia.md`. Eso acredita
  de dónde se leyó, no una dependencia: Skevi no sigue ese repositorio, no
  versiona su material y no se sincroniza con él. La atribución por archivo
  de la plantilla es registro de origen, no obligación contractual. Al
  escribirla se comprueba que no arrastra expresión literal del original: si
  la arrastrara, dejaría de ser destilación.
- **El alcance de Skevi no se amplía.** El Operador decidió que Skevi es
  cuerpo normativo para diseñar software y para operar **agentes de IA** que
  crean y mantienen proyectos, y que operar al ejecutor no es operar sistemas
  en producción. Por eso quedan fuera postmortem y runbook, y con ellos la
  minimización de datos personales, la custodia de evidencia, la severidad de
  impacto de dominio y los folios de autorización de ejecución: pertenecen a
  quien opera el sistema. `proposito` y `no_ofrece` no cambian.
- **`ofrece` gana una línea, marcada experimental.** Declarar una capacidad
  que cabe en el alcance vigente no lo amplía; omitirla sería crecer por
  acumulación. La línea se retira junto con la plantilla si ésta no sale de
  experimental (PROP-010 §3.5).
- **El catálogo no convierte en verificación lo que sigue siendo revisión.**
  Lo aplica el ejecutor, que normalmente es un agente, así que rige ADR-024 y
  `06-componentes-con-llm.md`: la salida de una revisión asistida es salida
  no determinista por mucho que esté estructurada. Lo que el catálogo aporta
  es forma comprobable —clase, pregunta de ataque, evidencia esperada—, no
  certeza.

Alternativas descartadas:

- **Importar el plugin como dependencia.** Acopla un proveedor a un corpus
  que declara no tener ninguna, y obliga a seguir su cadencia.
- **Ampliar el alcance a operación** para admitir postmortem y runbook.
  Descartada por el Operador: mezcla dos sentidos de «operar» y arrastra al
  corpus reglas de dominio que no le tocan.
- **Mitigaciones preautorizadas en runbook** (C2a). Su control central
  —comprobar antes de ejecutar que la aceptación sigue vigente y no
  revocada— exige un registro de vigencia que ningún documento de Skevi
  define, y construirlo sería gobernanza de autoridad, cedida en
  `project-manifest.yaml`. Sin ese registro la comprobación sólo puede
  autoatestarse, que es el defecto que pretendía cerrar.

Procedencia: [PROP-010](../proposals/PROP-010-destilacion-engineering.md),
aceptada en su §7. Seis rondas adversariales de contexto fresco, registradas
en `../reviews/`; ninguna cerró en `proceed` y el Operador decidió firmar
igualmente: las cuatro últimas ya no hallaban defectos del contenido sino de
la autodescripción del documento. Esa omisión, y los otros tres límites
—decisiones sin acta, identidad autodeclarada del revisor de la primera ronda
e independencia de modelo de las demás—, están declarados en §7 como riesgos
residuales aceptados con nombre.
