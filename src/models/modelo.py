import polars as pl
import numpy as np
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))
from src.cleaning.limpiado import limpiar_datos
from config.rutas import RUTA_DATOS_CRUDOS

df_limpio = limpiar_datos(RUTA_DATOS_CRUDOS)
print("Filas sin nulos en edad:", df_limpio.shape[0])


medidas_simples = df_limpio.select([
    pl.col("edad_primer_union").mean().alias("Media_Edad"),
    pl.col("edad_primer_union").median().alias("Mediana_Edad"),
    pl.col("edad_primer_union").mode().first().alias("Moda_Edad"),
    pl.col("edad_primer_union").quantile(0.25).alias("Q1_Edad"),
    pl.col("edad_primer_union").quantile(0.75).alias("Q3_Edad"),
    pl.col("edad_primer_union").quantile(0.10).alias("P10_Edad"),
    pl.col("edad_primer_union").quantile(0.90).alias("P90_Edad"),
    
    pl.col("num_hijos").mean().alias("Media_Hijos"),
    pl.col("num_hijos").median().alias("Mediana_Hijos"),
    pl.col("num_hijos").mode().first().alias("Moda_Hijos"),
    pl.col("num_hijos").quantile(0.25).alias("Q1_Hijos"),
    pl.col("num_hijos").quantile(0.75).alias("Q3_Hijos"),
    pl.col("num_hijos").quantile(0.10).alias("P10_Hijos"),
    pl.col("num_hijos").quantile(0.90).alias("P90_Hijos"),
    pl.col("nivel_escolaridad").mode().alias("moda_escolaridad"),

    pl.col("ingreso_pareja").mean().alias("Media_ingreso_pareja"),
    pl.col("ingreso_pareja").median().alias("Mediana_ingreso_pareja"),
    pl.col("ingreso_pareja").mode().first().alias("Moda_ingreso_pareja"),
    pl.col("ingreso_pareja").quantile(0.25).alias("Q1_ingreso_pareja"),
    pl.col("ingreso_pareja").quantile(0.75).alias("Q3_ingreso_pareja"),
    pl.col("ingreso_pareja").quantile(0.10).alias("P10_ingreso_pareja"),
    pl.col("ingreso_pareja").quantile(0.90).alias("P90_ingreso_pareja")
])

medidas_simples


edades = df_limpio["edad_primer_union"].to_numpy()
hijos = df_limpio["num_hijos"].to_numpy()
ingreso_pareja = df_limpio["ingreso_pareja"].to_numpy()
pesos = df_limpio["factor_expansion"].to_numpy()

media_edad_ponderada = np.average(edades, weights=pesos)
media_hijos_ponderada = np.average(hijos, weights=pesos)
media_ingreso_pareja = np.average(ingreso_pareja, weights=pesos)

print(f"Media SIMPLE de Edad:    {medidas_simples['Media_Edad'][0]:.2f} años")
print(f"Media PONDERADA de Edad: {media_edad_ponderada:.2f} años")
print("-" * 40)
print(f"Media SIMPLE de Hijos:    {medidas_simples['Media_Hijos'][0]:.2f}")
print(f"Media PONDERADA de Hijos: {media_hijos_ponderada:.2f}")
print("-" * 40)
print(f"Media SIMPLE de ingreso_pareja:    {medidas_simples['Media_ingreso_pareja'][0]:.2f}")
print(f"Media PONDERADA de ingreso_pareja: {media_ingreso_pareja:.2f}")




medidas_variabilidad = df_limpio.group_by("sufrio_violencia_pareja").agg([
    
    # Medidas para edad en la primera unión
    (pl.col("edad_primer_union").max() - pl.col("edad_primer_union").min()).alias("Rango_Edad"), #Rango (Máximo - Mínimo)
    pl.col("edad_primer_union").var().alias("Varianza_Edad"),
    pl.col("edad_primer_union").std().alias("Desv_Std_Edad"),
    ((pl.col("edad_primer_union").std() / pl.col("edad_primer_union").mean()) * 100).alias("CV_Edad_%"),
    (pl.col("edad_primer_union").quantile(0.75) - pl.col("edad_primer_union").quantile(0.25)).alias("IQR_Edad"),

    # medidas para numeros de hijos
    (pl.col("num_hijos").max() - pl.col("num_hijos").min()).alias("Rango_Hijos"),
    pl.col("num_hijos").var().alias("Varianza_Hijos"),
    pl.col("num_hijos").std().alias("Desv_Std_Hijos"),
    ((pl.col("num_hijos").std() / pl.col("num_hijos").mean()) * 100).alias("CV_Hijos_%"),
    (pl.col("num_hijos").quantile(0.75) - pl.col("num_hijos").quantile(0.25)).alias("IQR_Hijos"),

    (pl.col("ingreso_pareja").max() - pl.col("ingreso_pareja").min()).alias("Rango_ingreso_pareja"),
    pl.col("ingreso_pareja").var().alias("Varianza_ingreso_pareja"),
    pl.col("ingreso_pareja").std().alias("Desv_Std_ingreso_pareja"),
    ((pl.col("ingreso_pareja").std() / pl.col("ingreso_pareja").mean()) * 100).alias("CV_ingreso_pareja_%"),
    (pl.col("ingreso_pareja").quantile(0.75) - pl.col("ingreso_pareja").quantile(0.25)).alias("IQR_ingreso_pareja")

])
#0=No reportó violencia de pareja
#1=Reportó violencia de pareja
medidas_variabilidad