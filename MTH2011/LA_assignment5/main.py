import sympy as sy

# Q2 
T=sy.Matrix([[1,-1,1,0],[0,0,-1,1],[0,1,-1,1]])
imT = T.columnspace()
kerT = T.nullspace()
rankT = T.rank()

# Q4 worked
L = sy.Matrix([[0,1,0],[1,0,1],[0,1,1]])
R = sy.Matrix([[2,1,0],[1,2,2],[1,0,2]])

M=L.LUsolve(R)
