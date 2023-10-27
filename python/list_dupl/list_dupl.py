list=["A", "B", "C", "D", "A"]

new_list=[]
for value in list:
    if value not in new_list:
        new_list.append(value)

print(new_list)