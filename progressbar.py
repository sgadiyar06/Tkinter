from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry('300x200')

#create a progress bar
progress = Progressbar(root,orient=HORIZONTAL,length=100,mode='determinate')
progress.pack()

#function responsible for the visuals which load
def bar():
    import time
    for i in range(1,11):
        progress['value'] = 10 * i
        root.update_idletasks()
        time.sleep(1)

#create button to start the visual
button = Button(root,text='Start',command = bar)
button.pack()

root.mainloop()