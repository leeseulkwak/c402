#문제: 사용자로부터 문자열을 입력받아, 그 문자열에서 모음(a, e, i, o, u)의 개수를 출력하세요.

# string=input("문자열을 입력 해주세요\n")

# count=0
# for char in string:  
#     if char in "aeiou":
#         count+=1

# print("모음의 개수는".format(count))

text = input("문자열을 입력하세요: ")
count = 0
for char in text:
    if char in "aeiouAEIOU":
        count += 1
print(f"모음의 개수: {count}")

