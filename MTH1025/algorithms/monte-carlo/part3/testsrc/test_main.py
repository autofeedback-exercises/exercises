import AutoFeedback.varchecks as vc
from AutoFeedback.randomclass import randomvar
from AutoFeedback.plotclass import line
import AutoFeedback.plotchecks as pc
from AutoFeedback.bcolors import bcolors as b
from AutoFeedback.utils import get_internal as get


import unittest
import numpy as np


theta = np.linspace(0, 2*np.pi, 100)
x = np.cos(theta)
y = np.sin(theta)
circle = line(x, y, colour=["red", "r", (1.0, 0.0, 0.0, 1)], label="circle")

x = [-1, 1, 1, -1, -1]
y = [-1, -1, 1, 1, -1]
square = line(x, y, colour=["blue", "b", (0.0, 0.0, 1.0, 1)], label="square")



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
                f"{b.FAIL}The {nm} coordinates are not uniformly distributed between -1 and 1{b.ENDC}")
            print(f"{b.WARNING}{30*'='}\n{b.ENDC}")
            return False
    return True

def doImports():
    try:
        xin = get('xin')
        xout = get('xout')
        yin = get('yin')
        yout = get('yout')
    except ImportError:
        print(
            f"{b.FAIL}One or more of the lists xin, xout, yin or yout are not defined.{b.ENDC}")
        print(f"{b.WARNING}{30*'='}\n{b.ENDC}")
        raise ImportError

    xlist = xin + xout
    ylist = yin + yout
    return xin, xout, xlist, yin, yout, ylist

class UnitTests(unittest.TestCase):


    def test_numpoints(self):

        xin, xout, xlist, yin, yout, ylist = doImports()

        if len(xlist) != 1000:
            print(
                f"{b.FAIL}The total number of values in xin and xout is not 1000.{b.ENDC}")
            print(f"{b.WARNING}{30*'='}\n{b.ENDC}")
            assert(False)
        if len(ylist) != 1000:
            print(
                f"{b.FAIL}The total number of values in yin and yout is not 1000.{b.ENDC}")
            print(f"{b.WARNING}{30*'='}\n{b.ENDC}")
            assert(False)

    def test_xlist(self):
        xin, xout, xlist, yin, yout, ylist = doImports()
        try:
            assert check_uniform(xlist, 'x')
        except AssertionError:
            assert(False)

    def test_ylist(self):
        xin, xout, xlist, yin, yout, ylist = doImports()
        try:
            assert check_uniform(ylist, 'y')
        except AssertionError:
            assert(False)


    def test_plot(self):
        xin, xout, xlist, yin, yout, ylist = doImports()
        try:
            fighand = get('fighand')
            x1, y1 = zip(*fighand.get_lines()[-2].get_xydata())
            x2, y2 = zip(*fighand.get_lines()[-1].get_xydata())
            x1 = list(x1) ; x2 = list(x2)
            y1 = list(y1);  y2 = list(y2)
            pltx = x1+x2; pltx.sort()
            plty = y1+y2; plty.sort()
            varx = xin + xout; varx.sort()
            vary = yin + yout; vary.sort()
            assert(pltx == varx)
            assert(plty == vary)
        except AssertionError:
            from AutoFeedback.bcolors import bcolors as b
            print(f"{b.FAIL}Plotted data sets 'points' do not match the variables xin, xout and yin, yout{b.ENDC}")
            print(f"{b.WARNING}{30*'='}\n{b.ENDC}")
            assert(False)

        try:
            if x1[0]**2 + y1[0]**2 < 1:
                interior = line(x1, y1, colour=["red", "r", (1.0, 0.0, 0.0, 1)],
                                marker = ".", label="interior")
                exterior = line(x2, y2, colour=["blue", "b", (0.0, 0.0, 1.0, 1)],
                                marker = ".", label="exterior")
                assert(False not in [x**2 + y**2 < 1 for x,y in zip(x1, y1)])
                assert(False not in [x**2 + y**2 > 1 for x,y in zip(x2, y2)])
            else:
                exterior = line(x1, y1, colour=["red", "r", (1.0, 0.0, 0.0, 1)],
                                marker = ".", label="interior")
                interior = line(x2, y2, colour=["blue", "b", (0.0, 0.0, 1.0, 1)],
                                marker = ".", label="exterior")
                assert(False not in [x**2 + y**2 > 1 for x,y in zip(x1, y1)])
                assert(False not in [x**2 + y**2 < 1 for x,y in zip(x2, y2)])
        except AssertionError:
            from AutoFeedback.bcolors import bcolors as b
            print( f"{b.FAIL}Points are not properly divided into exterior and interior of the circle{b.ENDC}")
            print(f"{b.WARNING}{30*'='}\n{b.ENDC}")
            assert(False)

        assert(pc.check_plot([circle, square, interior, exterior], output=True))


