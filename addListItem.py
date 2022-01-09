from tkinter import *
from tkinter import ttk
import os
from PIL import Image, ImageTk
import sys
import tkinter.messagebox
import models as models


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

    # Store
    lb2 = Label(labelFrame,text="Desired Store : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    groceryInfo2 = Entry(labelFrame)
    groceryInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)

    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=lambda:addNew(root,groceryInfo1,groceryInfo2))
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black',command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

def addNew(inputRoot,inputItem,inputStore):
    itemEntry = inputItem.get()
    storeEntry = inputStore.get()
    print(f"\nItem Entered: {itemEntry}\nStore Entered: {storeEntry}\n")
    newEntry = models.Item(itemEntry, storeEntry)
    models.Item.writeJson(newEntry)
    tkinter.messagebox.showinfo("Submission Successful","The item was successfully submitted. You may now close this window, or proceed to enter another item")