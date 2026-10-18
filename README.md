# actividad_ML1

# Integrantes:

Rober Andres Castillo 

Oscar Javier Garcia

## Reporte del proyecto

### Objetivo

El proyecto carga desde Hugging Face el dataset `mrseba/boston_house_price`, lo convierte en un DataFrame y genera un reporte descriptivo de los datos.

### Desarrollo realizado

El trabajo se desarrollo en el siguiente orden:

1. **Configuracion del entorno**

	Se creo el entorno virtual `.venv` para mantener aisladas las dependencias del proyecto y se selecciono como interprete de Python para VS Code y Jupyter.

2. **Instalacion de dependencias**

	Se agregaron en `requirements.txt` las librerias necesarias para el analisis de datos, la visualizacion, machine learning, notebooks y Hugging Face: `numpy`, `pandas`, `matplotlib`, `seaborn`, `scikit-learn`, `jupyter`, `ipykernel`, `huggingface-hub` y `datasets`.

3. **Conexion con Hugging Face**

	Se configuro el acceso a Hugging Face mediante `datasets` y `huggingface-hub`. El dataset utilizado es `mrseba/boston_house_price`, que contiene informacion relacionada con precios de viviendas.

4. **Implementacion del cargador**

	Se implemento `HFDatasetLoader` en `src/clases_po/hf__loader.py`. Esta clase permite seleccionar el nombre del dataset, la configuracion, la division (`split`), el limite de filas y el directorio de cache.

5. **Exportacion de datos**

	El cargador convierte el dataset a un DataFrame de pandas y permite guardarlo en formatos `csv`, `json`, `parquet` o `xlsx`. En este proyecto se genero `datos/precios_casas.csv`.

6. **Analisis exploratorio**

	Se analizaron las dimensiones del dataset, los tipos de datos, los valores nulos y las estadisticas descriptivas. El conjunto contiene 506 filas y 14 columnas, con 120 valores nulos distribuidos en seis variables. La variable objetivo `MEDV` no presenta valores nulos.

7. **Generacion del reporte**

	Se implemento la clase `Reportes` en `src/clases_po/reportes.py`. Esta clase genera un resumen con la cantidad de filas y columnas, tipos de datos, valores nulos y estadisticas descriptivas. El resultado se guarda en `reportes/precios_casas.txt`.

8. **Integracion en Jupyter**

	El flujo completo se documento y ejecuto en `Semana 1.ipynb`. El notebook configura la ruta del proyecto, importa las clases, carga los datos, muestra las primeras filas, genera el reporte y guarda los resultados.

9. **Automatizacion**

	Se agrego el workflow `.github/workflows/ejecutar-semana-1.yml` para ejecutar automaticamente el notebook cuando se realiza un `push` a la rama `main`. El workflow instala las dependencias, ejecuta el notebook y actualiza los resultados generados.

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
