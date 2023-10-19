

def flatten():
    output = []
    for i in lst:
        if type(i) == list:
            # 차원가소 후 append
            # [] + [2]
            output = output + flatten(i)
        else:
            # [].append(1)
            output.append(i)

lst = [1,[2],[1,[3]]]
print(flatten(lst))

# >>> [1] + [2]
# [1, 2]
