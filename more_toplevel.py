#program to create top level widgets using a button

from tkinter import *

root = Tk()
root.title('Root Window')
root.geometry('450x300')

label = Label(root,text='This is in the root')
label.pack()

#a function for the 1st top level window
def Open_TopLevel1():
    #create top level widget
    top1 = Toplevel(root)
    top1.title('TOP LEVEL 1')
    top1.geometry('200x200')
    #create a label
    label = Label(top1,text='This window is in TOP LEVEL 1 window')
    label.pack()
    #button to create another top level widget
    new = Button(top1,text='New window',command=Open_TopLevel2)
    new.pack()
    #create an exit button
    exit = Button(top1,text='Exit',command=top1.destroy)
    exit.pack()

    #keep the window open until manually closed
    top1.mainloop()


def Open_TopLevel2():
    #Top level widget creation
    top2 = Toplevel()
    top2.title('TOP LEVEL 2')
    top2.geometry('200x100')

    #label
    label = Label(top2,text='This window is in TOP LEVEL 2 window')
    label.pack()

    #exit
    exit = Button(top2,text='Exit',command=top2.destroy)
    exit.pack()

    #keep the window open until manually closed
    top2.mainloop()


#button to create toplevel widget
button = Button(root,text='Open TOP LEVEL 1',command=Open_TopLevel1)
button.pack()

#exit
exit = Button(root,text='Exit',command=root.destroy)
exit.pack()


root.mainloop()