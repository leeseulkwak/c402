#문제: 사용자로부터 5번 숫자를 입력받아, 그 숫자들의 평균을 계산하고 출력하세요.

total=0
for i in range(5):
    number=int(input("숫자를 입력하세요"))
    total+=number

average=total/5
print("평균은 {}".format(average))



# number1=int(input("첫번째 숫자를 입력해주세요\n"))
# number2=int(input("두번째 숫자를 입력해주세요\n"))
# number3=int(input("세번째 숫자를 입력해주세요\n"))
# number4=int(input("네번째 숫자를 입력해주세요\n"))
# number5=int(input("다섯번쨰 숫자를 입력해주세요\n"))


# sum=number1+number2+number3+number4+number5

# average=(sum/5)
# print(average)