#문제: 주어진 딕셔너리에서 'apple'의 값을 출력하세요.

fruits={"apple" : 10, "banana" : 5, "cherry" : 7}


# #키  출력
# for key in fruits.keys():  
#     print(key)
# #리스트로 전환하여 출력
# print(list(fruits.keys()))


# #값  출력
# for value in fruits.values():
#     print(value)
# #리스트로 전환하여 출력
# print(list(fruits.values()))

#apple의 키 값 출력
# values=list(fruits.values())
# print(values[0])

# for key, value in fruits.items():
#     if key=='apple':
#         print(value)

print(fruits["apple"])