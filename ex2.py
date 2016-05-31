from tkinter import *

# making window
mainWindow = Tk()
mainWindow.title('Extron Python Training')

lights = [[100, 100, 100, 100, 100, 100], [10, 20, 30, 40, 50, 60]]

labels = [1, 2, 3, 4, 5, 6]
scales = [1, 2, 3, 4, 5, 6]

# making labels and scales
for i in range(0, 6):
    labels[i] = Label(mainWindow, relief = 'groove', width = 6)
    labels[i].grid(row=i+1, column=1)
    labels[i].configure(text = str(lights[0][0]) + ' %')
    scales[i] = Scale(mainWindow, variable = lights[0][0], orient=HORIZONTAL)
    scales[i].grid(row=i+1, column=2)



# making button 01 function
def preset01Call():
    for i in range(0, 6):
        labels[i].configure(text = str(lights[0][i]) + ' %')
        scales[i].set(lights[0][i])

# making button 02 function
def preset02Call():
    for i in range(0, 6):
        labels[i].configure(text = str(lights[1][i]) + ' %')
        scales[i].set(lights[1][i])

def preset01Set():
    for i in range(0, 6):
        lights[0][i] = scales[i].get()

def preset02Set():
    for i in range(0, 6):
        lights[1][i] = scales[i].get()

# preset buttons
preset01Btn = Button(mainWindow)
preset02Btn = Button(mainWindow)
preset01Btn.grid(row=7, column=1)
preset02Btn.grid(row=8, column=1)
preset01Btn.configure(text = 'Preset 01 Call', command = preset01Call)
preset02Btn.configure(text = 'Preset 02 Call', command = preset02Call)

# preset buttons
Preset01Save = Button(mainWindow)
Preset02Save = Button(mainWindow)
Preset01Save.grid(row=7, column=2)
Preset02Save.grid(row=8, column=2)
Preset01Save.configure(text = 'Preset 01 Save', command = preset01Set)
Preset02Save.configure(text = 'Preset 02 Save', command = preset02Set)





# show window
mainWindow.mainloop()