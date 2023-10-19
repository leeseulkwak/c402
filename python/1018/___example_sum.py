row=['1', '2', '3', '4', '5']
    

def my_fun(r):
        print("{}전달".format(r))
        sum=0
        for i in r:
                #sum=0은 안됨 for문 밖에서
                i2=int(i)
                print("i는 순환 {} {}".format(i2, type(i)))
                sum+=i2
        print("합은 {}".format(sum))


my_fun(row)

# row=['1', '2', '3', '4', '5']

# def my_fun2(list):
        
#         sum=0

#         for i in list:
#             i2=int(i)
#             sum=sum+i2
#         print(sum)

# my_fun2(row)



#row 함수를 전달하고
#함수에서 리시트의 각 요소를 순환한다.
#순환하면서 얻어진 요소는 문자열이라 숫자로 타입을 변경
#합을 구하는 변수에 하나씩 순환하면 더한다.