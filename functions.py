import pandas, bokeh
import tkinter as tkinter
from tkinter import filedialog, messagebox

def loadFile():
    theFile = filedialog.askopenfilename()

    if theFile.endswith(".csv"):
        theData = pandas.read_csv(theFile)
        print(theData)
    elif theFile.endswith(".xls"):
        theData = pandas.read_excel(theFile)
        print(theData)
    else:
        tkinter.messagebox.showwarning(message="Please select a valid file format. .csv, .xls, or .xlsx")
        theFile = filedialog.askopenfilename()