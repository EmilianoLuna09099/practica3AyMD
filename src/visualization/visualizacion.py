import polars as pl
import matplotlib.pyplot as plt
import sys
from pathlib import Path


sys.path.append(str(Path(__file__).resolve().parents[2]))

from src.cleaning.limpiado import limpiar_datos
from config.rutas import RUTA_DATOS_CRUDOS

df_limpio = limpiar_datos(RUTA_DATOS_CRUDOS)

carpeta_salida = Path(__file__).resolve().parent / "graficas_generadas"
carpeta_salida.mkdir(exist_ok=True)

etiquetas_violencia = {0: "No reportó", 1: "Reportó violencia"}


def preparar_datos_boxplot(columna: str):

    grupos = []
    etiquetas = []
    for codigo, etiqueta in etiquetas_violencia.items():
        valores = (
            df_limpio
            .filter(pl.col("sufrio_violencia_pareja") == codigo)
            .select(pl.col(columna).drop_nulls())
            .to_series()
            .to_list()
        )
        grupos.append(valores)
        etiquetas.append(etiqueta)
    return grupos, etiquetas


def graficar_boxplot(columna: str, titulo: str, nombre_archivo: str, unidad: str = ""):
    grupos, etiquetas = preparar_datos_boxplot(columna)

    fig, ax = plt.subplots(figsize=(7, 5))
    caja = ax.boxplot(
        grupos,
        tick_labels=etiquetas,
        patch_artist=True,
        showmeans=True,
    )

    colores = ["#4C9AFF", "#FF6B6B"]
    for parche, color in zip(caja["boxes"], colores):
        parche.set_facecolor(color)
        parche.set_alpha(0.6)

    ax.set_title(titulo, fontsize=13, fontweight="bold")
    ax.set_ylabel(unidad if unidad else columna)
    ax.set_xlabel("Sufrió violencia de pareja")
    ax.grid(axis="y", linestyle="--", alpha=0.4)

    fig.tight_layout()
    ruta = carpeta_salida / nombre_archivo
    fig.savefig(ruta, dpi=150)
    plt.close(fig)
    print(f"Guardado: {ruta}")


# --- Boxplots individuales ---
graficar_boxplot(
    columna="edad_primer_union",
    titulo="Edad en la primera unión según violencia de pareja",
    nombre_archivo="boxplot_edad_primer_union.png",
    unidad="Edad (años)",
)

graficar_boxplot(
    columna="num_hijos",
    titulo="Número de hijos según violencia de pareja",
    nombre_archivo="boxplot_num_hijos.png",
    unidad="Número de hijos",
)

graficar_boxplot(
    columna="ingreso_pareja",
    titulo="Ingreso de la pareja según violencia de pareja",
    nombre_archivo="boxplot_ingreso_pareja.png",
    unidad="Ingreso ($)",
)

variables = [
    ("edad_primer_union", "Edad primera unión", "Años"),
    ("num_hijos", "Número de hijos", "Hijos"),
    ("ingreso_pareja", "Ingreso de la pareja", "Ingreso ($)"),
]

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

for ax, (columna, titulo, unidad) in zip(axes, variables):
    grupos, etiquetas = preparar_datos_boxplot(columna)
    caja = ax.boxplot(grupos, tick_labels=etiquetas, patch_artist=True, showmeans=True)
    for parche, color in zip(caja["boxes"], ["#4C9AFF", "#FF6B6B"]):
        parche.set_facecolor(color)
        parche.set_alpha(0.6)
    ax.set_title(titulo, fontsize=11, fontweight="bold")
    ax.set_ylabel(unidad)
    ax.grid(axis="y", linestyle="--", alpha=0.4)

fig.suptitle("Comparación de variables según violencia de pareja", fontsize=14, fontweight="bold")
fig.tight_layout()
ruta_panel = carpeta_salida / "boxplots_panel_completo.png"
fig.savefig(ruta_panel, dpi=150)
plt.close(fig)
print(f"Guardado: {ruta_panel}")

print("\nListo. Revisa la carpeta:", carpeta_salida)