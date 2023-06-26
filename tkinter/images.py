from tkinter import *
from  PIL import ImageTk, Image

root = Tk()
root.title('Ngoc anh ngok nghek')
root.iconbitmap('E:\\workspace\\python\\tkinter\\test.ico')

my_img = ImageTk.PhotoImage(Image.open('E:\\workspace\\python\\ML and AI\\imageanalysis\\puppy.jpg'))
my_label = Label(image = my_img)
my_label.pack()


button_quit = Button(root, text = 'Exit program', command = root.quit)
button_quit.pack()

root.mainloop()
