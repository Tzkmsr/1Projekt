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

    teacher_name = input("Zadej jmeno ucitele: ")
    teacher_age = input("Zadej vek ucitele: ")
    teacher_address = input("Zadej adresu ucitele: ")


    cur = conne.cursor()
    query = '''
    INSERT INTO teacher(name, age, address)
    VALUES (%s, %s, %s)
    '''
    
    cur.execute(query, (teacher_name, teacher_age, teacher_address))
    conne.commit()
    conne.close()

insert_data()
