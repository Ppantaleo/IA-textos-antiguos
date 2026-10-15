# Materiales auditables del TFM sobre IA y textos antiguos

Repositorio de código y datos del trabajo de fin de máster **"Aplicaciones de
inteligencia artificial a la restauración e interpretación de textos antiguos:
hacia un marco de metadatos y preservación digital de sus resultados"**.

Autor: Patricio Iván Pantaleo ([ORCID 0000-0002-8104-8975](https://orcid.org/0000-0002-8104-8975)).
Máster Universitario en Bibliotecas, Archivos y Continuidad Digital,
Universidad Carlos III de Madrid. Director: Ricardo Eito Brun.

El trabajo es una **revisión de alcance** conforme a PRISMA-ScR. Este
repositorio existe para que cualquier lector pueda comprobar cómo se
construyó el corpus: con qué cadenas, en qué fechas, con qué criterios y con
qué decisiones. El protocolo completo está en [`docs/proyecto.md`](docs/proyecto.md), con su versión para imprimir en [`docs/proyecto.pdf`](docs/proyecto.pdf).

Repositorio: <https://github.com/Ppantaleo/IA-textos-antiguos>

## Contenido

| Carpeta | Qué hay |
|---|---|
| `scripts/` | Búsqueda en OpenAlex, fusión con Scopus, deduplicación, cuaderno de revisión del cribado, verificación de la bibliografía contra Crossref y preparación de este repositorio |
| `consultas/` | Las cadenas de búsqueda en vigor, una por fuente |
| `registros/` | Registro de la corrida de OpenAlex y de la fusión: fecha, cifras, duplicados, recuperación del conjunto semilla. Y el informe de verificación de la bibliografía |
| `datos/bruto/` | Lo recuperado tal como lo devolvió cada fuente, sin tocar |
| `datos/` | Corpus único tras la deduplicación, en CSV y en BibTeX |
| `cribado/` | Instrucciones del cribado asistido, propuesta de la IA sin modificar y decisiones del autor |
| `docs/` | Documento de proyecto, índice tentativo de la memoria y bibliografía. Es la versión viva: se edita aquí |
| `impresion/` | Plantilla LaTeX y guion de composición de los PDF de `docs/` |

Se publica **solo la corrida en vigor (v1)**. El piloto (v0) sirvió para
calibrar la cadena de búsqueda y no sostiene ningún resultado; queda en la
carpeta de trabajo del autor.

En `cribado/` conviven dos estados de la misma propuesta, y los dos son parte
del registro: `propuesta-ia-v1.csv` es la propuesta original sin modificar, tal
como la exige el protocolo, y `propuesta-ia-v1.1.csv` es la misma propuesta
tras aplicar las enmiendas EN1 a EN4, con las columnas que indican qué cambió.

## Reproducir la búsqueda

Requiere Python 3.11 o posterior. No hay dependencias externas: solo biblioteca
estándar.

```bash
python3 scripts/buscar_openalex.py v1          # consulta la API y escribe la corrida
python3 scripts/fusionar.py v1 scopus-v1 fusion-v1 "2026-09-14"
python3 scripts/verificar_crossref.py          # comprueba la bibliografía contra Crossref
python3 scripts/preparar_revision.py           # rehace el cuaderno de revisión del cribado
```

`preparar_revision.py` requiere openpyxl y reproduce el cuaderno en blanco:
las mismas 803 filas, con la muestra del 10 % de exclusiones sorteada con
semilla fija. La copia que el autor rellena no se publica; sus decisiones
acaban en `cribado/decisiones.csv`.

Los *scripts* de `scripts/` son copia literal de los que se ejecutan en la
carpeta de trabajo y esperan su estructura (`consultas/`, `corridas/<nombre>/`)
junto al archivo. Para reejecutarlos, basta con copiarlos a un directorio que
tenga `consultas/` al lado. Los documentos de `docs/`, en cambio, se editan
aquí; `bash impresion/compilar.sh` rehace sus PDF cuando hace falta.

La consulta a OpenAlex es reproducible y gratuita; las cifras pueden variar
ligeramente respecto de las registradas, porque la base se actualiza a diario.
Cada corrida deja su propio `registro.md` con la fecha y los conteos del día.

La consulta a Scopus se ejecuta a mano en *Advanced document search* con la
cadena de `consultas/scopus-v1.txt` y se exporta en CSV con resumen y palabras
clave. Requiere acceso institucional.

## Sobre los datos en bruto

Se publican sin recortes, porque sin ellos la auditoría se queda en la palabra
del autor: `datos/bruto/openalex-v1.jsonl` (lo que devolvió la API, 11,5 MB) y
`datos/bruto/scopus-v1.csv` (la exportación manual, 3,1 MB).

> **Advertencia sobre Scopus.** Esa exportación procede de una base de
> suscripción (Elsevier) y sus condiciones de uso no contemplan la
> redistribución. Se publica para hacer auditable el relevamiento, en la
> cantidad mínima necesaria para ello y sin ánimo de lucro. Si Elsevier lo
> requiere, se sustituirá por la lista de identificadores (DOI y título) con la
> que cualquier persona con acceso institucional puede reconstruirla.

## Uso de inteligencia artificial

El relevamiento usa un asistente de IA (Claude, de Anthropic) para consultar
APIs, escribir los *scripts* y **proponer** una decisión de cribado por
registro. La propuesta no es una decisión: el autor revisa todas las
inclusiones, los dudosos y las revisiones, y una muestra aleatoria de las
exclusiones. El alcance exacto del uso está declarado en el apartado 8 de
[`docs/proyecto.md`](docs/proyecto.md); las instrucciones que recibió el modelo,
en [`cribado/instrucciones-cribado-ia.md`](cribado/instrucciones-cribado-ia.md).

Se publica la propuesta sin modificar junto a las decisiones del autor, por el
mismo motivo que el trabajo estudia: una salida de modelo debería viajar con el
registro de qué la produjo, con qué instrucciones y quién la validó.

## Licencias

Código, MIT (`LICENSE`). Datos y documentación, CC BY 4.0
(`LICENSE-datos.md`).
