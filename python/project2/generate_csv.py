
# generate_csv.py

import csv
import random

import generate_data as gd

try:
    num_of_files = int(input("생성할 CSV 파일의 개수를 입력하세요: "))
except ValueError:
    print("올바른 숫자를 입력하세요.")
    exit()

for file_num in range(1, num_of_files + 1):
    csv_file_name = f"output_{file_num}.csv"

    num_of_rows = random.randint(100, 3000)

    with open(csv_file_name, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)

        header = ["이름", "연락처(HP)"]
        writer.writerow(header)

        for _ in range(num_of_rows):
            data_row = [
                gd.generate_name(),
                gd.generate_phone_number()
            ]
            writer.writerow(data_row)
    
    print(f"{csv_file_name} 파일이 생성되었습니다.")



