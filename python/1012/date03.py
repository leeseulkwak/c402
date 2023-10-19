import datetime
now=datetime.datetime.now()

if 3<=now.month<=5:
        print(f"{now.month}은 봄입니다.")

if 9<=now.month<=11:
        print(f"{now.month}은 가을입니다.")



if 9<=now.month and now.month<=11:
        print("가을")




