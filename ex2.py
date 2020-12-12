#question 2
'''
Write a GUI application with a single button. Initially the button is labeled
0, but each time it is clicked, the value on the button increases by 1.
'''
from tkinter import *

root = Tk()

count = IntVar()
count.set(0)
def increment():
    count.set(count.get()+1)
frame = Frame(root)
frame.pack()
button = Button(frame,textvariable=count,command=increment,width=20,height=10,font=('20'))
button.pack()
exit_button = Button(root,text='exit',command=root.destroy)
exit_button.pack()

root.mainloop()