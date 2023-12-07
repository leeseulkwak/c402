import mariadb
import sys


class MariaDBConnector:
    def __init__(self, config):
        self.config = config
        self.conn = None

    def connect(self):
        try:
            self.conn = mariadb.connect(**self.config)
            return self.conn
        except mariadb.Error as e:
            print(f"마리아디비 연결시 에러: {e}")
            sys.exit(1)

    def close(self):
        if self.conn:
            self.conn.close()

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'admin',
    'password': '1234',
    'database': 'Chatbot'
}

# db = MariaDBConnector(config)

# conn=db.connect()
# cur = conn.cursor()
# cur.execute('SELECT id FROM chatbot_data')

# print(cur.execute)

# # elm_data = cur.fetchall()

# GRADES = ['A','B','C']

# for i in elm_data:
#     grade = random.choice(GRADES)
#     batch = (i[0],grade)
#     cur.execute('INSERT INTO grades(enrollment_id, grade) values (%s,%s)',batch)
#     conn.commit()

# db.close()