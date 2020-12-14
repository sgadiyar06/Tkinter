from tkinter import *

root = Tk()

#create dictionary for faster button creation
values = {"RadioButton 1" : "1", 
          "RadioButton 2" : "2", 
          "RadioButton 3" : "3", 
          "RadioButton 4" : "4", 
          "RadioButton 5" : "5"} 
#iterate throught dictionary rather than create the buttons one by one
for (text,value) in values.items():
    Radiobutton(root,text=text,
                value = value,indicator=0,
                background = 'light blue').pack()
button = Button(root,text='Exit',command=root.destroy)
button.pack()

root.mainloop()