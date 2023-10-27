numbers=[273, 103, 5, 32, 65, 9, 72, 800, 99]

for i in numbers:  #리스트 값을 읽어 오기
    if i % 2 ==0:
        print("{}는 짝수입니다.".format(i))
    else: 
        print("{}는 홀수입니다".format(i))