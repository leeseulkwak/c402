import datetime

now=datetime.datetime.now()


#오전 구분
if now.hour < 12:
    print("오전")

elif now.hour >=12:
    print("오후")

