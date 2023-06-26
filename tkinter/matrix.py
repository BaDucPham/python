from distutils import command
from tkinter import *
from pandas import reset_option
import sympy
from sympy import *
from sympy.abc import x
import numpy as np
from collections import defaultdict
import re

# Set up the main windows
root = Tk()
root.title('Matrix calculator')
root.iconbitmap('E:\\workspace\\python\\tkinter\\icon\\test.ico')
x = sympy.symbols('x')

# The block of function
def creat_mat():
    global dct, nrows, cols, name
    nr,nl = int(nrows.get()),int(ncols.get())
    dct = defaultdict(Entry)
    btn_input = Button(frame1,text = 'Save matrix',  command = save_mat)
    btn_input.grid(row = nr , column = 0, columnspan=nl)
    for widget in frame1.winfo_children():
        if widget != btn_input:
            widget.destroy()
    if name.get() != 'I' or nr != nl:
        for i in range(nr):
            for j in range(nl):
              dct['mat_{}_{}'.format(i,j)] = Entry(frame1,width=3)
              dct['mat_{}_{}'.format(i,j)].grid(row = i, column = j, padx = 1, pady = 1)
    
def mat_2_txt(mat):
    nr,nl = mat.shape
    return ''.join('\n\t'.join(['\t'.join(['{:<10}'.format(str(mat[i,j])) for j in range(nl)]) for i in range(nr)]))
    
def save_mat():
    global dct, matA, nrows, ncols,name,lb
    nr,nl = int(nrows.get()),int(ncols.get())
    matA = eye(nr)
    if name.get() != 'I' or nr !=nl:
        matA =  Matrix([[dct['mat_{}_{}'.format(i,j)].get() for j in range(nl)] for i in range(nr)])
    list_all_mat[name.get()] = matA

    ot = ''
    for name_mat, mat in list_all_mat.items():
        nr,nl = mat.shape
        ot += '{:<5} = {:<5}'.format(name_mat,'') + mat_2_txt(mat) + '\n'
    lb.config(text = ot)

def rank(mat):
    return mat.rank()

def rref(mat):
    return mat.rref()

def transpose(mat):
    return mat.transpose()

def im_ker(mat):
    nr,nl = mat.shape
    mat = Matrix(BlockMatrix([mat.transpose(),eye(nr)]))
    mat, v = rref(mat)
    im = []
    ker = []
    for i in range(nr):
        if any(c != 0 for c in mat[i,:nl]):
            im.append(Matrix(mat[i,:nl]))
        else:
            ker.append(Matrix(mat[i,nl:]))
    if len(ker) == 0:
        ker.append(Matrix([0 for _ in range(nr)]))
    return (im,ker)


def calcul():
    global e,res,list_all_mat
    C = e.get()
    C_split = re.split('(\W)', C)
    for i in range(len(C_split)):
        if C_split[i] in list_all_mat.keys():
            C_split[i] = "list_all_mat['{}']".format(C_split[i])
        elif C_split[i] == '^':
            C_split[i] = '**'
    ex = ''.join(C_split)
    ot = ''
    try:
        rest = eval(ex)
        if isinstance(rest,int):
            ot = str(rest)
        elif isinstance(rest,sympy.matrices.dense.MutableDenseMatrix):
            mat_res = np.array(rest)
            ot = mat_2_txt(mat_res)
        elif isinstance(rest,tuple):
            im,ker = rest
            ot = 'im = \n' + '\n'.join([mat_2_txt(c) for c in im]) + '\nker = \n' + '\n'.join([mat_2_txt(c) for c in ker])
        else:
            mat,temp = rest
            ot = mat_2_txt(np.array(mat))
    except Exception as error:
        ot = str(error)
    res.config(text = ot)
    


# The widget part 

frame0 = LabelFrame(root, text = 'Input matrix')
frame0.grid(row = 0 , column = 0)

name_label = Label(frame0,text = 'Name of matrix')
name_label.grid(row = 0, column = 0,padx = 10, pady = 10)
name = Entry(frame0,width=2, fg = 'blue', borderwidth=1)
name.grid(row = 0, column = 1, padx = 10, pady = 10)

nrows_label = Label(frame0,text = 'Number of rows')
nrows_label.grid(row = 1, column = 0,padx = 10, pady = 10)
nrows = Entry(frame0,width=2, fg = 'blue', borderwidth=1)
nrows.grid(row = 1, column = 1, padx = 10, pady = 10)

ncols_label = Label(frame0,text = 'Number of columns')
ncols_label.grid(row = 2, column = 0,padx = 10, pady = 10)
ncols = Entry(frame0,width=2, fg = 'blue', borderwidth=1)
ncols.grid(row = 2, column = 1, padx = 10, pady = 10)

btn_creat = Button(frame0, text = 'Create matrix',
                    command = creat_mat)           
btn_creat.grid(row = 3 , column = 0, columnspan=2, padx = 10, pady = 10)

frame1 = LabelFrame(root, text = 'Create matrix')
frame1.grid(row = 1 , column = 0)


frame2 = LabelFrame(root, text = 'Showing matrix')
frame2.grid(row = 0 , column = 1)


list_all_mat = defaultdict()
        
lb = Label(frame2)
lb.grid(row = 1, column = 0, padx = 10, pady = 10)


frame3 = LabelFrame(root, text = 'Operations')
frame3.grid(row = 1 , column = 1, padx = 10, pady = 10)
e = Entry(frame3,width=20, fg = 'blue', borderwidth=1)
e.grid(row = 0, column = 0, padx = 10, pady = 10)
res = Label(frame3)
res.grid(row = 2, column = 0, padx = 10, pady = 10)
btn_com = Button(frame3,text = 'Compute',  command = calcul)
btn_com.grid(row = 1 , column = 0)
root.mainloop()