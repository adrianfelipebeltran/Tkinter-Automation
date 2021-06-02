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


filepath = filedialog.askopenfilename(initialdir="C:\\Users\\Cakow\\PycharmProjects\\Main",
                                          title="Open file okay?",
                                          filetypes= (("excel file","*.xlsx"),
                                         ("all files","*.*")))

window = tk.Tk()
window.title("This is also Alex Ramirez's Fault")
window.geometry('500x500')

def interp():
    test = float(e1.get())
    print (test)
    df = pd.read_excel(filepath, sheetname = '1')
    plt.style.use('ggplot')
    fig, ax = plt.subplots()
    x = len(df['depth'])
    print(x)
    print(df)
    z=0
    overburden = 0
    depthlast = 0
    addedinterp = 0
    zz = 0

    while z+1 < x:
        print('depth')
        print (df.iloc[z]['depth'])
        depth = df.iloc[z]['depth']
        depthlast = df.iloc[z-1]['depth']
        z = z+1
        if test<df.iloc[z]['depth']:
            if depth < depthlast:
                deltadepth = depthlast - depth
                unit = df.iloc[z]['unit weight']
                additional = deltadepth*unit
                overburden = deltadepth*unit + overburden
                print(overburden)
        if test>=df.iloc[z]['depth'] and addedinterp==0:
            print('interpolation time baby')
            depth = df.iloc[z+1]['depth']
            depthlastlast = df.iloc[z-2]['depth']
            print('depth is below')
            print(depth)
            print('depth z-2 is below')
            print(depthlastlast)
            u1 = df.iloc[z+1]['unit weight']
            u2 = df.iloc[z-2]['unit weight']
            print('below is u1')
            print(u1)
            print('below is u2')
            print(u2)
            print('below is the x_factor')
            x_factor = (test-depthlast)/(depth-depthlast)
            print(x_factor)
            total = abs(u1-u2)
            print('total differnce between u1 and u2')
            print(total)
            deep = test-depthlast
            if df.iloc[z-2]['depth']<df.iloc[z]['depth']:
                return
            if u1<u2:
                print(x_factor)
                unitweight = u2 - total*x_factor
                print('u1 less than u2')
            if u2<u1:
                unitweight = total*x_factor + u2
                print('u2 less than u1')                
            if u2==u1:
                unitweight = u1
                print('u2 and u1 are identical')
                
            print('unitweight interpolation is')
            print(unitweight)
            print('your input is this much from the previous depth')
            print(deep)
            addedinterp = unitweight*deep
            print(addedinterp)
            print('below is the overburden before interpolation')
            print(overburden)
            overburden = overburden - addedinterp
            print('below is the overburden after interpolation')
            print(overburden)
    print("did it work or nah")
    print('overburden is below i guess')
    print(overburden)

e1 = Entry(window)
e1.pack()
b4 = tk.Button(window, text="DO NOT PUSH THIS BUTTON", width = 25, height = 2, command=interp)
b4.pack()

window.mainloop()
#y = df['unit weight']
#ax.set_title('Design Line Interpolation')
#ax.set_ylabel('unitweight')
#ax.set_xlabel('depth')
#plt.plot(x,y)
#global f
#f = interp1d(x, y)
#xxx = np.linspace(-80, 0, 10000, endpoint=False)
#yy = f(x)
#print(f(-38))
#plt.plot(x, yy)
#plt.show(
