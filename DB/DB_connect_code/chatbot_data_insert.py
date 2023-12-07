from utils.DBConnector import MariaDBConnector
import utils.DBConnector
import csv, os

#커넥션 수행
config=utils.DBConnector.config

db = MariaDBConnector(config)
conn=db.connect()
conn.commit()

#csv 파일 읽어 오기
f=open('ChData.csv', 'r', encoding='UTF8')
csvReader=csv.reader(f)

for row in csvReader:
    question=row[0]
    answer=row[1]
    label = row[2]
    print(question)
    print(answer)
    print(label)

    sql = "insert into chatbot_data  (question, answer, label) values ('%s', '%s', %d)"
    with conn.cursor() as cursor:
        cursor.execute(sql, (question, answer, label))

# DB의 변화 저장
conn.commit()
f.close() 
conn.close()