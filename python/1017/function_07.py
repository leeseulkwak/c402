def my_fn(a=None, b=None):
    if a==None or b==None:
        return print("두개의 값을 입력")
    c=a+b # 1,2 값을 전달받아
    return c #3을 출력

print(my_fn())
print(my_fn(1,2))