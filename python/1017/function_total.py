PI=3.14
n=1

#return 값이 없음
def my_add():
    print(my_del())

#실수ㅡㄹ 반환
def my_del():
    cal=n*PI
    return cal

n2 =my_del()
my_add()
print(n2)
