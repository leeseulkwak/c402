
import os
import read
import write

# 파일 읽기
# 합산
# 파일 쓰기

# 파일 읽기
current_dir = os.getcwd()
csv_file = current_dir + '\\project\\file.csv'
list = read.read_file(csv_file)

# 합산
sum = 0
for i in list:
    if type(i) is str:
        i = int(i)
    sum += i

print(list, "의 합은 ", sum)

# 파일 쓰기
text = "sum: {}".format(sum)
write.write_file(text)



