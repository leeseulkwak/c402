#구구단 출력
#각 단을 가로로 출력

for i in range(1, 10): 
    for j in range(2,10):
        result=j*i
        print(f"{j}x{i}={result}", end='\t') #탭 문자로 구분
    print() # 각 행의 끝에 줄 바꿈 문자 출력