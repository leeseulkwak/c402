#문제: 문자열을 입력받아, 그 문자열의 모든 모음을 대문자로 변환하는 함수 capitalize_vowels를 작성하세요.
str="adkekfhasb"

def capitalize_vowels(s):
    return ' '.join([char.upper() if char in 'aeouk' else char for char in s])

print(capitalize_vowels(str))