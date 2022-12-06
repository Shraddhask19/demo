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

my_w=tk.Tk()
my_w.title('Assignment No. 2')
my_w.geometry("450x350")

menubar=tk.Menu(my_w)
menu_f=tk.Menu(menubar,tearoff=0)
menu_ct=tk.Menu(menubar,tearoff=0)
menu_disp=tk.Menu(menubar,tearoff=0)
menu_display=tk.Menu(menubar,tearoff=0)


menubar.add_cascade(label='Upload file',menu=menu_f)
trv=ttk.Treeview(my_w,selectmode= 'browse')
trv = ttk.Treeview(my_w, columns=10, show='headings', height=10)
trv.grid(row=1,column=2,columnspan=3,padx=50,pady=50)
trv['show'] = 'tree'
my_w['bg']='#9A9ACD'
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
        menubar.add_cascade(label='Chi-Square Test',menu=menu_ct)
        menubar.add_cascade(label='Pearson coefficient & Covariance',menu=menu_disp)
        menubar.add_cascade(label='Normalization',menu=menu_display)
        menu_ct.add_command(label='select',command=lambda:show_attribute())
        menu_disp.add_command(label='select',command=lambda:show_dispersion())
        menu_display.add_command(label='select',command=lambda:show_Plots())
        def show_attribute():
            if(file):
                fob=open(file,'r')
                data = pd.read_csv(file)
                cols = []
            for i in data:
                cols = data.columns
                clickedAttribute1 = StringVar()
                clickedAttribute1.set("Select Attribute1")
                dropCols = OptionMenu(my_w, clickedAttribute1, *cols)
                dropCols.grid(column=1,row=5)
                clickedAttribute2 = StringVar()
                clickedAttribute2.set("Select Attribute2")
                dropCols = OptionMenu(my_w, clickedAttribute2, *cols)
                dropCols.grid(column=2,row=5)
                clickedClass = StringVar()
                clickedClass.set("Select Class")
                dropCols = OptionMenu(my_w, clickedClass, *cols)
                dropCols.grid(column=3,row=5)
                Button(my_w,text="Compute",command= lambda:computeOperation()).grid(column=2,row=7,padx=20,pady=30)
        

                def computeOperation():
                    attribute1 = clickedAttribute1.get()
                    attribute2 = clickedAttribute2.get()
                    category = clickedClass.get()
                    arrClass = data[category].unique()
                    g = data.groupby(category)
                    f = {
                    attribute1: 'sum',
                    attribute2: 'sum'
                    }
                    v1 = g.agg(f)
                    print(v1)
                    v = v1.transpose()
                    print(v)
                    
                    tv1 = ttk.Treeview(my_w,height=3)
                    tv1.grid(column=1,row=8,padx=5,pady=8)
                    tv1["column"] = list(v.columns)
                    tv1["show"] = "headings"
                    for column in tv1["columns"]:
                        tv1.heading(column, text=column)

                    df_rows = v.to_numpy().tolist()
                    for row in df_rows:
                        tv1.insert("", "end", values=row)

                    total = v1[attribute1].sum()+v1[attribute2].sum()
                    chiSquare = 0.0
                    for i in arrClass:
                        chiSquare += (v.loc[attribute1][i]-(((v[i].sum())*(v1[attribute1].sum()))/total))*(v.loc[attribute1][i]-(((v[i].sum())*(v1[attribute1].sum()))/total))/(((v[i].sum())*(v1[attribute1].sum()))/total)
                        chiSquare += (v.loc[attribute2][i]-(((v[i].sum())*(v1[attribute2].sum()))/total))*(v.loc[attribute2][i]-(((v[i].sum())*(v1[attribute2].sum()))/total))/(((v[i].sum())*(v1[attribute2].sum()))/total)
                    
                    degreeOfFreedom = (len(v)-1)*(len(v1)-1)
                    Label(my_w,text="Chi-square value is "+str(chiSquare), justify='center',height=2,fg="green").grid(column=1,row=9,padx=5,pady=8) 
                    Label(my_w,text="Degree of Freedom is "+str(degreeOfFreedom), justify='center',height=2,fg="green").grid(column=1,row=10,padx=5,pady=8) 
                    res = ""
                    if chiSquare > degreeOfFreedom:
                        res = "Attributes " + attribute1 + ' and ' + attribute2 + " are strongly correlated."
                    else:
                        res = "Attributes " + attribute1 + ' and ' + attribute2 + " are not correlated."
                    Label(my_w,text=res, justify='center',height=2,fg="green").grid(column=1,row=11,padx=5,pady=8)

        def show_dispersion():
                if(file):
                    fob=open(file,'r')
                    data = pd.read_csv(file)
                    cols = []
                for i in data:
                    cols = data.columns
                    clickedAttribute1 = StringVar()
                    clickedAttribute1.set("Select Attribute1")
                    dropCols = OptionMenu(my_w, clickedAttribute1, *cols)
                    dropCols.grid(column=1,row=5)
                    clickedAttribute2 = StringVar()
                    clickedAttribute2.set("Select Attribute2")
                    dropCols = OptionMenu(my_w, clickedAttribute2, *cols)
                    dropCols.grid(column=2,row=5)
                    Button(my_w,text="Compute",command= lambda:ComputeDispersion()).grid(column=2,row=7,padx=20,pady=30) 
                    # trv.insert("",'end',iid=None,text=data)
        
                    def ComputeDispersion():
                        attribute1 = clickedAttribute1.get()
                        attribute2 = clickedAttribute2.get()
                        
                        sum = 0
                        for i in range(len(data)):
                            sum += data.loc[i, attribute1]
                        avg1 = sum/len(data)
                        sum = 0
                        for i in range(len(data)):
                            sum += (data.loc[i, attribute1]-avg1)*(data.loc[i, attribute1]-avg1)
                        var1 = sum/(len(data))
                        sd1 = math.sqrt(var1)
                        
                        sum = 0
                        for i in range(len(data)):
                            sum += data.loc[i, attribute2]
                        avg2 = sum/len(data)
                        sum = 0
                        for i in range(len(data)):
                            sum += (data.loc[i, attribute2]-avg2)*(data.loc[i, attribute2]-avg2)
                        var2 = sum/(len(data))
                        sd2 = math.sqrt(var2)
                        
                        sum = 0
                        for i in range(len(data)):
                            sum += (data.loc[i, attribute1]-avg1)*(data.loc[i, attribute2]-avg2)
                        covariance = sum/len(data)
                        pearsonCoeff = covariance/(sd1*sd2)    
                        Label(my_w,text="Covariance value is "+str(covariance), justify='center',height=2,fg="blue").grid(column=1,row=8,padx=5,pady=8) 
                        Label(my_w,text="Correlation coefficient(Pearson coefficient) is "+str(pearsonCoeff), justify='center',height=2,fg="blue").grid(column=1,row=9,padx=5,pady=8) 
                        res = ""
                        if pearsonCoeff > 0:
                            res = "Attributes " + attribute1 + ' and ' + attribute2 + " are positively correlated."
                        elif pearsonCoeff < 0:
                            res = "Attributes " + attribute1 + ' and ' + attribute2 + " are negatively correlated."
                        elif pearsonCoeff == 0:
                            res = "Attributes " + attribute1 + ' and ' + attribute2 + " are independant."
                        Label(my_w,text=res, justify='center',height=2,fg="blue").grid(column=1,row=11,padx=5,pady=8)

        def show_Plots():
            if(file):
                    fob=open(file,'r')
                    data = pd.read_csv(file)
                    cols = []
            for i in data.columns:
                cols.append(i)
                clickedAttribute1 = StringVar()
                clickedAttribute1.set("Select Attribute1")
                dropCols = OptionMenu(my_w, clickedAttribute1, *cols)
                dropCols.grid(column=1,row=5)
                clickedAttribute2 = StringVar()
                clickedAttribute2.set("Select Attribute2")
                dropCols = OptionMenu(my_w, clickedAttribute2, *cols)
                dropCols.grid(column=2,row=5)
                clickedClass = StringVar()
                clickedClass.set("Select class")
                dropCols = OptionMenu(my_w, clickedClass, *cols)
                dropCols.grid(column=3,row=5)
                normalizationOperations = ["Min-Max normalization","Z-Score normalization","Normalization by decimal scaling"]
                clickedOperation = StringVar()
                clickedOperation.set("Select Normalization Operation")
                dropOperations = OptionMenu(my_w, clickedOperation, *normalizationOperations)
                dropOperations.grid(column=4,row=5)
                Button(my_w,text="Compute",command= lambda:computePlotOperation()).grid(column=2,row=7,padx=20,pady=30)


                def computePlotOperation():
                        attribute1 = clickedAttribute1.get()
                        attribute2 = clickedAttribute2.get() 
                        operation = clickedOperation.get()
                        if operation == "Min-Max normalization":
                            n = len(data)
                            arr1 = []
                            for i in range(len(data)):
                                arr1.append(data.loc[i, attribute1])
                            arr1.sort()
                            min1 = arr1[0]
                            max1 = arr1[n-1]
                            
                            arr2 = []
                            for i in range(len(data)):
                                arr2.append(data.loc[i, attribute2])
                            arr2.sort()
                            min2 = arr2[0]
                            max2 = arr2[n-1]
                            
                            for i in range(len(data)):
                                data.loc[i, attribute1] = ((data.loc[i, attribute1]-min1)/(max1-min1))
                            
                            for i in range(len(data)):
                                data.loc[i, attribute2] = ((data.loc[i, attribute2]-min2)/(max2-min2))
                        elif operation == "Z-Score normalization":
                            sum = 0
                            for i in range(len(data)):
                                sum += data.loc[i, attribute1]
                            avg1 = sum/len(data)
                            sum = 0
                            for i in range(len(data)):
                                sum += (data.loc[i, attribute1]-avg1)*(data.loc[i, attribute1]-avg1)
                            var1 = sum/(len(data))
                            sd1 = math.sqrt(var1)
                            
                            sum = 0
                            for i in range(len(data)):
                                sum += data.loc[i, attribute2]
                            avg2 = sum/len(data)
                            sum = 0
                            for i in range(len(data)):
                                sum += (data.loc[i, attribute2]-avg2)*(data.loc[i, attribute2]-avg2)
                            var2 = sum/(len(data))
                            sd2 = math.sqrt(var2)
                            
                            for i in range(len(data)):
                                data.loc[i, attribute1] = ((data.loc[i, attribute1]-avg1)/sd1)
                            
                            for i in range(len(data)):
                                data.loc[i, attribute2] = ((data.loc[i, attribute2]-avg2)/sd2)
                        elif operation == "Normalization by decimal scaling":        
                            j1 = 0
                            j2 = 0
                            n = len(data)
                            arr1 = []
                            for i in range(len(data)):
                                arr1.append(data.loc[i, attribute1])
                            arr1.sort()
                            max1 = arr1[n-1]
                            
                            arr2 = []
                            for i in range(len(data)):
                                arr2.append(data.loc[i, attribute2])
                            arr2.sort()
                            max2 = arr2[n-1]
                            
                            while max1 > 1:
                                max1 /= 10
                                j1 += 1
                            while max2 > 1:
                                max2 /= 10
                                j2 += 1
                            
                            for i in range(len(data)):
                                data.loc[i, attribute1] = ((data.loc[i, attribute1])/(pow(10,j1)))
                            
                            for i in range(len(data)):
                                data.loc[i, attribute2] = ((data.loc[i, attribute2])/(pow(10,j2)))
                        
                        Label(my_w,text="Normalized Attributes", justify='center',height=2,fg="green").grid(column=1,row=8,padx=5,pady=8)         
                        tv1 = ttk.Treeview(my_w,height=15)
                        tv1.grid(column=1,row=9,padx=5,pady=8)
                        tv1["column"] = [attribute1,attribute2]
                        tv1["show"] = "headings"
                        for column in tv1["columns"]:
                            tv1.heading(column, text=column)
                        i = 0
                        while i < len(data):
                            tv1.insert("", "end", iid=i, values=(data.loc[i, attribute1],data.loc[i, attribute2]))
                            i += 1
                        sns.set_style("whitegrid")
                        sns.FacetGrid(data, hue=clickedClass.get(), height=4).map(plt.scatter, attribute1, attribute2).add_legend()
                        plt.title("Scatter plot")
                        plt.show(block=True)

my_w.config(menu=menubar)

my_w.mainloop()
