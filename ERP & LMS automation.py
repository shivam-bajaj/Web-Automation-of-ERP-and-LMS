from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import bs4
import getpass
import urllib3
import requests
import os
import sys
import mysql.connector as mariadb
from tkinter import *
#from PIL import ImageTk , Image

import time
import datetime

connection = mariadb.connect(user='root', password='@E1telligent', database='bajju')
cursor = connection.cursor()

root = Tk()
root.title("Project")
root.configure(bg="Light Yellow")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
def ERP(user,pas):
    browser = webdriver.Firefox()
    browser.get("http://erp.ncuindia.edu")
    username = browser.find_element_by_id("tbUserName")
    username.send_keys(user)
    password = browser.find_element_by_id("tbPassword")
    password.send_keys(pas)
    submit = browser.find_element_by_id("btnLogIn")
    submit.click()
    attend = browser.find_element_by_id("aAttandance")
    attend.click()

def LMS(user , pas, crse):
    browser = webdriver.Firefox()
    browser.get("http://lmsncu.ncuindia.edu")
    username = browser.find_element_by_id("username")
    username.send_keys(user)
    password = browser.find_element_by_id("password")
    password.send_keys(pas)
    submit = browser.find_element_by_id("loginbtn")
    submit.click()
    if crse == "Python" :
        ppt = browser.find_element_by_link_text("Introduction to Python (Dr Supriya Raheja)")
        ppt.click()
    elif crse == "DBMS" :
        ppt = browser.find_element_by_link_text("DBMS 2018")
        ppt.click()
    elif crse == "CAO" :
        ppt = browser.find_element_by_link_text("Computer Architecture and Organization by Monika Lamba")
        ppt.click()


def check(baju):
  if baju== "shb":
    print("Erp")
    user = username_box.get()
    pas = password_box.get()
    t=datetime.datetime.now().time()
    t=str(t)
    d=datetime.datetime.now().date()
    d=str(d)
    cursor.execute("insert into ERP(Username,Password,Date,Time) values(%s,%s,%s,%s)",(user, pas,d,t))
    connection.commit()
    root.destroy()
    ERP(user,pas)
  else :
    print("LMS")
    user=usernamebox.get()
    pas=passwordbox.get()
    crse=baju
    t = datetime.datetime.now().time()
    t = str(t)
    d = datetime.datetime.now().date()
    d = str(d)
    cursor.execute("insert into LMS(Username,Password,Course,Date,Time) values(%s,%s,%s,%s,%s)", (user, pas,crse, d, t))
    connection.commit()
    root.destroy()
    LMS(user,pas,crse)

top = Frame(root, width=400, height=200, bg="blue")
top.pack(side=TOP)
#img = Image.open("C:\\Users\\Shivam Bajaj\\Desktop\\ncu2.jpg")
#img = img.resize((350, 250), Image.ANTIALIAS)
#img = ImageTk.PhotoImage(img)
#im = Label(top, image=img)
#im.pack()
left = Frame(root, width=700, height=700, bg="Light Yellow")
left.pack(side=LEFT)
right = Frame(root, width=700, height=700, bg="Light Yellow")
right.pack(side=RIGHT)
erp = Label(left, font=("Comic Sans ms", 50, "bold"), text="ERP", anchor=N, fg="orange", bd=50, bg="Light Yellow")
erp.grid(row=0, column=0)

a2 = Label(left, text="\t   \n\t    ", bg="light yellow")
a2.grid(row=1, column=0)
a3 = Label(left, text="\t   \n\t    ", bg="light yellow")
a3.grid(row=3, column=0)
a4 = Label(left, text="\t   \n\t    ", bg="light yellow")
a4.grid(row=5, column=0)
lms = Label(right, font=("Comic Sans ms", 50, "bold"), text="LMS", anchor=E, fg="orange", bd=50, bg="Light Yellow")
lms.grid(row=0, column=0)
b1 = Label(right, text="\t    \t \n \t  ", bg="light yellow")
b1.grid(row=0, column=5)
b2 = Label(right, text="\t   \n\t    ", bg="light yellow")
b2.grid(row=1, column=5)
b3 = Label(right, text="\t   \n\t    ", bg="light yellow")
b3.grid(row=3, column=5)
b4 = Label(right, text="\t   \n\t    ", bg="light yellow")
b4.grid(row=5, column=5)


def clear_widget(event):
    # will clear out any entry boxes defined below when the user shifts
    # focus to the widgets defined below
    if username_box == left.focus_get() and username_box.get() == 'Enter Username':
        username_box.delete(0, END)
    elif password_box == password_box.focus_get() and password_box.get() == '     ':
        password_box.delete(0, END)

def repopulate_defaults(event):
    # will repopulate the default text previously inside the entry boxes defined below if
    # the user does not put anything in while focused and changes focus to another widget
    if username_box != left.focus_get() and username_box.get() == '':
        username_box.insert(0, 'Enter Username')
    elif password_box != left.focus_get() and password_box.get() == '':
        password_box.insert(0, '     ')


def login(*event):
    temp="shb"
    check(temp)

def loginp(*event):
    temp = Lb1.curselection()
    s=Lb1.get(temp)
    check(s)

# defines a grid 50 x 50 cells in the main window
rows = 0
while rows < 10:
    root.rowconfigure(rows, weight=1)
    root.columnconfigure(rows, weight=1)
    rows += 1

# adds username entry widget and defines its properties
username_box = Entry(left, width=30, font=(10))
username_box.insert(0, 'Enter Username')
username_box.bind("<FocusIn>", clear_widget)
username_box.bind('<FocusOut>', repopulate_defaults)
username_box.grid(row=1, column=1, sticky='NS')
s1 = Label(left, text="                               ", bg="Light Yellow")
s1.grid(row=2, column=1)

# adds password entry widget and defines its properties
password_box = Entry(left, show='?', width=30, font=(10))
password_box.insert(0,'     ')
password_box.bind("<FocusIn>",clear_widget)
password_box.bind('<FocusOut>', repopulate_defaults)
password_box.bind('<Return>', login)
password_box.grid(row=3, column=1, sticky='NS')
s1 = Label(left, text="                               ", bg="Light Yellow")
s1.grid(row=4, column=1)

# adds login button and defines its properties
login_btn = Button(left, text='Login', command=login, width=4, height=3)
login_btn.bind('<Return>', login)
login_btn.grid(row=5, column=1, sticky='NESW')
s1 = Label(left, text="                               ", bg="Light Yellow")
s1.grid(row=6, column=1)
s1 = Label(left, text="      \n\n\n\n\n\n\n\n ", bg="Light Yellow")
s1.grid(row=7, column=1)
s1 = Label(left, text="        \n\n\n\n\n \n\n\n\n         ", bg="Light Yellow")


def clearwidget(event):
    # will clear out any entry boxes defined below when the user shifts
    # focus to the widgets defined below
    if usernamebox == right.focus_get() and usernamebox.get() == 'Enter Username':
        usernamebox.delete(0,END)
    elif passwordbox == passwordbox.focus_get() and passwordbox.get() == '     ':
        passwordbox.delete(0,END)


def repopulatedefaults(event):
    # will repopulate the default text previously inside the entry boxes defined below if
    # the user does not put anything in while focused and changes focus to another widget
    if usernamebox != right.focus_get() and usernamebox.get() == '':
        usernamebox.insert(0, 'Enter Username')
    elif passwordbox != right.focus_get() and passwordbox.get() == '':
        passwordbox.insert(0, '     ')


# defines a grid 50 x 50 cells in the main window
rows = 0
while rows < 10:
    root.rowconfigure(rows, weight=1)
    root.columnconfigure(rows, weight=1)
    rows += 1

# adds username entry widget and defines its properties
usernamebox = Entry(right, width=30, font=(10))
usernamebox.insert(0, 'Enter Username')
usernamebox.bind("<FocusIn>", clearwidget)
usernamebox.bind('<FocusOut>', repopulatedefaults)
usernamebox.grid(row=1, column=1, sticky='NS')
s1 = Label(right, text="                               ", bg="Light Yellow")
s1.grid(row=2, column=1)

# adds password entry widget and defines its properties
passwordbox = Entry(right, show='?', width=30, font=(10))
passwordbox.insert(0,'     ')
passwordbox.bind("<FocusIn>", clearwidget)
passwordbox.bind('<FocusOut>', repopulatedefaults)
passwordbox.bind('<Return>', loginp)
passwordbox.grid(row=3, column=1, sticky='NS')
s1 = Label(right, text="                               ", bg="Light Yellow")
s1.grid(row=4, column=1)

Lb1 = Listbox(right, height=1, font=(10), selectmode=EXTENDED, bg="Orange", width=30)
Lb1.insert(0, "Select Course")
Lb1.insert(1, "Python")
Lb1.insert(2, "DBMS")
Lb1.insert(3,"CAO")
Lb1.select_set(0)
Lb1.grid(row=5, column=1)
s1 = Label(right, text="                               ", bg="Light Yellow")
s1.grid(row=6, column=1)

# adds login button and defines its properties
loginbtn = Button(right, text='Login', command=loginp, width=4, height=3)
loginbtn.bind('<Return>', loginp)
loginbtn.grid(row=7, column=1, sticky='NESW')
s1 = Label(right, text="                               ", bg="Light Yellow")
s1.grid(row=9, column=1)
s1 = Label(right, text="      \n\n\n\n\n\n\n\n ", bg="Light Yellow")
s1.grid(row=10, column=1)
s1 = Label(right, text="        \n\n\n\n\n \n\n\n\n         ", bg="Light Yellow")

root.mainloop()







db=Tk()
db.title("DATA BASE")
db.geometry("500x300+450+200")
db.configure(bg="black")


def clear(event):
    # will clear out any entry boxes defined below when the user shifts
    # focus to the widgets defined below
    if box == db.focus_get() and box.get() == 'Enter Username':
        box.delete(0, END)
    elif pbox == pbox.focus_get() and pbox.get() == '     ':
        pbox.delete(0, END)


def defaults(event):
    # will repopulate the default text previously inside the entry boxes defined below if
    # the user does not put anything in while focused and changes focus to another widget
    if box != db.focus_get() and box.get() == '':
        box.insert(0, 'Enter Username')
    elif pbox != db.focus_get() and pbox.get() == '':
        pbox.insert(0, '     ')

def erptable(*event):
    ebase=Tk()
    ebase.title("ERP DATABASE")
    ebase.geometry("900x600+350+150")
    ebase.configure(bg="black")
    f=Frame(ebase,width=200,height=100,bg="black")
    f.pack(side=TOP)
    l=Label(f, text="\t\t\n\t",bg="Black")
    l.grid(row=0,column=0)
    l1=Label(f,text="ERP", font=("Comic Sans ms", 40, "bold"),fg="red",bg="black")
    l1.grid(row=1, column=0)
    ft = Frame(ebase, width=600, height=550, bg="black")
    ft.pack(side=TOP)
    l = Label(ft, text="\n\n", bg="black")
    l.grid(row=0, column=0)

    a=Label(ft,text="Username",fg="white", bg="black",font=(15))
    a.grid(row=1,column=0)
    a = Label(ft, text="\t", fg="white", bg="black")
    a.grid(row=1, column=1)
    a = Label(ft, text="Password", fg="white", bg="black",font=(15))
    a.grid(row=1, column=2)
    a = Label(ft, text="\t", fg="white", bg="black",font=(15))
    a.grid(row=1, column=3)
    a = Label(ft, text="Date", fg="white", bg="black",font=(15))
    a.grid(row=1, column=4)
    a = Label(ft, text="\t", fg="white", bg="black",font=(15))
    a.grid(row=1, column=5)
    a = Label(ft, text="Time", fg="white", bg="black",font=(15))
    a.grid(row=1, column=6)
    l = Label(ft, text="    ", bg="black")
    l.grid(row=2, column=0)

    cursor.execute("Select * from ERP")

    row = cursor.fetchone()
    i = 3
    while row is not None:

        j = 0
        for d in row :
            l2 = Label(ft, text=d, fg="white", bg="black")
            l2.grid(row=i, column=j)
            j = j + 2




        i = i+1
        row=cursor.fetchone()




    ebase.mainloop()

def lmstable(*event):
    lbase=Tk()
    lbase.title("LMS DATABASE")
    lbase.geometry("900x600+350+150")
    lbase.configure(bg="black")
    f=Frame(lbase,width=200,height=100,bg="black")
    f.pack(side=TOP)
    l=Label(f, text="\t\t\n\t",bg="Black")
    l.grid(row=0,column=0)
    l1=Label(f,text="LMS", font=("Comic Sans ms", 40, "bold"),fg="red",bg="black")
    l1.grid(row=1, column=0)
    ft = Frame(lbase, width=600, height=550, bg="black")
    ft.pack(side=TOP)
    l = Label(ft, text="\n\n", bg="black")
    l.grid(row=0, column=0)

    a=Label(ft,text="Username",fg="white", bg="black",font=(15))
    a.grid(row=1,column=0)
    a = Label(ft, text="\t", fg="white", bg="black")
    a.grid(row=1, column=1)
    a = Label(ft, text="Password", fg="white", bg="black",font=(15))
    a.grid(row=1, column=2)
    a = Label(ft, text="\t", fg="white", bg="black",font=(15))
    a.grid(row=1, column=3)
    a = Label(ft, text="Course", fg="white", bg="black",font=(15))
    a.grid(row=1, column=4)
    a = Label(ft, text="\t", fg="white", bg="black",font=(15))
    a.grid(row=1, column=5)
    a = Label(ft, text="Date", fg="white", bg="black",font=(15))
    a.grid(row=1, column=6)
    a = Label(ft, text="\t", fg="white", bg="black", font=(15))
    a.grid(row=1, column=7)
    a = Label(ft, text="Time", fg="white", bg="black", font=(15))
    a.grid(row=1, column=8)
    l = Label(ft, text="    ", bg="black")
    l.grid(row=2, column=0)

    cursor.execute("Select * from LMS")

    row = cursor.fetchone()
    i = 3
    while row is not None:

        j = 0
        for d in row :
            l2 = Label(ft, text=d, fg="white", bg="black")
            l2.grid(row=i, column=j)
            j = j + 2




        i = i+1
        row=cursor.fetchone()



def tables():
    table = Tk()
    table.title("TABLES")
    table.geometry("500x300+450+200")
    table.configure(bg="LIGHT BLUE")
    s1 = Label(table, text="  \t \t\t\t", bg="light bLue")
    s1.grid(row=0, column=0)
    s1 = Label(table, text="               \n\n        ", bg="light bLue")
    s1.grid(row=0, column=1)
    erpbutton = Button(table,command= erptable ,text="ERP", font=(20), relief="ridge", bd=10, width=10, height=2, bg="black",fg="light blue")
    erpbutton.grid(row=1, column=1)
    s1 = Label(table, text="      \n\n\                ", bg="Light Blue")
    s1.grid(row=2, column=1)
    lmsbutton = Button(table,command= lmstable ,text="LMS",font=(20), relief="ridge", bd=10, width=10 , height =2 ,bg="black",fg="light blue")
    lmsbutton.grid(row=3, column=1)
    table.mainloop()

def logindb(*event):
    # Able to be called from a key binding or a button click because of the '*event'
    if box.get() == "bajju" and pbox.get() == "greatest":
        db.destroy()
        tables()
    else :
        db.destroy()
        print("!")

    # If I wanted I could also pass the username and password I got above to another
    # function from here.


# defines a grid 50 x 50 cells in the main window
rows = 0
while rows < 10:
    db.rowconfigure(rows, weight=1)
    db.columnconfigure(rows, weight=1)
    rows += 1

# adds username entry widget and defines its properties
s1 = Label(db, text="                               ", bg="BLACK")
s1.grid(row=0, column=5)
box = Entry(db, width=30, font=(10),bg="Light Blue")
box.insert(0, 'Enter Username')
box.bind("<FocusIn>", clear)
box.bind('<FocusOut>', defaults)
box.grid(row=1, column=5, sticky='NS')
s1 = Label(db, text="                               ", bg="BLACK")
s1.grid(row=2, column=5)
# adds password entry widget and defines its properties
pbox = Entry(db, show='?',width=30, font=(10), bg="Light Blue")
pbox.insert(0, '     ')
pbox.bind("<FocusIn>", clear)
pbox.bind('<FocusOut>', defaults)
pbox.bind('<Return>', logindb)
pbox.grid(row=3, column=5, sticky='NS')
s1 = Label(db, text="                               ", bg="BLACK")
s1.grid(row=4, column=5)
# adds login button and defines its properties
log = Button(db, text='Login', command=logindb,width=1, height=1,bg ="RED")
log.bind('<Return>', logindb)
log.grid(row=5, column=5, sticky='NESW')
db.mainloop()
connection.close()


