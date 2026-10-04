# Práctica 4: Medidas de Heterogeneidad y Concentración. Visualización de Datos

## Objetivo del Proyecto
El objetivo de este proyecto es continuar con el flujo de trabajo de la Práctica 3 sobre el dataset preprocesado de la **ENDIREH 2021**. Se calculan e interpretan medidas de localización, variabilidad, heterogeneidad (IQV, Gini-Simpson, Entropía de Shannon) y concentración (Coeficiente de Gini, Curva de Lorenz). Todo el análisis es acompañado de visualizaciones de datos y una interpretación ética del fenómeno de la violencia contra las mujeres.

## Fuente de los Datos
Los datos provienen de la **Encuesta Nacional sobre la Dinámica de las Relaciones en los Hogares (ENDIREH) 2021** (INEGI).
* *Nota:* Por políticas de tamaño de Git, el archivo original CSV contenido en `data/data-raw/` no se incluye en el repositorio.
* *Nota:* Se utiliza el archivo consolidado proporcionado por la ayudantía.

## Cómo instalar el entorno
Este proyecto utiliza Python 3.10+ y los frameworks `polars` y `matplotlib`.

1. Clonar el repositorio y entrar a la carpeta del proyecto.
2. Crear un entorno virtual:
   ```bash
   python -m venv venv
   ```
3. Activar el entorno virtual (Linux/Mac: `source venv/bin/activate` | Windows: `venv\Scripts\activate`)
4. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Cómo ejecutar el pipeline
El análisis exploratorio y descriptivo está dividido por temáticas en la carpeta de notebooks, según la rúbrica de la práctica:

1. **Localización y Variabilidad:** Ejecutar `notebooks/medidasDescriptivas.ipynb` (incluye EDA con Histogramas y Boxplots).
2. **Heterogeneidad:** Ejecutar `notebooks/medidasHeterogeneidad.ipynb` (IQV, Gini-Simpson, Entropía).
3. **Concentración:** Ejecutar `notebooks/medidasConcentracion.ipynb` (Curva de Lorenz y Coeficiente de Gini territorial).
4. **Síntesis:** Ejecutar `notebooks/comparacionGiniEntropia.ipynb` (Contraste teórico y empírico entre Gini y Entropía sobre la misma variable).
