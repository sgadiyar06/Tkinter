from tkinter import *

root = Tk()
#create a simple word label to add to the window

myLabel = Label(root, text = "Hello world")
myLabel2 = Label(root,text = 'My name is Sudarshan Gadiyar')

#pack the label on to a window
#myLabel.pack()

#I can also add them one by one in a grid
myLabel.grid(row = 0, column = 0)
myLabel2.grid(row = 1, column = 0)

#object oriented way
# myLabel = Label(root, text = "Hello world").grid(row = 0, column = 0)
# myLabel2 = Label(root,text = 'My name is Sudarshan Gadiyar').grid(row = 1, column = 0)

#tkinter loop has to be closed so it can give output
root.mainloop()
