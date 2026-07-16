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
import scipy.integrate 

def simpson_func(f, a, b, N):

    return scipy.integrate.simpson(f(np.linspace(a, b, N+1)), np.linspace(a, b, N+1))

simpson_func.inputs = [(np.sin, 0, 1, 4), (np.exp,-1, 1, 8), (np.cos, 0, 2.5, 7)]

def fsin(x):
    return np.sin(np.pi*x*x)

fsin.inputs = [(0,), (0.1,), (3,)]

I_exact,_  = scipy.integrate.fixed_quad(fsin, 0, 1, n=1001)

class UnitTests(unittest.TestCase):
    def test_errors(self):
        trap = get('trapezoidal')
        simp = get('simpsons')
        exact = get('exact')
        f_demo = get('f_demo')
        trap_error, simp_error = [], [] 
        h_vals = []
        N_vals = np.arange(10, 40, 2)
        for n in N_vals:
            trap_error.append(exact - trap(f_demo, 0, 2, n))
            simp_error.append(exact - simp(f_demo, 0, 2, n))
            h_vals.append(2/n)
        lines = [line(h_vals, trap_error, label='Trapezium'), line(h_vals, simp_error, label="Simpson's")]
        pc.check_plot(lines, output=True)

    def test_simp(self):
        assert fc.check_func(simpson_func)

    def test_fsin(self):
        assert fc.check_func(fsin)

    def test_I_exact(self):
        assert vc.check_vars('I_exact', expected=I_exact)

