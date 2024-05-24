try:
    import AutoFeedback.varchecks as vc
except Exception:
    import subprocess
    import sys

    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "AutoFeedback"])
    import AutoFeedback.varchecks as vc

import unittest
import sympy as sy

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


class UnitTests(unittest.TestCase):

    def test_1diffeq(self):
        assert vc.check_vars('diffeq', diffeq)

    def test_2solution(self):
        assert vc.check_vars('solution', solution)

    def test_3ic1(self):
        assert vc.check_vars('ic1', ic1)

    def test_4ic2(self):
        assert vc.check_vars('ic2', ic2)

    def test_5particular(self):
        assert vc.check_vars('particular', particular)
