from tkinter import *

# making window
mainWindow = Tk()
mainWindow.title('Extron Python Training')

pinStars = ''
pinCode = '1230'
pinEntered = ''

# defining push func
def pinTouch(but):
    global pinStars
    pinStars += '*'
    pinLabel.configure(text = pinStars)
    global pinEntered
    pinEntered += str(but)

# defining clear func
def pinClear():
    global pinEntered, pinStars
    pinEntered = ''
    pinStars = ''
    pinLabel.configure(text = pinStars)

# defining enter func
def pinEnter():
    global pinEntered, pinCode, pinStars
    if len(pinEntered) == 4:
        if pinEntered == pinCode:
            pinLabel.configure(text = 'DONE')
        else:
            pinLabel.configure(text = 'WRONG')
    elif len(pinEntered) > 4:
        pinLabel.configure(text = 'MUCH')
    else:
        pinLabel.configure(text = 'LESS')
    pinEntered = ''
    pinStars = ''

# defining delete func
def pinDelete():
    global pinEntered, pinStars
    pinEntered = pinEntered[:-1]
    pinStars = pinStars[:-1]
    pinLabel.configure(text = pinStars)

# making label
pinLabel = Label(mainWindow, relief = 'groove', height=2, width =7)

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