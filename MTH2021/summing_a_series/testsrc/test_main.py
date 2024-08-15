import AutoFeedback.funcchecks as fc
import unittest


class UnitTests(unittest.TestCase) :
    def test_cone(self):
        assert(fc.check_func('sum_geometric',[(0,10),(0.5,0),(1,10),(0.5,15)],[1,1,11,1.99996948242]))

