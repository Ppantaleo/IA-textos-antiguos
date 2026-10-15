#!/usr/bin/env python3
"""Verifica contra Crossref las referencias con DOI de un archivo BibTeX.

Para cada entrada con DOI consulta `api.crossref.org/works/<doi>` y compara lo
que dice la bibliografía con lo que devuelve el registro: título, año,
publicación, volumen y páginas. Las entradas sin DOI —normas, informes,
documentos institucionales— se listan aparte, porque su verificación es manual.

No corrige nada: escribe un informe para que el autor decida. Crossref no es
fuente de búsqueda en este trabajo, solo servicio de metadatos (§5.5).

Uso:
  python3 scripts/verificar_crossref.py [archivo.bib] [informe.md]
"""

import html
import json
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
BIB = Path(sys.argv[1]) if len(sys.argv) > 1 else REPO / "docs" / "bibliografia.bib"
INFORME = Path(sys.argv[2]) if len(sys.argv) > 2 else REPO / "registros" / "verificacion-bibliografia.md"

API = "https://api.crossref.org/works/"
# Añadir "mailto:<correo>" al User-Agent para entrar en el pool amable de Crossref.
AGENTE = "verificar-crossref/1.0 (TFM, Universidad Carlos III de Madrid)"
PAUSA = 0.5


def entradas(texto):
    """Devuelve [(clave, tipo, {campo: valor})] de un BibTeX, sin dependencias."""
    salida = []
    for m in re.finditer(r"@(\w+)\{([^,]+),", texto):
        tipo, clave = m.group(1).lower(), m.group(2).strip()
        # El cuerpo llega hasta la siguiente entrada o el final
        sig = texto.find("\n@", m.end())
        cuerpo = texto[m.end():sig if sig != -1 else len(texto)]
        campos = {}
        for c in re.finditer(r"(\w+)\s*=\s*\{(.*?)\}\s*,?\s*\n", cuerpo, re.S):
            campos[c.group(1).lower()] = " ".join(c.group(2).split())
        salida.append((clave, tipo, campos))
    return salida


def norm(s):
    s = unicodedata.normalize("NFKD", html.unescape(s or "").lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "", s)


def consultar(doi):
    pedido = urllib.request.Request(API + doi, headers={"User-Agent": AGENTE})
    try:
        with urllib.request.urlopen(pedido, timeout=30) as r:
            return json.load(r)["message"]
    except urllib.error.HTTPError as e:
        return {"__error__": f"HTTP {e.code}"}
    except Exception as e:                                    # red, tiempo de espera
        return {"__error__": type(e).__name__}


def comparar(campos, m):
    """Devuelve [(campo, valor en el .bib, valor en Crossref)] de lo que no coincide."""
    cr_titulo = (m.get("title") or [""])[0]
    cr_anio = str((m.get("issued", {}).get("date-parts") or [[""]])[0][0] or "")
    cr_pub = (m.get("container-title") or [""])[0] if m.get("container-title") else ""
    pares = [
        ("title", campos.get("title", ""), cr_titulo),
        ("year", campos.get("year", ""), cr_anio),
        ("journal/booktitle", campos.get("journal") or campos.get("booktitle", ""), cr_pub),
        ("volume", campos.get("volume", ""), m.get("volume", "") or ""),
        ("pages", campos.get("pages", ""), (m.get("page", "") or "").replace("-", "--")),
    ]
    difs = []
    for campo, mio, suyo in pares:
        if not mio or not suyo:            # si falta en un lado, no es discrepancia
            continue
        if norm(mio) != norm(suyo):
            difs.append((campo, mio, suyo))
    return difs


def main():
    texto = BIB.read_text(encoding="utf-8")
    todas = entradas(texto)
    con_doi = [(k, c) for k, _, c in todas if c.get("doi")]
    sin_doi = [(k, c) for k, _, c in todas if not c.get("doi")]

    ok, con_difs, fallos = [], [], []
    for i, (clave, campos) in enumerate(con_doi, 1):
        doi = campos["doi"]
        m = consultar(doi)
        if "__error__" in m:
            fallos.append((clave, doi, m["__error__"]))
        else:
            difs = comparar(campos, m)
            (con_difs if difs else ok).append((clave, doi, difs))
        print(f"  [{i}/{len(con_doi)}] {clave}", file=sys.stderr)
        time.sleep(PAUSA)

    hoy = time.strftime("%Y-%m-%d")
    L = [f"# Verificación de la bibliografía contra Crossref", "",
         f"- **Fecha:** {hoy}",
         f"- **Archivo:** `{BIB.name}`, {len(todas)} entradas",
         f"- **Con DOI:** {len(con_doi)} · **sin DOI:** {len(sin_doi)}",
         f"- **Coinciden:** {len(ok)} · **con discrepancias:** {len(con_difs)} · "
         f"**no resueltas:** {len(fallos)}", "",
         "Se comparan título, año, publicación, volumen y páginas. Un campo ausente",
         "en cualquiera de los dos lados no cuenta como discrepancia.", ""]

    if fallos:
        L += ["## DOI que no resuelven", "", "| Clave | DOI | Error |", "|---|---|---|"]
        L += [f"| `{k}` | {d} | {e} |" for k, d, e in fallos] + [""]
    if con_difs:
        L += ["## Discrepancias", "", "| Clave | Campo | En la bibliografía | En Crossref |", "|---|---|---|---|"]
        for k, _, difs in con_difs:
            L += [f"| `{k}` | {c} | {a} | {b} |" for c, a, b in difs]
        L += [""]
    L += ["## Entradas sin DOI", "",
          "Normas, informes y documentos institucionales: la verificación es manual",
          "y queda anotada en el campo `note` de cada entrada.", "",
          "| Clave | Título |", "|---|---|"]
    L += [f"| `{k}` | {c.get('title','')[:90]} |" for k, c in sin_doi]
    L += ["", "## Entradas verificadas sin discrepancias", "",
          ", ".join(f"`{k}`" for k, _, _ in ok), ""]

    INFORME.parent.mkdir(parents=True, exist_ok=True)
    INFORME.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"\n{INFORME.relative_to(REPO)}: {len(ok)} coinciden, "
          f"{len(con_difs)} con discrepancias, {len(fallos)} sin resolver")


if __name__ == "__main__":
    main()
