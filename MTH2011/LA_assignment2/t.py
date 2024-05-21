import sympy as sp

a,b,c=sp.symbols('a,b,c')
B=sp.Matrix([[1, a, a**2], [1, b, b**2], [1, c, c**2] ] )
sp.pprint(sp.factor(B.det()))

