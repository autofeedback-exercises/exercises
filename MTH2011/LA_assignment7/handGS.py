import sympy as sy

x = sy.symbols("x", real=True)
irange=(x,-1,1)

f0 = 1
f1 = x
f2 = x*x
M = [ sy.Matrix([f0]) , sy.Matrix([f1]) , sy.Matrix([f2]) ]

sy.pprint(sy.GramSchmidt(M))


v0 = f0/sy.integrate(1,irange)
sy.pprint(v0)
u1 = f1 - sy.integrate(f1*v0,irange)
v1 = u1 / sy.sqrt( sy.integrate(u1*u1,irange))
sy.pprint(v1)

u2 = f2 - sy.integrate(f2*v0,irange)*v0 - sy.integrate(f2*v1,irange)*v1
v2 = u2 / sy.sqrt( sy.integrate(u2*u2,irange) )
sy.pprint(v2)

sy.pprint(sy.integrate(v1*v1,irange))
sy.pprint(sy.integrate(v1*v0,irange))
sy.pprint(sy.integrate(v1*v2,irange))
sy.pprint(sy.integrate(v0*v2,irange))
