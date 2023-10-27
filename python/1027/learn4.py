#데이터 나누기
import os
import pandas as pd

from sklearn.model_selection import train_test_split

cwd=os.getcwd()
df=pd.read_csv(os.path.join(cwd, "1027", "basketball_stat.csv"))

# 데이터에서 분별력이 없는 특징(feature) 제거
df.drop(['2P', 'AST', 'STL'], axis=1, inplace=True)


# 20%의 테스트 데이터 분리
train, test=train_test_split(df, test_size=0.2)
print(train.shape[0])
print(test.shape[0])