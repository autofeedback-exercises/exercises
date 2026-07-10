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

def runge(x):
    return 1 / (25 + x**2)
runge.inputs = [(0,), (-3.1,), (7.1,)]

class UnitTests(unittest.TestCase):
    def test_runge(self):
        assert fc.check_func(runge)

    def test_xarrays(self):
        assert vc.check_vars('x5', np.linspace(-20, 20, 5))
        assert vc.check_vars('x11', np.linspace(-20, 20, 11))

    def test_yarrays(self):
        assert vc.check_vars('y5', runge(np.linspace(-20, 20, 5)))
        assert vc.check_vars('y11', runge(np.linspace(-20, 20, 11)))

    def test_plot(self):
        from scipy.interpolate import BarycentricInterpolator
        poly5 = BarycentricInterpolator(np.linspace(-20, 20, 5), runge(np.linspace(-20, 20, 5)))
        poly11 = BarycentricInterpolator(np.linspace(-20, 20, 11), runge(np.linspace(-20, 20, 11)))
        x_fine = get('x_fine')
        line1 = line(x_fine, poly5(x_fine), label='poly5')
        line2 = line(x_fine, poly11(x_fine), label='poly11')
        line3 = line(x_fine, runge(x_fine), label='runge')
        assert pc.check_plot([line1, line2, line3], output=True)

    def test_alias(self):
        x20 = np.linspace(0, 2*np.pi, 20)
        x21 = np.linspace(0, 2*np.pi, 21)
        line1 = line(x20, np.sin(20*x20), label='x20')
        line2 = line(x21, np.sin(20*x21), label='x21')
        assert pc.check_plot([line1, line2], output=True)

    def test_noisy(self):
        from scipy.interpolate import UnivariateSpline
        x_noisy = get('x_noisy')
        y_noisy = get('y_noisy')
        x_fine = get('x_fine')
        s0 = UnivariateSpline(x_noisy, y_noisy, s=0)(x_fine)
        s1 = UnivariateSpline(x_noisy, y_noisy, s=1)(x_fine)
        s01 = UnivariateSpline(x_noisy, y_noisy, s=0.1)(x_fine)
        lines= [line(x_fine, s0, label='s=0'),
                line(x_fine, s1, label='s=1'),
                line(x_fine, s01, label='s=0.1'), 
                line(x_noisy, y_noisy, label='noisy data')]
        assert pc.check_plot(lines, output=True)

