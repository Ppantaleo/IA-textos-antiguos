#!/usr/bin/env bash
# Compone los PDF de lectura e impresión con pandoc y XeLaTeX.
# Fuentes y salidas en docs/. Solo se ejecuta a mano, cuando hace falta un PDF
# nuevo: los .md de docs/ son la versión viva.
# Uso: bash impresion/compilar.sh   (desde la raíz del repositorio)
set -euo pipefail
cd "$(dirname "$0")/.."

FECHA=$(LC_TIME=es_ES.UTF-8 date '+%-d de %B de %Y')
comun=(
  --from=markdown+smart
  --pdf-engine=xelatex
  --include-in-header=impresion/preambulo.tex
  --shift-heading-level-by=-1
  --standalone
  -V documentclass=article
  -V papersize=a4
  -V geometry:margin=2.6cm
  -V fontsize=11pt
  -V lang=es
  -V linestretch=1.12
  -V colorlinks=true
  -V linkcolor=acento
  -V urlcolor=acento
  -V toccolor=black
  -V date="$FECHA"
)

# El título, el subtítulo y los autores se leen de la cabecera YAML del origen:
# para cambiarlos se edita el Markdown, no este script.
# componer <origen> <destino.pdf> <pie> <índice: si|no>
componer() {
  local origen=$1 destino=$2 pie=$3 indice=$4
  local cabecera cuerpo
  cabecera=$(mktemp /tmp/cabecera-XXXX.tex)
  cuerpo=$(mktemp /tmp/cuerpo-XXXX.md)

  printf '\\renewcommand{\\documentoid}{%s}\n' "$pie" > "$cabecera"

  # El primer encabezado del origen es el título de la portada, y el apartado
  # "Título", redundante con ella: se quitan los dos antes de componer.
  awk '
    NR==1 && /^# / {next}                      # título, ya está en la portada
    /^## Título/ {sec=1; next} /^## / {sec=0}  # apartado "Título", redundante
    /^\*\*Relevamiento/ {par=1}                # título repetido en el cuerpo
    par && /^$/ {par=0; next}
    !sec && !par' "$origen" > "$cuerpo"

  local opciones=("${comun[@]}" --include-in-header="$cabecera")
  [[ $indice == si ]] && opciones+=(--toc --toc-depth=3)

  pandoc "$cuerpo" "${opciones[@]}" -o "$destino"
  rm -f "$cabecera" "$cuerpo"
  echo "  $destino"
}

componer docs/proyecto.md docs/proyecto.pdf \
  "Proyecto de TFM · P. I. Pantaleo" si

componer docs/indice-tfm.md docs/indice-tfm.pdf \
  "Índice tentativo · P. I. Pantaleo" no
