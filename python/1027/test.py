# 모델 테스트
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

import learn5 as learn

x_train=learn.x_train
y_train=learn.y_train

test=learn.test
k=learn.k

knn=KNeighborsClassifier(n_neighbors=k)

#knn 모델 학습
knn.fit(x_train, y_train.values.ravel())

#테스트에 사용될 속성 지정
x_test=test[['3P', 'BLK', 'TRB']]

#선수 포지션에 대한 정답을 지정
y_test=test[['Pos']]

#테스트 시작
pred=knn.predict(x_test)

#모델 예측 정확도 출력
print("accuracu:" + str(accuracy_score(y_test.values.ravel(), pred)))

#예측된 값을 출력해 확인
compariwon=pd.DataFrame({'prediction':pred, 'ground_truth': y_test.values.ravel()})
print(compariwon)

