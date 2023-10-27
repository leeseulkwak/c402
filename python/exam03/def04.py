#문제: 주어진 리스트에서 최댓값과 최솟값을 제외한 나머지 요소의 합을 반환하는 함수 sum_without_extremes를 작성하세요.

list=[322,11,23,2,1,5,73,433]

def sum_without_extremes(lst):
    lst.remove(min(lst))
    lst.remove(max(lst))
    return sum(lst)

print(sum_without_extremes(list))