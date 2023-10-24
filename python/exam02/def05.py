#문제: 사용자로부터 숫자 n을 입력받아, n! (n 팩토리얼)을 계산하는 함수를 작성하고 실행하세요.



number=int(input("숫자를 입력해주세요\n"))

def fact(n):
    output=1
    for i in range(1, n+1):
        output*=i
    return output

print(fact(number))


