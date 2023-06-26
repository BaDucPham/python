from tkinter import *
from  PIL import ImageTk, Image

root = Tk()
root.title('Ngoc anh ngok nghek')
root.iconbitmap('E:\\workspace\\python\\tkinter\\icon\\test.ico')


my_img1 = ImageTk.PhotoImage(Image.open('E:\\workspace\\python\\ML and AI\\imageanalysis\\puppy.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('E:\\workspace\\python\\tkinter\\images\\connected__improved__version_2__by_pikaira_d73kndi-fullview.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('E:\\workspace\\python\\tkinter\\images\\20494859.jpg'))
my_img4 = ImageTk.PhotoImage(Image.open('E:\\workspace\\python\\tkinter\\images\\download.jpg'))

image_list = [my_img1,my_img2,my_img3,my_img4]




def click(image_number=1):
    global my_label
    global button_forward
    global button_back
    global status

    my_label.grid_forget()

    my_label = Label(image = image_list[image_number])
    my_label.grid(row = 0, column = 0, columnspan = 3)

    button_forward = Button(root, text = '>>', command = lambda: click(image_number+1))
    button_back = Button(root, text = '<<', command = lambda: click(image_number-1))
    if image_number == len(image_list)-1:
        button_forward = Button(root, text = '>>', state = DISABLED)
    if image_number == 0:
        button_back = Button(root, text = '<<', state = DISABLED)
    button_back.grid(row=1,column = 0)
    button_forward.grid(row=1,column = 2)

    status.grid_forget()
    status = Label(root, text = 'Image {} of {}'.format(image_number+1,len(image_list)),bd=1,relief=SUNKEN, anchor= E)
    status.grid(row = 2, column = 0, columnspan = 3, sticky=W+E)


my_label = Label(image = my_img1)
my_label.grid(row = 0, column = 0, columnspan = 3)

button_forward = Button(root, text = '>>', command = lambda: click())
button_exit = Button(root, text = 'Exit program', command = root.quit)
button_back = Button(root, text = '<<', state = DISABLED)
button_back.grid(row=1,column = 0)
button_exit.grid(row=1,column = 1)
button_forward.grid(row=1,column = 2)

status = Label(root, text = 'Image 1 of {}'.format(len(image_list)),bd=1,relief=SUNKEN, anchor= E)
status.grid(row = 2, column = 0, columnspan = 3, sticky=W+E)


root.mainloop()
