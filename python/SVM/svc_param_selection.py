import os
import pandas as pd

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

cwd=os.getcwd()
df=pd.read_csv(os.path.join(cwd, "SVM", "basketball_stat.csv"))

# 20%의 테스트 데이터 분리
train,test=train_test_split(df, test_size=0.2)

def svc_param_selection(X, y, nfolds):
    #탐색하려는 파라미터의 범위를 정의하는 리스트
    #kernel:사용할 커널의 종류
    #gamma:RBF 커널의 매개변수로 여기서는 6가지 값에 대해 탐색
    #C:SVM의 규제 파라미터로 6가지 값에 대해 탐색

    svm_parameters=[
        {'kernel':['rbf'],
         'gamma':[0.00001, 0.00001, 0.001, 0.01, 0.1, 1],
         'C':[0.01, 0.1, 1, 10, 100, 1000]
         }
    ]

    # GridSearchCV: Scikit-learn의 모델 선택 모듈에 있는 클래스
    # 주어진 파라미터 범위 내에서 가장 좋은 성능을 나타내는 파라미터 조합을 찾는다.
    # SVC(): SVM 분류기 객체
    # svm_parameters: 탐색할 파라미터의 범위
    # cv=10: 10-fold cross-validation을 사용
    clf = GridSearchCV(SVC(), svm_parameters, cv=nfolds)

    # GridSearchCV 객체를 학습 데이터에 맞춰 학습
    # X_train과 y_train 데이터를 사용
    # y_train.values.ravel()을 통해 y_train 값을 1D 배열로 만들어 준다
    clf.fit(X, y)

    print(clf.best_params_)
    
    # 함수의 반환 값은 clf, 즉 학습된 GridSearchCV 객체이다.
    return clf


X_train = train[['3P', 'BLK']]
y_train = train[['Pos']]

# 최적의 파라미터를 sklearn의 gridsearch를 통해 구합니다.
clf = svc_param_selection(X_train, y_train.values.ravel(), 10)
