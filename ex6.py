from tkinter import *
import os, json, hashlib, binascii

# making window
mainWindow = Tk()
mainWindow.title('Extron Python Training')

loggedIn = False
pinCorrect = False

salt = 'salt'

pinStars = ''
pinEntered = ''
userID = ''
newPin = ''

file = open('ex6.ini', 'r')
pinCodes = json.load(file)
file.close()

# defining reset func
def resetAll():
    global pinStars, pinEntered
    pinStars = ''
    pinEntered = ''

# encryption func
def encrypt(pin):
    pinB = pin.encode(encoding='UTF-8')
    #saltB = salt.encode(encoding='UTF-8')
    pinCrypted = hashlib.md5(pinB)
    #print (" ", pin, "\n", pinB ,"\n", pinCrypted.hexdigest())
    return pinCrypted.hexdigest()

# defining push func
def pinTouch(but):
    global pinStars, pinEntered, pinCodes, userID, newPin
    if loggedIn:
        if pinCorrect:
            pinStars += '*'
            newPin += str(but)
            pinLabel.configure(text = newPin)
        else:
            pinStars += '*'
            pinLabel.configure(text = pinStars)
            pinEntered += str(but)
    else:
        userID += str(but)
        pinLabel.configure(text = userID)

# defining clear func
def pinClear():
    global pinEntered, pinStars, userID, newPin
    resetAll()
    userID = ''
    newPin = ''
    pinLabel.configure(text = pinStars)

# defining enter func
def pinEnter():
    global pinEntered, pinStars, userID, pinCodes, loggedIn, pinCorrect, newPin
    file = open('ex6.ini', 'r')
    pinCodes = json.load(file)
    file.close()
    if loggedIn:
        if pinCorrect:
            file = open('ex6.ini', 'w')
            pinCodes[userID] = str(encrypt(newPin))
            json.dump(pinCodes, file)
            pinLabel.configure(text = 'SAVED')
            userID = ''
            newPin = ''
            resetAll()
            loggedIn = False
            pinCorrect = False
        else:
            pinCrypted = str(encrypt(pinEntered))
            print (pinCrypted, '\n', str(pinCodes.get(userID)))
            if pinCrypted == str(pinCodes.get(userID)):
                pinCorrect = True
                pinLabel.configure(text = 'OK')
            else:
                pinCorrect = False
                loggedIn = False
                pinStars = ''
                pinEntered = ''
                userID = ''
                newPin = ''
    else:
        if userID in pinCodes.keys():
            loggedIn = True
            pinLabel.configure(text = 'LOGGED')
        else:
            loggedIn = False
            pinLabel.configure(text = 'NOT LOGGED')
            userID = ''
            resetAll()

# defining delete func
def pinDelete():
    global pinEntered, pinStars, userID, newPin
    if loggedIn:
        if pinCorrect:
            newPin = newPin[:-1]
            pinLabel.configure(text = newPin)
        else:
            pinEntered = pinEntered[:-1]
            pinStars = pinStars[:-1]
            pinLabel.configure(text = pinStars)
    else:
        userID = userID[:-1]
        pinLabel.configure(text = userID)

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
file.close()