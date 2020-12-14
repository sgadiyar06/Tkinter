from tkinter import *
from tkinter.font import Font
root = Tk()
root.geometry('300x200')
root.title('Spinbox')

sb = Spinbox(root,from_= 0,to=20,width=30,
             font = Font(family='Helvetica',size = 36,weight='bold'))  #increase font size to increase the height of the box
sb.pack()



root.mainloop()