# Modelos ensemble (Stacking y Voting)
from sklearn.ensemble import StackingClassifier, VotingClassifier, RandomForestClassifier, GradientBoostingClassifier


def create_stacking_classifier(estimators, final_estimator, cv=10):
	"""Crea un StackingClassifier con los estimadores dados."""
	return StackingClassifier(estimators=estimators, final_estimator=final_estimator, cv=cv)

def create_voting_classifier(estimators, voting='soft'):
	"""Crea un VotingClassifier con los estimadores dados."""
	return VotingClassifier(estimators=estimators, voting=voting)
