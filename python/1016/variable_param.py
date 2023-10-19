def print_n_times(n, *values):
    #n번 반복합니다.
    for i in range(n):
        #values는 리스트처럼 활용 합니다.
        for value in values:
            print(value)
        
        print()

print_n_times(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")