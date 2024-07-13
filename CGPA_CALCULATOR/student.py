from tkinter import *   # tkinter for GUI
from decimal import Decimal  #for round figur of cgpa and tga
import sqlite3   #for database work
from tkinter import ttk  #for special effect in Sgpa
import re  #for decription of data
import login

def main(username):
    win = Tk()
    win.title("Student Dashboard")
    win.geometry("300x200")
    win.title('Cgpa Calculator')
    win.configure(bg='#00ffcc')

    db = sqlite3.connect('mysql.db')
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS result(name TEXT, id TEXT PRIMARY KEY, Sgpa1 REAL, Sgpa2 REAL, cgpa REAL)")
    db.commit()
    
    search1=StringVar()

    entry14=Entry(win,textvariable=search1,justify='center') #Entry field
    entry14.grid(row=29,column=6)

    button1=ttk.Button(win,text="Search",width=10,command = lambda : search(search1,pos1,pos2,pos3,pos4,pos5)) #Button for action
    button1.grid(row=29,column=7)
    
    pos1 = StringVar()
    pos2 = StringVar()
    pos3 = StringVar()
    pos4 = StringVar()
    pos5 = StringVar()

    pos6 = Label(win,text = "Name:",bg="#00ffcc",font="Times 11 bold") #label
    pos6.grid(row=30,column=1)
    pos6=Label(win,textvariable=pos1,bg="#00ffcc") #label
    pos6.grid(row=30,column=6)

    pos7 = Label(win,text = "Id:",bg="#00ffcc",font="Times 11 bold") #label
    pos7.grid(row=31,column=1)
    pos7=Label(win,textvariable=pos2,bg="#00ffcc") #label
    pos7.grid(row=31,column=6)

    pos8 = Label(win,text = "Sgpa1:",bg="#00ffcc",font="Times 11 bold") #label
    pos8.grid(row=32,column=1)
    pos8=Label(win,textvariable=pos3,bg="#00ffcc") #label
    pos8.grid(row=32,column=6)

    pos9 = Label(win,text = "Sgpa2:",bg="#00ffcc",font="Times 11 bold") #label
    pos9.grid(row=33,column=1)
    pos9=Label(win,textvariable=pos4,bg="#00ffcc") #label
    pos9.grid(row=33,column=6)

    pos10 = Label(win,text = "Cgpa:",bg="#00ffcc",font="Times 11 bold") #label
    pos10.grid(row=34,column=1)
    pos10=Label(win,textvariable=pos5,bg="#00ffcc") #label
    pos10.grid(row=34,column=6)  

    button_back=ttk.Button(win,text="Back",width=15,command=lambda : back(win))
    button_back.grid(row = 38, column = 7)
        
    win.mainloop()

def search(search1,pos1,pos2,pos3,pos4,pos5):
    search=str(search1.get())
    search=change(search)
    conn = sqlite3.connect('mysql.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT name FROM result where id ='+search)
    a=cursor.fetchall()
    a=str(a)
    a=unchange(a)  #using decription
    a = "".join(re.findall("[a-zA-V]", a))
    pos1.set(a.capitalize())
    
    cursor.execute('SELECT id FROM result where id ='+search)
    b=cursor.fetchall()
    b=str(b)
    b=unchange(b) #using decription
    b = " ".join(re.findall("[0-9]+", b))
    pos2.set(b)
    
    cursor.execute('SELECT Tgpa1 FROM result where id ='+search)
    c=cursor.fetchall()
    pos3.set(c)
    
    cursor.execute('SELECT Tgpa2 FROM result where id ='+search)
    d=cursor.fetchall()
    pos4.set(d)
    
    cursor.execute('SELECT cgpa FROM result where id ='+search)
    e=cursor.fetchall()
    pos5.set(e)

# for encription
def change(a):
    a=list(a)
    str=""
    for i in a:
        i=ord(i)
        i=i+1
        i=chr(i)
        str=str+i
    return str

#for dicription
def unchange(a):
    a=list(a)
    st=""
    for i in a:
        i=ord(i)
        i=i-1
        i=chr(i)
        st=st+i
    return st

def back(win):
    win.destroy()
    login.main()
