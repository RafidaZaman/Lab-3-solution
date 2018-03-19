
import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
X =[]
y =[]
def get_data(filename):
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)

        for row in csvFileReader:

            X.append(int(row[0]))
            y.append(int(row[1]))

    print("Data:")
    print(X)
    print(y)
    plt.scatter(X,y)

    print("20% test and 80% training data:")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
    print(X_train)
    print(y_train)
    print(train_test_split(y, shuffle=False))


get_data('file.csv')


