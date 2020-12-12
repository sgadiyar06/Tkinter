'''
A very simple calculator which can perform the 4 basic operations on only 2 numbers
'''
from tkinter import *

root = Tk()
root.title('Simple Calculator')

#entry widgets for the interface
e = Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_click(number):
    # e.delete(0,END)
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def button_clear():
    e.delete(0,END)

def add_button():
    first_number = e.get()
    global f_num
    global math_op
    math_op = 'addition'
    f_num = int(first_number)
    e.delete(0,END)

def sub_button():
    first_number = e.get()
    global f_num
    global math_op
    math_op = 'subtraction'
    f_num = int(first_number)
    e.delete(0,END)

def multiply_button():
    first_number = e.get()
    global f_num
    global math_op
    math_op = 'multiply'
    f_num = int(first_number)
    e.delete(0,END)

def div_button():
    first_number = e.get()
    global f_num
    global math_op
    math_op = 'division'
    f_num = int(first_number)
    e.delete(0,END)

def equal_button():
    second_num = e.get()
    e.delete(0,END)
    
    if math_op=='addition':
        e.insert(0,f_num + int(second_num))
    
    if math_op=='subtraction':
        e.insert(0,f_num - int(second_num))
    
    if math_op=='multiply':
        e.insert(0,f_num * int(second_num))
    
    if math_op=='division':
        e.insert(0,f_num / int(second_num))

#define the buttons
button_1 = Button(root,text='1',padx=40,pady=20,command=lambda: button_click(1))
button_2 = Button(root,text='2',padx=40,pady=20,command=lambda: button_click(2))
button_3 = Button(root,text='3',padx=40,pady=20,command=lambda: button_click(3))
button_4 = Button(root,text='4',padx=40,pady=20,command=lambda: button_click(4))
button_5 = Button(root,text='5',padx=40,pady=20,command=lambda: button_click(5))
button_6 = Button(root,text='6',padx=40,pady=20,command=lambda: button_click(6))
button_7 = Button(root,text='7',padx=40,pady=20,command=lambda: button_click(7))
button_8 = Button(root,text='8',padx=40,pady=20,command=lambda: button_click(8))
button_9 = Button(root,text='9',padx=40,pady=20,command=lambda: button_click(9))
button_0 = Button(root,text='0',padx=40,pady=20,command=lambda: button_click(0))
button_add = Button(root,text='+',padx=39,pady=20,command=add_button)
button_equal = Button(root,text='=',padx=89,pady=20,command=equal_button)
button_clear = Button(root,text='Clear',padx=79,pady=20,command=button_clear)

button_sub = Button(root,text='-',padx=41,pady=20,command=sub_button)
button_multiply = Button(root,text='*',padx=40,pady=20,command=multiply_button)
button_div = Button(root,text='/',padx=41,pady=20,command=div_button)

#putting the button on the screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_add.grid(row=5,column=0)
button_clear.grid(row=4,column=1,columnspan=2)
button_equal.grid(row=5,column=1,columnspan=2)

button_sub.grid(row=6,column=0)
button_multiply.grid(row=6,column=1)
button_div.grid(row=6,column=2)

root.mainloop()