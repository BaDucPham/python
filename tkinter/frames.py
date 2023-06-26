from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


root = Tk()
root.title('Ngoc Anh ngok nghek')
root.iconbitmap('E:\\workspace\\python\\tkinter\\icon\\test.ico')

frame = LabelFrame(root, text = 'This is my frame...', padx= 50, pady = 50)
frame.pack(padx = 10,  pady = 10)

r = IntVar()
MODES =  [('a','a'),('b','b'),('c','c'),('d','d')]

ch = StringVar()
ch.set('a')

for charac, val in MODES:
    Radiobutton(root, text = charac, variable=ch, value= val) .pack(anchor=W)

def clicked(value):
    myLabel = Label(frame, text = value)
    myLabel.pack()

def popup(value):
    response = messagebox.askyesno('The value is', value)
    Label(root,text = response).pack()

myButton = Button(frame, text = 'Click', command = lambda: popup(ch.get()))
myButton.pack()
root.mainloop()