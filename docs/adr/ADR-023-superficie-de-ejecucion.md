# ADR-023: Superficie de ejecución declarada del ejecutor automatizado

Estado: aceptado; implementado como punto 8 del §6 del estándar.

Contexto: el corpus gradúa con detalle la autoridad **de Git** —§4.3, §6.2,
ADR-017, ADR-018, y la excepción local más restrictiva de `AGENTS.md`— y esa
graduación es su punto más fuerte frente a OWASP LLM06 «Excessive Agency».
Pero cubría *qué hace* el ejecutor y no *con qué puede hacerlo*: qué comandos
invoca, qué rutas lee, si tiene salida a red, en qué entorno corre y qué
comparte con el del humano. El cotejo de
[`crosswalk-estandares.md`](../crosswalk-estandares.md) lo confirmó como
hueco doble: NIST SSDF **PO.5** «Implement and Maintain Secure Environments
for Software Development» sin cubrir, y el límite del propio LLM06. Ninguna
línea de `project-manifest.yaml` §`no_ofrece` cedía ese plano a otro
proyecto: era un hueco sin dueño, no una frontera.

Decisión: Skevi norma el **mecanismo** de la superficie de ejecución, opción
A de PREGUNTA-M6-1, resuelta por el humano el 2026-09-07. Se declara por
tarea y con polaridad cerrada —se permite lo enumerado, se rechaza lo
demás— sobre cinco ejes: herramientas invocables (incluidos los servidores
de herramientas externas, que son frontera del sistema y llevan contrato,
revisión de amenazas y kill switch), sistema de archivos, red, aislamiento
del entorno, y secretos respecto de la ventana de contexto. Ampliar la
superficie es operación con autoridad separada (§4.3), no un ajuste de
configuración.

**Frontera con praxis-dev.** El manifiesto cede a `praxis-dev` tres cosas:
«autoridad, conformidad ni perfiles de aseguramiento». Este ADR no toca las
dos últimas —define qué debe estar acotado y declarado, no cómo se audita ni
qué perfil cumple—, y la última frase del punto 8 lo dice en la norma misma.

La primera, «autoridad», exige una lectura explícita que la primera emisión
de este ADR no dio (hallazgo de la ronda fresca del 2026-09-08). El punto 8
crea una clase nueva de operación con autoridad separada, y una lectura
literal de esa línea la cedería. Pero esa lectura literal es incompatible
con el corpus **desde antes de este ADR**: §4.3, §6.2, ADR-017 y ADR-018 ya
norman autoridad en detalle, y la excepción local de `AGENTS.md` la endurece.
Si «autoridad» significara todo el plano, esas cuatro fuentes ya lo estarían
invadiendo. La lectura que hace coherente al corpus es la que este ADR
adopta: Skevi norma el **mecanismo** de graduación de permisos; `praxis-dev`
recibe la autoridad como plano de gobernanza —quién otorga, bajo qué
conformidad, con qué perfil de aseguramiento—.

Esa lectura es una interpretación, no una decisión registrada: la tensión es
preexistente y precisar la línea del manifiesto es una decisión de política
que corresponde al humano. Queda abierta como PREGUNTA-M6-3 en
[SPEC-M6](../specs/SPEC-M6-2026-09-07-seis-mejoras.md) y **no** se resuelve
modificando `no_ofrece` por cuenta del ejecutor.

**Ubicación: §6, no §2.5.** El análisis que originó esta mejora proponía una
sección nueva en §2 «Diseño de sistemas». Se descarta: §2 norma el sistema
que se construye, no el entorno del ejecutor que lo construye; ponerlo ahí
sería un error de categoría. §6 «Trabajo asistido por agentes» ya es donde
un ejecutor lee sobre su propia operación, y el punto 8 queda contiguo al
escalado (7) y al reporte (9), con el reporte renumerado de 8 a 9.

Alternativas descartadas:

- **Remitir a praxis-dev sin regla** (opción B). Deja el mayor hueco del
  corpus con dueño nominal y sin cubrir, y contradice que §4.3 ya norme
  mecanismo de autoridad sin invadir conformidad.
- **Partir mecanismo y perfiles entre dos repos** (opción C). Correcta a
  largo plazo, pero exige coordinar un cambio en `praxis-dev` que este
  trabajo no tiene autoridad para hacer. La opción A no la impide: los
  perfiles siguen cedidos y pueden construirse encima.
- **Enumerar herramientas concretas** (nombres de binarios, servidores MCP
  específicos). Acopla el estándar a un ecosistema de herramientas que
  caduca; §6 aplica a «cualquier ejecutor automatizado, sin depender de
  ninguno en particular».
- **Un gate que verifique la superficie.** No es comprobable desde dentro
  del repositorio: la superficie vive en el entorno del ejecutor, no en sus
  archivos. Declararlo verificable sería el anti-patrón del gate vacuo que
  ADR-014 bloqueó.

Consecuencias: la declaración de superficie pasa a ser parte del contrato de
delegación, junto al alcance y las prohibiciones. Un ejecutor sin superficie
declarada opera fuera de norma aunque su contrato de tarea sea impecable. El
silencio deja de ser permiso en el eje de red: sin declaración, no hay red.
Un secreto que entró al contexto se trata como comprometido, con la misma
regla de revocación-antes-que-limpieza de §5.4. La regla consume presupuesto
de la ruta de lectura (ADR-021): el estándar y `04` crecieron, y el margen
restante es de dos dígitos — la próxima ampliación del §6 obligará a decidir,
que es exactamente para lo que existe el presupuesto. La ocupación vigente la
reporta el gate.

Verificación: `python3 scripts/check_sizes.py` → `OK` con la ruta de lectura
dentro de su presupuesto; renumeración comprobada con `grep -n` sobre los
puntos 7, 8 y 9 del §6; cotejo actualizado en
[`crosswalk-estandares.md`](../crosswalk-estandares.md) (PO.5 y LLM06).

Procedencia: PREGUNTA-M6-1 de
[SPEC-M6](../specs/SPEC-M6-2026-09-07-seis-mejoras.md), resuelta por
instrucción directa del humano el 2026-09-07 con la opción A; T05 del
[plan M6](../plans/2026-09-07-seis-mejoras.md);
[`crosswalk-estandares.md`](../crosswalk-estandares.md) (SSDF PO.5, OWASP
LLM06 y LLM02).
Razón: cerrar el hueco sin dueño entre la autoridad por operación y el
entorno real en que se ejerce, sin invadir el plano de conformidad.
