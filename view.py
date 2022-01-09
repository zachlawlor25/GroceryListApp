from tkinter import *
from tkinter import ttk
import os
from PIL import Image, ImageTk
import sys
import tkinter.messagebox
import models as models
import json

def viewList():
    root = Toplevel()
    root.title("View List")

    print('New window opened')

    root.minsize(width=800,height=700)
    root.maxsize(width=800,height=700)
    root.geometry("800x700")

    #Background image
    script_dir = os.getcwd()
    rel_path = "resources/store.jpeg"
    abs_path = os.path.join(script_dir,rel_path)
    # Show image using label
    img = ImageTk.PhotoImage(Image.open(abs_path).resize((800, 700))) # the one-liner I used in my app
    background = Label(root, image=img)
    background.image = img
    background = Label(root, image=img)
    background.place(x = 0, y = 0)

    
    # Close button
    quitBtn = Button(root,text="Close",bg='#f7f1e3', fg='black',command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

    #clear list button
    clearBtn = Button(root,text="Clear List",bg='#f7f1e3', fg='black',command=lambda:clearList(root))
    clearBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

    #Heading layout
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="View List", bg='black', fg='white', font = ('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    tableFrame = Frame(root,bg='black')
    tableFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)

    #scrollbar
    table_scroll = Scrollbar(tableFrame)
    table_scroll.pack(side=RIGHT, fill=Y)

    my_table = ttk.Treeview(tableFrame,yscrollcommand=table_scroll.set, xscrollcommand =table_scroll.set)

    my_table.pack()

    table_scroll.config(command=my_table.yview)
    table_scroll.config(command=my_table.xview)

    my_table['columns'] = ('id','item', 'store')

    # format columns
    my_table.column("#0", width=0,  stretch=NO)
    my_table.column('id',anchor=CENTER,width=150)
    my_table.column("item",anchor=CENTER, width=150)
    my_table.column("store",anchor=CENTER,width=150)

    #Create Headings 
    my_table.heading("#0",text="",anchor=CENTER)
    my_table.heading("id",text="ID",anchor=CENTER)
    my_table.heading("item",text="Item",anchor=CENTER)
    my_table.heading("store",text="Store",anchor=CENTER)

    #add data from json

    # Opening JSON file
    f = open('items.json')
 
    # returns JSON object as
    # a dictionary
    data = json.load(f)
    
    # Iterating through the json
    # list
    for i in data:
        #print(f"Item {i}: {data[i]}")
        my_table.insert(parent='', index='end', iid=i, text='', values=(i, data[i]['item'], data[i]['store']))

    my_table.pack()

def clearList(root):
    with open("items.json", 'r+') as f:
        f.truncate(0)
    root.destroy()
