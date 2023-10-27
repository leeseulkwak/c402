#문제: 주어진 정수 n에 대해, n이 소수인지 아닌지를 판별하는 함수 is_prime를 작성하세요.

number=11
def is_prime(n):
    if n<=1:
        return False
    
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

print(is_prime(number))