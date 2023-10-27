#knn파라미터 찾기

import os
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
# import sklearn.neighbors as nb 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

cwd = os.getcwd()

df = pd.read_csv(os.path.join(cwd, "kNN", "data.csv"))

# 20%의 테스트 데이터 분리
train, test = train_test_split(df, test_size=0.1)

print(train)
print(test)

# #최적의 k를 찾기 위해 k의 범위를 3부터 학습 데이터의 절반까지 지정
k_list=[]
#range([start], stop, [step])를 이용하면 3,5,7 
for i in range(1, 9):
    k_list.append(i)
print(k_list)
cross_validation_scores=[]
x_train=train[['LEN']]
y_train=train[['WIT']]

for k in k_list:
    knn = KNeighborsClassifier(n_neighbors=k)
    print(knn)

    scores = cross_val_score(knn, x_train, y_train.values.ravel(), cv=7, scoring='accuracy')
    print(scores)
#     cross_validation_scores.append(scores.mean())
#     print(cross_validation_scores)

# # k=k_list[cross_validation_scores.index(max(cross_validation_scores))]

# if __name__ == "__main__":
#     #k에 따른 정확도를 시각화
#     plt.plot(k_list, cross_validation_scores)
#     plt.xlabel('the number of k')
#     plt.ylabel('Accuracy')
#     plt.show()

#     print(cross_validation_scores)

#     print("가장 적합한 k는 {}이다".format(k))




