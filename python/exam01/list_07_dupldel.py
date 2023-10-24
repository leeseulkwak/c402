#문제: 주어진 리스트에서 중복 값을 제거한 새로운 리스트를 만드세요.
numbers = [1, 2, 2, 3, 4, 4, 5]

result=set(numbers)
print(list(result))



arr = [6, 5, 6, 4, 4, 1, 1, 2, 3, 9, 8, 7, 9, 8, 7]
result = [] # 중복 제거된 값들이 들어갈 리스트

for value in arr:
    if value not in result:
        result.append(value)

print(result)
