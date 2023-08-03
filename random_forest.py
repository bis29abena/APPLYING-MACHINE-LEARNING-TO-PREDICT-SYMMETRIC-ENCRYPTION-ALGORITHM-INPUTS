import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt
from generate_data import generate_data
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV


# get your training and testing data
training_data = generate_data(1000)

test_data = generate_data(100)

# define your training and testing data 
X_train = pd.DataFrame([[int(x) for x in list(a)] for (a, b) in training_data])

y_train = pd.DataFrame([int(b) for (a, b) in training_data])

X_test = pd.DataFrame([[int(x) for x in list(a)] for (a, b) in test_data])

y_test = pd.DataFrame([int(b) for (a, b) in test_data])

max_features_range = np.arange(1, 11, 1)
n_estimators_range = np.arange(10, 210, 10)

param_grid = dict(max_features=max_features_range, n_estimators=n_estimators_range)

# print(X_train)
model = RandomForestClassifier()

grid = GridSearchCV(estimator=model, param_grid=param_grid)

grid.fit(X_train, np.array(y_train).ravel())

print(grid.best_params_, grid.best_score_)

