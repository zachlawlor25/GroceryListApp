from tkinter import *
from tkinter import ttk
import os
from PIL import Image, ImageTk
import sys


def addToList():
    root = Toplevel()
    root.title("Add To List")

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

        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="Add Grocery Items", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
        
    # grocery list item name
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

    lb1 = Label(labelFrame,text="Grocery Item : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)

    groceryInfo1 = Entry(labelFrame)
    groceryInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)


    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=root.destroy)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black',       command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)