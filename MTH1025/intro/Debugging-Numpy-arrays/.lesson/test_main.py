import AutoFeedback.varchecks as vc

import unittest
import numpy as np

class UnitTests(unittest.TestCase) :
    def test_x(self):
        myx=np.linspace(0,1,10)
        myx[0] = -1
        assert(vc.check_vars('x',myx))

    def test_x3(self):
        assert(vc.check_vars('x3',0.2222222222222222))

    def test_y(self):
        assert(vc.check_vars('y',np.arange(2,21,2)))

    def test_y5(self):
        assert(vc.check_vars('y5',np.arange(2,11,2)))

    def test_z(self):
        myz=[a*a for a in range(2,21,2)]
        assert(vc.check_vars('z',myz))

    def test_zdiff(self):
        assert(vc.check_vars('zdiff',12.0))

