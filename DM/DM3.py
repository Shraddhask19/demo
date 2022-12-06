#!/usr/bin/python
import sys
import os
import tkinter
from tkinter import *

def page1():
    page2text.pack_forget()

    os.system('giniIndex.py')
    
    page1text.pack()
    

def page2():
    page1text.pack_forget()
    # page3text.pack_forget()
    
    os.system('InformationGain.py')
    page2text.pack()

# def page3():
#     page1text.pack_forget()
#     page2text.pack_forget()
    
#     os.system('naivebayes.py')

#     page3text.pack()

window = tkinter.Tk()
window.title('Assignment 5')
window['bg']='#9A9ACD'
window.geometry("450x350")

# btn=Button(window, text="This is Button widget", fg='blue')
# btn.place(x=80, y=100)
page1btn = tkinter.Button(window, text="giniIndex", command=page1)
page1btn.place(x=80, y=100)
page2btn = tkinter.Button(window, text="InformationGain", command=page2)
page2btn.place(x=80, y=100)
# page3btn = tkinter.Button(window, text="naivebayes", command=page3)



page1text = tkinter.Label(window, text="This is giniIndex")
page2text = tkinter.Label(window, text="This is InformationGain")

# page3text = tkinter.Label(window, text="This is naivebayes")

# page1btn.place(relx=0.5, rely=0.5, anchor='center')

page1btn.pack()
page2btn.pack()
# page3btn.pack()


# page1text.pack()

window.mainloop()