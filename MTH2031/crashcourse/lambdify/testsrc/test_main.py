try:
    import AutoFeedback.varchecks as vc
    import AutoFeedback.funcchecks as fc
except Exception:
    import subprocess
    import sys

    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "AutoFeedback"])
    import AutoFeedback.varchecks as vc

import unittest
import sympy as sy
import numpy as np
from numpy.random import random

x, y, z = sy.symbols('x,y,z')


class UnitTests(unittest.TestCase):

    def test_f1(self):
        assert vc.check_vars('f1', x**2 - 3*x + 4)

    def test_f2(self):
        assert vc.check_vars('f2', sy.exp(-(x-y)**2))

    def test_f3(self):
        assert vc.check_vars('f3', sy.sin(x) + sy.cos(x))

    def test_f1_func(self):
        ins = [(0,), (1,), (random(1),), (random(3),)]
        myfunc = lambda x: x**2 -3*x+4
        outs = [myfunc(*inp) for inp in ins]
        assert fc.check_func('f1_func', ins, outs)

    def test_f2_func(self):
        ins = [(0, 1), (1, 0), (random(1), random(1)), (random(3), random(3))]
        myfunc = lambda x, y: np.exp(-(x-y)**2)
        outs = [myfunc(*inp) for inp in ins]
        assert fc.check_func('f2_func', ins, outs)

    def test_f3_func(self):
        ins = [(0,), (1,), (random(1),), (random(3),)]
        myfunc = lambda x: np.sin(x) + np.cos(x)
        outs = [myfunc(*inp) for inp in ins]
        assert fc.check_func('f3_func', ins, outs)
