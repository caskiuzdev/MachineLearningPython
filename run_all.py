import os
import subprocess

# Ejecutar los notebooks en orden
def run_notebooks():
    notebooks = [
        "notebooks/1_preprocessing.ipynb",
        "notebooks/2_training_individual_models.ipynb",
        "notebooks/3_ensemble_models.ipynb",
        "notebooks/4_evaluation.ipynb"
    ]
    for nb in notebooks:
        print(f"Ejecutando {nb} ...")
        os.system(f"jupyter nbconvert --to notebook --inplace --execute {nb}")
    print("¡Todos los notebooks ejecutados correctamente!")

# Lanzar la app web de Streamlit
def run_streamlit():
    print("Iniciando la app web de Streamlit...")
    subprocess.run(["streamlit", "run", "src/app.py"])

if __name__ == "__main__":
    run_notebooks()
    run_streamlit()
