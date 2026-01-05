# Preprocesamiento de los tres datasets

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from scipy.stats.mstats import winsorize

def load_dataset(path):
    return pd.read_csv(path)


def clean_data(df):
    """Elimina duplicados y filas con valores nulos."""
    df = df.drop_duplicates()
    df = df.dropna()
    return df

def winsorize_columns(df, columns, limits=(0.01, 0.01)):
    """Aplica winsorización a columnas continuas."""
    for col in columns:
        df[col] = winsorize(df[col], limits=limits)
    return df

def log_transform_columns(df, columns):
    """Aplica log1p a columnas seleccionadas."""
    for col in columns:
        df[col] = np.log1p(df[col])
    return df

def select_features_anova(X, y, k=5):
    """Selecciona las k mejores características usando ANOVA F-score."""
    from sklearn.feature_selection import SelectKBest, f_classif
    selector = SelectKBest(score_func=f_classif, k=k)
    X_new = selector.fit_transform(X, y)
    selected_features = X.columns[selector.get_support(indices=True)]
    return X_new, selected_features

def normalize_data(X_train, X_test):
    """Normaliza los datos usando StandardScaler (solo ajusta en train)."""
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled, scaler
