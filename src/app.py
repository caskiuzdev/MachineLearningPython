# Despliegue con Streamlit
import streamlit as st
import joblib
import numpy as np
from pymongo import MongoClient
import shap
import os

# Configuración MongoDB (ajusta tu URI de Atlas aquí)
MONGO_URI = "mongodb+srv://clinica_basededatos:oSasIH5Uq2doFTW0@dbclinico.naipusy.mongodb.net/?appName=DBClinico"
client = MongoClient(MONGO_URI)
db = client["usuarios_app"]
usuarios = db["usuarios"]

st.set_page_config(page_title='Predicción de Riesgo de Infarto', page_icon='❤️')

# --- LANDING PAGE ---
def mostrar_landing():
    st.markdown(
        """
        <style>
        @media (max-width: 600px) {
            .landing-content { font-size: 1em !important; }
            .landing-title { font-size: 2em !important; }
        }
        #MainMenu, header, footer, .stDeployButton, .st-emotion-cache-1avcm0n {display: none !important;}
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown("<h1 class='landing-title' style='text-align:center;color:#1565c0;'>Bienvenido/a a la Predicción de Riesgo de Infarto</h1>", unsafe_allow_html=True)
    st.markdown("<p class='landing-content' style='text-align:center;font-size:1.3em;'>Sistema inteligente para la predicción clínica cardiológica. Inicia sesión o regístrate para continuar.</p>", unsafe_allow_html=True)
    col1, col2 = st.columns([1,1])
    with col1:
        if st.button("INICIAR SESIÓN"):
            st.session_state.pagina = "login"
            st.rerun()
    with col2:
        if st.button("REGISTRARSE"):
            st.session_state.pagina = "registro"
            st.rerun()

def mostrar_login():
    st.markdown("<h2 style='text-align:center;'>Iniciar Sesión</h2>", unsafe_allow_html=True)
    usuario = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")
    if st.button("Entrar"):
        user = usuarios.find_one({"usuario": usuario, "password": password})
        if user:
            st.session_state.usuario = usuario
            st.session_state.pagina = "app"
            st.success("¡Bienvenido/a, {}!".format(usuario))
            st.rerun()
        else:
            st.error("Usuario o contraseña incorrectos.")
    if st.button("Volver"):
        st.session_state.pagina = "inicio"
        st.rerun()

def mostrar_registro():
    st.markdown("<h2 style='text-align:center;'>Registro de Usuario</h2>", unsafe_allow_html=True)
    usuario = st.text_input("Nuevo usuario")
    password = st.text_input("Nueva contraseña", type="password")
    if st.button("Registrar"):
        if usuarios.find_one({"usuario": usuario}):
            st.error("El usuario ya existe.")
        else:
            usuarios.insert_one({"usuario": usuario, "password": password})
            st.success("Usuario registrado correctamente. Ahora puedes iniciar sesión.")
            st.session_state.pagina = "login"
            st.rerun()
    if st.button("Volver"):
        st.session_state.pagina = "inicio"
        st.rerun()

def mostrar_navbar():
    st.markdown(
        f"""
        <div style='background:#1565c0;padding:10px;color:white;display:flex;justify-content:space-between;'>
            <span>Usuario: {st.session_state.usuario}</span>
            <span><a href='#' style='color:white;text-decoration:none;' onclick='window.location.reload()'>Cerrar sesión</a></span>
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("Cerrar sesión"):
        st.session_state.usuario = None
        st.session_state.pagina = "inicio"
        st.rerun()

def mostrar_app():
    mostrar_navbar()
    st.markdown("<h2 style='text-align:center;'>Predicción de Riesgo de Infarto</h2>", unsafe_allow_html=True)
    model_option = st.selectbox('Selecciona el modelo de predicción:', ['Modelo Dataset 1', 'Modelo Dataset 2', 'Modelo Dataset 3'])
    if model_option == 'Modelo Dataset 1':
        age = st.number_input('Edad (años)', min_value=0, max_value=120, value=50)
        gender = st.selectbox('Género biológico', ['Masculino', 'Femenino'])
        ckmb = st.number_input('CK-MB (U/L)', min_value=0.0, value=10.0)
        troponina = st.number_input('Troponina (ng/mL)', min_value=0.0, value=0.5)
        input_data = np.array([[age, 1 if gender=='Masculino' else 0, ckmb, troponina]])
    elif model_option == 'Modelo Dataset 2':
        exang = st.number_input('¿Angina inducida por ejercicio? (0=No, 1=Sí)', min_value=0, max_value=1, value=0)
        cp = st.number_input('Tipo de dolor de pecho (0-3)', min_value=0, max_value=3, value=0)
        oldpeak = st.number_input('Descenso del ST (oldpeak)', min_value=0.0, value=1.0)
        thalach = st.number_input('Frecuencia cardíaca máxima (thalach)', min_value=0, value=150)
        ca = st.number_input('Número de vasos principales (CA)', min_value=0, max_value=4, value=0)
        input_data = np.array([[exang, cp, oldpeak, thalach, ca]])
    else:
        time = st.number_input('Tiempo de seguimiento (días)', min_value=0, value=100)
        ejection_fraction = st.number_input('Fracción de eyección (%)', min_value=0, max_value=100, value=40)
        serum_creatinine = st.number_input('Creatinina sérica (mg/dL)', min_value=0.0, value=1.0)
        serum_sodium = st.number_input('Sodio sérico (mmol/L)', min_value=0, value=135)
        age = st.number_input('Edad (años)', min_value=0, max_value=120, value=60)
        input_data = np.array([[time, ejection_fraction, serum_creatinine, serum_sodium, age]])

    # --- Botón de predicción arriba ---
    if st.button('Predecir'):
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

    # Mostrar métricas de desempeño del modelo seleccionado
    st.markdown("### Métricas de desempeño del modelo (test interno)")
    metrics_path = None
    if model_option == 'Modelo Dataset 1':
        metrics_path = os.path.join('data', 'dataset1_metrics.joblib')
    elif model_option == 'Modelo Dataset 2':
        metrics_path = os.path.join('data', 'dataset2_metrics.joblib')
    else:
        metrics_path = os.path.join('data', 'dataset3_metrics.joblib')
    if os.path.exists(metrics_path):
        metrics = joblib.load(metrics_path)
        st.table({
            'Métrica': list(metrics.keys()),
            'Valor': [f"{v:.3f}" if isinstance(v, float) else v for v in metrics.values()]
        })
    else:
        st.info("No se encontraron métricas guardadas para este modelo.\n\nPara generarlas, ejecuta el notebook '4_evaluation.ipynb' desde Jupyter Notebook o VS Code. Esto calculará y guardará las métricas automáticamente.")

    # Mostrar validación externa si existe
    ext_metrics_path = metrics_path.replace('.joblib', '_external.joblib')
    if os.path.exists(ext_metrics_path):
        st.markdown("### Validación externa (dataset externo)")
        ext_metrics = joblib.load(ext_metrics_path)
        st.table({k: [f"{v:.3f}" if isinstance(v, float) else v] for k, v in ext_metrics.items()})

    # Interpretabilidad con SHAP
    st.markdown("### Interpretabilidad: Importancia de variables (SHAP)")
    st.write("Esta gráfica muestra qué variables clínicas tienen mayor impacto en la predicción del modelo. Cuanto más a la derecha esté una variable, más importante es para la decisión del modelo. El color indica si el valor de la variable es alto (rojo) o bajo (azul).")
    try:
        import matplotlib
        matplotlib.use('Agg')  # Forzar backend compatible con Streamlit
        import matplotlib.pyplot as plt
        if model_option == 'Modelo Dataset 1':
            X_train = joblib.load(os.path.join('data', 'dataset1_processed.joblib'))[0]
        elif model_option == 'Modelo Dataset 2':
            X_train = joblib.load(os.path.join('data', 'dataset2_processed.joblib'))[0]
        else:
            X_train = joblib.load(os.path.join('data', 'dataset3_processed.joblib'))[0]
        model = joblib.load(metrics_path.replace('_metrics.joblib', '_best_model.joblib'))
        import sklearn
        tree_classes = (
            getattr(sklearn.ensemble, 'RandomForestClassifier', None),
            getattr(sklearn.ensemble, 'GradientBoostingClassifier', None),
            getattr(sklearn.tree, 'DecisionTreeClassifier', None),
        )
        try:
            if any(isinstance(model, cls) for cls in tree_classes if cls is not None):
                explainer = shap.TreeExplainer(model)
                shap_values = explainer.shap_values(X_train)
                data_to_plot = X_train
            else:
                # Para modelos como SVC, KNN, etc.
                if hasattr(model, 'predict_proba'):
                    f = model.predict_proba
                else:
                    f = model.predict
                # Usar un sampleo mayor pero seguro
                sample = shap.sample(X_train, min(200, X_train.shape[0]))
                explainer = shap.KernelExplainer(f, sample)
                shap_values = explainer.shap_values(sample)
                data_to_plot = sample
            plt.figure(figsize=(8, 4))
            shap.summary_plot(shap_values, data_to_plot, show=False, plot_size=(8,4), color_bar=True)
            plt.gca().set_facecolor('#222222')
            plt.gcf().patch.set_facecolor('#222222')
            st.pyplot(plt.gcf())
            plt.close()
        except Exception as e:
            st.info(f"No se pudo mostrar la interpretabilidad SHAP: {e}")
    except Exception as e:
        st.info(f"No se pudo mostrar la interpretabilidad SHAP: {e}")

# --- CONTROL DE FLUJO ---
if "pagina" not in st.session_state:
    st.session_state.pagina = "inicio"
if "usuario" not in st.session_state:
    st.session_state.usuario = None

if st.session_state.usuario is None:
    if st.session_state.pagina == "login":
        mostrar_login()
    elif st.session_state.pagina == "registro":
        mostrar_registro()
    else:
        st.session_state.pagina = "inicio"
        mostrar_landing()
else:
    st.session_state.pagina = "app"
    mostrar_app()