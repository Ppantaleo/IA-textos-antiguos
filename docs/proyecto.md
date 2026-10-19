---
title: "Aplicaciones de inteligencia artificial a la restauración e interpretación de textos antiguos"
subtitle: |
  Hacia un marco de metadatos y preservación digital de sus resultados  
  Proyecto de trabajo de fin de máster
author: |
  Patricio Iván Pantaleo  
  Máster Universitario en Bibliotecas, Archivos y Continuidad Digital  
  Universidad Carlos III de Madrid  
  Director: Ricardo Eito Brun
---

## 1. Problema

Los sistemas de inteligencia artificial aplicados a textos antiguos producen
aserciones sobre objetos del patrimonio documental: restauran lagunas, atribuyen
origen geográfico, datan, transcriben, leen soportes físicamente inaccesibles.
Esas aserciones mayoritariamente son probabilísticas —el modelo no devuelve *un* resultado sino
una distribución sobre resultados posibles— y son revisadas, corregidas o
adoptadas por especialistas humanos.

El resultado de ese proceso es un activo digital que circula: se cita, se
reutiliza, se incorpora a ediciones y a bases de datos. Pero se desconoce en qué
medida ese activo viaja acompañado de la documentación que permitiría, más
adelante, saber qué lo produjo, con qué versión de qué modelo, con cuánta
certeza, y quién lo validó.

Ese desconocimiento —y no su respuesta presupuesta— es el punto de partida.

## 2. Pregunta de investigación

**RQ.** ¿Qué metadatos de proveniencia y preservación se registran actualmente
en las aplicaciones de inteligencia artificial a la restauración e
interpretación de textos antiguos?

Subpreguntas:

- **SQ1.** ¿Qué registra efectivamente cada proyecto, sin categorías previas?
- **SQ2.** ¿Cómo se mapea lo registrado sobre PREMIS, METS e ISO 23081?
- **SQ3.** ¿Qué exigen esos estándares que los proyectos no tengan, y qué tienen
  los proyectos que esos estándares no puedan alojar?
- **SQ4** *(condicional al hallazgo)*. Si se confirma una carencia, ¿qué
  extensión mínima la cubriría?

## 3. Objetivos

**General.** Relevar qué metadatos de proveniencia y preservación se registran
en las aplicaciones de IA a textos antiguos, y contrastar lo relevado con los
estándares archivísticos de preservación digital.

**Específicos.**

1. Construir, mediante protocolo reproducible, el corpus de proyectos que
   cumplen los criterios de inclusión.
2. Caracterizar inductivamente qué metadatos genera, usa y persiste cada
   proyecto, distinguiendo los de entrada y entrenamiento de los de salida.
3. Mapear lo relevado sobre PREMIS, METS e ISO 23081, y analizar el desajuste en
   ambas direcciones.
4. *(Condicional)* Si el relevamiento confirma carencias, esbozar una extensión
   de metadatos que las cubra, en anexo o corolario, validada conceptualmente
   sobre uno o dos casos.

## 4. Marco teórico

El objetivo general excede el alcance de un solo estándar. Pone en relación tres
cuerpos de literatura que hoy apenas se citan entre sí: el campo que aplica
inteligencia artificial a textos antiguos, el problema general de la
proveniencia de lo generado por máquinas y la normativa de preservación digital.
El marco se organiza en esos tres ejes y en su punto de cruce, que es donde se
sitúa la pregunta.

### 4.1 La IA aplicada a textos antiguos

El campo tiene ya un mapa propio: el *survey* de Sommerschield et al. (2023)
ordena las tareas —restauración de lagunas, atribución geográfica y temporal,
transcripción y HTR, traducción automática, desciframiento, búsqueda y
alineamiento de paralelos— y fija la delimitación del objeto que este trabajo
adopta en §5.1.

Lo que ese campo documenta de sí mismo está bien establecido: arquitectura del
modelo, composición del corpus de entrenamiento, procedimiento de evaluación y
métricas de rendimiento (exactitud *top-k*, tasa de error por carácter,
*perplexity*). Esa documentación responde a la pregunta de la comunidad de
aprendizaje automático —si el modelo funciona y es comparable con otros— y no a
la de la comunidad archivística —qué es, de dónde viene y qué garantías tiene
cada resultado concreto que el modelo produjo—. La distancia entre ambas
preguntas es el espacio del trabajo.

El rasgo que vuelve específico el problema es el estatuto de la salida: un
modelo de restauración no devuelve una lectura sino un conjunto ordenado de
lecturas posibles con sus probabilidades, y lo que se publica suele ser una de
ellas, elegida por un especialista. La aserción que circula es el producto
conjunto de un modelo y de un juicio humano, y ninguno de los dos queda
necesariamente inscrito en ella.

### 4.2 La proveniencia de lo generado por máquinas

Fuera del patrimonio documental hay instrumentos en circulación que abordan
partes del problema. Las **fichas de modelo** y las **hojas de datos**
(Mitchell et al., 2019; Gebru et al., 2021) documentan el modelo y el conjunto
de entrenamiento, no cada salida producida con ellos. **PROV-O** (Lebo et al.,
2013) es un vocabulario genérico de procedencia para la web de datos, no un
esquema de preservación. **C2PA** (Coalition for Content Provenance and
Authenticity, 2026) adhiere credenciales al archivo e identifica intervención
algorítmica, con la fotografía y los medios como dominio de origen.
**CIDOC-CRM** y **CRMdig** (CIDOC CRM Special Interest Group, 2023) modelan la
digitalización y la cadena de derivación en el ámbito museístico. Y la **nube
colaborativa europea para el patrimonio cultural** (ECCCH), que construye el
proyecto ECHOES entre 2024 y 2029 (ECHOES, 2024), muestra que el problema está
en la agenda institucional.

> **De dónde sale esta lista y qué estatuto tiene.** No procede de la búsqueda
> sistemática: el protocolo de §6.5 rastrea aplicaciones de IA a textos
> antiguos, no estándares de proveniencia. Se reunió por lectura dirigida
> durante el encuadre del trabajo, y de cada instrumento se verificó la versión
> vigente antes de citarlo. Es, por tanto, **horizonte de comparación y no
> hallazgo**: delimita el espacio del problema y obliga a comprobar si alguna
> pieza ya resuelta puede reutilizarse antes de proponer nada nuevo. **Qué
> instrumentos usan de hecho los proyectos es una pregunta del relevamiento**,
> no de este apartado: se responde con el bloque 9 del formulario de extracción
> y se informa en los resultados. Si la respuesta fuera que ninguno de estos
> nombres aparece en la práctica, eso también sería un resultado.

Ninguno de ellos pertenece al contenido curricular del máster ni es el vehículo
habitual de la preservación en archivos y bibliotecas, y por eso ninguno sirve
de base al marco.

### 4.3 La preservación digital como eje normativo

**Qué significa preservar.** En archivística, preservar no es guardar. El
modelo de referencia OAIS fija el criterio: la información preservada debe
seguir siendo **independientemente inteligible** para una comunidad designada,
sin depender de quien la produjo, y para lograrlo exige acompañarla de
información de descripción de la preservación, en la que la **proveniencia** es
una de las cuatro categorías obligatorias, junto con la referencia, el contexto
y la fijeza (Lavoie, 2014). La proveniencia no es entonces un adorno
descriptivo del objeto: es parte de lo que lo mantiene preservable.

Es además la condición de su autenticidad. La autenticidad de un documento
digital no se verifica mirándolo —no hay sello ni soporte que la sostenga—:
se infiere de su identidad y su integridad declaradas y del control documentado
sobre su custodia a lo largo del tiempo (Duranti y Rogers, 2012). Un objeto
digital sin ese registro puede leerse, pero no juzgarse.

**Por qué esto importa aquí.** La salida de un modelo aplicado a un texto
antiguo no es un dato más: es una aserción interpretativa sobre un bien
patrimonial —esta laguna decía esto, esta inscripción es de allí y de tal
fecha—, emitida con un grado de certeza y aceptada por alguien. Si se conserva
sin ese registro, la aserción se aplana: dentro de veinte años la lectura
restaurada será indistinguible de una lectura atestiguada, y la edición que la
incorporó no permitirá saber cuál era cuál. La pérdida no es técnica sino
epistémica, y es irreversible, porque reconstruir después qué modelo produjo
qué y quién lo validó suele ser imposible. En un campo donde la evidencia
material es escasa y las lecturas se acumulan unas sobre otras, esa confusión
contamina el registro.

**Por qué estos tres estándares.** Son los que gobiernan la conservación a
largo plazo en archivos y bibliotecas, que son el destinatario del trabajo. Que
una salida de IA sea preservable significa, en términos prácticos, que una
institución pueda ingestarla, describirla y conservarla con los instrumentos
que ya usa, sin inventar un circuito aparte.

| Estándar | Qué aporta al análisis |
|---|---|
| **PREMIS** | Modela `Object`, `Event`, `Agent` y `Rights`. Contempla que un *software* sea agente, con versión, ejecutando un evento fechado con un resultado sobre un objeto. Es el molde más directo para "qué modelo produjo esta salida" |
| **METS 2** | Empaquetado y estructura. Pregunta algo que PREMIS no: si existe siquiera un objeto digital con envoltorio, o si el resultado circula como dato suelto sin metadatos adheridos |
| **ISO 23081** | Modelo entidad-relación (documentos, agentes, actividades, reglas). Puente conceptual con el contenido ya cursado; da la estructura de nivel superior de la matriz |

Ediciones que se analizan: PREMIS 3.0 (PREMIS Editorial Committee, 2015),
publicada en junio de 2015 y revisada en noviembre, con esquema XML de enero
de 2016;
**METS 2** (Library of Congress, 2025), la revisión mayor que simplifica el
esquema y elimina la dependencia de XLink; ISO 23081-1:2017 e ISO 23081-2:2021.
La rama METS 1 sigue soportada y en uso en los repositorios existentes, así que
se la menciona cuando el contraste lo pida, pero el marco se construye sobre la
versión vigente.

El apartado siguiente lleva estos tres instrumentos al caso que nos ocupa: qué
ocurre cuando lo que hay que preservar es una aserción probabilística.

### 4.4 Punto de cruce: la salida como objeto a preservar

Los tres ejes se cruzan en una pregunta que ninguno responde solo: qué hace
falta que acompañe a una lectura restaurada por un modelo para que, dentro de
veinte años, siga siendo interpretable como lo que es —una propuesta con un
grado de certeza, producida por un sistema concreto y aceptada por alguien—, y
no un dato más dentro de una edición.

Tres tensiones conceptuales organizan ese cruce y guían la capa normativa del
análisis (§6.4):

1. **Determinismo frente a distribución.** PREMIS fue diseñado para eventos
   deterministas: una migración de formato se completa o falla. Un modelo emite
   un resultado probabilístico, y las alternativas descartadas también son
   información. La inspección de la norma lo confirma: de las 196 unidades
   semánticas del diccionario de datos —89 de objeto, 21 de evento, 18 de
   agente y 68 de derechos—, ninguna nombra confianza, probabilidad ni
   certeza, y el vocabulario de resultados de evento tiene tres términos:
   *success*, *fail* y *warning*. La palabra *confidence* aparece dos veces en
   las 283 páginas del diccionario, ambas en la discusión sobre fijeza y
   autenticidad, nunca como unidad. El grado de confianza solo cabe entonces
   como texto libre en `eventOutcomeDetailNote`, donde no es consultable ni
   comparable.
2. **Entidad intelectual frente a objeto.** PREMIS distingue la entidad
   intelectual del objeto digital que la representa. Una restauración obliga a
   decidir si la salida es una representación nueva del testimonio o una
   aserción sobre él; la respuesta cambia dónde se ancla la proveniencia.
3. **Evento de preservación frente a evento de interpretación.** El
   vocabulario de tipos de evento de PREMIS tiene 50 términos y todos designan
   operaciones técnicas: migración, normalización, comprobación de fijeza,
   extracción de metadatos, validación, cifrado. Una inferencia que propone
   texto no es una operación técnica sobre el objeto, sino un acto
   interpretativo que produce conocimiento nuevo.

Las cifras proceden de la inspección directa del diccionario de PREMIS 3.0, de
su esquema XML y de los treinta vocabularios de la Library of Congress
(s. f.), consultados el 15 de octubre de 2026.

## 5. Objeto de estudio

**"Textos antiguos"**, no "manuscritos". Es el término que cubre a la vez la
inscripción epigráfica (Ithaca, Aeneas: piedra y bronce; DR-LIFT: inscripciones
tamiles en piedra), el rollo y el papiro (DRI, Enoch), la tablilla (acadio,
lineal B) y el manuscrito (Lacuna). Las particularidades de cada soporte se
detallan dentro del trabajo.

### 5.1 Definición operativa de "texto antiguo"

Se adopta la delimitación de Sommerschield et al. (2023, p. 705), por ser la
referencia de autoridad del campo:

> "ancient texts written in ancient languages [...] all languages in use across
> the world, written on any medium and in any script, between the birth of
> writing systems in ancient Mesopotamia (3400 BCE) up until the conventional
> end of 'ancient history' in the late first millennium CE."

**Qué se fecha: el texto (la obra), no el soporte conservado.** Consecuencias
para el cribado:

- **Entran** las copias posteriores de obras antiguas. Por ejemplo, una
  aplicación sobre manuscritos medievales de la *Ilíada*.
- **No entran** las obras compuestas después del corte, aunque retomen textos
  antiguos (adaptaciones, paráfrasis) o usen una lengua de origen antiguo que
  siguió escribiéndose (latín medieval, chino literario tardío).
- La lengua y la escritura siguen sin ser criterio. El criterio es la
  época del texto.

**Corpus mixtos** (modelos entrenados con textos anteriores y posteriores al
corte): entran **solo si trabajan principalmente con textos anteriores al
corte**. Criterio provisional, a revisar con los casos reales del cribado.

## 6. Metodología

**Diseño: scoping review conforme a PRISMA-ScR (Tricco et al., 2018), con
análisis de artefacto embebido sobre el subconjunto inspeccionable.**

No es una revisión sistemática: no responde una pregunta de efectividad ni
practica valoración de calidad de evidencia. Es un mapeo de la extensión, el
rango y la naturaleza de una práctica. Su paso de *data charting* produce la
matriz comparativa, que es a la vez instrumento y producto.

### 6.1 Criterios de inclusión

Un proyecto entra si cumple **todas** estas condiciones (en §6.6 se
operacionalizan como C1–C4):

1. Existe un proceso de IA en la lectura o interpretación del material —
   incluido el análisis de **materialidad** del soporte, no solo del contenido.
2. Existe un producto digital resultante de esa acción sobre el cual evaluar
   metadatos. No es necesario que sea una imagen: puede ser texto, dato
   estructurado o modelo.
3. El material son **textos antiguos** según la definición de §5.1.
4. Si el corpus mezcla épocas, trabaja **principalmente** con textos anteriores
   al corte (§5.1).

**Lengua y escritura no son criterio de selección.** Entra una aplicación a
cualquier lengua o sistema de escritura antiguo (griego, latín, hebreo, acadio,
chino clásico, tamil, maya, etc.) si cumple las condiciones anteriores. Lo que
se evalúa es la aplicación de IA, no la tradición textual. La lengua y la
escritura se registran como variables descriptivas (§6.4).

### 6.2 Ventana temporal

**Corte: 2022**, con capítulo de antecedentes.

*Fundamento:* el corte no marca la aparición de la IA aplicada a textos antiguos
—que es anterior— sino el momento en que el problema de proveniencia se vuelve
efectivo. Pythia (Assael et al., 2019) restauraba y nada más; Ithaca (Assael
et al., 2022) restaura, atribuye
geográficamente y data, con interfaz pública. Es el punto en que estos sistemas
pasan a emitir múltiples clases de aserción, cada una con su incertidumbre, y a
circular fuera del laboratorio.

*Regla complementaria:* los proyectos activos de larga data entran por sus
publicaciones desde 2022, sin que su fecha de inicio los excluya. Así el DRI
—fundacional en 2016, con la lectura virtual del rollo de En-Gedi (Seales et
al., 2016)— permanece en el corpus.

### 6.3 Jerarquía de fuentes de evidencia

De mayor a menor peso probatorio:

1. **Salida del modelo tal como circula** (interfaz pública o resultado incorporado en publicaciones y bases; evidencia primaria)
2. Documentación del software y repositorio
3. Material suplementario
4. Artículo científico (declaración de los autores)

**Objeto de evaluación: la salida que circula y se cita**, no la
que puede reproducirse en local. El nivel 1 corresponde a la salida tal como la
entrega la interfaz pública del proyecto (p. ej., predictingthepast.com para
Ithaca y Aeneas) o tal como aparece incorporada en publicaciones y bases de
datos. La ejecución local y la lectura del código quedan como evidencia de
contraste (nivel 2).

> **Advertencia de interpretación.** Que un proyecto no sea auditable
> públicamente no prueba que no documente. La afirmación defendible es "no es
> verificable públicamente que documente", no "no documenta". Esa opacidad es en
> sí misma un hallazgo, y se lee en clave de prácticas FAIR.

### 6.4 Instrumento de análisis: dos capas

| Capa | Qué hace | Por qué |
|---|---|---|
| **A — Inductiva** | Registra qué documenta cada proyecto sin categorías previas | Un formulario derivado solo de PREMIS sería ciego a lo que los proyectos sí registran —corpus de entrenamiento, arquitectura, hiperparámetros, procedencia del material— que PREMIS no contempla |
| **B — Normativa** | Ubica lo relevado en PREMIS / METS / ISO 23081 | Deriva las categorías del estándar y no de la intuición del autor |

El análisis del vacío se lee **en las dos direcciones**: lo que el estándar exige
y no está, y lo que está y el estándar no puede alojar. La segunda dirección es
la más original: no dice que los proyectos estén mal, dice que el instrumento no
fue diseñado para esto.

**Dónde se miran los metadatos.** No se responde leyendo lo que los proyectos
dicen de sí mismos, sino mirando lo que entregan. Se recorren cuatro lugares en
el orden de peso probatorio de §6.3: la salida tal como circula, la
documentación y el repositorio, el material suplementario y los datos
depositados, y por último el artículo. Qué se examina en cada uno y qué se
obtiene, en el anexo B.

**Cómo se registra.** Cada celda guarda el valor encontrado, el nivel de
evidencia (1 a 4), la dirección consultada y la fecha. Cuando un dato no
aparece se distingue **no se registra** —se examinó la salida y el campo no
existe— de **no es verificable públicamente** —no hay salida que examinar—,
conforme a §6.3. No se ejecutan los modelos para producir salidas nuevas: se
observa lo que cada proyecto ya publica, y la lectura del código queda como
evidencia de contraste.

**Variables descriptivas** que caracterizan cada caso sin servir para
seleccionarlo: lengua, sistema de escritura y soporte (piedra, bronce, arcilla,
papiro, pergamino, bambú…). La unidad sobre la que se aplica el formulario se
define en §6.7.

### 6.5 Fuentes y estrategia de búsqueda bibliográfica

Lo que se busca en estas bases son **publicaciones**, no proyectos: ninguna
base indiza sistemas de IA. Los proyectos se derivan de la literatura que los
describe, y recién en la lectura de texto completo se reconstruye, a partir de
las publicaciones incluidas, qué proyecto hay detrás de cada una (§6.7).

| Fuente | Función | Justificación |
|---|---|---|
| **OpenAlex** (Priem et al., 2022) | Base principal | Cobertura amplia y abierta, con preprints y actas. Admite búsqueda booleana con filtro temporal y su API deja registro reproducible |
| **Scopus** (acceso UC3M) | Base complementaria | Cubre el punto débil de OpenAlex: en el piloto, el 16 % de los registros no tenía resumen. Busca también en palabras clave (`TITLE-ABS-KEY`) |
| ***Snowballing*** | Complemento | Hacia atrás y hacia adelante desde el conjunto semilla y los estudios incluidos, con `referenced_works` y `cited_by`. Recupera lo que la cadena no capta y se cuenta aparte en el diagrama PRISMA |

**Cadena.** Dos bloques unidos por AND: (1) términos generales de IA y (2)
términos de textos antiguos, soportes y escrituras. **No se incluyen nombres de
técnicas o arquitecturas** (CNN, RNN, transformer…), porque suben la cobertura a
costa de mucho ruido. Cada versión de la cadena se guarda en
`busqueda/consultas/` y no se sobrescribe. La sintaxis de OpenAlex y la de
Scopus no son idénticas; su equivalencia se documenta en el registro de cada
corrida.

**Registro para PRISMA-ScR.** Para cada fuente: fecha de ejecución, cadena
literal, registros recuperados, duplicados eliminados (por DOI y, si falta,
por título normalizado) y registros que pasan al cribado.

**Herramientas.** Todo lo automatizable deja un *script* publicado (§9) y lo
que no, queda declarado como manual: la consulta a OpenAlex, la fusión y
deduplicación, la verificación de la bibliografía y el cuaderno de revisión del
cribado tienen *script*; la consulta a Scopus se hace a mano. El detalle, en el
anexo C.

**Crossref** no es fuente de búsqueda —no admite operadores booleanos— y se usa
solo como servicio de metadatos (Hendricks et al., 2020): completa los
registros, genera el BibTeX a partir del DOI y permite comprobar que cada
referencia de la bibliografía existe y coincide con lo que el registro dice.

**Qué deja fuera esta estrategia.** Un proyecto que nunca haya publicado en la
literatura indizada no aparece por esta vía, aunque tenga interfaz pública y
sus salidas circulen: es el punto ciego de buscar proyectos a través de
artículos. Lo corrigen en parte el *snowballing* y, dentro de cada publicación
incluida, los enlaces al repositorio, a la interfaz y al depósito de datos, que
son los que llevan de la referencia al sistema. La limitación se declara en los
resultados: el corpus describe los proyectos **con presencia en la literatura
académica**, que no son todos los que existen.

### 6.6 Cribado por título y resumen

**Hoja de criterios.** Cada registro se evalúa con cuatro preguntas derivadas
de §6.1 y §5.1:

| # | Pregunta | Si la respuesta es "no" |
|---|---|---|
| C1 | ¿Hay un proceso de IA (aprendizaje automático, redes neuronales, visión por computador, modelos de lenguaje) aplicado a la lectura o interpretación del material, incluida su materialidad? | Excluir, E1 |
| C2 | ¿Hay un producto digital resultante (texto restaurado, transcripción, atribución, modelo, dataset, imagen procesada…)? | Excluir, E2 |
| C3 | ¿El material son textos antiguos según §5.1 (obra compuesta antes de finales del primer milenio d. C., en cualquier lengua, escritura o soporte)? | Excluir, E3 |
| C4 | Si el corpus mezcla épocas, ¿trabaja principalmente con textos anteriores al corte? | Excluir, E4 |

Códigos de exclusión adicionales:

- **E5:** tipo documental sin estudio primario (editorial, fe de erratas,
  retractación, presentación de volumen de actas, índice).
- **E6:** tema ajeno, cuando el registro entró por coincidencia léxica.
- **R:** revisión o *survey* pertinente. No entra en el corpus, pero se usa
  como fuente de *snowballing*.

**Regla de duda.** En esta fase, ante información insuficiente se marca
**dudoso** y el registro pasa a lectura de texto completo. Solo se excluye
cuando el título y el resumen permiten afirmarlo.

**Cribado asistido por IA.** La IA propone decisión, código y motivo para cada
registro; el autor revisa todas las inclusiones, los dudosos y las revisiones, y
una muestra aleatoria estratificada del 10 % de cada código de exclusión, con la
que se estima el acuerdo. Solo las decisiones revisadas entran en el corpus. El
alcance y las garantías de ese uso están en §8.

**Fuera de esta búsqueda:** la literatura archivística sobre PREMIS y
proveniencia no forma parte del corpus de proyectos y necesita su propia
búsqueda dirigida.

### 6.7 Unidad de análisis: el proyecto

El trabajo usa dos unidades distintas y no intercambiables:

- **Unidad de recuperación y cribado: la referencia bibliográfica.** Es la que
  cuenta el diagrama PRISMA-ScR, porque lo que se busca, se deduplica y se
  criba son publicaciones.
- **Unidad de análisis y de *charting*: el proyecto.** Es la que ocupa una fila
  de la matriz comparativa, porque los metadatos de proveniencia no los
  documenta un artículo, los documenta —o no— el sistema que produce las
  salidas.

La distinción importa: un proyecto puede tener cuatro publicaciones y una sola
política de documentación, y contarlo cuatro veces sobrerrepresentaría a los
equipos que más publican. Contar proyectos hace que la matriz describa
prácticas y no volumen editorial.

**Definición.** Un **proyecto** es un sistema o aplicación identificable que
produce salidas sobre un corpus de textos antiguos. Es una sola unidad cuando
coinciden cuatro rasgos: un modelo o sistema identificable (nombre propio,
repositorio o interfaz), un equipo responsable con continuidad, una tarea y un
corpus estables, y una salida que circula bajo una identidad reconocible.

**Reglas de agrupación y separación.** Varias publicaciones del mismo sistema
—artículo original, versión ampliada, evaluación posterior, descripción del
conjunto de datos— forman **una** unidad, y las posteriores aportan datos a la
misma fila. Un **modelo nuevo con salida propia** es unidad propia aunque lo
firme el mismo equipo: Pythia, Ithaca y Aeneas son tres unidades, y el linaje
se registra en un campo de la matriz. No crean unidad un ajuste de
hiperparámetros, una reimplementación ni una evaluación añadida; sí la crean
dos sistemas homónimos de equipos distintos.

**Estudios sin sistema identificable.** Buena parte de la literatura son
experimentos puntuales, sin nombre, sin código y sin interfaz. Excluirlos
sesgaría el relevamiento hacia los proyectos de alta visibilidad. Entran como
unidad, con la publicación como identificador, y la matriz distingue el tipo:

| Tipo de unidad | Qué es | Qué se espera del *charting* |
|---|---|---|
| **Sistema** | Tiene nombre, interfaz o repositorio; la salida circula de forma identificable | Se puede evaluar hasta el nivel 1 de evidencia (§6.3) |
| **Estudio** | Experimento publicado sin sistema identificable ni salida circulante | El análisis suele detenerse en los niveles 2 a 4; la ausencia de salida auditable se registra como dato, no como carencia del estudio |

**La accesibilidad pública no es criterio de inclusión.** Un proyecto entra si
cumple C1–C4 (§6.1), tenga o no interfaz abierta, repositorio o demostración en
línea. Muchos sistemas descritos en la literatura no son accesibles: los hay
internos de un equipo, de una empresa, restringidos por licencia del corpus o
simplemente nunca publicados como servicio. Todos ellos entran en el corpus si
cumplen los criterios, y entran como unidad de tipo *sistema* cuando tienen
identidad reconocible, aunque esa identidad solo conste en la publicación.

Lo que cambia con la accesibilidad no es la inclusión, es **hasta qué nivel de
evidencia puede llegar el análisis** (§6.3) y, por tanto, qué puede afirmarse:
de un proyecto sin salida accesible se registra *no es verificable
públicamente*, nunca *no documenta*. Esa asimetría es un hallazgo del
relevamiento, no una carencia del corpus, y por eso cada celda guarda el nivel
de evidencia con el que se obtuvo.

**Trazabilidad del paso de una unidad a otra.** La correspondencia entre
referencias y proyectos se publica como tabla (`busqueda/proyectos.csv`), con
una fila por referencia incluida y la clave del proyecto al que se asigna. El
informe final declara ambas cifras: estudios incluidos tras la lectura de texto
completo y proyectos resultantes. La agrupación es una decisión del autor, no
un cálculo: por eso se publica, para que sea discutible.

### 6.8 Formulario de extracción de datos

Las dos capas de §6.4 se operacionalizan como una guía de preguntas aplicada a
cada proyecto, que es el *data charting* de PRISMA-ScR. **Cada celda registra, además del hallazgo, el nivel de evidencia con
que se obtuvo** (§6.3), de modo que la asimetría entre proyectos auditables y
opacos quede visible en los datos.

El formulario tiene diez bloques y está en el anexo A.

Los bloques 1 a 9 forman la capa inductiva y el bloque 10, la normativa. Los
bloques 5 a 8 concentran el núcleo de la pregunta de investigación: son los que
distinguen una salida que puede preservarse con sentido de una que solo puede
archivarse como cadena de texto.

El formulario se aplica primero a dos proyectos de prueba —uno con interfaz
pública y otro sin ella— y se ajusta antes de aplicarlo al resto. Esa versión
de prueba y la definitiva se conservan ambas en el repositorio de materiales
(§9).

## 7. Corpus semilla

Un **conjunto semilla** es un grupo pequeño de trabajos que se sabe de
antemano que deberían estar en el corpus. Sirve para poner a prueba la
estrategia de búsqueda antes de confiar en ella: si la cadena no los recupera,
el problema está en la cadena y no en la literatura. Es la comprobación mínima
de que una revisión no está midiendo su propio punto ciego.

Los proyectos del documento inicial **no son la muestra**: son ese conjunto de
control. El corpus final lo determina el protocolo, y puede resultar mayor o
menor.

**Composición** (10 trabajos con publicación desde 2022, en
`busqueda/consultas/v1.json`): Ithaca (Assael et al., 2022), Aeneas (Assael et
al., 2025), Enoch (Popović et al., 2025), BiNet (Dhali et al., 2026), DR-LIFT
(Murugan y Visalakshi, 2024), lineal B (Papavassileiou et al., 2023), acadio
NMT (Gutherz et al., 2023), Lacuna (Levine et al., 2024), glifos mayas
(Pinilla-Buitrago et al., 2022) y el *survey* de Sommerschield et al. (2023).

**Regla de validación.** El conjunto semilla valida la **estrategia completa**
(bases de datos más *snowballing*), no solo la cadena. Se informan por
separado los trabajos recuperados por la cadena en cada base y los que se
recuperan por *snowballing*. Un trabajo semilla que no aparezca por ninguna vía
indica un fallo de la estrategia.

**Resultado de la comprobación.** Ya se ejecutó, con la cadena v1 del 14 de
septiembre de 2026: las bases recuperaron **8 de los 10** trabajos. Faltan
Lacuna, publicado en las actas de un taller que OpenAlex indiza sin resumen y
Scopus no cubre, y Pinilla-Buitrago, que la cadena no alcanza por no nombrar
técnicas de visión por computador. Los dos deben aparecer por *snowballing*, y
si no aparecieran, la estrategia tendría un fallo que habría que declarar.


## 8. Declaración de uso de inteligencia artificial

El trabajo usa un asistente de IA (Claude, de Anthropic, modelo Opus 5, a
través de Claude Code) como herramienta instrumental. Se declara aquí el
alcance exacto de ese uso, por coherencia con el objeto del propio trabajo —la
proveniencia de lo producido con ayuda de máquinas— y con la Guía de buenas
prácticas de los estudiantes de la Universidad Carlos III de Madrid (2012,
apartado 2.H).

**En qué se usa.**

| Tarea | Uso | Rastro que queda |
|---|---|---|
| Consulta de APIs | Construcción y ejecución de las consultas a OpenAlex y de la recuperación de metadatos por DOI en Crossref | Scripts y registro de cada corrida |
| Programación | Escritura de los *scripts* de búsqueda, fusión, deduplicación y preparación del cribado, en Python | Código completo en el repositorio público (§9) |
| Cribado por título y resumen | Propuesta de decisión, código y motivo para cada registro, según una hoja de instrucciones fija | Instrucciones literales, propuesta sin modificar y revisión del autor |
| Verificación | Detección de inconsistencias internas del protocolo y de los criterios aplicados | Registro de decisiones y de enmiendas |
| Redacción | Formulación y pulido de secciones a partir de decisiones tomadas por el autor en diálogo | El autor revisa, corrige y asume cada párrafo |

La IA no figura como autora ni como coautora, y no se la cita como fuente. El criterio sigue a los marcos vigentes de autoría y contribución —ICMJE y CRediT—, que reservan la autoría a quien puede responder por el trabajo (Pantaleo, 2025).

**En qué no se usa.** No se delegan las decisiones metodológicas, la definición
del objeto y de los criterios, la lectura de los textos completos, la
cumplimentación del formulario de *charting*, la interpretación de los
resultados ni las conclusiones. La IA no es fuente: nada se afirma en el
trabajo porque un modelo lo haya dicho, y las referencias se verifican una a
una contra Crossref o contra la publicación.

**Condición del cribado asistido.** La propuesta de la IA no es una decisión.
Es una capa previa, equivalente a la de un segundo cribador, sobre la que el
autor decide: revisa todas las inclusiones, los dudosos y los *surveys*, y una
muestra aleatoria estratificada de las exclusiones, con la que se estima el
acuerdo. La cifra de acuerdo se informa en la memoria. Las propuestas sin
revisar no entran en el corpus.

**Trazabilidad.** Las instrucciones que recibió el modelo, su propuesta sin
modificar y las decisiones del autor se conservan por separado y se publican
(§9), por el mismo criterio que el trabajo exige a los proyectos que estudia:
que la salida viaje con el registro de qué la produjo y quién la validó.

## 9. Repositorio de materiales

Los materiales que permiten auditar y reproducir el relevamiento se publican en
un repositorio de código abierto, al que la memoria remite desde la
metodología: <https://github.com/Ppantaleo/IA-textos-antiguos>. Contiene:

los *scripts* de búsqueda, fusión, deduplicación y verificación de la
bibliografía, con sus informes; las cadenas de cada versión en su formato
literal; el registro de cada corrida; las instrucciones del cribado asistido,
la propuesta de la IA sin modificar y el *script* que genera el cuaderno de
revisión; las decisiones del autor y la correspondencia entre referencias y
proyectos (§6.7); y el formulario de extracción con la matriz resultante.

El código se publica bajo licencia MIT y los datos y documentos propios bajo
CC BY 4.0. **Se publican también los datos en bruto de las dos fuentes**: la
respuesta de la API de OpenAlex y la exportación manual de Scopus. Sin ellos,
la auditoría del relevamiento se detiene en la palabra del autor. La
exportación de Scopus procede de una base de suscripción cuyas condiciones de
uso no contemplan la redistribución: se publica como material de auditoría, en
la cantidad mínima necesaria, y se sustituirá por la lista de identificadores
si el titular lo requiere.

Se publica solo la corrida en vigor. El piloto que sirvió para calibrar la
cadena no sostiene ningún resultado y queda en la carpeta de trabajo.

La memoria no reimprime lo que el repositorio ya contiene: sus anexos se
limitan a la matriz comparativa y al diagrama PRISMA-ScR.

## 10. Plan de la memoria

**Estructura.** La exigida por la memoria de verificación del máster
(Universidad Carlos III de Madrid, s. f.) para el TFM: diseño de la investigación (objeto, objetivos, hipótesis, metodología,
fuentes), resultados, discusión, conclusiones y referencias.

**Extensión: 50 a 60 páginas**, incluidas portada, índice y bibliografía. Los
anexos pueden excederla; los materiales extensos van al repositorio (§9).

| Parte | Páginas |
|---|---|
| Portada, índice, resúmenes (ES/EN) | 4 |
| 1. Introducción y problema | 5 |
| 2. Marco teórico | 10 |
| 3. Objeto de estudio | 2 |
| 4. Metodología | 7 |
| 5. Resultados del relevamiento | 15 |
| 6. Discusión y análisis del desajuste | 6 |
| 7. Conclusiones y líneas abiertas | 3 |
| Referencias | 4 |
| **Total** | **56** |

El reparto sigue el orden de este proyecto: el objeto de estudio se define
antes del método, porque el método lo aplica. El índice tentativo completo, con
los apartados de cada capítulo, está en el repositorio (§9).

**Referencias: entre 50 y 60**, conforme a la orientación del director. Reparto
previsto: estándares y normativa (8), campo de la IA aplicada a textos antiguos
(25), proveniencia y documentación de modelos (8), metodología de revisión (5)
y preservación digital y archivística (8).

> **Cómo se concilia ese límite con una revisión de alcance.** El corpus puede
> superar las sesenta referencias, así que se presenta **como tabla en anexo**
> —autor, año, proyecto y DOI— y en la lista de referencias solo entran los
> trabajos citados en el cuerpo. Es la práctica habitual y mantiene legible la
> bibliografía sin ocultar el corpus.

**Calendario.** La convocatoria elegida es la de **febrero de 2027**, cuya
fecha límite de entrega es el **1 de febrero de 2027** y cuya matrícula vence
el 30 de noviembre de 2026.

| Hito | Fecha |
|---|---|
| **Matrícula del TFM, curso 26/27** (convocatoria de febrero) | antes del **30 de noviembre de 2026** |
| Revisión del cribado, lectura de texto completo, *snowballing* y extracción de datos | octubre y noviembre de 2026 |
| Capítulos 1 a 4: introducción, marco teórico, objeto de estudio y metodología | fines de noviembre de 2026 |
| Capítulo 5: resultados del relevamiento | antes del 23 de diciembre de 2026 |
| Capítulos 6 y 7, resúmenes y anexos: **borrador completo al director** | 12 de enero de 2027 |
| Revisión del director y correcciones | del 12 al 27 de enero de 2027 |
| **Entrega del TFM** | **1 de febrero de 2027**, fecha límite de la convocatoria |
| Defensa | febrero o marzo de 2027 |

Dos avisos sobre este calendario. El primero: la entrega es una fecha
administrativa y no admite prórroga, de modo que el borrador tiene que estar
cerrado tres semanas antes para dejar margen a la revisión del director y al
informe de tutoría. El segundo: los hitos van encadenados y el capítulo 5 no
puede escribirse antes de cerrar la extracción de datos, así que un retraso en
la revisión del cribado se traslada entero a lo que sigue.

Si el calendario no se cumpliera, las convocatorias siguientes del mismo curso
entregan el 21 de junio y el 13 de septiembre de 2027, ambas con matrícula
hasta el 31 de enero de 2027.

## Referencias

\begingroup\small

Solo las obras citadas en este documento. El estilo sigue APA 7.ª edición, a
confirmar con el director. La bibliografía completa del trabajo se mantiene en el
repositorio (`docs/bibliografia.bib`) y se verifica contra Crossref
(`registros/verificacion-bibliografia.md`).

Assael, Y., Sommerschield, T. y Prag, J. (2019). Restoring ancient text using
deep learning: A case study on Greek epigraphy. *Proceedings of the 2019
Conference on Empirical Methods in Natural Language Processing (EMNLP-IJCNLP)*,
6367–6374. <https://doi.org/10.18653/v1/D19-1668>

Assael, Y., Sommerschield, T., Shillingford, B., Bordbar, M., Pavlopoulos, J.,
Chatzipanagiotou, M., Androutsopoulos, I., Prag, J. y de Freitas, N. (2022).
Restoring and attributing ancient texts using deep neural networks. *Nature*,
*603*(7900), 280–283. <https://doi.org/10.1038/s41586-022-04448-z>

Assael, Y., Sommerschield, T., Cooley, A., Shillingford, B., Pavlopoulos, J.,
Suresh, P., Herms, B., Grayston, J., Maynard, B., Dietrich, N., Wulgaert, R.,
Prag, J., Mullen, A. y Mohamed, S. (2025). Contextualizing ancient texts with
generative neural networks. *Nature*, *645*(8079), 141–147.
<https://doi.org/10.1038/s41586-025-09292-5>

CIDOC CRM Special Interest Group. (2023). *Definition of the CIDOC Conceptual
Reference Model, version 7.2.3* (versión oficial en correspondencia con ISO
21127). <https://cidoc-crm.org/versions-of-the-cidoc-crm>

Coalition for Content Provenance and Authenticity. (2026). *Content
Credentials: C2PA technical specification, version 2.4*.
<https://spec.c2pa.org/specifications/specifications/2.4/>

Dhali, M. A., de Wit, J. W. y Schomaker, L. (2026). BiNet: A deep
encoder-decoder network for binarizing degraded ancient manuscripts. En
*Document Analysis and Recognition – ICDAR 2025 Workshops* (pp. 166–193).
Springer. <https://doi.org/10.1007/978-3-032-09371-4_11>

Duranti, L. y Rogers, C. (2012). Trust in digital records: An increasingly
cloudy legal area. *Computer Law & Security Review*, *28*(5), 522–531.
<https://doi.org/10.1016/j.clsr.2012.07.009>

ECHOES. (2024). *European Collaborative Cloud for Cultural Heritage (ECCCH)*.
Proyecto Horizon Europe coordinado por el CNRS, 2024–2029.
<https://www.echoes-eccch.eu/>

Gebru, T., Morgenstern, J., Vecchione, B., Vaughan, J. W., Wallach, H., Daumé
III, H. y Crawford, K. (2021). Datasheets for datasets. *Communications of the
ACM*, *64*(12), 86–92. <https://doi.org/10.1145/3458723>

Gutherz, G., Gordin, S., Sáenz, L., Levy, O. y Berant, J. (2023). Translating
Akkadian to English with neural machine translation. *PNAS Nexus*, *2*(5).
<https://doi.org/10.1093/pnasnexus/pgad096>

Hendricks, G., Tkaczyk, D., Lin, J. y Feeney, P. (2020). Crossref: The
sustainable source of community-owned scholarly metadata. *Quantitative Science
Studies*, *1*(1), 414–427. <https://doi.org/10.1162/qss_a_00022>

International Organization for Standardization. (2017). *ISO 23081-1:2017.
Information and documentation – Records management processes – Metadata for
records – Part 1: Principles*.

International Organization for Standardization. (2021). *ISO 23081-2:2021.
Information and documentation – Metadata for managing records – Part 2:
Conceptual and implementation issues*.

Lavoie, B. (2014). *The Open Archival Information System (OAIS) reference
model: Introductory guide* (2.ª ed.). Digital Preservation Coalition.
<https://doi.org/10.7207/twr14-02>

Lebo, T., Sahoo, S. y McGuinness, D. (Eds.). (2013). *PROV-O: The PROV
ontology*. W3C Recommendation. <https://www.w3.org/TR/prov-o/>

Levine, L., Li, C. T., Bremer-McCollum, L., Wagner, N. y Zeldes, A. (2024).
Lacuna Language Learning: Leveraging RNNs for ranked text completion in
digitized Coptic manuscripts. *Proceedings of the 1st Workshop on Machine
Learning for Ancient Languages (ML4AL 2024)*, 61–70.
<https://doi.org/10.18653/v1/2024.ml4al-1.8>

Library of Congress. (2025). *METS: Metadata Encoding and Transmission
Standard* (esquema 1.12.1; versión 2 publicada en 2025).
<https://www.loc.gov/standards/mets/>

Library of Congress. (s. f.). *PREMIS preservation vocabularies*.
<https://id.loc.gov/vocabulary/preservation.html>

Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson, B.,
Spitzer, E., Raji, I. D. y Gebru, T. (2019). Model cards for model reporting.
*Proceedings of the Conference on Fairness, Accountability, and Transparency
(FAT\* '19)*, 220–229. <https://doi.org/10.1145/3287560.3287596>

Murugan, B. y Visalakshi, P. (2024). Ancient Tamil inscription recognition
using detect, recognize and labelling, interpreter framework of text method.
*Heritage Science*, *12*(1). <https://doi.org/10.1186/s40494-024-01522-9>

Pantaleo, P. (2025, 19 de junio). *Authorship and contribution in the age of
AI: Notes on the current debate*. Paideia Studio.
<https://doi.org/10.62059/9x4p2w>

Papavassileiou, K., Kosmopoulos, D. I. y Owens, G. (2023). A generative model
for the Mycenaean Linear B script and its application in infilling text from
ancient tablets. *Journal on Computing and Cultural Heritage*, *16*(3), 1–25.
<https://doi.org/10.1145/3593431>

Pinilla-Buitrago, L. A., Martínez-Trinidad, J. F. y Carrasco-Ochoa, J. A.
(2022). Encoding hieroglyph segments to represent hieroglyphs following the bag
of visual word model for retrieval. *Expert Systems with Applications*, *201*,
116983. <https://doi.org/10.1016/j.eswa.2022.116983>

Popović, M., Dhali, M. A., Schomaker, L., van der Plicht, J., Lund Rasmussen,
K., La Nasa, J., Degano, I., Perla Colombini, M. y Tigchelaar, E. (2025).
Dating ancient manuscripts using radiocarbon and AI-based writing style
analysis. *PLOS One*, *20*(6), e0323185.
<https://doi.org/10.1371/journal.pone.0323185>

PREMIS Editorial Committee. (2015). *PREMIS data dictionary for preservation
metadata, version 3.0* (junio de 2015, revisado en noviembre de 2015). Library
of Congress. <https://www.loc.gov/standards/premis/v3/premis-3-0-final.pdf>

Priem, J., Piwowar, H. y Orr, R. (2022). *OpenAlex: A fully-open index of
scholarly works, authors, venues, institutions, and concepts* (arXiv:2205.01833).
<https://arxiv.org/abs/2205.01833>

Seales, W. B., Parker, C. S., Segal, M., Tov, E., Shor, P. y Porath, Y. (2016).
From damage to discovery via virtual unwrapping: Reading the scroll from
En-Gedi. *Science Advances*, *2*(9).
<https://doi.org/10.1126/sciadv.1601247>

Sommerschield, T., Assael, Y., Pavlopoulos, J., Stefanak, V., Senior, A., Dyer,
C., Bodel, J., Prag, J., Androutsopoulos, I. y de Freitas, N. (2023). Machine
learning for ancient languages: A survey. *Computational Linguistics*, *49*(3),
703–747. <https://doi.org/10.1162/coli_a_00481>

Tricco, A. C., Lillie, E., Zarin, W., O'Brien, K. K., Colquhoun, H., Levac, D.,
Moher, D., Peters, M. D. J., Horsley, T., Weeks, L., Hempel, S., Akl, E. A.,
Chang, C., McGowan, J., Stewart, L., Hartling, L., Aldcroft, A., Wilson, M. G.,
Garritty, C., … Straus, S. E. (2018). PRISMA extension for scoping reviews
(PRISMA-ScR): Checklist and explanation. *Annals of Internal Medicine*,
*169*(7), 467–473. <https://doi.org/10.7326/M18-0850>

Universidad Carlos III de Madrid. (2012). *Guía de buenas prácticas de los
estudiantes de la Universidad Carlos III de Madrid* (aprobada por el Consejo de
Gobierno el 29 de noviembre de 2012).

Universidad Carlos III de Madrid. (s. f.). *Memoria para la verificación del
Máster Universitario en Bibliotecas, Archivos y Continuidad Digital* (Real
Decreto 822/2021; plan vigente a partir del curso 2023-2024).

\endgroup

## Anexos

### Anexo A · Formulario de extracción de datos

| Bloque | Preguntas | Parámetros registrados |
|---|---|---|
| **1. Identificación** | ¿Qué sistema es, quién lo sostiene, desde cuándo? | Nombre, equipo, institución, años, referencias, tipo de unidad, linaje |
| **2. Material de entrada** | ¿Sobre qué trabaja y de dónde viene? | Lengua, escritura, soporte, época, corpus de origen, licencia, identificador de los testimonios |
| **3. Proceso** | ¿Qué hace y con qué? | Tarea, familia de modelo, versión, datos de entrenamiento, dependencia de servicios externos |
| **4. Salida** | ¿Qué produce y dónde circula? | Forma del resultado, canal (interfaz, repositorio, publicación, base de datos), formato, licencia, identificador persistente |
| **5. Enlace entrada–salida** | ¿La salida permite volver al testimonio del que procede? | Presencia de identificador del material de origen en la salida; granularidad del enlace |
| **6. Incertidumbre** | ¿Se expresa el grado de certeza y las alternativas? | Forma (probabilidad, *top-k*, intervalo, ninguna), persistencia de las alternativas descartadas |
| **7. Intervención humana** | ¿Consta que alguien revisó y aceptó el resultado? | Existencia de revisión, identificación del revisor, fecha, efecto sobre la salida |
| **8. Identidad del productor** | ¿La salida dice qué la produjo? | Versión del modelo, fecha de la inferencia, versión del software, parámetros |
| **9. Empaquetado y preservación** | ¿Hay objeto digital con metadatos adheridos y plan? | Esquema, repositorio de depósito, política de preservación, versionado |
| **10. Capa normativa** | ¿Dónde se aloja cada hallazgo en PREMIS, METS e ISO 23081? | Entidad y elemento del estándar, o anotación de desajuste |

### Anexo B · Dónde se miran los metadatos

| Lugar | Qué se examina | Qué se obtiene |
|---|---|---|
| **1. La salida que circula** | Se pide al sistema una salida por su interfaz pública y se examina lo que devuelve: la página de resultado, el archivo descargable (JSON, CSV, XML, TEI, imagen) y sus campos. Si el resultado ya está incorporado a una edición o a una base, se examina el registro tal como esa base lo publica | Qué acompaña de hecho al resultado cuando circula: identificadores, versión del modelo, fecha, confianza, alternativas, enlace al testimonio de origen |
| **2. Documentación y repositorio** | README, ficha de modelo, esquema de respuesta de la API, estructura del objeto de salida en el código, metadatos del depósito (Zenodo, Hugging Face), licencia | Qué declara el proyecto que registra, aunque no se vea en la salida |
| **3. Material suplementario y datos depositados** | Tablas de resultados, conjuntos de datos publicados, apéndices | Campos presentes en los datos que acompañan a la publicación |
| **4. Artículo** | Apartado de métodos y declaraciones de los autores | Lo que el equipo afirma que hace |

### Anexo C · Herramienta de cada paso

| Paso | Herramienta | Qué deja |
|---|---|---|
| Consulta a OpenAlex | `scripts/buscar_openalex.py` | Respuesta en bruto, BibTeX, conteos por término, recuperación del conjunto semilla y `registro.md` de la corrida |
| Consulta a Scopus | **Manual.** *Advanced document search* y exportación en CSV con resumen y palabras clave | Cadena literal, fecha de ejecución y el CSV exportado |
| Fusión y deduplicación | `scripts/fusionar.py` | Corpus único por DOI y, si falta, por título normalizado; cifras de identificación para el diagrama PRISMA |
| Cribado por título y resumen | Instrucciones fijas a la IA, decisiones del autor (§6.6) | Propuesta sin modificar, decisiones y motivos |
| Metadatos y BibTeX desde Crossref | `scripts/verificar_crossref.py` | Informe de verificación de cada DOI contra Crossref: coincidencia de título, año, publicación y páginas |
| *Snowballing* | Pendiente, con `referenced_works` y `cited_by` de OpenAlex | Se publicará con su corrida |
