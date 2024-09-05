from AutoFeedback import check_func, check_vars, check_plot
from AutoFeedback.utils import get_internal as get
from AutoFeedback.plotclass import line

import unittest
import sympy as sy
import numpy as np

t = sy.symbols('t')
y = sy.Function('y')(t)
d2y = y.diff(t, 2)
dy = y.diff(t, 1)
diffeq = sy.Eq(d2y + 2*dy + 5*y, 5*t**2+12)
solution = sy.dsolve(diffeq)
equation = solution.rhs

C1, C2 = sy.symbols('C1, C2')

ic1 = sy.Eq(equation.subs(t, 0), 0)
ic2 = sy.Eq(equation.diff(t).subs(t, 0), 0)

solution_ics = sy.solve([ic1, ic2], (C1, C2))

particular = equation.subs(solution_ics)
f_ = sy.lambdify([t], particular)


class UnitTests(unittest.TestCase):

    def test_1diffeq(self):
        assert check_vars('diffeq', diffeq)

    def test_2solution(self):
        assert check_vars('solution', solution)

    def test_3ic1(self):
        assert check_vars('ic1', ic1)

    def test_4ic2(self):
        assert check_vars('ic2', ic2)

    def test_5particular(self):
        assert check_vars('particular', particular)

    def test_func(self):
        from numpy.random import random
        ins = [(0,), (1,), (random(1)), (random(3),)]
        outs = [f_(*inp) for inp in ins]
        assert check_func('particular_func', ins, outs)

    def test_nt(self):
        assert check_vars('nt', np.linspace(-1, 1, 100))

    def test_ny(self):
        assert check_vars('ny', f_(np.linspace(-1, 1, 100)))

    def test_plot(self):
        nt = np.linspace(-1, 1, 100)
        myl = line(nt, f_(nt))
        assert check_plot([myl], explabels=['t', 'y(t)'], output=True)
