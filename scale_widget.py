from tkinter import *

root = Tk()

#create a interactive variable
v1 = DoubleVar()

#create a scale widget
scl = Scale(root,variable=v1,from_=1,to=100,orient=VERTICAL)
scl.pack()

#a function to fetch the current value on the slider
def print_val():
    value = 'Slider value is '+str(v1.get())
    label.config(text=value)
#create a label to display the value
label = Label(root)
label.pack()

#a button to fetch to call the function print_val
button = Button(root,text='Show value',command=print_val)
button.pack()
#exit button
exit = Button(root,text='Exit',command=root.destroy)
exit.pack()

root.mainloop()