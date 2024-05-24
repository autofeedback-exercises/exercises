try:
    import AutoFeedback.varchecks as vc
    import AutoFeedback.funcchecks as fc
except Exception:
    import subprocess
    import sys

    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "AutoFeedback"])
    import AutoFeedback.varchecks as vc
    import AutoFeedback.funcchecks as fc

import unittest
import numpy as np
from numpy.random import random
from scipy.integrate import odeint


def mypend(x, y):
    t, o = x
    return [o, -0.25*o - 5. * np.sin(t)]


def mydiff(x, y):
    return x/y


myy = odeint(mydiff, -10, np.linspace(-5, 5, 100))
myres = odeint(mypend, [np.pi/2, 0.0], np.linspace(0, 10, 100))


def initial_value_error(varname, exp, act):
    from AutoFeedback.bcolors import bcolors
    emsg = f"""The initial value of {varname} is incorrect. We expected it to
be {exp} but instead got {act}. Ensure that the inital value(s) that you
pass to odeint are correct """
    print(f"{bcolors.FAIL}{emsg}{bcolors.ENDC}")
    print(f"{bcolors.WARNING}{30*'='}\n{bcolors.ENDC}")


class UnitTests(unittest.TestCase):

    def test_1_dydt(self):
        ins = [(0, 1), (1, 1), (random(1), random(1)), (random(3), random(3))]
        outs = [mydiff(*inp) for inp in ins]
        assert fc.check_func('dydt', ins, outs)

    def test_2_y(self):
        try:
            assert vc.check_vars('y',  myy, output=False)
        except AssertionError:
            try:
                from main import y
                if y[0] != -10:
                    initial_value_error('y', -10, y[0])
                    return
            except ImportError:
                pass
        assert vc.check_vars('y',  myy)

    def test_3_pend(self):
        ins = [([0, 1], 0), ([1, 0], 1), ([random(1), random(1)], 0)]
        outs = [mypend(*inp) for inp in ins]
        assert fc.check_func('pend', ins, outs)

    def test_4_pendulum(self):
        try:
            assert vc.check_vars('theta',  myres[:, 0], output=False)
        except AssertionError:
            try:
                from main import theta, omega
                if theta[0] != np.pi/2:
                    initial_value_error('theta', np.pi/2, theta[0])
                    return
                if omega[0] != 0:
                    initial_value_error('omega', 0, omega[0])
                    return
            except ImportError:
                pass
        assert vc.check_vars('theta',  myres[:, 0])
