#!/usr/bin/env python3
"""Regenera el contenido público del repositorio desde la carpeta de trabajo.

La carpeta de trabajo (`01-research/`) es la fuente única; este repositorio es
su proyección auditable. El script copia los scripts, las cadenas de búsqueda y
los registros de cada corrida, y reduce las tablas de cribado para no
redistribuir resúmenes (ver LICENSE-datos.md).

Uso:
  python3 scripts/preparar_repositorio.py [ruta a 01-research]
"""

import csv
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
TRABAJO = Path(sys.argv[1]) if len(sys.argv) > 1 else REPO.parent / "01-research"
BUSQUEDA = TRABAJO / "busqueda"

# Columnas que nunca se publican: provienen en parte de Scopus
VETADAS = {"resumen", "abstract", "palabras_clave"}


def copiar(origen, destino):
    destino.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(origen, destino)
    print(f"  {destino.relative_to(REPO)}")


def reducir_csv(origen, destino):
    """Copia un CSV sin las columnas vetadas."""
    with open(origen, newline="") as f:
        filas = list(csv.DictReader(f))
    campos = [c for c in filas[0] if c not in VETADAS]
    destino.parent.mkdir(parents=True, exist_ok=True)
    with open(destino, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=campos, extrasaction="ignore")
        w.writeheader()
        w.writerows(filas)
    print(f"  {destino.relative_to(REPO)}  ({len(filas)} filas, "
          f"{len(filas[0]) - len(campos)} columnas omitidas)")


def main():
    assert BUSQUEDA.is_dir(), f"No se encuentra {BUSQUEDA}"

    print("Scripts:")
    for n in ("buscar_openalex.py", "fusionar.py"):
        copiar(BUSQUEDA / n, REPO / "scripts" / n)

    print("Cadenas de búsqueda:")
    for p in sorted((BUSQUEDA / "consultas").iterdir()):
        copiar(p, REPO / "consultas" / p.name)

    print("Registros de corrida:")
    for p in sorted(BUSQUEDA.glob("corridas/*/registro.md")):
        copiar(p, REPO / "registros" / f"{p.parent.name}.md")

    print("Cribado:")
    copiar(BUSQUEDA / "cribado" / "instrucciones-cribado-ia.md",
           REPO / "cribado" / "instrucciones-cribado-ia.md")
    copiar(BUSQUEDA / "cribado" / "decisiones.csv", REPO / "cribado" / "decisiones.csv")
    for n in ("propuesta-ia-v1.csv", "propuesta-ia-v1.1.csv"):
        reducir_csv(BUSQUEDA / "cribado" / n, REPO / "cribado" / n)

    print("Corpus:")
    reducir_csv(BUSQUEDA / "corridas" / "fusion-v1" / "cribado.csv",
                REPO / "datos" / "corpus-v1.csv")

    print("Documentación:")
    copiar(TRABAJO / "proyecto.qmd", REPO / "docs" / "proyecto.md")
    copiar(TRABAJO / "decisiones.md", REPO / "docs" / "decisiones.md")

    for opcional, destino in (("proyectos.csv", "datos/proyectos.csv"),
                              ("charting.csv", "datos/charting.csv")):
        p = BUSQUEDA / opcional
        if p.exists():
            copiar(p, REPO / destino)


if __name__ == "__main__":
    main()
