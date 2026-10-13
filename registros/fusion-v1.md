# Fusión `fusion-v1`

- **Fecha de fusión:** 2026-09-14T09:04:43
- **OpenAlex:** corrida `v1` (ver `corridas/v1/registro.md`)
- **Scopus:** `scopus-v1/scopus_export_Sep 14-2026_83eff27e-c70d-4c47-bdb6-8a0ca484c245.csv`. Cadena: `consultas/scopus-v1.txt`. Ejecución y exportación manual: 2026-09-14 09:03 (hora local del archivo exportado, con Abstract & keywords; 935 resultados según Scopus). Solo documentos: la pestaña de preprints de Scopus no se exportó.
- **Deduplicación:** por DOI y, si falta, por título normalizado.

## Identificación (PRISMA-ScR)

| Paso | Registros |
|---|---|
| Recuperados en OpenAlex | 1555 |
| Recuperados en Scopus | 935 |
| **Total identificados** | **2490** |
| Duplicados internos de OpenAlex | 302 |
| Duplicados internos de Scopus | 1 |
| Duplicados entre fuentes | 596 |
| **Registros únicos para cribado** | **1591** |

## Aporte de cada fuente

- Solo en OpenAlex: 657
- Solo en Scopus: 338
- En ambas: 596
- Registros sin resumen tras la fusión: 70

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

## Decisiones de cribado aplicadas

Tomadas de `cribado/decisiones.csv`. excluir: 44
Pendientes de cribar: 1547

## Tipos documentales

Tipo de Scopus cuando existe; si no, el de OpenAlex (normalizado a minúsculas). Tipos como *conference-review* (presentación de un volumen de actas), *Erratum* o *Retracted* se revisan en el cribado; no se eliminaron automáticamente.

| Tipo | Registros |
|---|---|
| article | 707 |
| conference-paper | 469 |
| preprint | 156 |
| book-chapter | 74 |
| conference-review | 34 |
| dataset | 31 |
| other | 18 |
| review | 18 |
| book | 15 |
| software | 15 |
| dissertation | 13 |
| editorial | 7 |
| note | 7 |
| data-paper | 6 |
| report | 6 |
| conference-abstract | 4 |
| retracted | 3 |
| erratum | 2 |
| paratext | 2 |
| letter | 1 |
| supplementary-materials | 1 |
| book-review | 1 |
| reference-entry | 1 |
