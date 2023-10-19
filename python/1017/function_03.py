def print_ntimes(n, *values):
    for i in range(n):
        for value in values:
            print(value)
        print("==")

#print_ntimes(3)
print_ntimes(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")