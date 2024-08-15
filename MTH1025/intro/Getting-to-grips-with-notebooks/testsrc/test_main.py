import AutoFeedback.varchecks as vc
import unittest


class UnitTests(unittest.TestCase) :
    def test_q1(self):
        assert(vc.check_vars('x', 3))
