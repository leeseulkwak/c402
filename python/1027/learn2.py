#데이터 시각화

import os
import pandas as pd

#데이터의 시각화와 관련된 주요 작업을 seaborn을 통해 수행하면서
#동시에 그래프의 디테일한 조정이나 추가적인 수정을 위해 matplotlib의 기능을 활용

import seaborn as sns
import matplotlib.pyplot as plt

cwd=os.getcwd()
df=pd.read_csv(os.path.join(cwd, "1027", "basketball_stat.csv"))

# sns.lmplot(x='STL', y='2P', data=df, fit_reg=False, scatter_kws={"s":150}, markers=["o", "x"], hue="Pos")
# plt.title("STL and 2P in 2d plane")

# sns.lmplot(x='STL', y='3P', data=df, fit_reg=False, scatter_kws={"s":150}, markers=["o", "x"], hue="Pos")
# plt.title("STL and 3P in 2d plane")

sns.lmplot(x='TRB', y='2P', data=df, fit_reg=True, scatter_kws={"s":150}, markers=["o", "x"], hue="Pos")
plt.title("STL and 2P in 2d plane")



plt.show()

# sns.lmplot(): 데이터 포인트를 2차원 평면에 그리기 위해 사용. 이 함수는 matplotlib의 scatter 플롯 위에 회귀선을 추가하는 기능도 있지만, 여기서는 fit_reg=False로 설정하여 회귀선을 그리지 않았습니다.
# hue="Pos": 카테고리 변수 'Pos'의 값에 따라 포인트의 색상을 구분
# markers=["o", "x"]: 포인트의 마커 모양을 설정
#sns.lmplot(x='BLK', y='3P', data=df, fit_reg=False, scatter_kws={"s":150}, markers=["o", "x"], hue="Pos")
# 그래프의 제목을 설정 plt.title("BLK and 2P in 2d plane")

# 스틸과 2점슛, 어시스트와 2점슛, 블로킹과 3점슛, 리바운드와 3점슛

# 그래프를 화면에 표시


