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

def insert_data(name, age, address):
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
    
    cur.execute(query, (name, age, address))
    conne.commit()
    conne.close()

def search(id):
    conne = psycopg2.connect(
        dbname="student",
        user='postgres',
        password='admin',
        host='localhost',
        port='5432'
    )
    querry = '''
        SELECT * FROM teacher WHERE id = %s
        '''

    cur = conne.cursor()
    cur.execute(querry, (id,))
    row = cur.fetchone()
    print(row)
    conne.commit()
    conne.close()