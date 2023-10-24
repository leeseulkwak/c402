import cal_div
import cal_mul
import cal_sub
import cal_sum


x=int(input())
y=int(input())

if __name__=='__main__':
    a=cal_sum.sum(x, y)
    b=cal_sub.sub(y, x)
    c=cal_mul.mul(y, y)
    d=int(cal_div.div(y, x))

    print(a, b, c, d)