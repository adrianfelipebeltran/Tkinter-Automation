#!/usr/bin/env python
# -*- coding: utf-8 -*-

#****************************
#EXCEL MUST HAVE THE FOLLOWING:
#column named 'Pressure (tsf)' and 'Void Ratio'
#first row must be column names as indicated above
#****************************

#importing is important
from scipy.interpolate import interp1d
from scipy import optimize
import tkinter as tk
from tkinter import *
import tkFileDialog as filedialog
from tkinter import ttk
from tkFileDialog import askopenfilename
import pandas as pd
import matplotlib as pit
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import glob
import os
import functools
import math

#******************************************
#sheet_name = must be used if newer version
#older version of python necessitates sheetname

#LAST DEPTH OF SOIL NEEDS EXTRA IDENTICAL ROW BENEATH
#OR ELSE INTERPOLATION NEAR BOTTOM ERRONEOUS

#MUST HAVE column names 'depth' 'unit weight' no caps, spaces
#******************************************
    
window = tk.Tk()
window.title("good 'ol fashioned approximating")
 
window.geometry('600x500')

#setting style
style = ttk.Style(window)
#print(style.theme_names())
current_theme = style.theme_use()
#print(current_theme)
style.theme_use('xpnative')



def depthcalc():
    
    userinput = float(e1.get())
    global var1
    print(type(userinput))
    var1.set(userinput)
    print(userinput)
    print df.iloc[0]['depth']
    print df.iloc[1]['depth']
    print(f(userinput))
        
        

def excelfile():

    global filepath
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\Cakow\\PycharmProjects\\Main",
                                          title="Open file okay?",
                                          filetypes= (("excel file","*.xlsx"),
                                          ("all files","*.*")))
    print(filepath)
    global df
    df = pd.read_excel(filepath, sheetname = '1')
    plt.style.use('ggplot')
    fig, ax = plt.subplots()
    x = df['depth']
    print(len(df['depth']))
    y = df['unit weight']
    ax.set_title('Design Line Interpolation')
    ax.set_ylabel('unitweight')
    ax.set_xlabel('depth')
    plt.plot(x,y)
    global f
    f = interp1d(x, y)
    xxx = np.linspace(-80, 0, 10000, endpoint=False)
    yy = f(x)
    print(f(-38))
    plt.plot(x, yy)
    plt.show()
    

    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11, 12, 13, 14, 15], dtype=float)
    y = np.array([5, 7, 9, 11, 13, 15, 28.92, 42.81, 56.7, 70.59, 84.47, 98.36, 112.25, 126.14, 140.03])

#two = tk.Label(window, bg='gray', fg='white',font=('Arial', 12), width=50, textvariable=var2)
#two.pack()
#var2.set('(╯°□°)╯︵ data must be on sheet two of uploaded excel file and columns must be named "depth" and "unit weight" no extra caps or spaces (╯°□°)╯︵')
#I wanted to have a little text show up with this warning but that will be for later I suppose
    
b1 = tk.Button(window, text='Pick a file, any (relevant excel) file', width=30, height=2, command=excelfile)
b1.pack()

var1 = tk.StringVar()

L1 = Label(text="Enter Depth")
L1.pack()
e1 = Entry(bd=5)
e1.pack()

b1 = tk.Button(window, text='Pick a depth, any depth', width=20, height=2, command=depthcalc)
b1.pack()

window.mainloop()
