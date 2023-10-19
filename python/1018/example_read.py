import csv
import os

current_dir=os.getcwd()
#경로를 구분 할 때 \\를 사용
csv_file=current_dir+'\\1018\\example.csv'


def read_file(f):
    list = []
    #CSV파일 열기
    #파일을 읽기모드(r)로 열고(open) file에 담는다
    with open(f, mode='r') as file:

        # csv.reader 객체 생성
        # 읽은 파일의 각행을 반복 가능한 객체로 저장한다.
        csv_reader=csv.reader(file)

        #CSV 파일의 각행을 순회
        for row in csv_reader:
            # l.append(row)   # [[]]  배열이 추가됨
            list+= row # [] 해당 배열에 숫자가 추가됨
        
    return list  #list의 리턴 값은 [1,2]

if __name__=='__main__':

    
    current_dir=os.getcwd()

    csv_file=current_dir+'\\1018\\example.csv'
    print(csv_file)

    print('list:', read_file(csv_file))
