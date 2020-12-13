#question 4
'''
A GUI interface which converts the temperature from Fahrenheit
to degree celsius
'''

from tkinter import *

def to_cel(fahr):
    c = (fahr-32) * 5/9
    celsius.set(c)

root = Tk()

frame = Frame(root)
frame.pack()
frame2 = Frame(root)
frame2.pack()

celsius = IntVar()
fahr = IntVar()

label2 = Label(frame,text='Enter the value in Fahrenheit')
label2.pack()

entry = Entry(frame,textvar=fahr)
entry.pack()

label = Label(frame,textvar=celsius)
label.pack()

convert = Button(frame2,text='Convert',command= lambda: to_cel(fahr.get()))
convert.pack()
stop = Button(frame2,text='Exit',command=root.destroy) 
stop.pack()

root.mainloop()