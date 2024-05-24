import sympy as sy
x = sy.symbols('x')
G = sy.exp(-x**2)
sy.pprint(G.diff(x,2))
