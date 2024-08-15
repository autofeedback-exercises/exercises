import sympy as sp

#Q2 worked
A=sp.Matrix([[0,2,-1,],[2,3,-2],[-1,-2,0]])

sp.pprint(A.eigenvects())
P=sp.Matrix([[1,-2,-1],[0,1,-2],[1,0,1]])
D=sp.Matrix([[-1,0,0],[0,-1,0],[0,0,5]])
P1,D1=A.diagonalize()
sp.pprint(P1)
sp.pprint(P)
sp.pprint(D1)
sp.pprint(D)

N = sp.Matrix([[0,0,1],[1,0,0],[0,1,0]])
sp.pprint(N.eigenvects())
L,D = N.diagonalize()
sp.pprint(L)
sp.pprint(D)
