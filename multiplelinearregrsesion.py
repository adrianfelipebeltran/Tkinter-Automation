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


#filepath = filedialog.askopenfilename(initialdir="C:\\Users\\Cakow\\PycharmProjects\\Main",
#                                          title="Open file okay?",
#                                          filetypes= (("excel file","*.xlsx"),
#                                         ("all files","*.*")))

filepath = 'C:\Python Scripts\Excel\Book1.xlsx'
df = pd.read_excel(filepath, sheetname = '1')
plt.style.use('ggplot')
fig, ax = plt.subplots()
x = len(df['depth'])
print(df)
z=0
test = -49
overburden = 0
depthlast = 0
while z <= x:
    print('depth')
    print (df.iloc[z]['depth'])
    z = z+1
    if test<df.iloc[z]['depth']:
        if df.iloc[z]['depth'] < df.iloc[z-1]['depth']:
            depth = df.iloc[z]['depth']
            depthlast = df.iloc[z-1]['depth']
            deltadepth = depth - depthlast
            unit = df.iloc[z]['unit weight']
            addedinterp = 0
            print('overburden before')
            print(overburden)
            additional = deltadepth*unit
            print('additional')
            print(additional)
            overburden = deltadepth*unit + overburden
            print('overburden after')
            print(overburden)
    if test>=df.iloc[z]['depth'] and addedinterp==0:
        addedinterp = (df.iloc[z]['unit weight'] - df.iloc[z-1]['unit weight'])*((test-depth)/deltadepth)
        print('interpolation time baby')
        print(overburden)
        overburden = overburden - addedinterp
        print(overburden)
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
