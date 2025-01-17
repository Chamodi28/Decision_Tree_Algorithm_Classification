import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree

path = '/content/Decision_Tree_ Dataset.csv'
balance_data = pd.read_csv(path, sep= ',', header= 0)

print ("Dataset Lenght:: "), len(balance_data)
print ("Dataset Shape:: "), balance_data.shape

balance_data.head()

X = balance_data.values[:, 0:4]
Y = balance_data.values[:, 4]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3,random_state=100)
entropy = DecisionTreeClassifier(criterion = "entropy", random_state = 100, max_depth = 3, min_samples_leaf = 5)
entropy.fit(X_train, Y_train)

Y_predict = entropy.predict(X_test)

print(accuracy_score(Y_test, Y_predict)*100)

print(entropy.predict([[385,14079,594,4944]]))

print(entropy.predict([[205,10016,395,3044]]))
