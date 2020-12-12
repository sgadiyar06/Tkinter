from tkinter import *

root = Tk()

#entry widget
e = Entry(root, width = 20)
e.pack()
e.insert(0,'Enter your name:') #add a default value

#create a button function
def myClick():
    name = 'Hello ' + e.get()
    mylabel = Label(root,text = name)
    mylabel.pack()

#create a button
myButton = Button(root, text = 'Click Here', command = myClick)
myButton.pack()


root.mainloop()