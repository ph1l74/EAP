from tkinter import *

# making window
mainWindow = Tk()
mainWindow.title('Extron Python Training')

labels = [1, 2, 3, 4, 5, 6]
scales = [1, 2, 3, 4, 5, 6]

scalesValue = [1, 2, 3, 4, 5, 6]

# making labels
for i in range(0, 6):
    labels[i] = Label(mainWindow, relief = 'groove', width = 6)
    labels[i].grid(row=i+1, column=1)
    labels[i].configure(text = str(0) + ' %')

# defining func for showing scales value on labels
def showValues(self):
    for i in range (0,6):
        labels[i].configure(text = str(scales[i].get()) + ' %')

# making scales
for i in range(0, 6):
    scales[i] = Scale(mainWindow, variable = scalesValue[i], orient=HORIZONTAL, command = showValues)
    scales[i].grid(row=i+1, column=2)

# making button 01 call function
def preset01Call():
    file = open('ex3p01.ini', 'r')
    scalesValue = file.read().split(' ')
    for i in range (0,6):
        labels[i].configure(text = str(scalesValue[i]) + ' %')
        scales[i].set(scalesValue[i])
    file.close()

# making button 02 call function
def preset02Call():
    file = open('ex3p02.ini', 'r')
    scalesValue = file.read().split(' ')
    for i in range (0,6):
        labels[i].configure(text = str(scalesValue[i]) + ' %')
        scales[i].set(scalesValue[i])
    file.close()

# making button 01 save function
def preset01Set():
    file = open('ex3p01.ini', 'w')
    for i in range(0, 6):
        file.write(str(scales[i].get()) + " ")
    file.close()

# making button 02 save function
def preset02Set():
    file = open('ex3p02.ini', 'w')
    for i in range(0, 6):
        file.write(str(scales[i].get()) + ' ')
    file.close()

# preset call buttons
preset01Btn = Button(mainWindow)
preset02Btn = Button(mainWindow)
preset01Btn.grid(row=7, column=1)
preset02Btn.grid(row=8, column=1)
preset01Btn.configure(text = 'Preset 01 Call', command = preset01Call)
preset02Btn.configure(text = 'Preset 02 Call', command = preset02Call)

# preset save buttons
Preset01Save = Button(mainWindow)
Preset02Save = Button(mainWindow)
Preset01Save.grid(row=7, column=2)
Preset02Save.grid(row=8, column=2)
Preset01Save.configure(text = 'Preset 01 Save', command = preset01Set)
Preset02Save.configure(text = 'Preset 02 Save', command = preset02Set)

# show window
mainWindow.mainloop()