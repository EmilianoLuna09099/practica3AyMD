import polars as pl
import numpy as np
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))
from src.cleaning.limpiado import limpiar_datos
from config.rutas import RUTA_DATOS_CRUDOS

df_limpio = limpiar_datos(RUTA_DATOS_CRUDOS)



def giniSimpon(columna):
    
    resultado = df_limpio[columna].value_counts().with_columns(
        frecuencia_relativa_cuadrado = (pl.col("count") / pl.col("count").sum()) ** 2
    )
    
    suma_p2 = resultado["frecuencia_relativa_cuadrado"].sum()
    gini_simpson = 1 - suma_p2
    return gini_simpson


def iqv(columna):

    gini = giniSimpon(columna)
    k = df_limpio[columna].n_unique()  
    resultado = (k / (k - 1)) * gini
    return resultado

def entropia(columna):
    resultado = df_limpio[columna].value_counts().with_columns(
        frecuencia_relativa = (pl.col("count") / pl.col("count").sum())
    )

    entrop= (-resultado["frecuencia_relativa"] *(np.log(resultado["frecuencia_relativa"]) )).sum()
    return entrop
    