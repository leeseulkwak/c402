import datetime

str=input("입력>")
now=datetime.datetime.now()
time=now.hour

if str == "안녕":
    print("안녕하세요.")
elif str =="안녕하세요":
    print("안녕하세요.")
elif str =="지금 몇 시 야?":
    print(f"지금은 {time} 시입니다.")
elif str =="지금 몇 시 에요?":
    print(f"지금은 {time} 시입니다.")
else:
    print("잘지내?")