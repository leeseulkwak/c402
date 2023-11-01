s="1+2*33-4"

#연산자 목록
operateors=set('+-*/')

#문자열 파싱
result=[]
number=''

for char in s:
    if char in operateors:
        if number:
            result.append(int(number))
            number=''
        result.append
