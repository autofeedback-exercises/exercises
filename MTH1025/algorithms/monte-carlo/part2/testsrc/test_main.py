import AutoFeedback.varchecks as vc
from AutoFeedback.plotclass import line
import AutoFeedback.plotchecks as pc
from AutoFeedback.randomclass import randomvar

import unittest
import numpy as np


theta = np.linspace(0, 2*np.pi, 100)
x = np.cos(theta)
y = np.sin(theta)
circle = line(x, y, colour=["red", "r", (1.0, 0.0, 0.0, 1)], label="circle")

x = [-1, 1, 1, -1, -1]
y = [-1, -1, 1, 1, -1]
square = line(x, y, colour=["blue", "b", (0.0, 0.0, 1.0, 1)], label="square")


myx = 1000*[0]

plotx = randomvar(0, variance=(1/3), vmin=-1, vmax=1, isinteger=False)

points = line(plotx, plotx, colour=["black", "k", (0.0, 0.0, 0.0, 1)], marker=['.', ','], label="points")


def check_uniform(x, nm):
    a = [i for i in x if i < -0.5]
    b = [i for i in x if i > -0.5 and i <= 0]
    c = [i for i in x if i > 0 and i <= 0.5]
    d = [i for i in x if i > 0.5]
    for ii in [a, b, c, d]:
        try:
            assert(0.22 < len(ii)/len(x) and 0.28 > len(ii)/len(x))
        except AssertionError:
            from AutoFeedback.bcolors import bcolors as b
            print(
                f"{b.FAIL}The variable {nm} is not uniformly distributed between -1 and 1{b.ENDC}")
            print(f"{b.WARNING}{30*'='}\n{b.ENDC}")
            return False
    return True


def check_size(var, expected, varname):
    try:
        assert vc._check_size(var, expected), "size"
    except AssertionError as error:
        from AutoFeedback.variable_error_messages import print_error_message
        print_error_message(error, varname, expected, var)
    return True


class UnitTests(unittest.TestCase):

    def test_xlist(self):
        try:
            from __main__ import xlist
            assert check_uniform(xlist, 'xlist')
#            assert(vc.check_vars('xlist', myx))
            assert check_size(xlist, myx, 'xlist')
        except ImportError:
            assert(vc.check_vars('xlist', myx))
        except AssertionError:
            assert(False)

    def test_ylist(self):
        try:
            from __main__ import ylist
            assert check_uniform(ylist, 'ylist')
            assert check_size(ylist, myx, 'ylist')
        except ImportError:
            assert(vc.check_vars('ylist', myx))
        except AssertionError:
            assert(False)

    def test_equality(self):
        try:
            from __main__ import ylist, xlist
            assert(xlist!=ylist)
        except ImportError:
            pass
        except AssertionError:
            from AutoFeedback.bcolors import bcolors as b
            print( f"{b.FAIL}The variables xlist and ylist should not be identical, otherwise we plot points distributed not in the square, but on the straight line x=y\n{b.ENDC}")
            print(f"{b.WARNING}{30*'='}\n{b.ENDC}")
            assert(False)
            
    def test_plot(self):
        try:
            from __main__ import fighand
            x, y = zip(*fighand.get_lines()[2].get_xydata())
            from __main__ import xlist, ylist
            for xx, xxx, yy, yyy in zip(xlist, x, ylist, y):
                assert(xx == xxx)
                assert(yy == yyy)
        except ImportError:
            pass
        except AssertionError:
            from AutoFeedback.bcolors import bcolors as b
            print( f"{b.FAIL}Plotted data set 'points' does not match the variables xlist and ylist{b.ENDC}")
            print(f"{b.WARNING}{30*'='}\n{b.ENDC}")
            assert(False)
        except IndexError:
            pass

        assert(pc.check_plot([circle, square, points], output=True))


