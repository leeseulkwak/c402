from operations import add, sub, mul, div


if __name__=="__main__":
    a=int(input("첫번째 숫자를 입력하세요>"))
    b=int(input("첫번째 숫자를 입력하세요>"))

    print(f"{a}+{b}={add.add(a, b)}")
    print(f"{a}-{b}={sub.sub(a, b)}")
    print(f"{a}*{b}={mul.mul(a, b)}")
    print(f"{a}/{b}={div.div(a, b)}")