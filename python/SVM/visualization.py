import numpy as np
import matplotlib.pyplot as plt

import svc_param_selection

from sklearn.svm import SVC

# svc_param_selection에서 미리 학습된 SVM 분류기와 학습 데이터를 가져옴
clf = svc_param_selection.clf
train = svc_param_selection.train

# 시각화를 하기 위해, 최적의 C와 최적의 C를 비교하기 위한 다른 C를 후보로 저장합니다.
C_canditates = []
C_canditates.append(clf.best_params_['C'] * 0.01)
C_canditates.append(clf.best_params_['C'])
C_canditates.append(clf.best_params_['C'] * 100)

# 시각화를 하기 위해, 최적의 gamma와 최적의 gamma를 비교하기 위한 다른 gamma를 후보로 저장합니다.
gamma_candidates = []
gamma_candidates.append(clf.best_params_['gamma'] * 0.01)
gamma_candidates.append(clf.best_params_['gamma'])
gamma_candidates.append(clf.best_params_['gamma'] * 100)

X = train[['3P', 'BLK']]
Y = train['Pos'].tolist()

# 포지션에 해당하는 문자열 SG와 C를 벡터화합니다.
position = []
for gt in Y:
    if gt == 'C':
        position.append(0)
    else:
        position.append(1)

# 각각의 파라미터에 해당하는 SVM 모델을 만들어 classifiers에 저장합니다.
classifiers = []
for C in C_canditates:
    for gamma in gamma_candidates:
        clf = SVC(C=C, gamma=gamma)
        clf.fit(X.values, Y)
        classifiers.append((C, gamma, clf))

# 18,18 사이즈의 챠트를 구성합니다.
plt.figure(figsize=(18, 18))
# meshgrid()는 두 개의 1-D 배열을 입력 받아서 가능한 모든 조합의 2-D 좌표들을 생성
# np.linspace()는 주어진 시작 값과 끝 값을 포함한 지정된 개수의 값들로 구성된 균일한 간격의 배열을 생성하는 NumPy 함수
# 여기서는 0에서 4까지의 구간을 균일하게 100개의 값으로 나눈 배열을 생성하며, 이 배열은 0, 0.0404, 0.0808, ..., 4와 같이 100개의 값으로 구성
xx, yy = np.meshgrid(np.linspace(0, 4, 100), np.linspace(0, 4, 100))

# 각각의 모델들에 대한 결정 경계 함수를 적용하여 함께 시각화합니다.
for (k, (C, gamma, clf)) in enumerate(classifiers):
    Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    # 최적의 모델을 포함한 다른 파라미터로 학습된 모델들을 함께 시각화해봅니다.
    plt.subplot(len(C_canditates), len(gamma_candidates), k + 1)
    plt.title("gamma=10^%d, C=10^%d" % (np.log10(gamma), np.log10(C)),
              size='medium')

    # 서포트 벡터와 결정경계선을 시각화합니다.
    plt.pcolormesh(xx, yy, -Z, cmap=plt.cm.RdBu)
    plt.scatter(X['3P'], X['BLK'], c=position, cmap=plt.cm.RdBu_r, edgecolors='k')

# 그림 표시
plt.show()
