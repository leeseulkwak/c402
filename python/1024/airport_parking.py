
#리스트 데이터
data = """
공항별,계류장면적(m2),동시주기능력(대),주차장면적(m2),동시주차능력(대)
김포,1215487,"144(일반85,소형59)",351089,10646
김해,404251,"43(일반40,소형3)",181226,6739
제주,449393,"42(일반40,소형2)",142184,3578
청주,120390,"21(일반13,소형8)",164404,5267
대구,51182,"11(일반11,소형0)",21981,1579
무안,113094,"50(일반6,소형44)",94890,3009
양양,72385,"24(일반7,소형17)",14734,534
광주,44300,"5(일반5,소형0)",38300,1191
울산,33480,"6(일반4,소형2)",26530,554
여수,41868,"5(일반5,소형0)",30867,884
포항경주,32617,"5(일반5,소형0)",17327,452
사천,13140,"2(일반2,소형0)",9893,309
군산,13758,"2(일반2,소형0)",15888,519
원주,6590,"1(일반1,소형0)",4412,178
"""

line=(data.strip().split('\n'))
line2=line[10]

line2_values=line2.split(",")

print(line2)
area=line2_values[0]
num=line2_values[5]

print("{} 의 주차 가능 차량은 {} 대입니다".format(area, num))



# line2_values=line2.split(",")
# parking_area=line2_values[0]
# parking_capacity=line2_values[-1]

# print(parking_area, parking_capacity)