import cal_div
import cal_mul
import cal_sub
import cal_sum


if __name__=='__main__':
    a=cal_sum.sum(1,2)
    b=cal_sub.sub(2,1)
    c=cal_mul.mul(2,2)
    d=int(cal_div.div(2,1))

    print(a, b, c, d)