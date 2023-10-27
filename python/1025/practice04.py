numbers=[273, 103, 5, 32, 65, 9, 72, 800, 99]

for i in numbers:  #리스트 값을 읽어 오기
    print(type(i), type(numbers))
    print("{}는 {} 자릿수입니다.".format(i, len(str(i))))