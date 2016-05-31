from tkinter import *

window = Tk()

# scene levels 2 dimensional list here
# ------------------------------------#
label1 = Label( window,relief = 'groove',width = 6)
label2 = Label( window,relief = 'groove',width = 6)
label3 = Label( window,relief = 'groove',width = 6)
label4 = Label( window,relief = 'groove',width = 6)
label5 = Label( window,relief = 'groove',width = 6)
label6 = Label( window,relief = 'groove',width = 6)
scene1Btn = Button(window)
scene2Btn = Button(window)

# geometry
label1.grid()
label2.grid()
label3.grid()
label4.grid()
label5.grid()
label6.grid()
scene1Btn.grid()
scene2Btn.grid()

# ------------------------------------#
# scene recall function goes here
# ------------------------------------#

# Button Command
def recall1() :
    pass

def recall2() :
    pass

# initialise buttons
window.title('Extron Python Training')
label1.configure(text = '...')
label2.configure(text = '...')
label3.configure(text = '...')
label4.configure(text = '...')
label5.configure(text = '...')
label6.configure(text = '...')
scene1Btn.configure(text = 'Recall Scene 1', command = recall1)
scene2Btn.configure(text = 'Recall Scene 2', command = recall2)

#sustain window
window.mainloop()
