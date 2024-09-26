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

x, y, z = sy.symbols('x,y,z')
g = sy.Function('g')(z)


class UnitTests(unittest.TestCase):

    def test_Eq1(self):
        assert(vc.check_vars('Eq1', sy.Eq(2*x+3*y, 3)))

    def test_Eq1_sol(self):
        try:
            assert(vc.check_vars('x', [sy.Rational(-3,2)]))
        except AssertionError:
            print("""If you have solved this by hand, and simply typed x=-3/2, the
checker will fail. Try using the .subs() method and sy.solve() function to
solve this simple problem instead""")

    def test_Expr(self):
        assert(vc.check_vars('f', sy.exp(sy.sin(y))))

    def test_deriv(self):
        assert(vc.check_vars('f_', sy.exp(sy.sin(y)).diff(y)))

    def test_g(self):
        assert(vc.check_vars('g', sy.Function('g')(z)))

    def test_diffeq(self):
        assert(vc.check_vars('diffeq', sy.Eq(g.diff(z, 2), 2*z**2 + g)))

    def test_gsol(self):
        assert(vc.check_vars('gsol',
                             sy.dsolve(sy.Eq(g.diff(z, 2), 2*z**2 + g))))
