# Fusión `fusion-piloto-v0`

- **Fecha de fusión:** 2026-09-14T07:17:05
- **OpenAlex:** corrida `piloto-v0` (ver `corridas/piloto-v0/registro.md`)
- **Scopus:** `scopus-piloto-v0/scopus_export_Sep 14-2026_15a00c01-8614-444f-9915-1aec0844de3e.csv`. Cadena: `consultas/scopus-piloto-v0.txt`. Exportación manual del 2026-09-14, solo documentos: la pestaña de preprints de Scopus no se exportó.
- **Deduplicación:** por DOI y, si falta, por título normalizado.

## Identificación (PRISMA-ScR)

| Paso | Registros |
|---|---|
| Recuperados en OpenAlex | 1766 |
| Recuperados en Scopus | 1101 |
| **Total identificados** | **2867** |
| Duplicados internos de OpenAlex | 330 |
| Duplicados internos de Scopus | 2 |
| Duplicados entre fuentes | 704 |
| **Registros únicos para cribado** | **1831** |

## Aporte de cada fuente

- Solo en OpenAlex: 732
- Solo en Scopus: 395
- En ambas: 704
- Registros sin resumen tras la fusión: 78

## Recuperación del seed set

| Clave | OpenAlex | Scopus |
|---|---|---|
| assael2022ithaca | sí | sí |
| assael2025aeneas | sí | sí |
| popovic2025enoch | sí | sí |
| dhali2026binet | sí | sí |
| murugan2024drlift | **NO** | sí |
| papavassileiou2023linearb | sí | sí |
| gutherz2023akkadian | sí | sí |
| levine2024lacuna | **NO** | **NO** |
| pinillabuitrago2022maya | **NO** | **NO** |
| sommerschield2023survey | sí | sí |

**Recuperados por al menos una fuente: 8/10**

## Tipos documentales

Tipo de Scopus cuando existe; si no, el de OpenAlex (normalizado a minúsculas). Tipos como *conference-review* (presentación de un volumen de actas), *Erratum* o *Retracted* se revisan en el cribado; no se eliminaron automáticamente.

| Tipo | Registros |
|---|---|
| article | 807 |
| conference-paper | 572 |
| preprint | 176 |
| book-chapter | 67 |
| conference-review | 44 |
| dataset | 36 |
| review | 20 |
| software | 17 |
| dissertation | 16 |
| book | 16 |
| other | 15 |
| data-paper | 8 |
| editorial | 8 |
| note | 7 |
| report | 6 |
| conference-abstract | 4 |
| retracted | 4 |
| erratum | 3 |
| paratext | 2 |
| letter | 1 |
| supplementary-materials | 1 |
| reference-entry | 1 |
