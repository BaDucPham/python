import re
from sympy import Matrix, lcm
from tkinter import *


root = Tk()
root.title('Chemical equation')
root.iconbitmap('E:\\vscode\\python\\tkinter\\icon\\test.ico')
elementList=[]
elementMatrix=[]

def addToMatrix(element, index, count, side):
    if(index == len(elementMatrix)):
       elementMatrix.append([])
       for x in elementList:
            elementMatrix[index].append(0)
    if(element not in elementList):
        elementList.append(element)
        for i in range(len(elementMatrix)):
            elementMatrix[i].append(0)
    column=elementList.index(element)
    elementMatrix[index][column]+=count*side
    
def findElements(segment,index, multiplier, side):
    elementsAndNumbers=re.split('([A-Z][a-z]?)',segment)
    i=0
    while(i<len(elementsAndNumbers)-1):#last element always blank
          i+=1
          if(len(elementsAndNumbers[i])>0):
            if(elementsAndNumbers[i+1].isdigit()):
                count=int(elementsAndNumbers[i+1])*multiplier
                addToMatrix(elementsAndNumbers[i], index, count, side)
                i+=1
            else:
                addToMatrix(elementsAndNumbers[i], index, multiplier, side)        
    
def compoundDecipher(compound, index, side):
    segments=re.split('(\([A-Za-z0-9]*\)[0-9]*)',compound)    
    for segment in segments:
        if segment.startswith("("):
            segment=re.split('\)([0-9]*)',segment)
            multiplier=int(segment[1])
            segment=segment[0][1:]
        else:
            multiplier=1
        findElements(segment, index, multiplier, side)


def balance():
    global eq
    global elementMatrix
    s = eq.get()
    s_split = s.strip().split('=')
    reactants, products = s_split[0], s_split[1]
    reactants=reactants.replace(' ','').split("+")
    products=products.replace(' ','').split("+")
    for i in range(len(reactants)):
        compoundDecipher(reactants[i],i,1)
    for i in range(len(products)):
        compoundDecipher(products[i],i+len(reactants),-1)
    elementMatrix = Matrix(elementMatrix)
    elementMatrix = elementMatrix.transpose()
    solution=elementMatrix.nullspace()[0]
    multiple = lcm([val.q for val in solution])
    solution = multiple*solution
    coEffi=solution.tolist()
    output=""
    for i in range(len(reactants)):
        output+=str(coEffi[i][0])+reactants[i]
        if i<len(reactants)-1:
            output+=" + "
    output+=" -> "
    for i in range(len(products)):
        output+=str(coEffi[i+len(reactants)][0])+products[i]
        if i<len(products)-1:
            output+=" + "
    frame1 = Label(root, text = re.sub('1', '', output))
    frame1.grid(row = 1 , column = 0,columnspan = 3)



eq_label = Label(root,text = 'Chemical equation')
eq_label.grid(row = 0, column = 0,padx = 10, pady = 10)
eq = Entry(root,width=30, fg = 'blue', borderwidth=1)
eq.grid(row = 0, column = 1, padx = 10, pady = 10)


btn_eq = Button(root, text = 'balance',
                    command = balance)           
btn_eq.grid(row = 0 , column = 2, padx = 10, pady = 10)

root.mainloop()