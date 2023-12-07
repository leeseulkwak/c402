from utils.DBConnector import MariaDBConnector
import utils.DBConnector

config=utils.DBConnector.config

db = MariaDBConnector(config)
conn=db.connect()

try :
    sql='''
    CREATE TABLE IF NOT EXISTS `chatbot_train_data`(
        `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
        `intent` VARCHAR(45) NULL,
        `ner` VARCHAR(1024) NULL,
        `query` TEXT NULL,
        `answer` text NOT NULL,
        `answer_image` VARCHAR(2048) NULL,
      PRIMARY KEY(`id`))
    ENGINE=InnoDB DEFAULT CHARSET=utf8
'''

#테이블 생성
    with conn.cursor() as cursor:
        cursor.execute(sql)
             
except Exception as e:
        print(e)

finally:
    if db is not None:
         db.close()

