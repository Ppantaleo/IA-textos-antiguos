# Instrucciones para el cribado asistido por IA (título y resumen)

Versión 1.1 · 2026-09-14 (v1 más las aclaraciones EN1–EN4) · Protocolo: `proyecto-tfm.md` §5.1, §5.6, §7.1;
`decisiones.md` D12–D14.

Este texto se entrega sin cambios a cada instancia de Claude que propone
decisiones. Es parte del registro metodológico.

## Contexto

TFM de archivística: *scoping review* (PRISMA-ScR) sobre aplicaciones de
inteligencia artificial a la restauración e interpretación de **textos
antiguos**. Más adelante se analizarán los metadatos de proveniencia de sus
salidas. En esta fase solo se decide si cada registro pasa a lectura de texto
completo.

## Preguntas

Responder en orden. El primer "no" claro determina el código de exclusión.

- **C1 · IA aplicada al material.** ¿Aplica un proceso de IA (aprendizaje
  automático, redes neuronales, visión por computador, modelos de lenguaje,
  clustering, etc.) a la lectura o interpretación de material escrito,
  incluido el análisis de su materialidad (tinta, soporte, escritura a mano)?
  Si no → **E1**. También es E1 un ensayo, opinión o marco teórico sobre IA y
  patrimonio sin aplicación, o una digitalización o catalogación sin IA.
- **C2 · Producto digital.** ¿Resulta un producto digital (texto restaurado,
  transcripción, traducción, atribución o datación, modelo, dataset, imagen
  procesada, herramienta)? Casi toda aplicación real lo cumple. Si no → **E2**.
- **C3 · Texto antiguo.** ¿El material son textos antiguos? Definición
  (Sommerschield et al. 2023): obras compuestas en lenguas y escrituras en uso
  desde el origen de la escritura (3400 a. C.) **hasta finales del primer
  milenio d. C.**, en cualquier lengua, escritura o soporte. **Se fecha la
  obra, no el soporte.** Una copia medieval de una obra antigua entra; una
  obra compuesta después del corte no entra, aunque use una lengua de origen
  antiguo. Si el material es escrito pero posterior → **E3**.
- **C4 · Corpus mixto.** Si el corpus mezcla textos anteriores y posteriores
  al corte, ¿trabaja **principalmente** con los anteriores? Si claramente no →
  **E4**.

## Otros códigos

- **E5:** sin estudio primario (editorial, fe de erratas, retractación,
  presentación o índice de un volumen de actas, prefacio, reseña de libro).
- **E6:** tema ajeno. El registro entró por coincidencia léxica y no trata de
  material escrito (p. ej., "inscription" en sentido no textual, arte rupestre
  sin escritura, cerámica, biología, ingeniería).
- **R:** revisión, *survey* o estado del arte **pertinente** (IA y textos
  antiguos, escrituras antiguas, epigrafía, papirología, HTR de documentos
  antiguos). No entra en el corpus; se usa para *snowballing*.
- **I:** incluir. Cumple C1–C4.
- **D:** dudoso. La información no alcanza para decidir; pasa a texto completo.

## Regla de duda

**Ante la duda, D, no exclusión.** Solo se excluye si el título y el resumen
permiten afirmarlo. Si falta el resumen y el título no basta, D.

## Orientaciones para casos frecuentes

- **Entran por C3:** egipcio (jeroglífico, hierático, demótico), cuneiforme
  (sumerio, acadio, hitita), lineal A y B, griego y latín antiguos, papiros,
  rollos del mar Muerto, Herculano, hebreo y arameo antiguos, copto (obras
  antiguas), maya clásico (250–900), inscripciones de oráculo y bronces chinos,
  tiras de bambú, brāhmī, inscripciones del Indo, rúnico antiguo (Elder
  Futhark), túrquico antiguo (Orjón, s. VIII), la Biblia y el Corán como obras
  (aunque el manuscrito sea posterior), textos canónicos sánscritos y pali
  compuestos en la Antigüedad.
- **No entran (E3):** manuscritos árabes, otomanos, persas o hebreos de obras
  medievales o modernas; latín medieval; textos litúrgicos o documentales
  medievales; documentos notariales; cifrados históricos; Voynich; códices
  mexicas o posclásicos; inscripciones tamiles cholas (s. X–XIII) o
  posteriores; documentos de archivo modernos; imprenta antigua.
- **Chino:** "ancient Chinese characters" referido a hueso oracular, bronce o
  bambú entra; "ancient books" (古籍) sin precisar suele ser Ming o Qing, así
  que D si no hay más datos, y E3 si el resumen deja claro que es tardío.
  Corpus de chino clásico que abarcan todas las dinastías → C4, normalmente D
  salvo que el resumen aclare el periodo.
- **Inscripciones sin fecha** ("ancient Tamil/Kannada/Telugu inscriptions",
  "stone inscriptions") → D, salvo que se indique la época.
- **Datasets y software:** si están hechos para o con IA sobre textos
  antiguos → I o D. Si son solo digitalización sin IA → E1.
- **Tesis doctorales, capítulos y preprints** se evalúan igual que los
  artículos.
- **Metadatos, proveniencia o preservación sin IA:** E1, pero en `nota`
  escribir "posible marco teórico".

## Aclaraciones v1.1 (enmiendas EN1–EN4 del protocolo, 2026-09-14)

- **EN1 · C1 exige aprendizaje.** Solo cuentan como IA los métodos basados en
  aprendizaje: aprendizaje automático, redes neuronales, LLM, clustering,
  modelos entrenados. El procesamiento de señal o imagen clásico sin
  aprendizaje (filtros, operadores, detección de bordes), la estadística, la
  entropía, la lógica difusa o el alineamiento de secuencias (p. ej.,
  Needleman-Wunsch) → **E1**. Si el resumen no deja claro si hay aprendizaje →
  D.
- **EN2 · Material antiguo real.** Una escritura antigua sin material antiguo
  real (datasets escritos a mano por participantes actuales, glifos generados
  desde fuentes Unicode, latín de estudiantes) → **E3**. Los datos sintéticos
  valen como entrenamiento **si** el modelo se evalúa o aplica sobre textos
  antiguos reales → puede ser I.
- **EN3 · Tarea dirigida al texto o al testimonio.** Fechar la obra vale para
  las tareas dirigidas al texto (transcripción/HTR, restauración, traducción,
  crítica textual, intertextualidad, clasificación de contenido). Si la tarea
  se dirige al **testimonio material posterior al corte** (identificar
  copistas, datar el manuscrito, analizar decoración, maquetación o
  materialidad del códice medieval o moderno) → **E3**, aunque la obra copiada
  sea antigua. Si el testimonio es antiguo (papiros, rollos del mar Muerto,
  tiras de bambú, hueso oracular), estas tareas sí entran.
- **EN4 · Retractados.** Un artículo retractado → **E5**, con la nota
  "retractado".

## Formato de salida

CSV con cabecera, UTF-8 y comillas estándar:

```
clave,decision,codigo,motivo,confianza,nota
```

- `decision`: `incluir` | `excluir` | `dudoso` | `revision`
- `codigo`: `I` | `D` | `E1`…`E6` | `R`
- `motivo`: en español, máximo 25 palabras, concreto (qué material, qué IA,
  qué época).
- `confianza`: `alta` | `media` | `baja`
- `nota`: opcional (p. ej., "posible marco teórico", "retractado").

Una fila por registro, con todas las claves del lote y sin inventar claves.
