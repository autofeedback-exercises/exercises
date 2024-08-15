import sympy as sy

x,y,z=sy.symbols("x,y,z")
Eq1=sy.Eq(5*x+3*y-7*z,4)
Eq2=sy.Eq(2*x-4*y+2*z,3)

sy.pprint(sy.solve([Eq1,Eq2],(x,z)))
