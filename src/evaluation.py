# Evaluación de modelos
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score


def evaluate_model(model, X_test, y_test):
	"""Evalúa un modelo sklearn y retorna métricas principales."""
	y_pred = model.predict(X_test)
	y_proba = model.predict_proba(X_test)[:,1] if hasattr(model, 'predict_proba') else None
	results = {
		'accuracy': accuracy_score(y_test, y_pred),
		'precision': precision_score(y_test, y_pred),
		'recall': recall_score(y_test, y_pred),
		'f1': f1_score(y_test, y_pred),
	}
	if y_proba is not None:
		results['auc'] = roc_auc_score(y_test, y_proba)
	return results
