from utils.DBConnector import MariaDBConnector
import utils.DBConnector
import csv, os

config=utils.DBConnector.config

db = MariaDBConnector(config)
conn=db.connect()

try :
    sql='select * from chatbot_data'
    with conn.cursor() as cursor:
        cursor.execute(sql)
        rows=cursor.fetchall()
        
        for row in rows:
            print(row)  

except Exception as e:
        print(e)

finally:
    if db is not None:
         db.close()

