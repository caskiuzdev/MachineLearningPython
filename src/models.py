# Modelos individuales
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier


from sklearn.model_selection import GridSearchCV

def train_model(model, X_train, y_train):
	"""Entrena un modelo sklearn."""
	model.fit(X_train, y_train)
	return model

def tune_hyperparameters(model, param_grid, X_train, y_train, cv=10):
	"""Realiza búsqueda de hiperparámetros con GridSearchCV."""
	grid = GridSearchCV(model, param_grid, cv=cv, scoring='accuracy')
	grid.fit(X_train, y_train)
	return grid.best_estimator_, grid.best_params_, grid.best_score_
