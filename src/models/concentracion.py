import polars as pl
import numpy as np
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))
from src.cleaning.limpiado import limpiar_datos
from config.rutas import RUTA_DATOS_CRUDOS

df_limpio = limpiar_datos(RUTA_DATOS_CRUDOS)


def gini_concentracion(df, columna_grupo, columna_valor):
  
    agregado = (
        df.group_by(columna_grupo)
        .agg(pl.col(columna_valor).sum().alias("total"))
    )

    x = agregado["total"].sort().to_numpy()
    n = len(x)
    i = np.arange(1, n + 1) 

    numerador = 2 * np.sum(i * x) - (n + 1) * np.sum(x)
    denominador = n * np.sum(x)

    gini = numerador / denominador
    return gini