# Corrida `piloto-v0`

- **Fecha de ejecución:** 2026-09-14T06:28:07
- **Fuente:** OpenAlex API (`/works`), campo `title_and_abstract.search`
- **Ventana:** 2022–2026 (`publication_year`)
- **Propósito:** PILOTO. No es la cadena del protocolo: sirve para medir el ruido de cada término y comprobar si se recupera el seed set. La cadena definitiva la decide el autor.

## Cadena

```
("artificial intelligence" OR "machine learning" OR "deep learning" OR "neural network" OR "computer vision" OR "language model") AND ("ancient text" OR "ancient script" OR "ancient language" OR "ancient manuscript" OR "historical manuscript" OR epigraphy OR inscription OR papyrus OR papyri OR "Dead Sea Scrolls" OR Herculaneum OR cuneiform OR "Linear B" OR hieroglyph OR khipu OR quipu OR "palm leaf" OR palaeography OR paleography)
```

## Conteos

- Registros según la API (`meta.count`): 1764
- Registros descargados: **1766** (anotado a posteriori; el conteo varía levemente al paginar y para PRISMA vale este)
- Duplicados eliminados (DOI o título): 333
- Registros únicos para cribado: **1433**
- Sin resumen en OpenAlex: 233
- Por tipo: article: 638, conference-paper: 396, preprint: 194, book-chapter: 65, dataset: 36, other: 21, software: 17, dissertation: 16, book: 14, data-paper: 9, editorial: 6, report: 6, conference-abstract: 5, review: 3, erratum: 2, paratext: 2, reference-entry: 1, retraction: 1, supplementary-materials: 1
- Costo de la corrida en la API: USD 0.035

## Recuperación del seed set

| Clave | DOI | ¿Recuperado? |
|---|---|---|
| assael2022ithaca | 10.1038/s41586-022-04448-z | sí |
| assael2025aeneas | 10.1038/s41586-025-09292-5 | sí |
| popovic2025enoch | 10.1371/journal.pone.0323185 | sí |
| dhali2026binet | 10.1007/978-3-032-09371-4_11 | sí |
| murugan2024drlift | 10.1186/s40494-024-01522-9 | **NO** |
| papavassileiou2023linearb | 10.1145/3593431 | sí |
| gutherz2023akkadian | 10.1093/pnasnexus/pgad096 | sí |
| levine2024lacuna | 10.18653/v1/2024.ml4al-1.8 | **NO** |
| pinillabuitrago2022maya | 10.1016/j.eswa.2022.116983 | **NO** |
| sommerschield2023survey | 10.1162/coli_a_00481 | sí |

**Recall: 7/10**

## Aporte de cada término

Registros que recupera cada término combinado con los demás bloques completos. Un conteo muy alto señala ruido; uno igual a 0, que el término sobra.

| Bloque | Término | Registros |
|---|---|---|
| IA | `"artificial intelligence"` | 485 |
| IA | `"machine learning"` | 423 |
| IA | `"deep learning"` | 564 |
| IA | `"neural network"` | 481 |
| IA | `"computer vision"` | 123 |
| IA | `"language model"` | 347 |
| textos antiguos | `"ancient text"` | 240 |
| textos antiguos | `"ancient script"` | 118 |
| textos antiguos | `"ancient language"` | 112 |
| textos antiguos | `"ancient manuscript"` | 106 |
| textos antiguos | `"historical manuscript"` | 174 |
| textos antiguos | `epigraphy` | 56 |
| textos antiguos | `inscription` | 592 |
| textos antiguos | `papyrus` | 75 |
| textos antiguos | `papyri` | 64 |
| textos antiguos | `"Dead Sea Scrolls"` | 32 |
| textos antiguos | `Herculaneum` | 44 |
| textos antiguos | `cuneiform` | 143 |
| textos antiguos | `"Linear B"` | 72 |
| textos antiguos | `hieroglyph` | 94 |
| textos antiguos | `khipu` | 8 |
| textos antiguos | `quipu` | 16 |
| textos antiguos | `"palm leaf"` | 122 |
| textos antiguos | `palaeography` | 24 |
| textos antiguos | `paleography` | 95 |
