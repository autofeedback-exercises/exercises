from AutoFeedback.funcchecks import check_func
from AutoFeedback.plotchecks import check_plot
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
                1 / lam, variance=1 / (lam * lam), vmin=0, isinteger=False, nsamples=100
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
        assert check_plot([line1], explabels=axislabels, explegend=False, output=True)

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
        assert check_plot([line1], explabels=axislabels, explegend=False, output=True)
