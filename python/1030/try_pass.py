list_input_a=["52", "273", "32", "스파이", "103"]

list_number=[]
for item in list_input_a: #숫자로 변환해서 리스트에 추가
    try:
        float(item)
        list_number.append(item)
        #여러가지 예외 사항이 발생 할 수 있다.
    except:
        #모든 예외 사항 처리
        pass

print("{} 내부에 있는 숫자는".format(list_input_a))
print("{}입니다.".format(list_number))