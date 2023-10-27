
# generate_data.py

import os
import random
import unittest

# 이름생성
last_name = ('김', '이', '박', '최', '정', '강', '조', '윤', '장', '임' '한', '오' '신', '서', '권', '황', '안', '송', '전', '백',
'허', '고', '문', '김', '남', '심', '류', '김', '원', '문', '주', '석', '손', '민', '유' '조', '남', '노' '백', '봉',
'정', '곽', '채', '홍', '신', '강', '노' '연', '공', '문')
first_name = []

directory = "project2"
file_name = "korean_top_name.txt"

file_path = os.path.join(directory, file_name)

with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

    for line in lines:
        name = line.strip()
        first_name.append(name)
        
##  korea_top_name에 있는 이름을 first_name 리스트에 추가



# 풀네임 생성
def generate_name():
    full_name = "{}{}".format(random.choice(last_name), random.choice(first_name))
    return full_name

        # listname 에 있는 "성"과 first_name에 있는 "이름"을 랜덤으로 생성



# 전화번호 생성
def generate_phone_number():
    if random.choice([True, False]):
        phone_number = '10'
        # _은 특정 변수에 대한 관심이 없거나 사용하지 않는 변수를 나타내는데 사용 - 관습?!
        for _ in range(8):
            phone_number += str(random.randint(0,9))
    else:
        phone_number = '11'
        for _ in range(7):
            phone_number += str(random.randint(0,9))
    return phone_number


class TestGeneratePhoneNumber(unittest.TestCase):
    def test_generate_phone_number(self):
        for _ in range(100):
            phone_number = generate_phone_number()
            self.assertTrue(len(phone_number) in [9, 10]) # 길이 테스트
            self.assertTrue(phone_number.startswith('10') or phone_number.startswith('11')) # 10 또는 11로 시작하는지 테스트


if __name__ == "__main__":
    # 랜덤 이름 출력 테스트
    print(generate_name())

    # 랜덤 전화번호 출력 테스트
    print(generate_phone_number())

    # 파이썬 유닛테스트(위와 같이 테스트하거나 또는 단위테스트를 하거나 선택)
    unittest.main()



