'''all exercises are from the practical programming book
unit 16 Creating GUI
'''
#question 1:
'''
Write a GUI application with a button labeled “Goodbye.” When the button
is clicked, the window closes.
'''
from tkinter import *

root = Tk()

exit_button = Button(root,text='Goodbye',command=root.quit)
exit_button.pack()

root.mainloop()