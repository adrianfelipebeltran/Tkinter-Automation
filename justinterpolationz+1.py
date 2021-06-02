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
                #print('depth z is')
                #print(depth)
                #print('depth z -1 is')
                #print(depthlast)
                unit = df.iloc[z]['unit weight']
                #print('overburden z-1')
                #print(overburden)
                additional = deltadepth*unit
                #print('additional')
                #print(additional)
                overburden = deltadepth*unit + overburden
                #print('overburden z')
                #print(overburden)
        if test>=df.iloc[z]['depth'] and addedinterp==0:
            print('interpolation time baby')
            depth = df.iloc[z]['depth']
            u1 = df.iloc[z]['unit weight']
            u2 = df.iloc[z-2]['unit weight']
            print('below is u1')
            print(u1)
            print('below is u2')
            print(u2)
                        #it seems we can't decide if z-2 or z-1 will always work
            x_factor = (test-depthlast)/(depth-depthlast)
            print(x_factor)
            total = abs(u1-u2)
            if u1<u2:
                unitweight = total*x_factor + u1
            if u2<u1:
                unitweight = total*x_factor + u2
            deep = test-depthlast
            if u2==u1:
                unitweight = u1
            print('unitweight interpolation is')
            print(unitweight)
            print('your input is this much from the previous depth')
            print(deep)
            addedinterp = unitweight*deep
            print(addedinterp)
            print(overburden)
            overburden = overburden - addedinterp
            print(overburden)
    print("did it work or nah")


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

