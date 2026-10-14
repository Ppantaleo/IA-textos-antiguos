#!/usr/bin/env python3
"""Regenera el contenido público del repositorio desde la carpeta de trabajo.

La carpeta de trabajo (`01-research/`) es la fuente única; este repositorio es
su proyección auditable. Se publica solo la corrida en vigor (v1): el piloto
(v0) sirvió para calibrar la cadena y no sostiene ningún resultado.

Uso:
  python3 scripts/preparar_repositorio.py [ruta a 01-research]
"""

import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
TRABAJO = Path(sys.argv[1]) if len(sys.argv) > 1 else REPO.parent / "01-research"
BUSQUEDA = TRABAJO / "busqueda"

CORRIDA = "v1"          # corrida de OpenAlex en vigor
SCOPUS = "scopus-v1"    # carpeta de la exportación de Scopus en vigor
FUSION = "fusion-v1"    # fusión de ambas


def copiar(origen, destino):
    assert origen.exists(), f"No existe {origen}"
    destino.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(origen, destino)
    mb = destino.stat().st_size / 1e6
    print(f"  {destino.relative_to(REPO)}  ({mb:.1f} MB)" if mb >= 1
          else f"  {destino.relative_to(REPO)}")


def main():
    assert BUSQUEDA.is_dir(), f"No se encuentra {BUSQUEDA}"

    print("Scripts:")
    for n in ("buscar_openalex.py", "fusionar.py"):
        copiar(BUSQUEDA / n, REPO / "scripts" / n)

    print("Cadenas de búsqueda:")
    copiar(BUSQUEDA / "consultas" / f"{CORRIDA}.json", REPO / "consultas" / f"{CORRIDA}.json")
    copiar(BUSQUEDA / "consultas" / f"{SCOPUS}.txt", REPO / "consultas" / f"{SCOPUS}.txt")

    print("Registros de corrida:")
    copiar(BUSQUEDA / "corridas" / CORRIDA / "registro.md", REPO / "registros" / f"{CORRIDA}.md")
    copiar(BUSQUEDA / "corridas" / FUSION / "registro.md", REPO / "registros" / f"{FUSION}.md")

    print("Datos en bruto:")
    copiar(BUSQUEDA / "corridas" / CORRIDA / "crudo.jsonl",
           REPO / "datos" / "bruto" / "openalex-v1.jsonl")
    exportaciones = list((BUSQUEDA / "corridas" / SCOPUS).glob("*.csv"))
    assert len(exportaciones) == 1, exportaciones
    copiar(exportaciones[0], REPO / "datos" / "bruto" / "scopus-v1.csv")

    print("Corpus fusionado:")
    copiar(BUSQUEDA / "corridas" / FUSION / "cribado.csv", REPO / "datos" / "corpus-v1.csv")
    copiar(BUSQUEDA / "corridas" / FUSION / "cribado.bib", REPO / "datos" / "corpus-v1.bib")

    print("Cribado:")
    for n in ("instrucciones-cribado-ia.md", "decisiones.csv",
              "propuesta-ia-v1.csv", "propuesta-ia-v1.1.csv"):
        copiar(BUSQUEDA / "cribado" / n, REPO / "cribado" / n)

    print("Documentación:")
    copiar(TRABAJO / "proyecto.qmd", REPO / "docs" / "proyecto.md")
    print("  docs/indice-tfm.md  (se mantiene a mano, no se regenera)")

    print("Opcionales (si ya existen):")
    for nombre, destino in (("proyectos.csv", "datos/proyectos.csv"),
                            ("charting.csv", "datos/charting.csv")):
        p = BUSQUEDA / nombre
        if p.exists():
            copiar(p, REPO / destino)


if __name__ == "__main__":
    main()
