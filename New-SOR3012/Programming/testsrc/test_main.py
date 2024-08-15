from AutoFeedback.plotclass import line
import AutoFeedback.plotchecks as pc
import AutoFeedback.varchecks as vc
from AutoFeedback.utils import get_internal as get
import unittest
import numpy as np


class UnitTests(unittest.TestCase):
    def test_fx(self):
        x = get("x")
        assert vc.check_vars("fx", np.abs(x))

    def test_fy(self):
        y = get("y")
        assert vc.check_vars("fy", np.abs(y))

    def test_fz(self):
        z = get("z")
        assert vc.check_vars("fz", np.abs(z))

    def test_arrayValues(self):
        yv = np.loadtxt('https://raw.githubusercontent.com/autofeedback-exercises/exercises/testpip/New-SOR3012/Programming/values.dat')
        for i in range(len(yv)):
            if yv[i] < 0:
                yv[i] *= -1
        assert vc.check_vars("yvals", yv)

    def test_arrayValues_1(self):
        xv = np.loadtxt('https://raw.githubusercontent.com/autofeedback-exercises/exercises/testpip/New-SOR3012/Programming/mydata.dat')
        yv = xv == 5
        assert vc.check_vars("yvals", yv)

    def test_arrayValues_2(self):
        xv = np.loadtxt('https://raw.githubusercontent.com/autofeedback-exercises/exercises/testpip/New-SOR3012/Programming/mydata.dat')
        yv = sum(xv == 5)
        assert vc.check_vars("nfives", yv)

    def test_nlefive(self):
        xv = np.loadtxt('https://raw.githubusercontent.com/autofeedback-exercises/exercises/testpip/New-SOR3012/Programming/mydata.dat')
        assert vc.check_vars("nlefive", sum(xv <= 5))

    def test_nmtfive(self):
        xv = np.loadtxt('https://raw.githubusercontent.com/autofeedback-exercises/exercises/testpip/New-SOR3012/Programming/mydata.dat')
        assert vc.check_vars("nmefive", sum(xv >= 5))

    def test_fib(self):
        xvals = np.linspace(0, 10, 11)
        yvals = 7 * xvals
        line1 = line(xvals, yvals)

        axislabels = ["Index", "Seven times table"]
        assert pc.check_plot(
            [line1], explabels=axislabels, explegend=False, output=True
        )

    def test_fib_1(self):
        xvals = np.linspace(0, 29, 30)
        yvals = xvals * xvals
        line1 = line(xvals, yvals)

        axislabels = ["Index", "Square"]
        assert pc.check_plot(
            [line1], explabels=axislabels, explegend=False, output=True
        )

    def test_fib_2(self):
        xvals = np.linspace(0, 99, 100)
        trig = xvals * (xvals + 1) / 2
        line1 = line(xvals, trig)

        axislabels = ["Index", "Triangular Numbers"]
        assert pc.check_plot(
            [line1], explabels=axislabels, explegend=False, output=True
        )

    def test_arrayValues_5(self):
        x = np.linspace(0, 70, 11)
        assert vc.check_vars("timesTable", x)

    def test_loop(self):
        assert vc.check_vars("i", 10)

    def test_arrayValues_6(self):
        x = np.linspace(0, 405, 16)
        assert vc.check_vars("timesTable", x)

    def test_loop_1(self):
        assert vc.check_vars("i", 15)

    def test_fib_3(self):
        xvals, fib = np.linspace(1, 100, 100), np.ones(100)
        for i in range(2, 100):
            fib[i] = fib[i - 2] + fib[i - 1]
        line1 = line(xvals, fib)

        axislabels = ["Index", "Fibonacci series"]
        assert pc.check_plot(
            [line1], explabels=axislabels, explegend=False, output=True
        )

    def test_fib_4(self):
        xvals, yvals = np.linspace(0, 19, 20), np.zeros(20)
        for i in range(20):
            yvals[i] = 0.5**i
        line1 = line(xvals, yvals)

        axislabels = ["Index", "Geometric series"]
        assert pc.check_plot(
            [line1], explabels=axislabels, explegend=False, output=True
        )

    def test_output(self):
        assert vc.check_vars("order", ["exponents", "multiplication", "addition"])

    def test_output_1(self):
        assert vc.check_vars("q1", 2704)
        assert vc.check_vars("q2", 0.5)
        assert vc.check_vars("q3", 2)
        assert vc.check_vars("q4", 18)

    def test_a1(self):
        assert vc.check_vars("a1", 3)

    def test_b2(self):
        assert vc.check_vars("b2", (4 + 5) / 2)

    def test_c3(self):
        assert vc.check_vars("c3", 3 * (9 + 4))

    def test_d4(self):
        assert vc.check_vars("d4", (7 + 4) * 5)

    def test_r(self):
        assert vc.check_vars("r", (4 + 5) * (3 + 1 / 2) / (7 * (10 - 4)))

    def test_numerator(self):
        assert vc.check_vars("numerator", 4)

    def test_denominator(self):
        assert vc.check_vars("denominator", 7 * (10 - 4))

    def test_c4(self):
        assert vc.check_vars("c3", 4)

    def test_e5(self):
        c3 = get("c3")
        assert vc.check_vars("e5", c3 + 5)

    def test_b3(self):
        c3 = get("c3")
        e5 = get("e5")
        assert vc.check_vars("b2", e5 * c3)

    def test_f6(self):
        e5 = get("e5")
        b2 = get("b2")
        assert vc.check_vars("f6", b2 + e5)

    def test_d5(self):
        c3 = get("c3")
        f6 = get("f6")
        assert vc.check_vars("d4", c3 / f6)

    def test_a2(self):
        c3 = get("c3")
        e5 = get("e5")
        f6 = get("f6")
        d4 = get("d4")
        assert vc.check_vars("a1", (c3 + e5) / (f6 + d4))

    def test_zero(self):
        assert vc.check_vars("zeroTimes", 0)

    def test_one(self):
        assert vc.check_vars("oneTimes", 13)

    def test_two(self):
        assert vc.check_vars("twoTimes", 2 * 13)

    def test_three(self):
        assert vc.check_vars("threeTimes", 3 * 13)

    def test_four(self):
        assert vc.check_vars("fourTimes", 4 * 13)

    def test_five(self):
        assert vc.check_vars("fiveTimes", 5 * 13)

    def test_six(self):
        assert vc.check_vars("sixTimes", 6 * 13)

    def test_seven(self):
        assert vc.check_vars("sevenTimes", 7 * 13)

    def test_eight(self):
        assert vc.check_vars("eightTimes", 8 * 13)

    def test_nine(self):
        assert vc.check_vars("nineTimes", 9 * 13)

    def test_ten(self):
        assert vc.check_vars("tenTimes", 10 * 13)

    def test_arrayValues_3(self):
        x = np.linspace(0, 70, 11)
        assert vc.check_vars("timesTable", x)

    def test_arrayValues_4(self):
        x = np.linspace(0, 70, 11)
        assert vc.check_vars("timesTable", x)

    def test_output_2(self):
        exp = """7
0.0 7.0 14.0 21.0 28.0 35.0 42.0 49.0 56.0 63.0 70.0
"""
        assert vc.check_vars("output", exp)
