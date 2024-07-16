from tkinter import *
import psycopg2

root = Tk()
root.title("ŠKOLA A DATABÁZE")
root.geometry("260x240")
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
button = Button(root, text="ADD")
button.grid(row=4,column=1)


root.mainloop()