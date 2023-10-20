import csv
import os

def read_file(f):
    list=[]
    with open(f, mode="r") as file:
        csv_reader=csv.reader(file)

        for i in csv_reader:
            list+=i
    return list

if __name__=="__main__":
 
    current_dir=os.getcwd()
    csv_file=current_dir+'\\project\\file.csv'

    print("list:", read_file(csv_file))    #csv_file의 경로의 값을 def read_file(f) 매개변수로 받아짐