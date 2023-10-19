num = [0, 1, 0]
i = 0
n = 2
i = int(input("피보나치 수열의 몇번째 숫자를 출력하시겠습니까? : "))

if i >= 2:
    print(f"{num[0]} + 0 = {num[2]}")
    while n <= i:
       num[2] = num[1] + num[0]
       print(f"{num[0]} + {num[1]} = {num[2]}")
       num[0] = num[1]
       num[1] = num[2]
       n += 1
else:
    print("Error : 2 이상의 자연수를 입력해주세요.")

print(f"\n{i}번째 피보나치 수열의 값은 {num[2]}입니다.")