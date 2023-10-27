example_list=["요소A", "요소B", "요소C"]

print(example_list)

print(enumerate(example_list))

print(list(enumerate(example_list)))

for i, value in enumerate(example_list):
    print(i, value)