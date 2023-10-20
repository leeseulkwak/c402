# 파일 읽기
import os
import example_read
import example_wirte

current_dir=os.getcwd()
# dir_name="1018"
# file_name="example.csv"
# #경로를 구분 할 때 \\를 사용
csv_file=current_dir+'\\1018\\example.csv'
list=example_read.read_file(csv_file)

# 합산
sum=0
for i in list:
    if type(i) is str:
        i=int(i)
    sum += i

print(list, "의 합은", sum)


# 파일 쓰기
text="sum:{}".format(sum)
example_wirte.write_file(text)