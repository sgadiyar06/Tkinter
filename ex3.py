'''
A DNA sequence is a string made up of As, Ts, Cs, and Gs. Write a GUI
application in which a DNA sequence is entered, and when the Count
button is clicked, the number of As, Ts, Cs, and Gs are counted and displayed in the window (see the image below)
'''

from tkinter import *

#function to count the frequency and store it in a dictionary
def char_count(dna,counter):
    data = DNA.get('0.0',END)
    counts = {}
    for char in "ATCG":
        counts[char] = data.count(char)
    output.set('Num As:{} Num Ts:{} Num Cs:{} Num Gs:{}'.format(counts['A'],counts['T'],counts['C'],counts['G']))



root = Tk()

#adding a frame
frame = Frame(root)
frame.pack()

#creating a variable for user input
DNA = Text(frame,height=10,width=40)
DNA.pack()


#output data variable
output = StringVar()

#new frame for the button and the output
new_frame = Frame(root)
new_frame.pack()

#button to perform the count operation
button = Button(new_frame,text='Count',command= lambda: char_count(DNA,output))
button.pack()


#output shown
label = Label(new_frame,textvar=output)
label.pack()



root.mainloop()