from tkinter import *
import os, json

# making window
mainWindow = Tk()
mainWindow.title('Extron Python Training')

pinCodes = {'user': ['0000', '9999'],
            'pin': ['1234', '4321']}

loggedIn = False

pinStars = ''
pinEntered = ''
userID = ''

# defining push func
def pinTouch(but):
    global pinStars, pinEntered, pinCodes, userID
    if loggedIn:
        pinStars += '*'
        pinLabel.configure(text = pinStars)
        pinEntered += str(but)
    else:
        userID += str(but)
        pinLabel.configure(text = userID)

# defining reset func
def resetAll():
    global pinStars, pinEntered, userID, loggedIn
    userID = ''
    pinStars = ''
    pinEntered = ''
    loggedIn = False

# defining clear func
def pinClear():
    global pinEntered, pinStars
    resetAll()
    pinLabel.configure(text = pinStars)
    print (pinEntered, pinStars)

# defining enter func
def pinEnter():
    global pinEntered, pinStars, userID, pinCodes, loggedIn
    if loggedIn:
        if pinEntered == pinCodes['pins']
        pinLabel.configure(text = 'WRONG')
    else:
        if userID in pinCodes['user']:
            loggedIn = True
            pinLabel.configure(text = 'LOGGED')
        else:
            pinLabel.configure(text = 'NO USER')
    resetAll()

# defining delete func
def pinDelete():
    global pinEntered, pinStars
    pinEntered = pinEntered[:-1]
    pinStars = pinStars[:-1]
    pinLabel.configure(text = pinStars)

# making label
pinLabel = Label(mainWindow, relief = 'groove', height=2, width =7)
pinLabel.config(text="USER ID")

# making buttons
pinBtn1 = Button(mainWindow)
pinBtn2 = Button(mainWindow)
pinBtn3 = Button(mainWindow)
pinBtn4 = Button(mainWindow)
pinBtn5 = Button(mainWindow)
pinBtn6 = Button(mainWindow)
pinBtn7 = Button(mainWindow)
pinBtn8 = Button(mainWindow)
pinBtn9 = Button(mainWindow)
pinBtn0 = Button(mainWindow)
pinBtnCLR = Button(mainWindow)
pinBtnENT = Button(mainWindow)
pinBtnDEL = Button(mainWindow)

buttons = [pinBtn0, pinBtn1, pinBtn2, pinBtn3, pinBtn4, pinBtn5, pinBtn6, pinBtn7, pinBtn8, pinBtn9, pinBtnCLR,
           pinBtnENT, pinBtnDEL]

# buttons config
pinLabel.grid(row=1, column=2)
pinBtnDEL.grid(row=1, column=3)
pinBtn7.grid(row=2, column=1)
pinBtn8.grid(row=2, column=2)
pinBtn9.grid(row=2, column=3)
pinBtn4.grid(row=3, column=1)
pinBtn5.grid(row=3, column=2)
pinBtn6.grid(row=3, column=3)
pinBtn1.grid(row=4, column=1)
pinBtn2.grid(row=4, column=2)
pinBtn3.grid(row=4, column=3)
pinBtnCLR.grid(row=5, column=1)
pinBtn0.grid(row=5, column=2)
pinBtnENT.grid(row=5, column=3)

for i in range(0,10):
    buttons[i].configure(text = i, height=2, width=5, command = lambda i = i : pinTouch(i))

pinBtnCLR.configure(text='CLR', height=2, width=5, command = pinClear)
pinBtnENT.configure(text='ENT', height=2, width=5, command = pinEnter)
pinBtnDEL.configure(text='<', height=2, width=5, command = pinDelete)

# show window
mainWindow.mainloop()