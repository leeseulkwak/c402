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

    print(my_add(1, 2))
    print(my_sub(1, 2))
    print(my_mul(1, 2))
    print(my_div(1, 2))