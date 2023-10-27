import datetime

now=datetime.datetime.now()

if 3<= now.month < 6:
    print("봄")

elif 6<=now.month <9:
    print("여름")

elif 9<=now.month <12:
    print("가을")

else:
    print("겨울")