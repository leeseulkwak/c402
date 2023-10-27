#문제: 주어진 리스트를 입력받아, 리스트의 모든 연속된 부분 리스트(sublist)를 반환하는 함수 all_sublists를 작성하세요.

list=[1,2,3,4,5,6,7,8,9,10,11,12,13]

def all_sublists(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)+1):
         return lst[i:j]

print(all_sublists(list))