import pandas
from bokeh.plotting import figure
from bokeh.io import output_file, show
import tkinter as tkinter
from tkinter import filedialog, messagebox

def loadFile():

    # Initialize variables for the file path and data frame containing the data.
    theFile = filedialog.askopenfilename()
    theData = pandas.DataFrame()

    # Check the type of the file loaded and execute relevant function. Prompt user to select valid file is none is selected.
    if theFile.endswith(".csv"):
        theData = pandas.read_csv(theFile)
    elif theFile.endswith((".xls",".xlsx")):
        theData = pandas.read_excel(theFile)
    else:
        tkinter.messagebox.showwarning(message="Please select a valid file format. .csv, .xls, or .xlsx")
        theFile = filedialog.askopenfilename()

    # TODO: iterate through columns in data file, present a pick list, and allow user to select columns for graph.
    x=theData["x"]
    y=theData["y"]
    # TODO: implement user-defined file name for graph. Default will be 'default_graph_DATETIME.html'.
    output_file("test.html")
    # TODO: implement user-defined graph paramters, like tools for the graph, type of graph, etc.
    theGraph=figure()
    theGraph.line(x,y)
    show(theGraph)