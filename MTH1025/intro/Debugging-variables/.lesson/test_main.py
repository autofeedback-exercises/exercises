import AutoFeedback.varchecks as vc
import unittest
from numpy import pi

class UnitTests(unittest.TestCase) :
    def test_q1(self):
        from numpy import cos
        assert(vc.check_vars('x',cos((pi/6)*3**0.5)))

    def test_q2(self):
        assert(vc.check_vars('y',0.5*3**0.5))

    def test_q3(self):
        assert(vc.check_vars('z',(pi/6)*3**0.5))

#    def test_output(self):
#        assert(vc.check_output('0.6161905084795576 0.8660254037844386 0.9068996821171088'))


