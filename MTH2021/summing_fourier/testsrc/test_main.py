import AutoFeedback.funcchecks as fc

from numpy import pi, linspace, sin
import unittest


class UnitTests(unittest.TestCase) :
    def test_sum(self):
        x = linspace(0, 1, 5)
        y = 0.1 * sin(pi*x/3) + 0.7 * sin(2*pi*x/3)
        inps = [([1, 1], 0, 1),
                ([1, 0], 1, 2),
                ([1, 2, 3], 1, 2),
                ([0.1, 0.7], x, 3)]
        outs = [0, 1, -2, y]
        assert(fc.check_func('fourierSum',inps, outs))
