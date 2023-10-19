import datetime

now =datetime.datetime.now()

print(now.year, "년")
print(f"{now.year} 년")


if now.hour<12:
        print("현재 시각은 {}시로 오전입니다." .format(now.hour))

if now.hour>=12:
        print(f"{now.hour} 시로 오후 입니다.")