#문제: 주어진 리스트(임의 입력값을 입력)의 모든 요소의 평균을 반환하는 함수 average를 작성하세요.

list=[1,2,3,4,5]

def average(lst):
    return sum(lst) / len(lst)

print(average(list))


