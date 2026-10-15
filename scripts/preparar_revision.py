#!/usr/bin/env python3
"""Genera el cuaderno con el que el autor revisa el cribado asistido por IA.

La propuesta de la IA no es una decisión (§5.6). El autor revisa **todas** las
inclusiones, los dudosos y las revisiones, y una **muestra aleatoria
estratificada del 10 % de cada código de exclusión**, con la que se estima el
acuerdo entre la propuesta y sus decisiones.

El muestreo es reproducible: semilla fija, códigos en orden alfabético y
registros en el orden del CSV de la propuesta. Ejecutarlo dos veces da el mismo
cuaderno.

Uso:
  python3 scripts/preparar_revision.py [propuesta.csv] [salida.xlsx]

Requiere openpyxl.
"""

import collections
import csv
import random
import sys
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

REPO = Path(__file__).resolve().parent.parent
PROPUESTA = Path(sys.argv[1]) if len(sys.argv) > 1 else REPO / "cribado" / "propuesta-ia-v1.1.csv"
SALIDA = Path(sys.argv[2]) if len(sys.argv) > 2 else REPO / "cribado" / "revision-autor-v1.xlsx"

SEMILLA = 20260914
FRACCION = 0.10
TOPE_RESUMEN = 3000   # el resumen completo está en la propuesta; aquí solo lo que se lee
VERSION = "v1.1, 2026-09-14"

RANGO_CONFIANZA = {"baja": 0, "media": 1, "alta": 2}
COLUMNAS = [("n", 5), ("grupo", 22), ("codigo_propuesto", 9), ("confianza", 9),
            ("motivo", 45), ("nota", 25), ("enmienda", 9), ("titulo", 55),
            ("anio", 6), ("tipo", 12), ("fuente_publicacion", 25), ("doi", 22),
            ("resumen", 80), ("clave", 22), ("CODIGO_AUTOR", 14),
            ("COMENTARIO_AUTOR", 35)]

INSTRUCCIONES = [
    f"Revisión del cribado asistido por IA — TFM ({VERSION})",
    "",
    "Qué revisar: todas las filas de los grupos 1–3 (incluir, revisión, dudoso) y la "
    f"muestra aleatoria del grupo 4 ({int(FRACCION*100)} % de cada código de exclusión, semilla {SEMILLA}).",
    "Cómo: en la columna CODIGO_AUTOR escribe OK si aceptas la propuesta, o el código que "
    "corresponda (I, D, R, E1–E6). COMENTARIO_AUTOR es opcional, pero conviene usarlo si cambias el código.",
    "Sugerencia de orden: dentro de cada grupo, las filas van de confianza baja a alta. "
    "Las de confianza alta suelen resolverse rápido.",
    "",
    "Códigos:",
    "I = incluir (pasa a texto completo)",
    "D = dudoso (pasa a texto completo)",
    "R = revisión o survey pertinente (fuera del corpus; fuente de snowballing)",
    "E1 = sin IA basada en aprendizaje (incluye EN1)",
    "E2 = sin producto digital",
    "E3 = no es texto antiguo según §7.1; sin material antiguo real (EN2); o tarea sobre el "
    "testimonio medieval o moderno (EN3)",
    "E4 = corpus mixto no principalmente antiguo",
    "E5 = sin estudio primario o retractado (EN4)",
    "E6 = tema ajeno (entró por coincidencia de palabras)",
    "",
    "Regla de duda: si no alcanza el título y el resumen, D.",
    "Criterios completos: docs/proyecto.md §5.6 y §7.1; cribado/instrucciones-cribado-ia.md.",
    "Columna 'enmienda': indica si la propuesta cambió al aplicar EN1–EN4; codigo_v1 y motivo_v1 "
    "están en propuesta-ia-v1.1.csv.",
]

GRUPOS = [("I", "1 · Incluir (revisión completa)"),
          ("R", "2 · Revisión/survey (revisión completa)"),
          ("D", "3 · Dudoso (revisión completa)")]
GRUPO_MUESTRA = f"4 · Exclusión (muestra aleatoria {int(FRACCION*100)} %)"


def muestra_exclusiones(filas):
    """10 % de cada código de exclusión, al menos uno, con semilla fija."""
    por_codigo = collections.defaultdict(list)
    for f in filas:
        if f["codigo"].startswith("E"):
            por_codigo[f["codigo"]].append(f)
    azar = random.Random(SEMILLA)
    elegidas = []
    for codigo in sorted(por_codigo):
        n = max(1, round(len(por_codigo[codigo]) * FRACCION))
        elegidas += azar.sample(por_codigo[codigo], n)
    return elegidas


def main():
    filas = list(csv.DictReader(open(PROPUESTA, newline="", encoding="utf-8")))
    por_confianza = lambda f: (RANGO_CONFIANZA[f["confianza"]], f["titulo"].lower())

    seleccion = []
    for codigo, nombre in GRUPOS:
        for f in sorted([x for x in filas if x["codigo"] == codigo], key=por_confianza):
            seleccion.append((nombre, f))
    muestra = muestra_exclusiones(filas)
    for f in sorted(muestra, key=lambda x: (x["codigo"], x["titulo"].lower())):
        seleccion.append((GRUPO_MUESTRA, f))

    libro = Workbook()
    hoja_i = libro.active
    hoja_i.title = "Instrucciones"
    hoja_i.column_dimensions["A"].width = 120
    for i, linea in enumerate(INSTRUCCIONES, 1):
        celda = hoja_i.cell(row=i, column=1, value=linea)
        celda.alignment = Alignment(wrap_text=True, vertical="top")
        if i == 1:
            celda.font = Font(bold=True, size=13)

    hoja = libro.create_sheet("Revisar")
    cabecera = [c for c, _ in COLUMNAS]
    hoja.append(cabecera)
    for celda in hoja[1]:
        celda.font = Font(bold=True, color="FFFFFF")
        celda.fill = PatternFill("solid", fgColor="1A1A1A")
        celda.alignment = Alignment(vertical="center")

    for n, (grupo, f) in enumerate(seleccion, 1):
        anio = int(f["anio"]) if (f["anio"] or "").isdigit() else f["anio"]
        hoja.append([n, grupo, f["codigo"], f["confianza"], f["motivo"], f.get("nota", ""),
                     f.get("enmienda", ""), f["titulo"], anio, f["tipo"],
                     f["fuente_publicacion"], f["doi"], f.get("resumen", "")[:TOPE_RESUMEN],
                     f["clave"], "", ""])

    for i, (_, ancho) in enumerate(COLUMNAS, 1):
        hoja.column_dimensions[get_column_letter(i)].width = ancho
    hoja.freeze_panes = "C2"
    ultima = len(seleccion) + 1
    hoja.auto_filter.ref = f"A1:{get_column_letter(len(COLUMNAS))}{ultima}"

    validacion = DataValidation(type="list", formula1='"OK,I,D,R,E1,E2,E3,E4,E5,E6"',
                                allow_blank=True, showDropDown=False)
    hoja.add_data_validation(validacion)
    validacion.add(f"O2:O{ultima}")

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    libro.save(SALIDA)

    reparto = collections.Counter(g for g, _ in seleccion)
    print(f"{SALIDA.relative_to(REPO)}: {len(seleccion)} filas")
    for g, n in sorted(reparto.items()):
        print(f"  {g}: {n}")


if __name__ == "__main__":
    main()
