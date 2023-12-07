import os

cwd=os.getcwd()
file_name=os.path.join(cwd, 'chatbot', 'data', 'train.txt')

with open(file_name, 'r', encoding='utf-8') as f:
        lines=f.readlines()
        print(lines)