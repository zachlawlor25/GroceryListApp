#!/Users/zach/Desktop/Python/grocery_list_app/GroceryListApp/venv/bin/python

from tkinter import *
from tkinter import ttk
import os
from PIL import Image, ImageTk
#Import functions
import addListItem as addListItem
import sys

#https://data-flair.training/blogs/library-management-system-python-project/

root = Tk()
root.title("Grocery List Application")

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

#create heading
headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="Welcome to the Grocery\nList Application", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

#Add button for adding to new list
btn1 = Button(root,text="Add List Item",bg='white', fg='black',highlightbackground = '#000000', command=lambda:addListItem.addToList())
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
btn2 = Button(root,text="BLANK",bg='black', fg='black',highlightbackground='#000000', command=lambda:sys.exit())
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="BLANK",bg='black', fg='black',highlightbackground='#000000', command=lambda:sys.exit())
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
btn4 = Button(root,text="BLANK",bg='black', fg='black',highlightbackground='#000000', command = lambda:sys.exit())
btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
    
btn5 = Button(root,text="Quit",bg='black', fg='black',highlightbackground='#000000', command = lambda:sys.exit())
btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)









#Run tkinter app
root.mainloop()