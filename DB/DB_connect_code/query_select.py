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

    sql = 'select * from chatbot_data'
    with conn.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)

except Exception as e:
    print(e)

finally:
    if db is not None:
        db.close()
