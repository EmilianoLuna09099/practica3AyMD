import polars as pl
import numpy as np
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

def gini_concentracion(df, columna_grupo, columna_valor):
    agregado = (
        df.group_by(columna_grupo)
        .agg(pl.col(columna_valor).sum().alias("total"))
    )
    x = agregado["total"].to_numpy()
    return gini_array(x)

def gini_array(x):
    """
    Calcula el coeficiente de Gini sobre un vector 1D de valores positivos.
    G = (2 * sum(i * x_(i)) - (n + 1) * sum(x_(i))) / (n * sum(x_(i)))
    """
    x = np.sort(np.asarray(x, dtype=float))
    n = len(x)
    total = np.sum(x)
    if n == 0 or total == 0:
        return 0.0
    i = np.arange(1, n + 1)
    numerador = 2 * np.sum(i * x) - (n + 1) * total
    denominador = n * total
    return float(numerador / denominador)

def curva_lorenz(df, columna_grupo, columna_valor):
    """
    Calcula los puntos (p, L) para graficar la Curva de Lorenz.
    - p: proporción acumulada de unidades (0 a 1).
    - L: proporción acumulada del valor o casos (0 a 1).
    """
    agregado = (
        df.group_by(columna_grupo)
        .agg(pl.col(columna_valor).sum().alias("total"))
    )
    x = agregado["total"].sort().to_numpy()
    x_acum = np.cumsum(x)
    total = x_acum[-1]
    
    # Inicia en (0, 0)
    L = np.insert(x_acum / total, 0, 0.0)
    p = np.linspace(0, 1, len(L))
    return p, L