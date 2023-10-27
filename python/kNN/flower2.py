#데이터 획득
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

cwd = os.getcwd()
df=pd.read_csv(os.path.join(cwd, "kNN", "data.csv"))

#데이터 샘플 확인
print(df.head())

# ## 포지션의 개수 확인
print(df.Kind.value_counts())


sns.lmplot(x='LEN', y='WIT', data=df, fit_reg=True, scatter_kws={"s":150}, markers=["o", "x"], hue="Kind")
plt.title("LEN and WIT")

plt.show()

