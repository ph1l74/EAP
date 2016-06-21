from tkinter import *
from exs import proj
import re


mainWindow = Tk()
mainWindow.title('Extron Python Training')

proj


# making buttons
pinBtnPON = Button(mainWindow)
pinBtnPOFF = Button(mainWindow)
pinBtnIn1 = Button(mainWindow)
pinBtnIn2 = Button(mainWindow)
pinBtnIn3 = Button(mainWindow)
pinBtnIn4 = Button(mainWindow)
pinBtnMuteON = Button(mainWindow)
pinBtnMuteOFF = Button(mainWindow)

buttons = [pinBtnPON, pinBtnPOFF, pinBtnIn1, pinBtnIn2, pinBtnIn3, pinBtnIn4, pinBtnMuteON, pinBtnMuteOFF]
button_names = ['Power ON', 'Power OFF', 'Input 1', 'Input 2', 'Input 3', 'Input 4', 'Vid Mute ON', 'Vid Mute OFF']

# buttons config
pinBtnPON.grid(row=2, column=1)
pinBtnPOFF.grid(row=2, column=2)
pinBtnIn1.grid(row=3, column=1)
pinBtnIn2.grid(row=3, column=2)
pinBtnIn3.grid(row=3, column=3)
pinBtnIn4.grid(row=3, column=4)
pinBtnMuteON.grid(row=4, column=1)
pinBtnMuteOFF.grid(row=4, column=2)

for i in range(0, 8):
    buttons[i].configure(text = button_names[i], height=3, width=9)

projStatus = ProjectorName.control('PWR_OFF')

# show window
mainWindow.mainloop()
