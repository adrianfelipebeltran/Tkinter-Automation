#!/usr/bin/env python
# -*- coding: utf-8 -*-

#****************************
#EXCEL MUST HAVE THE FOLLOWING:
#column named 'Pressure (tsf)' and 'Void Ratio'
#first row must be column names as indicated above
#bool_series = pd.notnull(df['Cv (ft2/day)'])
#bool series relies on existence of column named 'Cv (ft2/day)'
#this Cv column is assumed to have values everywhere except where the "start" tsf value might ruin the plotting of a chart
#so this column is used to delete that one string value from an otherwise normal list of numbers
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
from tkFileDialog import *
import tkinter as tk
from tkinter import *
import tkFileDialog as filedialog
from tkinter import ttk
from tkFileDialog import askopenfilename

#filepath = filedialog.askopenfilename(initialdir="C:",
#                                          title="Open file okay?",
#                                          filetypes= (("excel file","*.xlsx"),
#                                         ("all files","*.*")))

global path
path = 'C:\Python Scripts\Excel\Book1.xlsx'
df = pd.read_excel(path)
dff = pd.read_excel(path)
df.drop(['Machine Defl. (in.)', 'Reach', 'Boring', 'Depth', 'Sample #',
                  'USCS', 'Sat (%)', 'w (%)', 'gamma_d (pcf)', 'LL', 'PI',
                   'Gs', 'Pc (tsf)', 'Cc Lab', 'eo'], axis=1, inplace=True)

#identify which rows are filled with Null values
#so that we can remove
bool_series = pd.notnull(df['Pressure (tsf)'])
nonnan = df[bool_series]
#we will need to use the length of this series later on
global length
length = len(nonnan)
#we will need to use the length of this series later on
inter = nonnan['Pressure (tsf)']
intertwo = nonnan['Void Ratio']
#alternate bool_series to clean up data for plotting
bool_series_alternate = pd.notnull(df['Cv (ft2/day)'])
nonnantwo = df[bool_series_alternate]
interthree = nonnantwo['Pressure (tsf)']
interfour = nonnantwo['Void Ratio']
#change numbers into list for concatenation
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
window.title("This is Alex Ramirez's Fault")
 
window.geometry('500x600')
 
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
    global C_c
    C_c = (two-four)/math.log(three/one,(10))
    stringyfloat = str(C_c)
    print(one)
    print(two)
    string = 'the value of C_c is ' + stringyfloat
    print(string)
    dff['C_c new'] = ''
    dff.at[0, 'C_c new'] = C_c
    #calculating C_r
    length = len(nonnan)-1
    lengthh = length - 2
    onee = df.iloc[lengthh]['Pressure (tsf)']
    twoo = df.iloc[lengthh]['Void Ratio']
    threee = df.iloc[length]['Pressure (tsf)']
    fourr = df.iloc[length]['Void Ratio']
    global c_r
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
    print(dff)
    
    
def testme():
    s2 = dff.iloc[2]['Vertical Strain (%)']
    s1 = dff.iloc[1]['Vertical Strain (%)']
    p1 = dff.iloc[1]['Pressure (tsf)']
    p2 = dff.iloc[2]['Pressure (tsf)']
    sigmav = overburden
    Ev = s2-(p2-sigmav)*(s2-s1)/(p2-p1)
    dff['Ev'] = ''
    dff.at[0, 'Ev'] = Ev
    dff["Depth>5'"] = ''
    dff.at[0, "Depth>5'"] = dff.iloc[0]['Depth']
    dff.at[0, 'Ev'] = Ev
    if Ev < 3:
        dff.at[1, 'Ev']=1
    if Ev >=3:
        dff.at[1,'Ev']=0
    if dff.iloc[0]['Sat (%)']>95:
        dff.at[1, 'Sat (%)'] = 1
    if dff.iloc[0]['Sat (%)']<=95:       
        dff.at[1, 'Sat (%)'] = 0
    if dff.iloc[0]['Depth']>5:
        dff.at[1, "Depth>5'"] = 1
    if dff.iloc[0]['Depth']<=5:
        dff.at[1, "Depth>5'"] = 0
    #calculating sowers nc tsf always the same
    NC= pow(10, math.log10(three)+(four-dff.iloc[0]['eo'])/C_c)
    dff['Sowers(NC)(tsf)'] = ''
    dff.at[0, 'Sowers(NC)(tsf)'] = NC
    #initial slope is needed for Sowers OC tsf
    initial = (interfour.iloc[0]-interfour.iloc[1])/math.log10(interthree.iloc[0]/interthree.iloc[1])
    dff['Initial Slope']=''
    dff.at[0,'Initial Slope']= initial
    powow = 1/(C_c+initial)
    pboy1 = initial*math.log10(interthree.iloc[0])
    
    pboy2 = four-interfour.iloc[0]+C_c*math.log10(three)
       
    powowow = pboy2 + pboy1
    
    powowowow = powow*powowow
    
    OCC = pow(10,  powowowow)   
    dff['Sowers(OC)(tsf)']= ''
    dff.at[0,'Sowers(OC)(tsf)'] = OCC 
    dff['sigma_p = Pc']=''
    hellohelp = dff.iloc[0]['Pc (tsf)']
    print(hellohelp)
    dff.at[0,'sigma_p = Pc']= hellohelp
    dff['Difference < 25%']=''
    differencelessthan = abs((dff.iloc[0]['Pc (tsf)']- OCC)/dff.iloc[0]['Pc (tsf)'])
    dff.at[0, 'Difference < 25%']=differencelessthan
    if differencelessthan<0.25:
        dff.at[1, 'Difference < 25%']=1
    if differencelessthan>=0.25:
        dff.at[1,'Difference < 25%']=0
    print(dff)
    
def save():
    text = os.path.basename(path)
    one = 'C:\\New\\temp\\'
    two = '_output.csv'
    name = one + text + two
    dff.to_csv (name, index = False, header=True)
    print(dff)
    
def plot():
    #let's plot this son of a gun
    title = dff.iloc[0]['Boring']
    plt.style.use('ggplot')
    fig, ax = plt.subplots()
    #some uwu plot style shwag
    ax.set_title(title)
    ax.set_ylabel('Void Ratio')
    ax.set_xlabel('Effective Stress')
    plt.plot(interthree,interfour)
    plt.xscale("log")
    plt.show()

def plotsc():
    #lets figure out this schmertmann business
    
    pointoney= dff.iloc[0]['eo']-c_r*math.log10(dff.iloc[0]['Pc (tsf)']/overburden)
    
    varpointtwoy = 0.42*dff.iloc[0]['eo']
    varpointtwox = (four - varpointtwoy)/C_c

    pointtwoxalmost = pow(10, varpointtwox)
    
    pointtwox = three*pointtwoxalmost
    pointx = [pointtwox, overburden, dff.iloc[0]['Pc (tsf)']]
    pointy = [varpointtwoy, dff.iloc[0]['eo'], pointoney ]
    print(pointx)
    print(pointy)
    
    #let's plot this son of a gun
    title = dff.iloc[0]['Boring']
    plt.style.use('ggplot')
    fig, ax = plt.subplots()
    #some uwu plot style shwag
    ax.set_title(title)
    ax.set_ylabel('Void Ratio')
    ax.set_xlabel('Effective Stress')
    plt.plot(interthree,interfour)
    plt.plot(pointx, pointy)
    plt.xscale("log")
    plt.show()

def interp():
    dfff = pd.read_excel(path)
    pretest = dfff.iloc[0]['Depth']
    test = np.negative(pretest)
    print(test)
    df = pd.read_excel(path, sheetname = '1')
    x = len(df['depth'])
    z=0
    global overburden
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
            overburden= overburden/2000
    
    dff['sigma_v']=''
    dff.at[0, 'sigma_v']= overburden
    print('overburden is below')
    print(overburden)
    print(dff)
    
    

b1 = tk.Button(window, text='Select First "pressure --- void" Pair then click me', width=50, height=2, command=print_selection)
b1.pack()
b2 = tk.Button(window, text='Select Second "pressure --- void" Pair then click me', width=50, height=2, command=print_selection2)
b2.pack()
b9 = tk.Button(window, text='Overburden from Excel Column "Depth"', width=40, height=2, command=interp)
b9.pack()
b3 = tk.Button(window, text='Calculate C_c, C_r, etc from above selection', width=40, height=2, command=calc)
b3.pack()
b6 = tk.Button(window, text='Consolidation Test Rating (VT)', width=40,  height=2, command=testme)
b6.pack()
b10 = tk.Button(window, text='Plot w/out Schmertann', width=40, height = 2, command =plot)
b10.pack()
b7 = tk.Button(window, text='Plot w/ Schmertann', width=40, height = 2, command =plotsc)
b7.pack()
#e1 = Entry(window)
#e1.pack()
b8 = tk.Button(window, text='Save', width=15, height=2, command=save)
b8.pack()

lb = tk.Listbox(window, listvariable=conc)
lb.config(width = 50, height=100)
lb.insert(10, *conc)
lb.pack()

window.mainloop()
