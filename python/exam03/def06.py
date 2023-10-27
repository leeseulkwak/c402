#문제: 주어진 문자열에서 각 문자의 빈도수를 딕셔너리 형태로 반환하는 함수 char_frequency를 작성하세요.
string="aaeewwqqfte"

def char_frequency(s):

    freq={} #빈 딕셔너리 새성
    print(freq)
    for i in s:
        freq[i]=freq.get(i,0)+1
    return freq

print(char_frequency(string))