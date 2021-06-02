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
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import glob
import os
import functools
import math

path = 'C:\Python Scripts\Excel\Book1.xlsx'
df = pd.read_excel(path)
dff = pd.read_excel(path)
df.drop(['Machine Defl. (in.)', 'Reach', 'Boring', 'Depth', 'Sample #',
                  'USCS', 'Sat (%)', 'w (%)', 'gamma_d (pcf)', 'LL', 'PI',
                   'Gs', 'Pc (tsf)', 'Cc Lab', 'eo', 'Cr'], axis=1, inplace=True)

#identify which rows are filled with Null values
#so that the next command can remove
bool_series = pd.notnull(df['Cv (ft2/day)'])
nonnan = df[bool_series]
inter = nonnan['Pressure (tsf)']
intertwo = nonnan['Void Ratio']
series = inter.values.tolist()
print(series)
string = " tsf --- "
conc = ["{}{}".format(i,string) for i in series]

series1 = intertwo.values.tolist()
string3 = " void ratio"
conc2 = ["{}{}".format(i,string3) for i in series1]

# using map() + lambda + zip()
# interlist element concatenation
conc = list(map(lambda(i, j): i + j, zip(conc, conc2)))


window = tk.Tk()
window.title("This is Alex Ramirez's Fault")
 
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
    #calculating C_c
    C_c = (two-four)/math.log(three/one,(10))
    stringyfloat = str(C_c)
    string = 'the value of C_c is ' + stringyfloat
    print(string)
    dff['C_c new'] = ''
    dff.at[0, 'C_c new'] = C_c
    #calculating C_r
    length = len(nonnan) - 1
    lengthh = length - 2
    onee = df.iloc[lengthh]['Pressure (tsf)']
    twoo = df.iloc[lengthh]['Void Ratio']
    threee = df.iloc[length]['Pressure (tsf)']
    fourr = df.iloc[length]['Void Ratio']
    c_r = (fourr-twoo)/math.log(onee/threee,(10))
    stringyfloat3 = str(c_r)
    print('the value of C_r is ' + stringyfloat3)
    dff['C_r'] = ''
    dff.at[0, 'C_r'] = c_r
    #calculating CcR
    ccr2= dff.iloc[0]['eo']
    ccr1=C_c
    ccr = ccr1/(1+ccr2)
    dff['CcR']=''
    dff.at[0, 'CcR'] = ccr
    stringyfloat2 = str(ccr)
    string2 = 'the value of CcR is ' + stringyfloat2
    print(string2)
    dff['CcR'] = ''
    dff.at[0, 'CcR'] = ccr
    #let's plot this son of a gun
    title = dff.iloc[0]['Boring']
    plt.style.use('ggplot')
    fig, ax = plt.subplots()
    #some uwu plot style shwag
    ax.set_title(title)
    ax.set_ylabel('Void Ratio')
    ax.set_xlabel('Effective Stress')
    plt.plot(inter,intertwo)
    plt.xscale("log")
    plt.show()
   
    
b1 = tk.Button(window, text='Choose Wisely 1', width=15, height=2, command=print_selection)
b1.pack()
b2 = tk.Button(window, text='Choose Wisely 2', width=15, height=2, command=print_selection2)
b2.pack()
b3 = tk.Button(window, text='Ill do the math for you, you lazy bum', width=40, height=2, command=calc)
b3.pack()
lb = tk.Listbox(window, listvariable=conc)
lb.config(width = 50, height=100)
lb.insert(10, *conc)
lb.pack()
 
window.mainloop()
