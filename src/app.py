# Despliegue con Streamlit
import streamlit as st


import joblib
import numpy as np


st.set_page_config(page_title='Predicción de Riesgo de Infarto', page_icon='❤️')
st.title('Predicción de riesgo de infarto')
st.write('Bienvenido/a. Esta aplicación permite predecir el riesgo de infarto a partir de tus datos clínicos usando modelos de inteligencia artificial entrenados.')

# Selección de modelo y dataset
model_option = st.selectbox('Selecciona el modelo de predicción:', ['Modelo Dataset 1', 'Modelo Dataset 2', 'Modelo Dataset 3'])

# Ingreso de datos (ajustar según variables de cada dataset)
if model_option == 'Modelo Dataset 1':
	age = st.number_input('Edad (años)', min_value=0, max_value=120, value=50)
	gender = st.selectbox('Género biológico', ['Masculino', 'Femenino'])
	ckmb = st.number_input('CK-MB (U/L)', min_value=0.0, value=10.0)
	troponina = st.number_input('Troponina (ng/mL)', min_value=0.0, value=0.5)
	# ...otros inputs según dataset 1
	input_data = np.array([[age, 1 if gender=='Masculino' else 0, ckmb, troponina]])
elif model_option == 'Modelo Dataset 2':
	exang = st.number_input('¿Angina inducida por ejercicio? (0=No, 1=Sí)', min_value=0, max_value=1, value=0)
	cp = st.number_input('Tipo de dolor de pecho (0-3)', min_value=0, max_value=3, value=0)
	oldpeak = st.number_input('Descenso del ST (oldpeak)', min_value=0.0, value=1.0)
	thalach = st.number_input('Frecuencia cardíaca máxima (thalach)', min_value=0, value=150)
	ca = st.number_input('Número de vasos principales (CA)', min_value=0, max_value=4, value=0)
	# ...otros inputs según dataset 2
	input_data = np.array([[exang, cp, oldpeak, thalach, ca]])
else:
	time = st.number_input('Tiempo de seguimiento (días)', min_value=0, value=100)
	ejection_fraction = st.number_input('Fracción de eyección (%)', min_value=0, max_value=100, value=40)
	serum_creatinine = st.number_input('Creatinina sérica (mg/dL)', min_value=0.0, value=1.0)
	serum_sodium = st.number_input('Sodio sérico (mmol/L)', min_value=0, value=135)
	age = st.number_input('Edad (años)', min_value=0, max_value=120, value=60)
	# ...otros inputs según dataset 3
	input_data = np.array([[time, ejection_fraction, serum_creatinine, serum_sodium, age]])

# Botón para predecir (requiere modelo entrenado y cargado)
if st.button('Predecir'):
	# Selección del modelo a cargar
	if model_option == 'Modelo Dataset 1':
		model_path = 'data/dataset1_best_model.joblib'
	elif model_option == 'Modelo Dataset 2':
		model_path = 'data/dataset2_best_model.joblib'
	else:
		model_path = 'data/dataset3_best_model.joblib'

	try:
		model = joblib.load(model_path)
		pred = model.predict(input_data)
		prob = model.predict_proba(input_data) if hasattr(model, 'predict_proba') else None
		st.success(f'Resultado: {"ALTO RIESGO" if pred[0] else "BAJO RIESGO"}')
		if prob is not None:
			st.write(f'Probabilidad de alto riesgo: {prob[0][1]*100:.1f}%')
	except Exception as e:
		st.error(f'Ocurrió un error al cargar o usar el modelo: {e}')
	# model = joblib.load('ruta_al_modelo_entrenado.joblib')
	# pred = model.predict(input_data)
	# st.write('Predicción:', pred)
