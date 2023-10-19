import time

number=0

target_tick=time.time()+5
while time.time()<target_tick:
    number+=1

    print(f"5초 동안 {number}번 반복했습니다.")