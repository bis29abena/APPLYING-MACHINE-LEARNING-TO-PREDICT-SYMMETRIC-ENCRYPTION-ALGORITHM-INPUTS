import numpy as np
from xgboost import XGBClassifier, plot_tree
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt
from generate_data import generate_data


# get your training and testing data
training_data = generate_data(1000)

test_data = generate_data(100)

# define your training and testing data 
X_train = pd.DataFrame([[int(x) for x in list(a)] for (a, b) in training_data])

y_train = pd.DataFrame([int(b) for (a, b) in training_data])

X_test = pd.DataFrame([[int(x) for x in list(a)] for (a, b) in test_data])

y_test = pd.DataFrame([int(b) for (a, b) in test_data])


# fit model on training data

model = XGBClassifier()

model.fit(X_train, y_train)

# make prdictions on test data
predictions = model.predict(X_test)

# evalute predictions
accuracy = accuracy_score(y_test, predictions)

print(f"Accuracy Score: {round(accuracy * 100.0, 2)}%")

# getting a confusion matrix
cm = confusion_matrix(y_test, predictions)

print("Confusion Matrix")
print(cm)

plot_tree(model)

plt.show()