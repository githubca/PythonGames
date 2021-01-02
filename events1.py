from tkinter import *
import sys

def hello(event):
    print("Single Click, Button-l") 
def doubleClicked(event):                           
    print("Double Click, button-1") 
    sys.exit()
def tripleClicked(event):
    print("triple click, button-1")

widget = Button(None, text='Mouse Clicks')
widget.pack()
widget.bind('<Button-1>', hello)
widget.bind('<Double-Button-1>', doubleClicked) 
widget.bind('<Triple-Button-1>', doubleClicked) 

widget.mainloop()