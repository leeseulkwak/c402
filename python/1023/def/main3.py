import cal_sum
import cal_sub
import cal_mul
import cal_div


x=int(input("수식을 입력하세요\n"))
y=str(input())
z=int(input())


if __name__=='__main__':

    if y == '+':
        a= x+z

    elif  y =='-':
        b=x-z

    elif  y =='*':
        c=x*z

    elif y =="/":
        d=x/z

    else:
        print("종료")
    
    # a=cal_sum.sum(x, y)
    # b=cal_sub.sub(x, y)
    # c=cal_mul.mul(x, y)
    # d=int(cal_div.div(x, y))

    print(a, b, c, d)