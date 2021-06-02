import tkinter as tk
from tkinter import *
import tkFileDialog as filedialog


def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\Cakow\\PycharmProjects\\Main",
                                          title="Open file okay?",
                                          filetypes= (("excel file","*.xlsx"),
                                          ("all files","*.*")))
    file = open(filepath,'r')
    print(filepath)
    file.close()

window = Tk()
button = Button(text="Open",command=openFile)
button.pack()
window.mainloop()
