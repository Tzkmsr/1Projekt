from tkinter import *
import psycopg2
from module import *

root = Tk()
root.title("ŠKOLA A DATABÁZE")
root.geometry("300x350")
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

button_search = Button(root, text='SEARCH', command=lambda:search(entry_id.get()))
button_search.grid(row=7, column=1)


root.mainloop()