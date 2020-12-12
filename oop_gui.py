from tkinter import *

class Counter:
    '''
    GUI program using the concepts of Object Oriented Programming
    '''
    def __init__(self,parent):
        '''
        Creation of the GUI
        '''
        #setting a frame for the window
        self.parent = parent
        self.frame = Frame(parent)
        self.frame.pack()

        #setting a counter variable
        self.state = IntVar()
        self.state.set(0)
        
        #adding a label
        self.label = Label(self.frame,textvariable=self.state)
        self.label.pack()

        #adding button
        # self.up = Button(self.frame,text='Up',command=self.up_click)
        self.up = Button(self.frame,text='Up',command= lambda: self.b_click(1))
        self.up.pack(side='left')
        
        #adding button
        # self.down = Button(self.frame,text='Down',command=self.down_click)
        self.down = Button(self.frame,text='Down',command= lambda: self.b_click(-1))
        self.down.pack(side='left')

        #adding a quit button
        self.exit = Button(self.frame,text='quit',command=self.quit_click)
        self.exit.pack()

    def up_click(self):
        '''
        Button functionality for the up counter button
        '''
        self.state.set(self.state.get() + 1)

    def down_click(self):
        '''
        Button functionality for the down counter button
        '''
        self.state.set(self.state.get() - 1)

    def b_click(self,value):
        '''
        Button functionality for the up/down counter button
        '''
        self.state.set(self.state.get() + value)

    def quit_click(self):
        '''
        Button functionality for the exit button
        '''
        self.parent.destroy()

if __name__ == "__main__":
    
    root = Tk()
    mycounter = Counter(root)
    root.mainloop()