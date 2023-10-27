#데이터 획득
import os
import pandas as pd

cwd = os.getcwd()
df=pd.read_csv(os.path.join(cwd, "1027", "basketball_stat.csv"))

#데이터 샘플 확인
print(df.head())

# #포지션의 개수 확인
print(df.Pos.value_counts())