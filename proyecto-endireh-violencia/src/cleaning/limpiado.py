import polars as pl
import sys

sys.path.append("../..")

from config.rutas import RUTA_DATOS_CRUDOS

df = pl.read_csv(RUTA_DATOS_CRUDOS)

cols_a_eliminar = [c for c in df.columns if c.endswith("_desc") or c.endswith("primer_union")]
df_sin_desc = df.drop(cols_a_eliminar)



df_limpio = df_sin_desc.with_columns([
    pl.col("ingreso_pareja").is_not_null().alias("tiene_pareja"),
    pl.col("ingreso_pareja").fill_null(0).alias("ingreso_pareja"),
])

print(df_limpio.columns)
