from tkinter import *
import psycopg2

root = Tk()
root.title("ŠKOLA A DATABÁZE")
root.geometry("240x240")
root.resizable(False, False)

## Labels, Entreies
label_general = Label(root, text="ADD DATA")
label_general.grid(row=0, column=1)

# name section
label_name = Label(root, text='NAME')
label_name.grid(row=1, column=0)

entry_name = Entry(root)
entry_name.grid(row=1, column=1)


root.mainloop()