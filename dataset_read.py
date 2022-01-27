import pandas as pd
dataset = pd.read_csv('winequality-red.csv', sep=';')
x = dataset.iloc[:, 0:11]
y = dataset.iloc[:, -1]
print(dataset, "\n")
print(x, "\n")
print(y, "\n")
X = x.values
Y = y.values
print(X, "\n")
print(Y, "\n")
