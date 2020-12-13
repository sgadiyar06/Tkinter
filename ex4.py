#question 4
'''
A GUI interface which converts the temperature from Fahrenheit
to degree celsius
'''

from tkinter import *

def to_cel(fahr):
    c = (fahr-32) * 5/9
    converted.set(c)

def to_fahr(cel):
    f = (cel*9/5) + 32
    converted.set(f)

root = Tk()

frame = Frame(root)
frame.pack()
frame2 = Frame(root)
frame2.pack()

value = IntVar()
converted = IntVar()

state = StringVar()

state.set('Enter the value in Fahrenheit')
temp = 'Fahr'

def change_state():
    global temp
    if temp == 'Fahr':
        state.set('Enter the value in Celsius')
        temp = 'Cel'
    else:
        state.set('Enter the value in Fahrenheit')
        temp = 'Fahr'


label2 = Label(frame,textvar=state)
label2.pack()

entry = Entry(frame,textvar=value)
entry.pack()

label = Label(frame,textvar=converted)
label.pack()

change = Button(frame2,text='Change',command=change_state)
change.pack()

convert = Button(frame2,text='Convert',command= lambda: to_cel(value.get()) if temp=='Fahr' else to_fahr(value.get()) )
convert.pack()
stop = Button(frame2,text='Exit',command=root.destroy) 
stop.pack()

root.mainloop()