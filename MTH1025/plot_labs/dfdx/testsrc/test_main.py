try:
    from AutoFeedback import varchecks as vc
    from AutoFeedback import plotchecks as pc
    from AutoFeedback import funcchecks as fc
    from AutoFeedback.plotclass import line
except:

    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install",
                           "AutoFeedback[plot]"])
    from AutoFeedback import funcchecks as fc
    from AutoFeedback import var as vc
    from AutoFeedback import plotchecks as pc
    from AutoFeedback.plotclass import line

import unittest
import numpy as np


myx = [-10+i*0.1 for i in range(201)]
myf = [np.exp(-x*x) for x in myx]
mye = [-2*x*np.exp(-x*x) for x in myx]
mydf = [10*(x-y) for x, y in zip(myf[1:], myf[:-1])]
mydf.append(mydf[-1])

x2 = [-10+i*0.5 for i in range(41)]
f2 = [np.exp(-x*x) for x in x2]
df2 = [2*(x-y) for x, y in zip(f2[1:], f2[:-1])]
df2.append(df2[-1])
line1 = line(myx, mye, label="Exact Derivative",
             colour=['k', 'black', (0.0, 0.0, 0.0, 1)])
line2 = line(myx, mydf, label="Numerical Derivative, delx=0.1",
             colour=['r', 'red', (1.0, 0.0, 0.0, 1)])
line3 = line(x2, df2, label="Numerical Derivative, delx=0.5",
             colour=['b', 'blue', (0.0, 0.0, 1.0, 1)])
axislabels = ["x", "df/dx", ""]


class UnitTests(unittest.TestCase):
    def test_step1(self):
        assert(vc.check_vars('delx', 0.1))

    def test_step2(self):
        assert(vc.check_vars('x', myx))

    def test_step3(self):
        assert(vc.check_vars('f', myf))

    def test_step4(self):
        assert(vc.check_vars('exact_derivative', mye))

    def test_step5(self):
        assert(pc.check_plot([line1], explabels=axislabels,
                             explegend=True, output=True, check_partial=True))

    def test_step6(self):
        assert(vc.check_vars('df99', mydf[99]))

    def test_step7(self):
        assert(vc.check_vars('err99', abs(mydf[99]-mye[99])))

    def test_step8(self):
        assert(fc.check_func('numerical_derivative', [([0, 1, 2], 0.1), (myf, 0.1), (myf, 0.2), (myx, 0.1)], [
               [10, 10, 10], mydf, [0.5*i for i in mydf], [1 for i in myx]]))

    def test_plot(self):
        assert(pc.check_plot([line1, line2, line3],
                             explabels=axislabels, explegend=True, output=True))
