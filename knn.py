from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
irisDataset=load_iris()
a= irisDataset.data
b= irisDataset.target
train_a,test_a,train_b,test_b = train_test_split(a,b,test_size = 0.3, random_state =42)
knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(train_a,train_b)
c=knn.predict(test_a)
print(c)

