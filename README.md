# actividad_ML1

# Integrantes:

Rober Andres Castillo /

Oscar Javier Garcia

## Reporte del proyecto

### Objetivo

El proyecto carga desde Hugging Face el dataset `mrseba/boston_house_price`, lo convierte en un DataFrame y genera un reporte descriptivo de los datos.

### Desarrollo realizado

- Se configuro un entorno virtual `.venv` para ejecutar el proyecto.
- Se agregaron las dependencias de analisis de datos, visualizacion, machine learning, Jupyter y Hugging Face en `requirements.txt`.
- Se implemento `HFDatasetLoader` en `src/clases_po/hf__loader.py`.
- El cargador permite seleccionar el dataset, la division, el limite de filas y el formato de salida (`csv`, `json`, `parquet` o `xlsx`).
- Se implemento la clase `Reportes` en `src/clases_po/reportes.py`.
- El reporte incluye dimensiones, tipos de datos, valores nulos y estadisticas descriptivas.
- El informe se guarda en `reportes/precios_casas.txt` y los datos descargados en `datos/precios_casas.csv`.
- El flujo completo se documenta y ejecuta en `Semana 1.ipynb`.

### Resultado del analisis

El dataset contiene 506 filas y 14 columnas. Se identificaron 120 valores nulos distribuidos en las columnas `CRIM`, `ZN`, `INDUS`, `CHAS`, `AGE` y `LSTAT`. La columna objetivo `MEDV` no presenta valores nulos. Los tipos de datos son numericos y se generaron estadisticas descriptivas para todas las variables.

### Instalacion y ejecucion

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Luego se puede abrir `Semana 1.ipynb` en Jupyter o VS Code y seleccionar el kernel `.venv`.

### Autenticacion opcional de Hugging Face

La autenticacion solo es necesaria para acceder a repositorios privados:

```bash
python -m pip install --upgrade huggingface_hub
hf auth login
hf auth whoami
```
