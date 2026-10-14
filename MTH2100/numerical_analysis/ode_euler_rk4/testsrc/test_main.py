try:
    from AutoFeedback import varchecks as vc
    from AutoFeedback import funcchecks as fc
    from AutoFeedback import plotchecks as pc
    from AutoFeedback.plotclass import line
    from AutoFeedback.utils import get_internal as get
except:

    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback[plot]"])
    from AutoFeedback import var as vc
    from AutoFeedback import funcchecks as fc
    from AutoFeedback import plotchecks as pc
    from AutoFeedback.plotclass import line
    from AutoFeedback.utils import get_internal as get

import unittest
import numpy as np

def delta_f(f, delta_x):
    return np.cos(f) * delta_x

delta_f.inputs = [(1, 0.1), (0, 0.01), (0.7, 3)]


def update_inhomo(x, state):
    y, v = state
    return [v, 3*x+2+v+6*y]
update_inhomo.inputs = [(0.1, [0.2, 0.3]), (-0.3, [0.9, 0])]

def pendulum(t, state):
    g = 9.8
    L=1
    theta, phi = state
    return [phi, -(g/L)*np.sin(theta)]
pendulum.inputs = [(0.1, [0.2, 0.3]), (-0.3, [0.9, 0])]

def simple(t, state):
    g = 9.8
    L=1
    theta, phi = state
    return [phi, -(g/L)*theta]
simple.inputs = [(0.1, [0.2, 0.3]), (-0.3, [0.9, 0])]

def stiff(t, state):
    y = state[0]
    return [-1000*y + 3000 - 2000*np.exp(-t)]
stiff.inputs = [(0.1, [0.2]), (-0.3, [0.9])]

def butterfly(t, state):
    omega = 10
    rho = 28
    beta = 8/3
    x, y, z = state
    return [omega * (y-x), x*(rho-z)-y, x*y-beta*z]
butterfly.inputs = [(0.1, [0.2, 0.3, 0.1]), (-0.3, [0.9, 0, 0.9])]    


class UnitTests(unittest.TestCase):
    def test_delta_f(self):
        assert fc.check_func(delta_f)

    def test_arrays(self):
        dx = get('delta_x')
        f_array = get('f_array')
        x_array = get('x_array')
        my_farray = [0]
        for _ in range(len(f_array)-1):
            my_farray.append(my_farray[-1]+delta_f(my_farray[-1], dx))
        if not np.isclose(x_array[-1], 10):
            my_xarray = np.arange(0, 10+dx, dx)
            assert vc.check_vars('x_array', my_xarray)
        assert vc.check_vars('x_array', [ii*dx for ii in range(len(f_array))])
        assert vc.check_vars('f_array', my_farray)

    def test_plot(self):
        f_array = get('f_array')
        x_array = get('x_array') 
        pc.check_plot([line(x_array, f_array, label='f_array')], output=True)


    def test_inhomo(self):
        assert fc.check_func(update_inhomo)

    def test_inhomo_plot(self):
        euler = get('euler')
        x, s = euler(update_inhomo, 0, [0.3, 0], 1, 0.01)
        pc.check_plot([line(x, s[0], label='solution')], output=True)

    def test_pendulum(self):
        assert fc.check_func(pendulum)

    def test_simple(self):
        assert fc.check_func(pendulum)

    def test_stiff(self):
        assert fc.check_func(stiff)

    def test_butterfly(self):
        assert fc.check_func(butterfly)