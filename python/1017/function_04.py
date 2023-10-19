# 매개 변수의 기본값 지정을 권장

def print_ntimes(value="blank", n=2):
    for i in range(n):
        print(value)
     
print_ntimes()
print_ntimes("a")
print_ntimes(3) # n의 매개 변수가 아님. 3을 2번 출력
print_ntimes(n=3) # n의 매개 변수가 아님.