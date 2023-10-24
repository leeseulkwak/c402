import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import KFold, cross_val_score

# 데이터 로드
data = """
5.1,3.5,Setosa
4.9,3.0,Setosa
6.0,3.0,Versicolor
6.2,2.8,Versicolor
5.5,2.3,Versicolor
6.3,3.3,Setosa
5.8,2.7,Versicolor
6.7,3.0,Setosa
"""
lines = data.strip().split('\n')
print(lines)
samples = [line.split(',') for line in lines]
print(samples)

# 데이터를 feature와 label로 분리
X = np.array([[float(sample[0]), float(sample[1])] for sample in samples])
print(X)
y = np.array([sample[2] for sample in samples])
print(y)

# k값 범위 설정 (예: 1~7, 데이터 개수가 8개이므로 최대 7까지 설정)
k_values = list(range(1, 8))
best_k = k_values[0]
best_score = 0

# 5-fold 교차 검증
kf = KFold(n_splits=5, shuffle=True, random_state=42)

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X, y, cv=kf, scoring="accuracy")
    mean_score = scores.mean()
    
    if mean_score > best_score:
        best_score = mean_score
        best_k = k
        
    print(f"k = {k}, Accuracy: {mean_score * 100:.2f}%")

print(f"Best k value is {best_k} with accuracy of {best_score * 100:.2f}%")


