#문제: 100 이하의 피보나치 수열을 출력하세요.

a, b = 0, 1
while a <= 100:
    print(a)
    a, b = b, a+b
