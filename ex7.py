from tkinter import *
#from exs.proj import devProj

import re

mainWindow = Tk()
mainWindow.title('Extron Python Training')

clrBlue = "#65c5f0"
clrRed = "#ff6666"
clrGreen = "#00d9a3"

class devProj:

    def __init__ (self, name):
        self.name = name

    def control(function) :
        if function[:3] == 'PWR' :
            if 'on' in function.lower() :
                return 'Power ON'
            elif 'off' in function.lower() :
                return'Power OFF'
            else:
                return'ERR1'
        elif function[:3] == 'INP':
            inp = function[4:]
            return'Input ' + inp
        elif function[:3] == 'PMT':
            if 'on' in function.lower() :
                return'Picture mute on'
            elif 'off' in function.lower() :
                return'Picture mute off'
            else :
                return'ERR2'
        else :
            return'ERR0'

    def feedback (function):
        global BtnPON, BtnPOFF, BtnIn1, BtnIn2, BtnIn3, BtnIn4, BtnMuteON, BtnMuteOFF
        print (function)
        if function[:5] == 'Power':
            if 'on' in function.lower():
                BtnPON.configure(background=clrGreen)
                BtnPOFF.configure(background="white")
            elif 'off' in function.lower():
                BtnPON.configure(background="white")
                BtnPOFF.configure(background=clrRed)
        elif function[:5] == 'Input':
            input = function[6:]
            print (input)
            if input == '1':
                BtnIn2.configure(background="white")
                BtnIn3.configure(background="white")
                BtnIn4.configure(background="white")
                BtnIn1.configure(background=clrBlue)
            if input == '2':
                BtnIn1.configure(background="white")
                BtnIn3.configure(background="white")
                BtnIn4.configure(background="white")
                BtnIn2.configure(background=clrBlue)
            if input == '3':
                BtnIn2.configure(background="white")
                BtnIn1.configure(background="white")
                BtnIn4.configure(background="white")
                BtnIn3.configure(background=clrBlue)
            if input == '4':
                BtnIn2.configure(background="white")
                BtnIn3.configure(background="white")
                BtnIn1.configure(background="white")
                BtnIn4.configure(background=clrBlue)
        elif function[:12] == 'Picture mute':
            if 'on' in function.lower():
                BtnMuteOFF.configure(background="white")
                BtnMuteON.configure(background=clrRed)
            elif 'off' in function.lower():
                BtnMuteON.configure(background="white")
                BtnMuteOFF.configure(background=clrGreen)

def sendMessage(function):
    print (devProj.control(function))
    devProj.feedback(devProj.control(function))

# making buttons
BtnPON = Button(mainWindow)
BtnPOFF = Button(mainWindow)
BtnIn1 = Button(mainWindow)
BtnIn2 = Button(mainWindow)
BtnIn3 = Button(mainWindow)
BtnIn4 = Button(mainWindow)
BtnMuteON = Button(mainWindow)
BtnMuteOFF = Button(mainWindow)

# buttons config
BtnPON.grid(row=2, column=1)
BtnPOFF.grid(row=2, column=2)
BtnIn1.grid(row=3, column=1)
BtnIn2.grid(row=3, column=2)
BtnIn3.grid(row=3, column=3)
BtnIn4.grid(row=3, column=4)
BtnMuteON.grid(row=4, column=1)
BtnMuteOFF.grid(row=4, column=2)

BtnPON.configure(text='Power ON', height=3, width=9, background="white", command=lambda: sendMessage('PWR_ON'))
BtnPOFF.configure(text='Power OFF', height=3, width=9, background="white", command=lambda: sendMessage('PWR_OFF'))
BtnIn1.configure(text='Input 1', height=3, width=9, background="white", command= lambda: sendMessage('INP_1'))
BtnIn2.configure(text='Input 2', height=3, width=9, background="white", command= lambda: sendMessage('INP_2'))
BtnIn3.configure(text='Input 3', height=3, width=9, background="white", command= lambda: sendMessage('INP_3'))
BtnIn4.configure(text='Input 4', height=3, width=9, background="white", command= lambda: sendMessage('INP_4'))
BtnMuteON.configure(text='Vid Mute ON', height=3, width=9, background="white", command=lambda: sendMessage('PMT_ON'))
BtnMuteOFF.configure(text='Vid Mute OFF', height=3, width=9, background="white", command=lambda: sendMessage('PMT_OFF'))

# show window
mainWindow.mainloop()