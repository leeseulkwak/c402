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

df = pd.read_csv(os.path.join(cwd, "1027", "basketball_stat.csv"))

# 데이터에서 분별력이 없는 특징(feature) 제거
df.drop(['2P', 'AST', 'STL'], axis=1, inplace=True)

# 20%의 테스트 데이터 분리
train, test = train_test_split(df, test_size=0.2)


#최적의 k를 찾기 위해 k의 범위를 3부터 학습 데이터의 절반까지 지정
max_k_range = train.shape[0] // 2
k_list=[]

#range([start], stop, [step])를 이용하면 3,5,7 
for i in range(3, max_k_range, 2):
    k_list.append(i)

print(k_list)

cross_validation_scores=[]
x_train=train[['3P', 'BLK', 'TRB']]
y_train=train[['Pos']]

for k in k_list:
    knn = KNeighborsClassifier(n_neighbors=k)
    #print(knn)
    scores = cross_val_score(knn, x_train, y_train.values.ravel(), cv=10, scoring='accuracy')
    print(scores)
#     cross_validation_scores.append(scores.mean())

# k=k_list[cross_validation_scores.index(max(cross_validation_scores))]

# if __name__ == "__main__":
#     #k에 따른 정확도를 시각화
#     plt.plot(k_list, cross_validation_scores)
#     plt.xlabel('the number of k')
#     plt.ylabel('Accuracy')
#     plt.show()

#     print(cross_validation_scores)

#     print("가장 적합한 k는 {}이다".format(k))




