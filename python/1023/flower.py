import numpy as np
from sklearn.neighbors import KNeighborsClassifier

X=np.array([[5.1, 3.5], 
                [4.9, 3.0], 
                [6.0, 3.0], 
                [6.2, 2.8], 
                [5.5, 2.3], 
                [6.3, 3.3],
                [5.8, 2.7], 
                [6.7, 3.0]])


#꽃의 종류 (0: setosa, 1:versicolor)
y=np.array([0, 0, 1, 1, 1, 0, 1, 0])

#KNN 모델 생성(K=3으로 설정)
knn=KNeighborsClassifier(n_neighbors=3)

#모델 학습
knn.fit(X, y)

new_flower=np.array([[5.4, 2.8]])
predicted_class=knn.predict(new_flower)

if predicted_class[0]==0:
    print("Setosa 꽃입니다.")
else:
    print("Versicolor 꽃입니다.")