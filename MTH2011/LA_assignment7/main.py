import sympy as sy

V = [ sy.Matrix([1,2,1]),sy.Matrix([1,1,1]) ]

basis = sy.GramSchmidt(V,orthonormal=True)

z = sy.Matrix([2,2,2])

a, b = sy.symbols("a,b")

coeff = sy.solve(a*basis[0] +b*basis[1] - z)
