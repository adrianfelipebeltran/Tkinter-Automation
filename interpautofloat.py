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
from tkFileDialog import *
import tkinter as tk
from tkinter import *
import tkFileDialog as filedialog
from tkinter import ttk
from tkFileDialog import askopenfilename

path = 'C:\Python Scripts\Excel\Book1.xlsx'
df = pd.read_excel(path)
dff = pd.read_excel(path)
df.drop(['Machine Defl. (in.)', 'Reach', 'Boring', 'Depth', 'Sample #',
                  'USCS', 'Sat (%)', 'w (%)', 'gamma_d (pcf)', 'LL', 'PI',
                   'Gs', 'Pc (tsf)', 'Cc Lab', 'eo', 'Cr'], axis=1, inplace=True)

def interp():
    test = float(dff.iloc[0]['Depth'])
    print (test)
    df = pd.read_excel(path, sheetname = '1')
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
            print('below is the amount of weight added')
            print(addedinterp)
            print('below is the overburden before interpolation')
            print(overburden)
            overburden = overburden - addedinterp
            print('below is the overburden after interpolation')
            print(overburden)
    
    print('overburden is below')
    print(overburden)

b1 = tk.Button(window, text='Choose Wisely 1', width=15, height=2, command=print_selection)
b1.pack()

lb = tk.Listbox(window, listvariable=conc)
lb.config(width = 50, height=100)
lb.insert(10, *conc)
lb.pack()

window.mainloop()
