#!/usr/bin/python
import sys
import os
import tkinter
from tkinter import *

def page1():
    page2text.pack_forget()
    page5text.pack_forget()
    os.system('DM1.py')
    page1text.pack()
    

def page2():
    page1text.pack_forget()
    page3text.pack_forget()
    page4text.pack_forget()
    page5text.pack_forget()
    os.system('DM2.py')
    page2text.pack()

def page3():
    page1text.pack_forget()
    page2text.pack_forget()
    page4text.pack_forget()
    page5text.pack_forget()
    os.system('DM3.py')
    page3text.pack()

def page4():
    page1text.pack_forget()
    page2text.pack_forget()
    page3text.pack_forget()
    page5text.pack_forget()
    os.system('extractRules.py')
    page4text.pack()

def page5():
    page1text.pack_forget()
    page2text.pack_forget()
    page3text.pack_forget()
    page4text.pack_forget()
    os.system('asg5.py')
    page5text.pack()

def page6():
    page1text.pack_forget()
    page2text.pack_forget()
    page3text.pack_forget()
    page4text.pack_forget()
    page5text.pack_forget()
    page7text.pack_forget()
    page8text.pack_forget()
   
    os.system('asg6.py')
    page5text.pack()

def page7():
    page1text.pack_forget()
    page2text.pack_forget()
    page3text.pack_forget()
    page4text.pack_forget()
    page5text.pack_forget()
    page6text.pack_forget()
    page8text.pack_forget()
   
    os.system('asg7.py')
    page5text.pack()

def page8():
    page1text.pack_forget()
    page2text.pack_forget()
    page3text.pack_forget()
    page4text.pack_forget()
    page5text.pack_forget()
    page6text.pack_forget()
    page7text.pack_forget()
   
    os.system('asg8.py')
    page5text.pack()

window = tkinter.Tk()
window.title('Data Mining GUI')
window['bg']='#9A9ACD'
window.geometry("450x350")

# btn=Button(window, text="This is Button widget", fg='blue')
# btn.place(x=80, y=100)
page1btn = tkinter.Button(window, text="Assignment 1", command=page1)
page1btn.place(x=80, y=100)
page2btn = tkinter.Button(window, text="Assignment 2", command=page2)
page2btn.place(x=80, y=100)
page3btn = tkinter.Button(window, text="Assignment 3", command=page3)
page3btn.place(x=80, y=100)
page4btn = tkinter.Button(window, text="Assignment 4", command=page4)
page4btn.place(x=80, y=100)
page5btn = tkinter.Button(window, text="Assignment 5", command=page5)
page5btn.place(x=80, y=100)
page6btn = tkinter.Button(window, text="Assignment 6", command=page6)
page6btn.place(x=80, y=100)
page7btn = tkinter.Button(window, text="Assignment 7", command=page7)
page7btn.place(x=80, y=100)
page8btn = tkinter.Button(window, text="Assignment 8", command=page8)
page8btn.place(x=80, y=100)


page1text = tkinter.Label(window, text="This is Assignment 1")
page2text = tkinter.Label(window, text="This is Assignment 2")
page3text = tkinter.Label(window, text="This is Assignment 3")
page4text = tkinter.Label(window, text="This is Assignment 4")
page5text = tkinter.Label(window, text="This is Assignment 5")
page6text = tkinter.Label(window, text="This is Assignment 6")
page7text = tkinter.Label(window, text="This is Assignment 7")
page8text = tkinter.Label(window, text="This is Assignment 8")

# page1btn.place(relx=0.5, rely=0.5, anchor='center')


page1btn.pack()
page2btn.pack()
page3btn.pack()
page4btn.pack()
page5btn.pack()
page6btn.pack()
page7btn.pack()
page8btn.pack()

# page1text.pack()

window.mainloop()