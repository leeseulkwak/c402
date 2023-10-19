import csv
import os

current_dir = os.getcwd()
    # 경로를 구분할 때 \\를 사용
csv_file = current_dir + '\\test\\parkarea.csv' # 현재 파일 경로를 설정하여 변수에 연동
print(csv_file)

f = open(csv_file, 'r', encoding='EUC-KR') #변수를 통해서 파일 내용을 읽어 오기
rdr = csv.reader(f)
for line in rdr:
    print(line)