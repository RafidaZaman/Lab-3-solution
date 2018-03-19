import numpy as np 
import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
clf = LinearDiscriminantAnalysis()

def filename(input):
    with open(input, 'r') as csvfile:
        df = pd.DataFrame.from_csv(csvfile)
        classes = np.array([1, 1, 1, 1, 2, 2, 2])
        data_matrix = df.as_matrix()
        print(data_matrix)
        clf.fit(data_matrix, classes)
        print("Prediction:")
        print(clf.predict([[2.81, 5.46]]))


filename('inputdata1.csv')



