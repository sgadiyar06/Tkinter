from tkinter import *

root = Tk()

root.title('Program')

quit_button = Button(root,text='EXIT',bg='red',command=root.quit)
quit_button.pack()

root.mainloop()
