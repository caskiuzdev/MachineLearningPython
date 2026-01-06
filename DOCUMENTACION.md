# Documentación del Proyecto: Predicción de Riesgo de Infarto con Machine Learning

## Descripción General
Este proyecto implementa un sistema completo para la predicción de riesgo de infarto utilizando técnicas de aprendizaje automático. Incluye el preprocesamiento de datos clínicos, entrenamiento de modelos individuales y de ensamble, evaluación de desempeño y despliegue de una aplicación web interactiva con Streamlit.

La solución está orientada a la investigación y aplicación clínica, permitiendo a usuarios cargar datos, seleccionar modelos y obtener predicciones de riesgo de manera sencilla y visual.

---

## Estructura de Carpetas

- **data/**: Contiene los datasets originales, los datos preprocesados y los modelos entrenados (archivos `.joblib`).
- **notebooks/**: Jupyter Notebooks para cada etapa del flujo de trabajo (preprocesamiento, entrenamiento, ensamble, evaluación, despliegue).
- **src/**: Código fuente Python modularizado (preprocesamiento, modelos, evaluación, app web).
- **requirements.txt**: Lista de dependencias necesarias para ejecutar el proyecto.
- **run_all.py**: Script para ejecutar todo el flujo de procesamiento y entrenamiento de manera automatizada.
- **DOCUMENTACION.md**: Este archivo, con la guía completa de uso y configuración.

---

## Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Recomendado: entorno virtual (venv)

---

## Instalación y Configuración

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/caskiuzdev/MachineLearningPython.git
   cd MachineLearningPython/estructura_final
   ```

2. **Crear y activar un entorno virtual (opcional pero recomendado):**
   ```bash
   python -m venv .venv
   # En Windows:
   .venv\Scripts\activate
   # En Linux/Mac:
   source .venv/bin/activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Estructura esperada de archivos:**
   - Los modelos y datos deben estar en la carpeta `data/`.
   - Los notebooks y scripts en sus respectivas carpetas.

---

## Flujo de Trabajo

### 1. Preprocesamiento de Datos
- Ejecutar el notebook `notebooks/1_preprocessing.ipynb` para limpiar, transformar y seleccionar atributos de los datasets clínicos.
- Los datos procesados se guardan en `data/` como archivos `.joblib`.

### 2. Entrenamiento de Modelos Individuales
- Ejecutar `notebooks/2_training_individual_models.ipynb` para entrenar modelos clásicos (Regresión Logística, SVM, Árboles, etc.) sobre cada dataset.
- Los mejores modelos se guardan en `data/`.

### 3. Modelos de Ensamble
- Ejecutar `notebooks/3_ensemble_models.ipynb` para crear y entrenar modelos de ensamble (stacking, voting).

### 4. Evaluación
- Ejecutar `notebooks/4_evaluation.ipynb` para comparar el desempeño de todos los modelos (accuracy, precision, recall, f1, auc).

### 5. Despliegue Web
- Ejecutar `notebooks/5_deployment_streamlit.ipynb` para ver instrucciones y pruebas del despliegue web.

### 6. App Web Interactiva
- Desde la carpeta `estructura_final`, ejecutar:
  ```bash
  streamlit run src/app.py
  ```
- Se abrirá una interfaz web donde se puede seleccionar el modelo, ingresar datos y obtener la predicción de riesgo.

---

## Personalización y Configuración

- **Agregar nuevos modelos:**
  - Editar o agregar funciones en `src/models.py` y actualizar los notebooks de entrenamiento.
- **Modificar variables de entrada:**
  - Cambiar los campos de entrada en `src/app.py` según las variables clínicas de interés.
- **Ajustar hiperparámetros:**
  - Modificar los grids de búsqueda en los notebooks de entrenamiento.
- **Cambiar el idioma o textos:**
  - Todos los textos de la app web pueden editarse en `src/app.py`.
- **Actualizar datasets:**
  - Reemplazar los archivos en `data/` y volver a ejecutar el flujo de preprocesamiento y entrenamiento.

---

## Despliegue en la Nube (Streamlit Cloud)

1. Sube la carpeta `estructura_final` a un repositorio público de GitHub.
2. Ve a [https://streamlit.io/cloud](https://streamlit.io/cloud) y conecta tu cuenta de GitHub.
3. Selecciona el repositorio y el archivo principal `src/app.py`.
4. La app se desplegará y tendrás una URL pública para compartir.

---

## Notas Técnicas

- Los modelos se guardan y cargan con `joblib`.
- El código es modular y fácilmente extensible.
- Los notebooks pueden ejecutarse en Google Colab o localmente.
- La app web está completamente en español y es personalizable.

---

## Créditos y Contacto

Este proyecto fue desarrollado como parte de una tesis de grado. Para dudas, sugerencias o colaboración, contacta al autor a través del repositorio de GitHub.
