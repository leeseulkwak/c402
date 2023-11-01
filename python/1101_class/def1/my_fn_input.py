#계산기

def my_add(n1, n2):
    n3=n1+n2
    return n3

def my_sub(n1, n2):
    n3=n1-n2
    return n3

def my_mul(n1, n2):
    n3=n1*n2
    return n3

def my_div(n1, n2):
    if n2 == 0:
        print("분모는 0이 올 수 없습니다.")
        pass
    else:
        n3=n1/n2
        return n3

if __name__=="__main__":

#사용자로부터 값을 입력 받음
    a=int(input("첫번째 숫자를 입력해주세요>>"))
    b=int(input("두번째 숫자를 입력해주세요>>"))

    print(f"{a}+{b}={my_add(a, b)}")
    print(f"{a}-{b}={my_sub(a, b)}")
    print(f"{a}*{b}={my_mul(a, b)}")
    print(f"{a}/{b}={my_div(a, b)}")