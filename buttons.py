from tkinter import *

root = Tk()

#a function to perform when the button is clicked
def myClick():
    mylabel = Label(root,text = 'You clicked the button')
    mylabel.pack()

#creating the button
myButton = Button(root, text = 'Click here', padx = 25, pady = 25, command = myClick)
myButton.pack()

root.mainloop()
