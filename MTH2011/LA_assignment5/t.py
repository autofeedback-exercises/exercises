import sympy as sp

V = sp.Matrix([[1,1,0],[0,1,1],[0,0,1]])
R = sp.Matrix([[2,3,4],[4,6,6],[4,3,2]])

sp.pprint(V)
sp.pprint(R)
T=V.LUsolve(R)
sp.pprint(T)
