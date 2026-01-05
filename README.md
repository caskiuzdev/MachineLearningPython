# Proyecto: Predicción de Riesgo de Infarto con Machine Learning

## Estructura
- data/: Datasets originales
- notebooks/: Notebooks para cada etapa del pipeline
- src/: Scripts Python para cada módulo

## Pasos principales
1. Preprocesamiento de datos
2. Entrenamiento de modelos individuales
3. Modelos ensemble (stacking y voting)
4. Evaluación de modelos
5. Despliegue con Streamlit

## Requisitos
Instala dependencias con:
```
pip install -r requirements.txt
```

## Ejecución
- Ejecuta los notebooks en orden para reproducir el pipeline.
- Para la app web:
```
streamlit run src/app.py
```
