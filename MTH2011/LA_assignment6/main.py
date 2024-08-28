import sympy as sp
A=sp.Matrix([[1,-1,-1,],[1,3,1],[-3,1,-1]])
Epairs = (A.eigenvects())
print(Epairs)
P, D = A.diagonalize()
print(P)
print(D)
