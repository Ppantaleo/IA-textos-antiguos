# Materiales auditables del TFM sobre IA y textos antiguos

Repositorio de código y datos del trabajo de fin de máster **"Relevamiento de
aplicaciones con inteligencia artificial en la restauración e interpretación de
textos antiguos: hacia un marco de metadatos y preservación digital de sus
resultados"**.

Autor: Patricio Iván Pantaleo ([ORCID 0000-0002-8104-8975](https://orcid.org/0000-0002-8104-8975)).
Máster Universitario en Bibliotecas, Archivos y Continuidad Digital,
Universidad Carlos III de Madrid. Director: Ricardo Eito Brun.

El trabajo es una **revisión de alcance** conforme a PRISMA-ScR. Este
repositorio existe para que cualquier lector pueda comprobar cómo se
construyó el corpus: con qué cadenas, en qué fechas, con qué criterios y con
qué decisiones. El protocolo completo está en [`docs/proyecto.md`](docs/proyecto.md).

## Contenido

| Carpeta | Qué hay |
|---|---|
| `scripts/` | Búsqueda en OpenAlex, fusión con Scopus, deduplicación y preparación de este repositorio |
| `consultas/` | Cadenas de búsqueda, una por versión y por fuente. No se sobrescriben |
| `registros/` | Registro de cada corrida: fecha, cifras, duplicados, recuperación del conjunto semilla |
| `cribado/` | Instrucciones del cribado asistido, propuesta de la IA sin modificar y decisiones del autor |
| `datos/` | Corpus único tras la deduplicación |
| `docs/` | Protocolo y registro de decisiones |

## Reproducir la búsqueda

Requiere Python 3.11 o posterior. No hay dependencias externas: solo biblioteca
estándar.

```bash
python3 scripts/buscar_openalex.py v1          # consulta la API y escribe la corrida
python3 scripts/fusionar.py v1 scopus-v1 fusion-v1 "2026-09-14"
```

Los *scripts* son copia literal de los que se ejecutan en la carpeta de
trabajo y esperan su estructura (`consultas/`, `corridas/<nombre>/`) junto al
archivo. Para reejecutarlos, basta con copiarlos a un directorio que tenga
`consultas/` al lado.

La consulta a OpenAlex es reproducible y gratuita; las cifras pueden variar
ligeramente respecto de las registradas, porque la base se actualiza a diario.
Cada corrida deja su propio `registro.md` con la fecha y los conteos del día.

La consulta a Scopus se ejecuta a mano en *Advanced document search* con la
cadena de `consultas/scopus-v1.txt` y se exporta en CSV con resumen y palabras
clave. Requiere acceso institucional.

## Qué no está aquí, y por qué

- **La exportación en bruto de Scopus.** Las condiciones de uso de la base no
  permiten redistribuirla. Se publican la cadena, la fecha, las cifras y los
  identificadores necesarios para reconstruirla.
- **La columna de resumen** de las tablas de cribado, por la misma razón: parte
  de los resúmenes procede de Scopus.
- **Los datos en bruto de OpenAlex** (`crudo.jsonl`, unos 11 MB). Se regeneran
  con el script de búsqueda.

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
