import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt
from generate_data import generate_data
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import GridSearchCV


# get your training and testing data
training_data = generate_data(1000)

test_data = generate_data(100)

# define your training and testing data 
X_train = pd.DataFrame([[int(x) for x in list(a)] for (a, b) in training_data])

y_train = pd.DataFrame([int(b) for (a, b) in training_data])

X_test = pd.DataFrame([[int(x) for x in list(a)] for (a, b) in test_data])

y_test = pd.DataFrame([int(b) for (a, b) in test_data])

list_penalty = ["l1", "l2", "elasticnet", None]
list_alpha = np.arange(0.001, 1,)

param_grid = dict(penalty=list_penalty, alpha=list_alpha)

model = SGDClassifier()

grid = GridSearchCV(estimator=model, param_grid=param_grid, cv=5)

grid.fit(X_train, np.array(y_train).ravel())

print(grid.best_params_, grid.best_score_)

# model.fit(X_train, np.array(y_train).ravel())

# y_pred = model.predict(X_test)

# print(accuracy_score(y_test, y_pred))