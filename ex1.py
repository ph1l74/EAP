from tkinter import *

# making window
mainWindow = Tk()
mainWindow.title('Extron Python Training')

lights = [[100, 100, 100, 100, 100, 100], [10, 20, 30, 40, 50, 60]]

# making labels
labels = [1, 2, 3, 4, 5, 6]

for i in range(0, 6):
    labels[i] = Label(mainWindow, relief = 'groove', width = 6)
    labels[i].pack(anchor=CENTER)
    labels[i].configure(text = str(lights[0][0]) + ' %')

# making buttons
Preset01Btn = Button(mainWindow)
Preset02Btn = Button(mainWindow)
Preset01Btn.pack(anchor=CENTER)
Preset02Btn.pack(anchor=CENTER)

# making button 01 function
def preset01():
    for i in range(0, 6):
        labels[i].configure(text = str(lights[0][i]) + ' %')

# making button 02 function
def preset02():
    for i in range(0, 6):
        labels[i].configure(text = str(lights[1][i]) + ' %')

# buttons config

Preset01Btn.configure(text = 'Preset 01', command = preset01)
Preset02Btn.configure(text = 'Preset 02', command = preset02)

# show window
mainWindow.mainloop()