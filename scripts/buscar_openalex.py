#!/usr/bin/env python3
"""Búsqueda bibliográfica en OpenAlex para el TFM, en modo reproducible.

Toma una cadena booleana, la busca en título y resumen dentro de una ventana
temporal y guarda en la carpeta de la corrida:

  registro.md     fecha, cadena, conteos, costo, recuperación del seed set y
                  aporte de cada término (para el diagrama PRISMA)
  resultados.csv  una fila por trabajo, para el cribado (título, resumen, etc.)
  resultados.bib  BibTeX generado desde los metadatos de OpenAlex
  crudo.jsonl     respuesta original de la API, sin modificar

Uso:
  python3 buscar_openalex.py piloto-v0

La configuración de cada corrida vive en consultas/<nombre>.json. Así, cada
versión de la cadena queda registrada y no se sobrescribe.
"""

import csv
import datetime as dt
import json
import re
import sys
import time
import unicodedata
import urllib.parse
import urllib.request
from pathlib import Path

API = "https://api.openalex.org/works"
BASE = Path(__file__).resolve().parent
SELECT = ",".join([
    "id", "doi", "title", "publication_year", "publication_date", "type",
    "language", "authorships", "primary_location", "biblio",
    "abstract_inverted_index", "cited_by_count", "ids",
])


def get(params):
    url = API + "?" + urllib.parse.urlencode(params)
    for intento in range(4):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                datos = json.load(r), float(r.headers.get("x-ratelimit-cost-usd") or 0)
            time.sleep(1)  # evita el 429 por ráfaga de peticiones
            return datos
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503) and intento < 3:
                time.sleep(2 ** intento * 3)
                continue
            raise


def filtro(cadena, desde, hasta):
    # OpenAlex separa filtros con coma: la cadena no puede contener comas.
    assert "," not in cadena, "La cadena no puede contener comas"
    return f"title_and_abstract.search:{cadena},publication_year:{desde}-{hasta}"


def contar(cadena, cfg):
    d, costo = get({"filter": filtro(cadena, cfg["desde"], cfg["hasta"]),
                    "per_page": 1, "select": "id"})
    return d["meta"]["count"], costo


def bloque(terminos):
    return "(" + " OR ".join(terminos) + ")"


def resumen(inv):
    if not inv:
        return ""
    pos = {}
    for palabra, idx in inv.items():
        for i in idx:
            pos[i] = palabra
    return " ".join(pos[i] for i in sorted(pos))


def norm_titulo(t):
    t = unicodedata.normalize("NFKD", t or "").encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]", "", t.lower())


def doi_corto(doi):
    return (doi or "").lower().replace("https://doi.org/", "")


def esc(s):
    s = (s or "").replace("\n", " ")
    s = s.replace("{", "").replace("}", "")
    return re.sub(r"([&%#])", r"\\\1", s)


def clave(w, usadas):
    aut = w.get("authorships") or []
    apellido = "anon"
    if aut:
        nombre = aut[0]["author"].get("display_name") or ""
        apellido = nombre.split()[-1] if nombre.split() else "anon"
    palabra = next((p for p in re.findall(r"[A-Za-z]+", w.get("title") or "")
                    if len(p) > 3), "sin")
    base = norm_titulo(apellido) + str(w.get("publication_year") or "") + palabra.lower()
    k, n = base, 1
    while k in usadas:
        n += 1
        k = f"{base}{chr(96 + n)}"
    usadas.add(k)
    return k


def bibtex(w, k):
    loc = w.get("primary_location") or {}
    src = loc.get("source") or {}
    venue = src.get("display_name") or ""
    tipo_src = src.get("type") or ""
    tipo = w.get("type")
    if tipo == "preprint" or not venue:
        et, venue_campo = "misc", "howpublished"
    elif tipo_src == "conference":
        et, venue_campo = "inproceedings", "booktitle"
    elif tipo in ("book-chapter",):
        et, venue_campo = "incollection", "booktitle"
    elif tipo == "dissertation":
        et, venue_campo = "phdthesis", "school"
    else:
        et, venue_campo = "article", "journal"
    autores = " and ".join(esc(a["author"].get("display_name"))
                           for a in (w.get("authorships") or []))
    b = w.get("biblio") or {}
    paginas = "--".join(p for p in (b.get("first_page"), b.get("last_page")) if p)
    campos = [
        ("title", "{" + esc(w.get("title")) + "}"),
        ("author", autores),
        (venue_campo, esc(venue)),
        ("year", str(w.get("publication_year") or "")),
        ("volume", b.get("volume")),
        ("number", b.get("issue")),
        ("pages", paginas),
        ("doi", doi_corto(w.get("doi"))),
        ("url", loc.get("landing_page_url")),
        ("abstract", esc(resumen(w.get("abstract_inverted_index")))),
        ("note", "OpenAlex " + w["id"].rsplit("/", 1)[-1] + f"; tipo: {tipo}"),
    ]
    cuerpo = ",\n".join(f"  {c} = {{{v}}}" for c, v in campos if v)
    return f"@{et}{{{k},\n{cuerpo}\n}}\n"


def main(nombre):
    cfg = json.loads((BASE / "consultas" / f"{nombre}.json").read_text())
    salida = BASE / "corridas" / nombre
    salida.mkdir(parents=True, exist_ok=True)
    costo_total = 0.0

    bloques = [bloque(b["terminos"]) for b in cfg["bloques"]]
    cadena = " AND ".join(bloques)

    # 1. Conteo total y aporte de cada término (manteniendo fijos los otros bloques)
    total, c = contar(cadena, cfg)
    costo_total += c
    aporte = []
    for i, b in enumerate(cfg["bloques"]):
        resto = [x for j, x in enumerate(bloques) if j != i]
        for t in b["terminos"]:
            n, c = contar(" AND ".join(resto + [t]), cfg)
            costo_total += c
            aporte.append((b["nombre"], t, n))

    if total > cfg.get("max_registros", 4000):
        print(f"{total} registros superan max_registros; se descargan solo los conteos.")
        trabajos = []
    else:
        # 2. Descarga paginada con cursor
        trabajos, cursor = [], "*"
        with open(salida / "crudo.jsonl", "w") as crudo:
            while cursor:
                d, c = get({"filter": filtro(cadena, cfg["desde"], cfg["hasta"]),
                            "per_page": 200, "cursor": cursor, "select": SELECT})
                costo_total += c
                for w in d["results"]:
                    crudo.write(json.dumps(w, ensure_ascii=False) + "\n")
                    trabajos.append(w)
                cursor = d["meta"].get("next_cursor") if d["results"] else None

    # 3. Deduplicación: por DOI y, si no hay, por título normalizado
    vistos, unicos, duplicados = set(), [], 0
    for w in trabajos:
        claves = {norm_titulo(w.get("title"))}
        if w.get("doi"):
            claves.add(doi_corto(w["doi"]))
        if claves & vistos:
            duplicados += 1
            continue
        vistos |= claves
        unicos.append(w)

    # 4. Recuperación del seed set
    seed = cfg.get("seed", {})
    dois = {doi_corto(w.get("doi")) for w in trabajos}
    titulos = {norm_titulo(w.get("title")) for w in trabajos}
    recup = []
    for k, s in seed.items():
        ok = s["doi"].lower() in dois or norm_titulo(s["titulo"]) in titulos
        recup.append((k, s["doi"], ok))

    # 5. Salidas para cribado
    usadas = set()
    with open(salida / "resultados.csv", "w", newline="") as f, \
         open(salida / "resultados.bib", "w") as fb:
        cw = csv.writer(f)
        cw.writerow(["clave", "anio", "tipo", "titulo", "autores", "fuente", "doi",
                     "openalex", "citas", "resumen", "decision", "motivo"])
        fb.write(f"% OpenAlex, corrida '{nombre}', {dt.date.today()}\n% {cadena}\n\n")
        for w in sorted(unicos, key=lambda w: (-(w.get("publication_year") or 0),
                                               w.get("title") or "")):
            k = clave(w, usadas)
            src = ((w.get("primary_location") or {}).get("source") or {})
            cw.writerow([
                k, w.get("publication_year"), w.get("type"), w.get("title"),
                "; ".join(a["author"].get("display_name") or ""
                          for a in (w.get("authorships") or [])),
                src.get("display_name"), doi_corto(w.get("doi")),
                w["id"].rsplit("/", 1)[-1], w.get("cited_by_count"),
                resumen(w.get("abstract_inverted_index")), "", "",
            ])
            fb.write(bibtex(w, k) + "\n")

    sin_resumen = sum(1 for w in unicos if not w.get("abstract_inverted_index"))
    tipos = {}
    for w in unicos:
        tipos[w.get("type")] = tipos.get(w.get("type"), 0) + 1

    # 6. Registro
    L = [
        f"# Corrida `{nombre}`", "",
        f"- **Fecha de ejecución:** {dt.datetime.now().isoformat(timespec='seconds')}",
        "- **Fuente:** OpenAlex API (`/works`), campo `title_and_abstract.search`",
        f"- **Ventana:** {cfg['desde']}–{cfg['hasta']} (`publication_year`)",
        f"- **Propósito:** {cfg.get('proposito', '')}", "",
        "## Cadena", "", "```", cadena, "```", "",
        "## Conteos", "",
        f"- Registros según la API (`meta.count`): {total}",
        f"- Registros descargados: **{len(trabajos)}** (el conteo puede variar levemente al paginar; para PRISMA vale este)",
        f"- Duplicados eliminados (DOI o título): {duplicados}",
        f"- Registros únicos para cribado: **{len(unicos)}**",
        f"- Sin resumen en OpenAlex: {sin_resumen}",
        f"- Por tipo: {', '.join(f'{k}: {v}' for k, v in sorted(tipos.items(), key=lambda x: -x[1]))}",
        f"- Costo de la corrida en la API: USD {costo_total:.3f}", "",
        "## Recuperación del seed set", "",
        "| Clave | DOI | ¿Recuperado? |", "|---|---|---|",
    ]
    L += [f"| {k} | {d} | {'sí' if ok else '**NO**'} |" for k, d, ok in recup]
    n_ok = sum(ok for *_, ok in recup)
    L += ["", f"**Recall: {n_ok}/{len(recup)}**", "",
          "## Aporte de cada término", "",
          "Registros que recupera cada término combinado con los demás bloques completos. "
          "Un conteo muy alto señala ruido; uno igual a 0, que el término sobra.", "",
          "| Bloque | Término | Registros |", "|---|---|---|"]
    L += [f"| {b} | `{t}` | {n} |" for b, t, n in aporte]
    (salida / "registro.md").write_text("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "piloto-v0")
