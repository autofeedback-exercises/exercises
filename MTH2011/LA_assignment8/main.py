import sympy as sy

A = sy.Matrix([[1,0,0], [1,1,0], [1, 1, 1]])

Astar = A.adjoint()

Hermitian = (A == Astar)
normal = (A*Astar == Astar * A)
unitary = (A*Astar == sy.eye(3))

B = sy.Matrix([[1,2,0], [0,1,2], [2,0, 1]])
U, D = B.diagonalize(normalize=True)
print(U)


