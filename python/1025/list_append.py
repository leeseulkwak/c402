list_a=[1,2,3]


#####  리스트 맨뒤에 요소 추가하기
list_a.append(4)

list_a.append(5)
print(list_a)




##### 리스트 중간에 요소 추가하기 

list_a.insert(0,100)
print(list_a)


list_a.insert(1,100)
print(list_a)


list_a.insert(6,100)
print(list_a)

list_a.extend([200,200,200])
print(list_a)

del list_a[0]
print(list_a)

list_a.pop(0)
print(list_a)