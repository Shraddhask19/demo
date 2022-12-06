from email.policy import default
from itertools import groupby
from select import select
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from tkinter import ttk
from turtle import width
import pandas as pd
import numpy as np
import csv
import math
import matplotlib.pyplot as plt
import seaborn as sns

window=tk.Tk()
window.title('DATA MINING')
window.geometry("800x600")

menubar=tk.Menu(window)
menu_f=tk.Menu(menubar,tearoff=0)
menu_ct=tk.Menu(menubar,tearoff=0)
menu_disp=tk.Menu(menubar,tearoff=0)
menu_display=tk.Menu(menubar,tearoff=0)


menubar.add_cascade(label='Upload file',menu=menu_f)
trv=ttk.Treeview(window,selectmode= 'browse')
trv = ttk.Treeview(window, columns=10, show='headings', height=25)
trv.grid(row=1,column=2,columnspan=3,padx=50,pady=50)
trv['show'] = 'tree'
window['bg']='pink'
style = ttk.Style()
style.theme_use("default")
style.map("Treeview")
menu_f.add_command(label='new',command=lambda:upload_file())

def upload_file():
    file=filedialog.askopenfilename()
    if(file):
        fob=open(file,'r')
        i=0
        for data in fob:
            trv.insert("",'end',iid=i,text=data)
            i=i+1


        def show_attribute():
            if(file):
                fob=open(file,'r')
                data = pd.read_csv(file)
                cols = []
        # menubar.add_cascade(label='Central tendancy',menu=menu_ct)
        # menubar.add_cascade(label='Dispersion',menu=menu_disp)
        # menubar.add_cascade(label='Display Plots',menu=menu_display)
        # menu_ct.add_command(label='select',command=lambda:show_attribute())
        # menu_disp.add_command(label='select',command=lambda:show_dispersion())
        # menu_display.add_command(label='select',command=lambda:show_Plots())

        # if(my_w=='black'):
        #     my_w=='normal'
        # else:
        #      my_w=='black'
    
  
# Adding File Menu and commands
# Assignment1 = Menu(menubar, tearoff = 0)
# menubar.add_cascade(label ='Assignment1', menu = Assignment1)
# Assignment1.add_command(label ='New File', command = None)
# Assignment1.add_command(label ='Open...', command = None)
# Assignment1.add_command(label ='Save', command = None)
# Assignment1.add_separator()
# Assignment1.add_command(label ='Exit', command = window.destroy)
  
# Adding Edit Menu and commands
# edit = Menu(menubar, tearoff = 0)
# menubar.add_cascade(label ='Assignment2', menu = edit)
# edit.add_command(label ='Cut', command = None)
# edit.add_command(label ='Copy', command = None)
# edit.add_command(label ='Paste', command = None)
# edit.add_command(label ='Select All', command = None)
# edit.add_separator()
# edit.add_command(label ='Find...', command = None)
# edit.add_command(label ='Find again', command = None)
  
# Adding Help Menu
# help_ = Menu(menubar, tearoff = 0)
# menubar.add_cascade(label ='Assignment3', menu = help_)
# help_.add_command(label ='Tk Help', command = None)
# help_.add_command(label ='Demo', command = None)
# help_.add_separator()
# help_.add_command(label ='About Tk', command = None)
  
# # display Menu
# window.config(menu = menubar)


# def nextPage():
#     window.destroy()
#     import DM1


# user_name = Label(window,
#                   text = "Username").place(x = 40,
#                                            y = 60) 
# submit_button = Button(window,
#                        text = "Submit").place(x = 40,
#                                               y = 130)                                         

window.config(menu=menubar)
window.mainloop()