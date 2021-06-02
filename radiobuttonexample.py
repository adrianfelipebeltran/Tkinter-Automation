#!/usr/bin/env python
# -*- coding: utf-8 -*-

#****************************
#EXCEL MUST HAVE THE FOLLOWING:
#column named 'Pressure (tsf)' and 'Void Ratio'
#first row must be column names as indicated above
#****************************

#importing is important 
import tkinter as tk
import pandas as pd
import matplotlib as pit
import numpy as np
import datetime as dt
import glob
import os
import functools
import math

path = 'C:\Python Scripts\Excel\Book1.xlsx'
df = pd.read_excel(path)
df.drop('Machine Defl. (in.)', axis =1, inplace=True)
df = df.dropna()
print(df)
inter = df['Pressure (tsf)']
intertwo = df['Void Ratio']
series = inter.values.tolist()
string = " tsf --- "
conc = ["{}{}".format(i,string) for i in series]

series1 = intertwo.values.tolist()
string3 = " void ratio"
conc2 = ["{}{}".format(i,string3) for i in series1]

# using map() + lambda + zip()
# interlist element concatenation
conc = list(map(lambda(i, j): i + j, zip(conc, conc2)))


window = tk.Tk()
window.title('这儿会有数学的答案')
 
window.geometry('500x500')
 
var1 = tk.StringVar()
l = tk.Label(window, bg='green', fg='yellow',font=('Arial', 12), width=50, textvariable=var1)
l.pack()

var2 = tk.StringVar()
l = tk.Label(window, bg='green', fg='yellow',font=('Arial', 12), width=50, textvariable=var2)
l.pack()

def print_selection():
    #in green the selection is printed after pressing button
    value = lb.get(lb.curselection())   
    var1.set(value)
    #the index of the value selected is a tuple
    tuple1 = lb.curselection()
    # Convert Tuple to integer
    # Using reduce() + lambda
    global res
    res = functools.reduce(lambda sub, ele: sub * 10 + ele, tuple1)
    # printing value straight from dataframe
    global one
    one = df.iloc[res]['Pressure (tsf)']
    global two
    two = df.iloc[res]['Void Ratio']
    print(one)
    print(two)

def print_selection2():
    #in green the selection is printed after pressing button
    value = lb.get(lb.curselection())   
    var2.set(value)
    #the index of the value selected is a tuple
    tuple2 = lb.curselection()
    # Convert Tuple to integer
    # Using reduce() + lambda
    resi = functools.reduce(lambda sub, ele: sub * 10 + ele, tuple2)
    # printing value straight from dataframe
    global three
    three = df.iloc[resi]['Pressure (tsf)']
    global four
    four = df.iloc[resi]['Void Ratio']
    print(three)
    print(four)

def calc():
    answer = (two-four)/math.log(three/one,(10))
    print(answer)
    
    
b1 = tk.Button(window, text='Value 1', width=15, height=2, command=print_selection)
b1.pack()
b2 = tk.Button(window, text='Value 2', width=15, height=2, command=print_selection2)
b2.pack()
b3 = tk.Button(window, text='Calculate!', width=15, height=2, command=calc)
b3.pack()
lb = tk.Listbox(window, listvariable=conc)
lb.config(width = 50, height=100)
lb.insert(10, *conc)
lb.pack()
 
window.mainloop()
