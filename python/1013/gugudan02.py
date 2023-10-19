#3개의 그리드로 나누어 출력
#1~9까지의 숫자에 대한 반복

for i in range(1,10):
    #2~4단 출력
    for j in range(2,5):
        print(f"{j}*{i}={j*i}", end="\t")
    print("", end="\t")

# 5~7단 출력
    for j in range(5, 8):
        print(f"{j} x {i} = {j*i}", end="\t")
    print("", end="\t")
    
# 8~9단 출력
    for j in range(8, 10):
        print(f"{j} x {i} = {j*i}", end="\t")
    print("\n")
