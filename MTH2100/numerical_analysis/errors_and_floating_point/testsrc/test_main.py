try:
    from AutoFeedback import varchecks as vc
    from AutoFeedback import funcchecks as fc
    from AutoFeedback import plotchecks as pc
    from AutoFeedback.plotclass import line
except:

    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback[plot]"])
    from AutoFeedback import var as vc
    from AutoFeedback import plotchecks as pc
    from AutoFeedback.plotclass import line

import unittest
import numpy as np

def forward_diff(f, x, h):
    return (f(x+h)-f(x))/h

def backward_diff(f, x, h):
    return (f(x)-f(x-h))/h

def central_diff(f, x, h):
    return (f(x+h)-f(x-h))/(2*h)

backward_diff.inputs = [(np.cos, 1.0, 0.01), (np.exp, 0.3, 0.00001), (np.sin, -3, 0.5)]
central_diff.inputs = [(np.cos, 1.0, 0.01), (np.exp, 0.3, 0.00001), (np.sin, -3, 0.5)]

h_values= np.logspace(-1,-15,15)
err_fwd = np.array([abs(forward_diff(np.sin, 1.0, h) - np.cos(1.0)) for h in h_values])
err_bwd = np.array([abs(backward_diff(np.sin, 1.0, h) - np.cos(1.0)) for h in h_values])
err_cen = np.array([abs(central_diff(np.sin,  1.0, h) - np.cos(1.0)) for h in h_values])

line1=line(h_values, err_fwd, linestyle=['-', 'solid'],\
colour=['b','blue',(0.0,0.0,1.0,1)],label='Forward')
line2=line(h_values, err_bwd, linestyle=['--','dashed'],\
colour=['g','green',(0.0,1.0,0.0,1)],label='Backward')
line3=line(h_values, err_cen, linestyle=['-', 'solid'],
colour=['r','red',(1.0,0.0,0.0,1)], label='Central')

axislabels=["Step size","Absolute error",""]

def second_diff(f, x, h):
    return (f(x+h)+f(x-h)-2*f(x))/(h**2)
second_diff.inputs = [(np.cos, 1.0, 0.01), (np.exp, 0.3, 0.00001), (np.sin, -3, 0.5)]

err_2nd = np.array([abs(second_diff(np.exp, 1.0, h) - np.e) for h in h_values])
line4=line(h_values, err_2nd)

class UnitTests(unittest.TestCase):
    def test_backward(self):
        assert fc.check_func(backward_diff)

    def test_central(self):
        assert fc.check_func(central_diff)

    def test_hvalues(self):
        assert vc.check_vars('h_values', h_values)

    def test_err_fwd(self):
        assert vc.check_vars('err_fwd', err_fwd)

    def test_err_bwd(self):
        assert vc.check_vars('err_bwd', err_bwd)

    def test_err_cen(self):
        assert vc.check_vars('err_cen', err_cen)

    def test_plot(self):
        assert pc.check_plot([line1, line2, line3], explegend=True, output=True)

    def test_2nd(self):
        assert fc.check_func(second_diff)

    def test_plot2(self):
        assert pc.check_plot([line4], explegend=False, output=True)