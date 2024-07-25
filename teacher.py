from tkinter import *
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
    entry_name.delete(0, END)
    entry_age.delete(0, END)
    entry_address.delete(0, END)
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

    display_all()


def search(id):
    try:
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
        if row == None:
            display_search("unknown ID")
        else:
            display_search(row)
            conne.commit()
            conne.close()
    except:
        display_search("unknown ID")


def display_search(data):
    listbox = Listbox(root, width=25, height=2)
    listbox.grid(row=8, column=1)
    listbox.insert(0, data)


def display_search_all(data):
    listbox = Listbox(root, width=25, height=5)
    listbox.grid(row=9, column=1)
    for one_data in data:
        listbox.insert(0, one_data)


def  display_all():
    conne = psycopg2.connect(
        dbname="student",
        user='postgres',
        password='admin',
        host='localhost',
        port='5432'

    )

    querry = '''SELECT * FROM teacher'''

    cur = conne.cursor()
    cur.execute(querry
    )
    row = cur.fetchall()
    display_search_all(row)




root = Tk()
root.title("ŠKOLA A DATABÁZE")
root.geometry("380x370")
root.resizable(False, False)

## Labels, Entreies
label_general = Label(root, text="ADD DATA")
label_general.grid(row=0, column=1)

# name section
label_name = Label(root, text='NAME: ')
label_name.grid(row=1, column=0)

entry_name = Entry(root)
entry_name.grid(row=1, column=1)

# age section
label_age = Label(root, text='AGE: ')
label_age.grid(row=2, column=0)

entry_age = Entry(root)
entry_age.grid(row=2, column=1)

# address section
address_name = Label(root, text='ADDRESS: ')
address_name.grid(row=3, column=0)

entry_address = Entry(root)
entry_address.grid(row=3, column=1)

# button
button = Button(root, text="ADD", command=lambda:insert_data(entry_name.get(), entry_age.get(), entry_address.get()))
button.grid(row=4,column=1)

## SEARCH SECTION
# general label
label_search = Label(root, text='SEARCH DATA')
label_search.grid(row=5, column=1)

label_id = Label(root, text='SEARCH BY ID')
label_id.grid(row=6, column=0)

entry_id = Entry(root)
entry_id.grid(row=6, column=1)

button_search = Button(root, text='SEARCH', command=lambda:search(entry_id.get().strip()))
button_search.grid(row=6, column=2)

display_all()

root.mainloop()