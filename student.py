import psycopg2
from tkinter import *
import tkinter as tk


root = Tk()

def get_data(name, age, address):
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="786Beefzy", port="5432")
    curr = conn.cursor()
    query ='''INSERT INTO demo1(NAME, AGE, ADDRESS) VALUES (%s,%s,%s);'''
    curr.execute(query, (name, age, address))
    print("Data inserted")
    conn.commit()
    conn.close()

def search(id):
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="786Beefzy", port="5432")    
    curr = conn.cursor()
    query = '''SELECT * FROM demo1 WHERE id=%s;'''
    curr.execute(query,(id))
    print("Searching")
    row = curr.fetchone()
    print("Found\n{}".format(row))
    conn.commit()
    conn.close()
    

canvas = Canvas(root, height=480, width=480).pack()
frame = Frame(root)
frame.place(relx=0.3, rely=0.1, relheight=0.8, relwidth=0.8)

# Label = "Add Data"
label = Label(frame, text="Add data")
label.grid(row=0, column=1) 

# Label_name = "Name :"
label_name = Label(frame, text="Name : ")
label_name.grid(row=2, column=0)

# Entry_name = entry for name
entry_name = Entry(frame)
entry_name.grid(row=2, column=1)

# Label_age = "Age :"
label_age = Label(frame, text="Age : ")
label_age.grid(row=3, column=0)

# Entry_name = entry for name
entry_age = Entry(frame)
entry_age.grid(row=3, column=1)

# Label_address = "Address: "
label_address = Label(frame, text="Address :")
label_address.grid(row=4, column=0)

# Entry-address = entry for address
entry_address = Entry(frame)
entry_address.grid(row=4, column=1)

add_button = Button(frame, text="Add", command= lambda: get_data(entry_name.get(), entry_age.get(), entry_address.get()))
add_button.grid(row=5, column=1)

label_search = Label(frame, text="Search data")
label_search.grid(row=6, column=1)

label_search_id = Label(frame, text="Seach by id")
label_search_id.grid(row=7, column=0)

entry_search_id = Entry(frame)
entry_search_id.grid(row=7, column=1)

button_search_id = Button(frame, text="Seach", command= lambda: search(entry_search_id.get()))
button_search_id.grid(row=7, column=2)



root.mainloop()