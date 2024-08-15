import sympy as sp

# Q2 worked
T=sp.Matrix([[1,-1,1],[1,0,-1],[0,1,0],[1,1,-1]])
sp.pprint(T.columnspace())
sp.pprint(T.nullspace())
sp.pprint(T.rank())

# Q4 worked
V = sp.Matrix([[1,1,0],[0,1,1],[0,0,1]])
R = sp.Matrix([[2,3,4],[4,6,6],[4,3,2]])

sp.pprint(V)
sp.pprint(R)
M=sp.symbols("M")
expr = V*M - R
T=V.LUsolve(R)
sp.pprint(T)
sp.pprint(sp.solve(expr, 0*R,[M]))
