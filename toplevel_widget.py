from tkinter import *

root = Tk()
root.geometry('300x180')

#creating a label
label = Label(root,text='Root window')
label.pack()

#creating a top level widget
top = Toplevel()
top.geometry('180x110')

label2 = Label(top,text='First top level widget')
label2.pack()



root.mainloop()