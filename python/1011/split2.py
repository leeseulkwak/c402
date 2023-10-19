add1='청주,120390,"21(일반13,소형8)",164404,5267'
add2=add1.split(",")    #split함수를 이용해서 ,로 데이터를 나눔

list1=add2[2] # , 로 나눈 데이터 중에 2영역을 별도 분리
find1=list1.find("(") # 2영역 중에 '(' 위치 확인
find1_txt="{}".format(list1[1:find1]) # list1 1영역에서 (를 변수 find1로 주어서 값 넣기

print(find1_txt)



#################


add3='포항경주,32617,"5(일반5,소형0)",17327,452'
add4=add3.split(",")  #split함수를 이용해서 ,로 데이터를 나눔

list2=add4[2] # , 로 나눈 데이터 중에 2영역을 별도 분리
find2=list2.find("(") # 2영역 중에 '(' 위치 확인
find2_txt="{}".format(list2[1:find2]) # list1 1영역에서 (를 변수 find1로 주어서 값 넣기

print(find2_txt)