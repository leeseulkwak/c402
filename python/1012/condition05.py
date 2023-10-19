import datetime
now=datetime.datetime.now()
month=now.month

if  3 <= month <=5:
    print("봄입니다")

elif  6<= month <=8:
    print("여름입니다")

elif  9 <= month <=11:
    print("가을입니다.")
    
else:
    print("겨울입니다.")