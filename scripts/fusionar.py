#!/usr/bin/env python3
"""Fusiona una corrida de OpenAlex con una exportación CSV de Scopus.

Deduplica por DOI y, si falta, por título normalizado. Genera en
corridas/<salida>/:

  registro.md     conteos por fuente, solapamiento, recuperación del seed set
                  y cifras de identificación para el diagrama PRISMA-ScR
  cribado.csv     un registro único por fila, con la fuente de origen y
                  columnas vacías para decisión y motivo
  cribado.bib     BibTeX (entradas de OpenAlex, más las que solo están en
                  Scopus)

Uso:
  python3 fusionar.py piloto-v0 scopus-piloto-v0 fusion-piloto-v0 "2026-09-14"
  (el 4.º argumento es la fecha y hora de ejecución en Scopus)
"""

import csv
import datetime as dt
import glob
import json
import re
import sys
from collections import Counter
from pathlib import Path

from buscar_openalex import bibtex, clave, doi_corto, esc, norm_titulo, resumen

BASE = Path(__file__).resolve().parent
CORRIDAS = BASE / "corridas"


def cargar_openalex(nombre):
    with open(CORRIDAS / nombre / "crudo.jsonl") as f:
        return [json.loads(l) for l in f]


def cargar_scopus(carpeta):
    archivos = glob.glob(str(CORRIDAS / carpeta / "*.csv"))
    assert len(archivos) == 1, f"Se esperaba un CSV en {carpeta}, hay {len(archivos)}"
    with open(archivos[0], encoding="utf-8-sig") as f:
        return list(csv.DictReader(f)), Path(archivos[0]).name


def claves_de(doi, titulo):
    c = set()
    if doi:
        c.add("doi:" + doi.lower())
    t = norm_titulo(titulo)
    if t:
        c.add("t:" + t)
    return c


def bib_scopus(r, k):
    tipo = r.get("Document Type", "")
    if tipo in ("Conference paper", "Conference review"):
        et, vc = "inproceedings", "booktitle"
    elif tipo in ("Book chapter",):
        et, vc = "incollection", "booktitle"
    elif tipo == "Book":
        et, vc = "book", "publisher"
    else:
        et, vc = "article", "journal"
    paginas = "--".join(p for p in (r.get("Page start"), r.get("Page end")) if p)
    abstract = r.get("Abstract", "")
    if abstract.startswith("[No abstract"):
        abstract = ""
    campos = [
        ("title", "{" + esc(r.get("Title")) + "}"),
        ("author", " and ".join(esc(a.strip()) for a in r.get("Authors", "").split(";") if a.strip())),
        (vc, esc(r.get("Source title"))),
        ("year", r.get("Year")),
        ("volume", r.get("Volume")),
        ("number", r.get("Issue")),
        ("pages", paginas),
        ("doi", (r.get("DOI") or "").lower()),
        ("url", r.get("Link")),
        ("abstract", esc(abstract)),
        ("keywords", esc("; ".join(x for x in (r.get("Author Keywords"), r.get("Index Keywords")) if x))),
        ("note", f"Scopus {r.get('EID')}; tipo: {tipo}"),
    ]
    cuerpo = ",\n".join(f"  {c} = {{{v}}}" for c, v in campos if v)
    return f"@{et}{{{k},\n{cuerpo}\n}}\n"


def main(oa_nombre, sc_carpeta, salida_nombre, sc_fecha="2026-09-14"):
    cfg = json.loads((BASE / "consultas" / f"{oa_nombre}.json").read_text())
    oa = cargar_openalex(oa_nombre)
    sc, sc_archivo = cargar_scopus(sc_carpeta)
    salida = CORRIDAS / salida_nombre
    salida.mkdir(parents=True, exist_ok=True)

    # Registros unificados: {claves, fuentes, oa, sc}
    registros = []
    indice = {}

    def agregar(claves, fuente, dato):
        existentes = {indice[c] for c in claves if c in indice}
        if existentes:
            reg = registros[min(existentes)]
            # Si un registro enlaza dos que estaban separados, se unen
            for i in sorted(existentes - {min(existentes)}):
                otro = registros[i]
                if otro is None:
                    continue
                reg["claves"] |= otro["claves"]
                reg["fuentes"] |= otro["fuentes"]
                reg["oa"] = reg["oa"] or otro["oa"]
                reg["sc"] = reg["sc"] or otro["sc"]
                registros[i] = None
            dup = fuente in reg["fuentes"]
        else:
            reg = {"claves": set(), "fuentes": set(), "oa": None, "sc": None}
            registros.append(reg)
            dup = False
        reg["claves"] |= claves
        reg["fuentes"].add(fuente)
        reg[fuente] = reg[fuente] or dato
        pos = registros.index(reg)
        for c in reg["claves"]:
            indice[c] = pos
        return dup

    dup_oa = sum(agregar(claves_de(doi_corto(w.get("doi")), w.get("title")), "oa", w) for w in oa)
    dup_sc = sum(agregar(claves_de(r.get("DOI"), r.get("Title")), "sc", r) for r in sc)
    unicos = [r for r in registros if r is not None]

    solo_oa = sum(1 for r in unicos if r["fuentes"] == {"oa"})
    solo_sc = sum(1 for r in unicos if r["fuentes"] == {"sc"})
    ambas = sum(1 for r in unicos if r["fuentes"] == {"oa", "sc"})

    # Seed set
    filas_seed = []
    for k, s in cfg["seed"].items():
        cl = claves_de(s["doi"], s["titulo"])
        reg = next((r for r in unicos if r["claves"] & cl), None)
        f = reg["fuentes"] if reg else set()
        filas_seed.append((k, "sí" if "oa" in f else "**NO**", "sí" if "sc" in f else "**NO**"))

    # Decisiones de cribado ya tomadas (cribado/decisiones.csv), por DOI o título
    decisiones = {}
    ruta_dec = BASE / "cribado" / "decisiones.csv"
    if ruta_dec.exists():
        with open(ruta_dec) as fd:
            for d in csv.DictReader(fd):
                for c in claves_de(d["doi"], d["titulo"]):
                    decisiones[c] = (d["decision"], d["motivo"])

    # Salidas
    usadas = set()
    aplicadas = Counter()
    tipos = Counter()
    with open(salida / "cribado.csv", "w", newline="") as fc, open(salida / "cribado.bib", "w") as fb:
        cw = csv.writer(fc)
        cw.writerow(["clave", "fuentes", "anio", "tipo", "titulo", "autores", "fuente_publicacion",
                     "doi", "resumen", "palabras_clave", "decision", "motivo"])
        fb.write(f"% Fusión {oa_nombre} (OpenAlex) + {sc_carpeta} (Scopus), {dt.date.today()}\n\n")

        def orden(r):
            anio = (r["oa"] or {}).get("publication_year") or int((r["sc"] or {}).get("Year") or 0)
            titulo = (r["oa"] or {}).get("title") or (r["sc"] or {}).get("Title") or ""
            return (-anio, titulo.lower())

        for r in sorted(unicos, key=orden):
            w, s = r["oa"], r["sc"]
            fuentes = "+".join(sorted({"oa": "OpenAlex", "sc": "Scopus"}[x] for x in r["fuentes"]))
            if w:
                k = clave(w, usadas)
                src = ((w.get("primary_location") or {}).get("source") or {})
                abstract = resumen(w.get("abstract_inverted_index"))
                if not abstract and s and not s.get("Abstract", "").startswith("[No abstract"):
                    abstract = s.get("Abstract", "")
                tipo = (s or {}).get("Document Type") or w.get("type")
                fila = [k, fuentes, w.get("publication_year"), tipo, w.get("title"),
                        "; ".join(a["author"].get("display_name") or "" for a in (w.get("authorships") or [])),
                        src.get("display_name"), doi_corto(w.get("doi")), abstract,
                        "; ".join(x for x in ((s or {}).get("Author Keywords"), (s or {}).get("Index Keywords")) if x)]
                fb.write(bibtex(w, k) + "\n")
            else:
                pseudo = {"authorships": [{"author": {"display_name": s.get("Authors", "").split(";")[0].split(",")[0]}}],
                          "title": s.get("Title"), "publication_year": s.get("Year")}
                k = clave(pseudo, usadas)
                tipo = s.get("Document Type")
                abstract = "" if s.get("Abstract", "").startswith("[No abstract") else s.get("Abstract", "")
                fila = [k, fuentes, s.get("Year"), tipo, s.get("Title"), s.get("Authors"),
                        s.get("Source title"), (s.get("DOI") or "").lower(), abstract,
                        "; ".join(x for x in (s.get("Author Keywords"), s.get("Index Keywords")) if x)]
                fb.write(bib_scopus(s, k) + "\n")
            tipo = (tipo or "").lower().replace(" ", "-")
            fila[3] = tipo
            tipos[tipo] += 1
            dec = next((decisiones[c] for c in r["claves"] if c in decisiones), ("", ""))
            if dec[0]:
                aplicadas[dec[0]] += 1
            cw.writerow(fila + list(dec))

    sin_resumen = 0
    with open(salida / "cribado.csv") as fc:
        sin_resumen = sum(1 for f in csv.DictReader(fc) if not f["resumen"].strip())

    L = [
        f"# Fusión `{salida_nombre}`", "",
        f"- **Fecha de fusión:** {dt.datetime.now().isoformat(timespec='seconds')}",
        f"- **OpenAlex:** corrida `{oa_nombre}` (ver `corridas/{oa_nombre}/registro.md`)",
        f"- **Scopus:** `{sc_carpeta}/{sc_archivo}`. Cadena: `consultas/{sc_carpeta}.txt`. "
        f"Ejecución y exportación manual: {sc_fecha}. Solo documentos: la pestaña de preprints de Scopus no se exportó.",
        "- **Deduplicación:** por DOI y, si falta, por título normalizado.", "",
        "## Identificación (PRISMA-ScR)", "",
        "| Paso | Registros |", "|---|---|",
        f"| Recuperados en OpenAlex | {len(oa)} |",
        f"| Recuperados en Scopus | {len(sc)} |",
        f"| **Total identificados** | **{len(oa) + len(sc)}** |",
        f"| Duplicados internos de OpenAlex | {dup_oa} |",
        f"| Duplicados internos de Scopus | {dup_sc} |",
        f"| Duplicados entre fuentes | {len(oa) + len(sc) - dup_oa - dup_sc - len(unicos)} |",
        f"| **Registros únicos para cribado** | **{len(unicos)}** |", "",
        "## Aporte de cada fuente", "",
        f"- Solo en OpenAlex: {solo_oa}",
        f"- Solo en Scopus: {solo_sc}",
        f"- En ambas: {ambas}",
        f"- Registros sin resumen tras la fusión: {sin_resumen}", "",
        "## Recuperación del seed set", "",
        "| Clave | OpenAlex | Scopus |", "|---|---|---|",
    ]
    L += [f"| {k} | {a} | {b} |" for k, a, b in filas_seed]
    total_ok = sum(1 for _, a, b in filas_seed if "sí" in (a, b))
    L += ["", f"**Recuperados por al menos una fuente: {total_ok}/{len(filas_seed)}**", "",
          "## Decisiones de cribado aplicadas", "",
          "Tomadas de `cribado/decisiones.csv`. " +
          (", ".join(f"{k}: {v}" for k, v in aplicadas.items()) or "Ninguna todavía."),
          f"Pendientes de cribar: {len(unicos) - sum(aplicadas.values())}", "",
          "## Tipos documentales", "",
          "Tipo de Scopus cuando existe; si no, el de OpenAlex (normalizado a minúsculas). Tipos como *conference-review* "
          "(presentación de un volumen de actas), *Erratum* o *Retracted* se revisan en el cribado; "
          "no se eliminaron automáticamente.", "",
          "| Tipo | Registros |", "|---|---|"]
    L += [f"| {t} | {n} |" for t, n in tipos.most_common()]
    (salida / "registro.md").write_text("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main(*sys.argv[1:5])
