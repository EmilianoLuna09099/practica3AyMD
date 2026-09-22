# Práctica 3: Análisis Exploratorio sobre Violencia contra las Mujeres

## Objetivo del Proyecto
El objetivo de este proyecto es estructurar un flujo de trabajo de minería de datos siguiendo estándares de la industria, aplicando un preprocesamiento (eliminación de nulos, corrección de tipos e imputación) y un Análisis Exploratorio de Datos. Se calculan medidas de localización y variabilidad utilizando métricas ponderadas para comparar estadísticamente a los grupos de mujeres que sufrieron o no violencia de pareja.

## Fuente de los Datos
Los datos utilizados provienen de la **Encuesta Nacional sobre la Dinámica de las Relaciones en los Hogares (ENDIREH) 2021**, levantada por el Instituto Nacional de Estadística y Geografía (INEGI) del gobierno de México.
* *Nota:* Por políticas de tamaño de Git, el archivo original CSV contenido en `data/data-raw/` no se incluye en este repositorio.
* *Nota:* Se utiliza el archivo proporcionado por la ayudante de laboratorio en lugar de los microdatos crudos directos del INEGI

## Cómo instalar el entorno
Este proyecto utiliza Python 3.10+ y `polars` como framework principal de manipulación de datos.

1. Clonar el repositorio y entrar a la carpeta del proyecto.
2. Crear un entorno virtual:
   ```bash
   python -m venv venv
   ```
3. Activar el entorno virtual:
   * En Linux/Mac: `source venv/bin/activate`
   * En Windows: `venv\Scripts\activate`
4. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Cómo ejecutar el pipeline
El análisis exploratorio se realiza mediante Jupyter Notebooks. Sigue este orden de ejecución:
1. Asegúrse de colocar el CSV proporcionado por la ayudante de laboratorio en el directorio`data/data-raw/`.
2. Ejecuta `notebooks/clasificacionVariables.ipynb` para la revisión de los tipos de datos.
3. Ejecuta `notebooks/medidasDescriptivas.ipynb` para visualizar el cálculo de tendencias centrales, dispersión y medias ponderadas.
