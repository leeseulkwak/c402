# from utils.DBConnector import MariaDBConnector

import os
import sys

cwd = os.getcwd()
sys.path.append(os.path.join(cwd, 'chatbot'))
print(sys.path)

from utils.DBConnector import MariaDBConnector
import utils.DBConnector as DBC

config = DBC.config
db = None

try:
    db = MariaDBConnector(config)
    conn = db.connect()

    sql = 'INSERT INTO chatbot_data (question, answer, label) VALUES ("1지망 학교 떨어졌어","위로해 드립니다.",0)'
    with conn.cursor() as cursor:
        cursor.execute(sql)
        conn.commit()
        
except Exception as e:
    print(e)

finally:
    if db is not None:
        db.close()
