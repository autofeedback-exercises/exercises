import AutoFeedback.varchecks as vc
import AutoFeedback.funcchecks as fc
from AutoFeedback.plotchecks import check_plot
from AutoFeedback.plotclass import line
from AutoFeedback.utils import get_internal as get
import unittest
import numpy as np
from numpy.random import random
from scipy.integrate import odeint
import pytest


def mypend(x, y):
    t, o = x
    return [o, -0.25*o - 5. * np.sin(t)]


def mydiff(x, y):
    return x/y


myy = odeint(mydiff, -10, np.linspace(-5, 5, 100))
myres = odeint(mypend, [np.pi/2, 0.0], np.linspace(0, 10, 100))


class UnitTests(unittest.TestCase):

    def test_plot1(self):
        myl = line(np.linspace(-5, 5, 100), np.linspace(-10, 10, 100))
        assert check_plot([myl], explabels=['t', 'y'], output=True)

    def test_1_dydt(self):
        ins = [(0, 1), (1, 1), (random(1), random(1)), (random(3), random(3))]
        outs = [mydiff(*inp) for inp in ins]
        assert fc.check_func('dydt', ins, outs)

    def test_2_y(self):
        assert vc.check_vars('y',  myy)

    def test_3_pend(self):
        ins = [([0, 1], 0), ([1, 0], 1), ([random(1), random(1)], 0)]
        outs = [mypend(*inp) for inp in ins]
        assert fc.check_func('pend', ins, outs)

    def test_4_pendulum(self):
        assert vc.check_vars('theta',  myres[:, 0])

    def test_plot2(self):
        myt = np.linspace(0, 10, 100)
        myl = line(myt, odeint(mypend, [np.pi/2, 0.0], myt)[:, 0])
        assert check_plot([myl], explabels=['t', 'theta'], output=True)
