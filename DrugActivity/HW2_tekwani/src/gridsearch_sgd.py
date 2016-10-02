from time import  time
import numpy as np
from sklearn.metrics import make_scorer, f1_score, classification_report
from sklearn import grid_search
from sklearn.linear_model import SGDClassifier
from feature_creation import X_train, y_train

clf = SGDClassifier()

parameters = [
                {'n_iter': [4000, 10000, 12000, 15000, 170000],
                 'penalty': ['l2', 'l1', 'elasticnet'],
                 'loss': ['hinge', 'log', 'perceptron', 'modified_huber'],
                 'alpha': [0.04, 0.07, 0.08, 0.09],
                 'shuffle': [True],
                 'class_weight': [{1:0.9, 0:0.1}, 'balanced'],
                 'learning_rate': ['optimal'],
                 'warm_start': [False]
                 }
            ]


start = time()
f1_scorer = make_scorer(f1_score)
gs = grid_search.GridSearchCV(clf, parameters, scoring=f1_scorer, n_jobs=-1)
gs.fit(X_train, y_train)

print "Grid scores: --------"
print gs.grid_scores_
print "Best estimator----"
print gs.best_estimator_
print "Best params ----"
print gs.best_params_
print "Best score: ", gs.best_score_
print "Finished in: ", (time() - start)


