try:
    import AutoFeedback.varchecks as vc
except:

    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    import AutoFeedback.varchecks as vc

import unittest
import sympy as sy

x,y,z,t = sy.symbols('x,y,z,t')

class UnitTests(unittest.TestCase) :

    def test_Eq1_1(self):
        assert(vc.check_vars('Eq1_1',sy.Eq(2*x+3*y,3)))

    def test_Eq1_2(self):
        assert(vc.check_vars('Eq1_2',sy.Eq(x-2*y,5)))

    def test_Eq1_3(self):
        assert(vc.check_vars('Eq1_3',sy.Eq(3*x+2*y,7)))

    def test_Eq2_1(self):
        assert(vc.check_vars('Eq2_1',sy.Eq(x+2*y-3*z+2*t,2)))

    def test_Eq2_2(self):
        assert(vc.check_vars('Eq2_2',sy.Eq(2*x+5*y-8*z+6*t,5)))

    def test_Eq2_3(self):
        assert(vc.check_vars('Eq2_3',sy.Eq(3*x+4*y-5*z+2*t,4)))

    def test_Eq3_1(self):
        assert(vc.check_vars('Eq3_1',sy.Eq(x**3*y**2*z**6,1)))

    def test_Eq3_2(self):
        assert(vc.check_vars('Eq3_2',sy.Eq(x**4*y**5*z**12,2)))

    def test_Eq3_3(self):
        assert(vc.check_vars('Eq3_3',sy.Eq(x**2*y**2*z**5,3)))

    def test_q1(self):
        assert(vc.check_vars('q1',{x:3, y:-1}))

    def test_q2(self):
        assert(vc.check_vars('q2',{y: -2*t + 2*z + 1, x: 2*t - z}))

    def test_q3(self):
        assert(vc.check_vars('q3',[(sy.Rational(729,4), sy.Rational(531441,8), sy.Rational(4,2187))]))
