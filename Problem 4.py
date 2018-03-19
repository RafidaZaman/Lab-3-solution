from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

iris = load_iris()

# X = features and y = response
X = iris.data
y = iris.target
print(iris)
knn = KNeighborsClassifier(n_neighbors=50)
knn.fit(X, y)
y_pred = knn.predict(X)
print("Accuracy:")
print(metrics.accuracy_score(y, y_pred))