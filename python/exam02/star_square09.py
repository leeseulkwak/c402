#문제: 사용자로부터 숫자 n을 입력받아, 별(*)로 이루어진 n x n 크기의 정사각형을 출력하세요.

n=int(input("숫자를 입력해주세요\n"))
for i in range(n):
    print('*'*n)