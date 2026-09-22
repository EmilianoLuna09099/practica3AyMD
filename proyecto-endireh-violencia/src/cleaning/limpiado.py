import polars as pl

def limpiar_datos(ruta_csv):
    #sys.path.append("../..")
    df = pl.read_csv(ruta_csv)
    cols_a_eliminar = [c for c in df.columns if c.endswith("_desc")]
    df_sin_desc = df.drop(cols_a_eliminar)
    
    df_limpio = df_sin_desc.with_columns([
        pl.col("ingreso_pareja").is_not_null().alias("tiene_pareja"),
        pl.col("ingreso_pareja").fill_null(0).alias("ingreso_pareja"),
        pl.col("num_hijos").is_not_null().alias("tiene_hijos"),
        pl.col("num_hijos").fill_null(0).alias("num_hijos"),
    ])
    
    df_limpio = df_limpio.drop_nulls(subset=["edad_primer_union"])
    
    return df_limpio
