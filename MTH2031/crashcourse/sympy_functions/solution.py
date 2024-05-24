import sympy as sy

x, y, z, t = sy.symbols('x,y,z,t')
Eq1 = sy.Eq(2*x+3*y, 3)
eq = Eq1.subs(y, 2)
x = sy.solve(eq, x)

f = sy.exp(sy.sin(y))
f_ = f.diff(y)

g = sy.Function('g')(z)

diffeq = sy.Eq(g.diff(z, 2), 2*z**2 + g)

gsol = sy.dsolve(diffeq)


