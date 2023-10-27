import os
import csv


#output_1 읽어오기
def read_file(f):
    list = []
    with open(f, mode='r', encoding='utf-8') as file:
        csv_reader=csv.reader(file)
        for row in csv_reader:
            list+= row       
    return list  
    
#output_2 읽어오기
def read_file2(f):
    list = []
    with open(f, mode='r', encoding='utf-8') as file:
        csv_reader=csv.reader(file)
        print(csv_reader)
        for row in csv_reader:
            list+= row 
    return list  

#중복제거
def merge_total(merge):
    
    new_merge=[]
    for value in merge:
        if value not in new_merge:
            new_merge.append(value)

    return new_merge


#연락처 '-'로 구분하기
def change_text(merge):
    
    new_merge=[]
    for value in merge:
        if value not in new_merge:
            new_merge.append(value)

    return new_merge



#모듈로 사용 할때 필요함
#재사용성 : 스크립트를 모듈로 사용할 떄, if__name=='__main__' :
if __name__=='__main__':

    current_dir=os.getcwd() #command work di
    csv_file=current_dir+'\\output_1.csv'
    csv_file2=current_dir+'\\output_2.csv'

    # output_1+output_2 merge함
    merge_info=read_file(csv_file)+read_file2(csv_file2) 
    print(merge_total(merge_info))