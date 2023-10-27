# 파일 읽기
import os
import read_output
import write_output

current_dir=os.getcwd()
csv_file=current_dir+'\\output_1.csv'
csv_file2=current_dir+'\\output_2.csv'
merge_info=read_output.read_file(csv_file)+read_output.read_file2(csv_file2) 
list=read_output.merge_total(merge_info)

print(list)
print(len(list))

for i in range(len(list)):
    if len(list[i])== 10:
        print(list[i])