import sympy as sp

# Q2 Worked
T= sp.Matrix([[1,-1,0],[0,1,-1],[-1,0,1]])

# test if self adjoint (hermitian) 
sp.pprint (T.adjoint()-T)

# test if unitary
sp.pprint(T.adjoint()*T - sp.eye(3))

# test if normal
sp.pprint(T.adjoint()*T - T*T.adjoint())


#Q4 worked
A = sp.Matrix([[0,2,1],[2,0,-1],[1,-1,-1]])


U,D = A.diagonalize(normalize=True)

sp.pprint(U)
sp.pprint(D)

sp.pprint(U*U.adjoint())
