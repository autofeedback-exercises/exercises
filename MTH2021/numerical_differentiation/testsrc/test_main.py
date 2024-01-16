import AutoFeedback.varchecks as vc


import unittest
import numpy as np


D = np.zeros((101, 101))
for ii in range(1, 100):
    D[ii, ii-1] = 100
    D[ii, ii+1] = 100
    D[ii, ii] = -200
x = np.linspace(-5, 5, 101)
f = np.exp(-x*x)
f2p = np.dot(D, f)


class UnitTests(unittest.TestCase):
    def test_1_N(self):
        assert(vc.check_vars('N',101))

    def test_2_x(self):
        assert(vc.check_vars('x',x))

    def test_3_h(self):
        assert(vc.check_vars('h',0.1))

    def test_4_h(self):
        assert(vc.check_vars('f', f))

    def test_5_D(self):
        assert(vc.check_vars('D',D))

    def test_6_dff(self):
        assert(vc.check_vars('f2p',f2p))

