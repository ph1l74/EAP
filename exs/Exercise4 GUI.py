'''
Python Training Exercise 4

Here is the GUI & storage for the PIN excersise

Rupert Powell 13-07-15
'''
from tkinter import *
import json             # for storing the pin hash variable
import os               # to write to the file system

window = Tk()

def digitEntered(but):
    ''' Digit 0-9 button pressed event '''
    PinLabel.configure(text = but)
    pass

def pinClear():
    ''' CLR button pressed event '''
    pass

def pinEnter():
    ''' ENT button pressed event '''
    pass

def pinBack():
    ''' < button pressed event '''
    pass

# check to see if the data file "pin.txt" already exists
fname = "pin.txt"
if os.path.isfile(fname):
    # file exists so get data
    with open(fname) as json_file:
        storedPin = json.load(json_file)
else:
    # no such file so set defaults
    # stores the default PIN code to a file if no file found on the disk
    storedPin = '1230'
    with open(fname, 'w') as outfile:
        json.dump(storedPin, outfile)    

PinLabel=Label(window, relief = 'groove', width = 9, text='PIN')

# define the number pad buttons for the GUI
Digit0Btn = Button(window)
Digit1Btn = Button(window)
Digit2Btn = Button(window)
Digit3Btn = Button(window)
Digit4Btn = Button(window)
Digit5Btn = Button(window)
Digit6Btn = Button(window)
Digit7Btn = Button(window)
Digit8Btn = Button(window)
Digit9Btn = Button(window)

# a list of all the digits
Digits = [Digit0Btn,Digit1Btn,Digit2Btn,Digit3Btn,Digit4Btn,Digit5Btn,
          Digit6Btn,Digit7Btn,Digit8Btn,Digit9Btn]

EnterBtn = Button(window)
BackBtn = Button(window)
ClearBtn = Button(window)

PinLabel.grid(row=1, column=2)
BackBtn.grid(row=1,column=3)
Digit7Btn.grid(row=2, column=1)
Digit8Btn.grid(row=2, column=2)
Digit9Btn.grid(row=2, column=3)
Digit4Btn.grid(row=3, column=1)
Digit5Btn.grid(row=3, column=2)
Digit6Btn.grid(row=3, column=3)
Digit1Btn.grid(row=4, column=1)
Digit2Btn.grid(row=4, column=2)
Digit3Btn.grid(row=4, column=3)
Digit0Btn.grid(row=5, column=2)
ClearBtn.grid(row=5,column=1) 
EnterBtn.grid(row=5,column=3) 


# Label all the objects on the window and set their commands
ClearBtn.configure(text='CLR', height=3, width=5, command = pinClear)
EnterBtn.configure(text='ENT', height=3, width=5, command = pinEnter)
BackBtn.configure(text='<', command = pinBack)
''' NOTE: The lambda command means the value of the button is passed 
at run-time, and not when the loop is run!'''
for x in range(0,10):
    Digits[x].configure(text=x, height=3, width=5, 
                        command = lambda x = x : digitEntered(x))
    
#invoke the window
window.mainloop()