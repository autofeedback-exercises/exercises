import AutoFeedback.varchecks as vc
import unittest
import numpy as np


class UnitTests(unittest.TestCase) :
    def test_y1(self):
        x=np.arange(0,6.1,0.5)
        aa=x*(4*x+6)+3
        assert(vc.check_vars('y1',aa))

    def test_y2(self):
        x=np.arange(0,6.1,0.5)
        bb=-x*x-1
        assert(vc.check_vars('y2',bb))

    def test_x1(self):
        cc=np.linspace(-np.pi,np.pi,1000)
        dd=cc*np.cos(cc)
        assert(vc.check_vars('x1',dd))

    def test_x2(self):
        cc=np.linspace(-np.pi,np.pi,1000)
        ee=cc/(cc+3)
        assert(vc.check_vars('x2',ee))

    def test_a(self):
        ff=np.array([n*(n+1) for n in range(100)])
        assert(vc.check_vars('a',ff))
    
