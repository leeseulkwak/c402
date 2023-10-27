#문제: 피보나치 수열의 n번째 값을 반환하는 함수 fibonacci를 작성하세요.


def fib(n):
    a,b = 1,1
    if n==1 or n==2:
        return 1
        
    for i in range(1,n):
        a,b = b, a+b

    return a

print(fib(7))