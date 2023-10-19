dan = int(input("출력하고 싶은 구구단의 단수를 입력하세요>>"))

# 입력받은 단의 구구단을 출력합니다.
print(f"\n[{dan}단]")
for i in range(1,10):
    print(f"\n{dan} x {i} = {dan*i}")