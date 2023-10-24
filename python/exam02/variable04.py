#문제: 사용자로부터 문자열을 입력받아, 그 문자열을 거꾸로 출력하세요.

a=list(input("입력해주세요\n"))

a.reverse()
a2=''.join(a)
print(a2)