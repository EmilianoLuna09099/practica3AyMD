from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RUTA_DATOS_CRUDOS = (
    BASE_DIR
    / "data"
    / "data-raw"
    / "Emiliano Luna Campos - endireh_ml_dataset_texto_fecha - Emiliano Luna Campos - endireh_ml_dataset_texto_fecha.csv"
)

RUTA_DATOS_PROCESADOS = BASE_DIR / "data" / "data-processed"

RUTA_DATOS_MODELO = BASE_DIR / "data" / "data-model"

RUTA_DATOS_INPUT_MODELO = BASE_DIR / "data" / "data-input-model"
