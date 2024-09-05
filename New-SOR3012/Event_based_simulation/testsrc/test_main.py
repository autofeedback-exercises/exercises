from AutoFeedback import check_vars, check_plot, check_func
from AutoFeedback.plotclass import line
from AutoFeedback.randomclass import randomvar
from AutoFeedback.utils import get_internal as get
import numpy as np
import unittest


class UnitTests(unittest.TestCase):
    def test_lam(self):
        inputs, var = [], []
        for j in range(1, 5):
            lam = j
            inputs.append((lam,))
            myvar1 = randomvar(
                1 / lam, variance=1 / (lam * lam),
                vmin=0, isinteger=False, nsamples=100
            )
            var.append(myvar1)
        assert check_func("exponential", inputs, var)

    def test_plot(self):
        xmax = get("xmax")
        nbins = get("nbins")
        lamd = get("lamd")
        delx, x, e, var, isi = xmax / nbins, [], [], [], []
        for i in range(nbins):
            x.append((i + 0.5) * delx)
            pval = np.exp(-lamd * i * delx) - np.exp(-lamd * (i + 1) * delx)
            e.append(pval / delx)
            var.append(pval * (1 - pval) / (delx * delx))
            isi.append(False)

        var = randomvar(e, variance=var, isinteger=isi)
        line1 = line(x, var)

        axislabels = ["Random variable value", "Probability"]
        assert check_plot([line1], explabels=axislabels,
                          explegend=False, output=True)

    def test_plot_1(self):
        lamd = get("lamd")
        nevents = get("nevents")
        e, var, isi, y = [], [], [], []
        for i in range(nevents):
            e.append((i + 1) / lamd)
            var.append((i + 1) / (lamd * lamd))
            y.append(i + 1)
            isi.append(False)

        var = randomvar(e, variance=var, isinteger=isi)
        line1 = line(var, y)

        axislabels = ["time", "number of events"]
        assert check_plot([line1], explabels=axislabels,
                          explegend=False, output=True)

    def test_variables(self):
        assert check_vars("lam", 0.5)
        assert check_vars("expr", 1.0)
        assert check_vars("N", 100000)

    def test_queue(self):
        lam = get("lam")
        expr = get("expr")
        N = get("N")
        p = lam / expr
        x, e, v, bmin, bmax, isi = [], [], [], [], [], []
        for i in range(9):
            x.append(i)
            prob = (1 - p) * (p**i)
            e.append(prob)
            v.append(prob * (1 - prob) / (N / 2))
            bmin.append(0)
            bmax.append(1)
            isi.append(False)

        rvar = randomvar(e, variance=v, vmin=bmin, vmax=bmax, isinteger=isi)
        line1 = line(x, rvar)
        axislabels = ["number of people in queue", "probability"]
        assert check_plot([], exppatch=line1, explabels=axislabels,
                          explegend=False, output=True)

    def test_lam_2(self):
        inputs, var = [], []
        for j in range(1, 5):
            lam = j * 0.2
            inputs.append((1000, lam, 1.0))
            myvar1 = randomvar(
                1 / (1 - lam), variance=0, vmin=0,
                isinteger=False, nsamples=100
            )
            var.append(myvar1)
        assert check_func("average_time_in_queue", inputs, var)
