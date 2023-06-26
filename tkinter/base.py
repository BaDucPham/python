from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import messagebox


root = Tk()
root.title('Ngoc Anh ngok nghek')
root.iconbitmap('E:\\workspace\\python\\tkinter\\icon\\test.ico')



def open():
    global my_img
    top = Toplevel()
    top.filename = filedialog.askopenfilename(initialdir='E:\\workspace\\python\\tkinter\\images', title= 'Select A File', filetypes=(('png files','*.png'),('jpg files','*.jpg'),('all files','*.*')))
    lbl = Label(top, text = 'Hello').pack()
    my_label = Label(top,text = top.filename).pack()
    my_img = ImageTk.PhotoImage(Image.open(top.filename))
    my_label =  Label(top,image=my_img).pack()
    btn = Button(top, text = 'close window', command = top.destroy).pack()

btn = Button(root, text='Open file', command=open).pack()

root.mainloop()