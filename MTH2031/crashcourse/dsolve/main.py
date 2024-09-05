import sympy as sy
import numpy as np
import matplotlib.pyplot as plt
t = sy.symbols('t')
y = sy.Function('y')(t)
d2y = y.diff(t, 2)
dy = y.diff(t, 1)
diffeq = sy.Eq(d2y + 2*dy + 5*y, 5*t**2+12)
sy.pprint(diffeq)
solution = sy.dsolve(diffeq)
sy.pprint(solution.rhs)
equation = solution.rhs
C1, C2 = sy.symbols('C1, C2')
ic1 = sy.Eq(equation.subs(t, 0), 0)
ic2 = sy.Eq(equation.diff(t).subs(t, 0), 0)
sy.pprint(ic1)
sy.pprint(ic2)
solution_ics = sy.solve([ic1, ic2], (C1, C2))
sy.pprint(solution_ics)
particular = equation.subs(solution_ics)
sy.pprint(particular)

nt = np.linspace(-1, 1, 100)
particular_func = sy.lambdify([t], particular)
ny = particular_func(nt)
plt.plot(nt, ny)
plt.xlabel('t')
plt.ylabel('y(t)')
# This code is required for the autofeedback- don't delete it!
fighand = plt.gca()
