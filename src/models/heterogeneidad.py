import polars as pl
import numpy as np
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))
from src.cleaning.limpiado import limpiar_datos
from config.rutas import RUTA_DATOS_CRUDOS

df_limpio = limpiar_datos(RUTA_DATOS_CRUDOS)


def giniSimpon(columna):
    """
    Índice de Gini-Simpson: GS = 1 - sum(p_i^2)
    """
    resultado = df_limpio[columna].value_counts().with_columns(
        frecuencia_relativa_cuadrado = (pl.col("count") / pl.col("count").sum()) ** 2
    )
    suma_p2 = resultado["frecuencia_relativa_cuadrado"].sum()
    return float(1 - suma_p2)


def iqv(columna):
    """
    Índice de Variación Cualitativa: IQV = (k / (k - 1)) * GS
    """
    gini = giniSimpon(columna)
    k = df_limpio[columna].n_unique()
    if k <= 1:
        return 0.0
    return float((k / (k - 1)) * gini)


def entropia(columna, base=2):
    """
    Entropía de Shannon en base 2 (bits): H = - sum(p_i * log2(p_i))
    0 <= H <= log2(k)
    """
    resultado = df_limpio[columna].value_counts().with_columns(
        frecuencia_relativa = (pl.col("count") / pl.col("count").sum())
    )
    p = resultado["frecuencia_relativa"].to_numpy()
    p = p[p > 0]
    
    if base == 2:
        entrop = -np.sum(p * np.log2(p))
    elif base == np.e:
        entrop = -np.sum(p * np.log(p))
    else:
        entrop = -np.sum(p * (np.log(p) / np.log(base)))
    return float(entrop)