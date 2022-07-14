import pandas as pd
import numpy as np
from sklearn import svm

from sklearn.datasets import load_iris

data = load_iris()

a = [list(flower) for flower in data.data]

print(a)
b = []

for i in range(50):
  b.append('Setosa')
for i in range(50):
  b.append('Versicolor')
for i in range(50):
  b.append('Virginica')

clf = svm.SVC()
clf.fit(a, b)

se_l, se_w, pe_l, pe_w = float(input("Enter in the sepal length: ")), float(input("Enter in the sepal width: ")), float(input("Enter in the petal length: ")), float(input("Enter in the petal width: "))

result = clf.predict([[se_l, se_w, pe_l, pe_w]])
print(result[0])
