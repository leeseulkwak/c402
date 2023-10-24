import random

# print(random.choice("abc"))

#print(random.randint(1, 10))

#print(range(1, 10))


# import random
# menu_list = ['IA,HA,CP']
# random_element = random.choice(menu_list)
# print(random_element)



users=range(1,101)
users=list(users)


menu=('아아', '핫아', '카푸치노')
menu_ok=random.choice(menu)

print("{}, {}에 당첨되었습니다.". format(users, menu_ok))
