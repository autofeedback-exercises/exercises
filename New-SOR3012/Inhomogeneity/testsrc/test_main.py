from AutoFeedback import check_plot, check_func
from AutoFeedback.plotclass import line
from AutoFeedback.randomclass import randomvar
from AutoFeedback.utils import get_internal as get
import unittest
import numpy as np


def inhomo_p(n):
    t, nevents = 0, 0
    while True:
        t = t - np.log(np.random.uniform(0, 1)) / 3
        if np.random.uniform(0, 1) <= (np.sin(t) + 2) / 3:
            nevents = nevents + 1
        if nevents == n:
            break
    return t


def sample(n, m):
    mean, S2 = 0, 0
    for i in range(m):
        myvar = inhomo_p(n)
        mean = mean + myvar
        S2 = S2 + myvar * myvar
    mean = mean / m
    var = (m / (m - 1)) * (S2 / m - mean * mean)
    return mean, var


class UnitTests(unittest.TestCase):
    def test_plot_3(self):
        nevents = get("nevents")
        e, var, isi, y = [], [], [], []
        for i in range(nevents):
            m, v = sample(i + 1, 200)
            e.append(m)
            var.append(v)
            y.append(i + 1)
            isi.append(False)

        var = randomvar(e, variance=var, isinteger=isi)
        line1 = line(var, y)

        axislabels = ["Time / s", "Number of events"]

        assert check_plot([line1], explabels=axislabels,
                          explegend=False, output=True)

    def test_plot(self):
        nevents = get("nevents")
        lamd = get("lamd")
        e, var, isi, y = [], [], [], []
        for i in range(nevents):
            e.append((i + 1) / lamd)
            var.append((i + 1) / (lamd * lamd))
            y.append(i + 1)
            isi.append(False)

        var = randomvar(e, variance=var, isinteger=isi)
        line1 = line(var, y)

        axislabels = ["Time / s", "Number of events"]
        assert check_plot([line1], explabels=axislabels,
                          explegend=False, output=True)

    def test_plot_2(self):
        nevents = get("nevents")
        e, var, isi, y = [], [], [], []
        for i in range(nevents):
            e.append(4 * (i + 1))
            var.append(i + 1)
            y.append(i + 1)
            isi.append(False)

        var = randomvar(e, variance=var, isinteger=isi)
        line1 = line(var, y)

        axislabels = ["Time / s", "Number of events"]
        assert check_plot([line1], explabels=axislabels,
                          explegend=False, output=True)

    def test_rate_func(self):
        xv, yv = [], []
        for i in range(1200):
            xv.append((i,))
            vv = i - np.floor(i / 600) * 600
            if vv < 60:
                yv.append(0.5)
            elif vv < 180:
                yv.append(1 / 6)
            elif vv < 240:
                yv.append(0.5)
            elif vv < 360:
                yv.append(1 / 6)
            elif vv < 420:
                yv.append(0.5)
            elif vv < 540:
                yv.append(1 / 6)
            else:
                yv.append(0.5)
        assert check_func("rate", xv, yv)

    def test_rate_func_2(self):
        xv, yv = [], []
        for i in range(1200):
            xv.append((i,))
            yv.append((1 / 6) * np.cos(2 * np.pi * (i - 30) / 180) + 1 / 3)
        assert check_func("rate", xv, yv)
