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

def insert_data(teacher_name, teacher_age, teacher_address):
    conne = psycopg2.connect(
        dbname="student",
        user='postgres',
        password='admin',
        host='localhost',
        port='5432'

    )

    cur = conne.cursor()
    query = '''
    INSERT INTO teacher(name, age, address)
    VALUES (%s, %s, %s)
    '''
    
    cur.execute(query, (teacher_name, teacher_age, teacher_address))
    conne.commit()
    conne.close()

insert_data('Lockhart', 35, 'Bradavice')
