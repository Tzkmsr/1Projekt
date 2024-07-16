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
            ADDRESS TEXT
        )'''
    )

    conne.commit()
    conne.close()

def insert_data():
    conne = psycopg2.connect(
        dbname="student",
        user='postgres',
        password='admin',
        host='localhost',
        port='5432'

    )

    cur = conne.cursor()
    cur.execute(
        '''
    INSERT INTO teacher(name, age, address)
    VALUES ('McGonagalova', 50, 'Bradavice')
    '''
    )

    conne.commit()
    conne.close()

