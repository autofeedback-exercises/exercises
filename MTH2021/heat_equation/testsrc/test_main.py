import AutoFeedback.funcchecks as fc

from numpy import pi, linspace, sin, exp, array
import unittest


class UnitTests(unittest.TestCase) :
    def test_sum(self):
        x = linspace(-pi, pi, 5)
        y = 0.1 * exp(-0.1) * sin(x) + 0.7 * exp(-0.9) * sin(3*x)
        z = 0.2 * exp(-0.2) * sin(x) + 1.4 * exp(-5) * sin(5*x)
        inps = [([1, 1], array([0, pi]), pi, 0, 1),
                ([1, 1], pi/2, pi, 0, 1),
                ([1, 2, 3], pi/2, pi, 0, 1),
                ([0.1, 0, 0.7], x, pi, 1, 0.1),
                ([0.2, 0, 0, 0, 1.4], x, pi, 2, 0.1)]
        outs = [[0, 0], 1, -2, y, z]
        assert(fc.check_func('fourierSum',inps, outs))
