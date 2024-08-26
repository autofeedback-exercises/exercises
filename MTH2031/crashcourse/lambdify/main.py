import sympy as sy
import numpy as np
x, y, z = sy.symbols('x, y, z')
# f1(x) = x^2 - 3x + 4
f1 = x**2 - 3*x + 4
f1_func = sy.lambdify([x], f1)
# f2(x,y) = e^-(x - y)^2
f2 = sy.exp(-(x-y)**2)
f2_func = sy.lambdify([x, y], f2)
#print(f2_func(0,1))
f3 = sy.sin(x) + sy.cos(x)
f3_func = sy.lambdify(x, f3)
xx = np.linspace(0, 2*np.pi)
yy = f3_func(xx)
