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
    x = len(df['depth'])
    print(x)
    print(df)
    z=0
    overburden = 0
    depthlast = 0
    addedinterp = 0
    zz = 0

    while z+1 < x:
        depth = df.iloc[z]['depth']
        depthlast = df.iloc[z-1]['depth']
        z = z+1
        if test<df.iloc[z-1]['depth']:
            if depth < depthlast:
                deltadepth = depthlast - depth
                print(deltadepth)
                unit = df.iloc[z-1]['unit weight']
                additional = deltadepth*unit
                overburden = deltadepth*unit + overburden
                print(overburden)
        if test>=df.iloc[z]['depth'] and addedinterp==0:
            if df.iloc[z-2]['depth']<df.iloc[z]['depth']:
                return
            print('interpolation time baby')
            depth = df.iloc[z+1]['depth']
            depthlastlast = df.iloc[z-2]['depth']
            print('depth is below')
            print(depth)
            print('depth z-2 is below')
            print(depthlastlast)
            u1 = df.iloc[z]['unit weight']
            deep = test-depthlast
            
            unitweight = u1
            print('unitweight is')
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
    
    print('overburden is below')
    print(overburden)
    


def plotmeplz():
    df = pd.read_excel(filepath, sheetname = '1')
    plt.style.use('ggplot')
    fig, ax = plt.subplots()
    xseries = df['depth']
    yseries = df['unit weight']
    ax.set_title('Design Line Interpolation')
    ax.set_ylabel('unitweight')
    ax.set_xlabel('depth')
    plt.plot(xseries,yseries)
    plt.show()
    xxx = np.linspace(-80, 0, 10000, endpoint=False)
    type(xxx)
    
e1 = Entry(window)
e1.pack()
b4 = tk.Button(window, text="DO NOT PUSH THIS BUTTON", width = 25, height = 2, command=interp)
b4.pack()
b5 = tk.Button(window, text = "Unit Weight v Depth Plot Plz", width =25, height=2, command = plotmeplz)
b5.pack()

window.mainloop()
#y = df['unit weight']
#ax.set_title('Design Line Interpolation')
#ax.set_ylabel('unitweight')
#ax.set_xlabel('depth')
#plt.plot(x,y)
#global f
#f = interp1d(x, y)

    
#yy = f(x)
#print(f(-38))
#plt.plot(x, yy)
#plt.show(
