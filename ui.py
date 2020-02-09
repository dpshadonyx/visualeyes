import functions
from tkinter import *

window=Tk()

loadButton=Button(window,text="Click to load a file",command=functions.loadFile)
loadButton.grid()

window.mainloop()