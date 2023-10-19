# 파일 경로나 이름을 추가할 수 있도록 수정 필요
def write_file(text):
    with open('.\\1018\\output.csv', 'w', encoding='utf-8') as file:
        file.write(text)

if __name__ == '__main__':
    text = "sum: 3"
    
    write_file(text)