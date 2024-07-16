import psycopg2

def create():
    conne = psycopg2.connect(
        dbname="student",
        user='postgres',
        password='admin',
        host='localhost',
        port='5432'

    )

    cur = conne.cursor()
    cur.execute(
        '''CREATE TABLE teacher(
            ID SERIAL,
            NAME TEXT,
            AGE INT,
            ADRESS TEXT
        )'''
    )

    conne.commit()
    conne.close()

    create()