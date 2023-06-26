import sympy
from sympy import *

A = Matrix([[1,1],[2,2]])
B = Matrix([[3,3],[4,4]])

C = Matrix(BlockMatrix([A,B]))
I = eye(2)
print(A)
print(B)
print(I)
C = Matrix(BlockMatrix([A,I]))
print(C)

s = 'CaO+HNO3=Ca(NO3)2+H2O'
s_split = s.split('=')
print(s_split)