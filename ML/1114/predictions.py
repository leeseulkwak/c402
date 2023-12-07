import joblib
import pandas as pd
import os
import time

cwd = os.getcwd()

# 저장된 모델 불러오기
loaded_model = joblib.load(os.path.join(cwd, "1114", "svm_model.pkl"))

# 새로운 데이터
new_data = pd.DataFrame({
    '3P': [5, 2, 3],
    'BLK': [1, 0, 2]
})

# 예측 시작 시간 기록
start_time = time.time()

# 모델을 사용한 예측
predictions = loaded_model.predict(new_data)

# 예측 종료 시간 기록
end_time = time.time()

# 소요 시간 계산
elapsed_time = end_time - start_time

# 결과 출력
print("예측된 포지션:", predictions)
print("예측에 소요된 시간: {:.4f}초".format(elapsed_time))
