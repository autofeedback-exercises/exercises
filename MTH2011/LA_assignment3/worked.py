import sympy as sy
a, b, c, x = sy.symbols("a, b, c, x")
alpha, beta, gamma = sy.symbols("alpha, beta, gamma")

f0 = (1+x)**2
f1 = 1+x
f2 = 1

px = a*x**2 + b*x + c
Eq1 = sy.Eq(alpha*f0 + beta*f1 + gamma*f2, px)

q0 = sy.solve(Eq1, [alpha, beta, gamma])
sy.pprint(q0)
