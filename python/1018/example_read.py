import csv  #프로그래밍 언어의 표준 라이브러리 중 하나인 csv 모듈을 가져오는 명령
import os

# current_dir=os.getcwd()
# #경로를 구분 할 때 \\를 사용
# csv_file=current_dir+'\\1018\\example.csv'

def read_file(f):
    list = []
    #CSV파일 열기
    #파일을 읽기모드(r)로 열고(open) file에 담는다
    with open(f, mode='r') as file:
        # csv.reader 객체 생성
        csv_reader=csv.reader(file)
        print(csv_reader)
        #CSV 파일의 각행을 반복
        for row in csv_reader:
            # l.append(row)   # [[]]  배열이 추가됨
            list+= row # [] 해당 배열에 숫자가 추가됨
        
    return list  #list의 리턴 값은 [1,2]



#모듈로 사용 할때 필요함
#재사용성 : 스크립트를 모듈로 사용할 떄, if__name=='__main__' :
if __name__=='__main__':

    current_dir=os.getcwd() #command work di

    csv_file=current_dir+'\\1018\\example.csv'
    # print(csv_file)

    print('list:', read_file(csv_file))
