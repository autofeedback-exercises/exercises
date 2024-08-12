from AutoFeedback.varchecks import check_vars
from AutoFeedback.plotchecks import check_plot
from AutoFeedback.funcchecks import check_func
from AutoFeedback.plotclass import line
from AutoFeedback.randomclass import randomvar
from AutoFeedback.utils import get_internal as get
import scipy
import numpy as np
import unittest


class UnitTests(unittest.TestCase):
    def test_plot(self):
        x = [
            0 - 0.05,
            1 - 0.05,
            2 - 0.05,
            3 - 0.05,
            4 - 0.05,
            5 - 0.05,
            6 - 0.05,
            0 + 0.05,
            1 + 0.05,
            2 + 0.05,
            3 + 0.05,
            4 + 0.05,
            5 + 0.05,
            6 + 0.05,
        ]
        var = np.ones(14) * 1 / 6
        var[0] = 0
        for i in range(7):
            var[7 + i] = scipy.stats.binom.pmf(i, 6, 0.5)
        line1 = line(x, var)

        axislabels = ["x", "P(X=x)"]
        assert check_plot(
            [], exppatch=line1, explabels=axislabels, explegend=False, output=True
        )

    def test_bernoulli(self):
        inputs, variables = [], []
        for i in range(1, 9):
            p = i * 0.1
            inputs.append((i * 0.1,))
            myvar = randomvar(p, variance=p * (1 - p), vmin=0, vmax=1, isinteger=True)
            variables.append(myvar)
        assert check_func("bernoulli", inputs, variables)

    def test_trials(self):
        inputs, variables = [], []
        for n in range(1, 10):
            nt = 10 * n
            for i in range(1, 9):
                p = i * 0.1
                inputs.append(
                    (
                        nt,
                        i * 0.1,
                    )
                )
                myvar1 = randomvar(
                    [nt * p, nt * (1 - p)],
                    variance=[nt * p * (1 - p), nt * p * (1 - p)],
                    vmin=[0, 0],
                    vmax=[nt, nt],
                    isinteger=[True, True],
                )
                variables.append(myvar1)
        assert check_func("repeated_trials", inputs, variables)

    def test_plot_1(self):
        prob = get("prob")
        x = [0, 1]
        var = randomvar(
            [prob, 1 - prob],
            variance=[prob * (1 - prob), prob * (1 - prob)],
            vmin=[0, 0],
            vmax=[1, 1],
            isinteger=[False, False],
        )
        line1 = line(x, var)

        axislabels = ["Outcome", "Probability"]
        assert check_plot(
            [], exppatch=line1, explabels=axislabels, explegend=False, output=True
        )

    def test_plot_2(self):
        nparam = get("nparam")
        prob = get("prob")
        nsamples = get("nsamples")
        x, e, var, bmin, bmax, isi = [], [], [], [], [], []
        for i in range(nparam + 1):
            x.append(i)
            pval = scipy.stats.binom.pmf(i, nparam, prob)
            e.append(pval)
            var.append(pval * (1 - pval) / nsamples)
            bmin.append(0)
            bmax.append(1)
            isi.append(False)

        var = randomvar(e, variance=var, vmin=bmin, vmax=bmax, isinteger=isi)
        line1 = line(x, var)

        axislabels = ["Random variable value", "Fraction of occurances"]
        assert check_plot(
            [], exppatch=line1, explabels=axislabels, explegend=False, output=True
        )

    def test_dice(self):
        inputs, variables = [], []
        for i in range(10):
            inputs.append(())
            myvar = randomvar(3.5, variance=35 / 12, vmin=1, vmax=6, isinteger=True)
            variables.append(myvar)
        assert check_func("dice_roll", inputs, variables)

    def test_histo(self):
        inputs, variables = [], []
        for i in range(1, 5):
            inputs.append((i * 100,))
            myvar = randomvar(
                1 / 6,
                variance=(1 / 6) * (5 / 6) / (i * 100),
                vmin=0,
                vmax=1,
                isinteger=False,
            )
            variables.append(myvar)
        assert check_func("histo_estimate", inputs, variables, calls=["dice_roll"])

    def test_lower(self):
        nsamples = get("nsamples")
        probs, isi = 1 / 6 * np.ones(6), [False, False, False, False, False, False]
        myvar = randomvar(
            probs,
            dist="chi2",
            variance=probs * (1 - probs) / nsamples,
            dof=nsamples - 1,
            limit=0.9,
            isinteger=isi,
        )
        assert check_vars("lower", myvar)

    def test_upper(self):
        nsamples = get("nsamples")
        probs, isi = 1 / 6 * np.ones(6), [False, False, False, False, False, False]
        myvar = randomvar(
            probs,
            dist="chi2",
            variance=probs * (1 - probs) / nsamples,
            dof=nsamples - 1,
            limit=0.9,
            isinteger=isi,
        )
        assert check_vars("upper", myvar)

    def test_plot_3(self):
        nsamples = get("nsamples")
        probs, x, isi = (
            1 / 6 * np.ones(6),
            np.linspace(1, 6, 6),
            [False, False, False, False, False, False],
        )
        var = randomvar(
            probs,
            variance=probs * (1 - probs) / nsamples,
            vmin=[0, 0, 0, 0, 0, 0],
            vmax=[1, 1, 1, 1, 1, 1],
            isinteger=isi,
        )
        line1 = line(x, var)
        axislabels = ["Outcome", "Fraction of occurances"]
        assert check_plot(
            [line1], exppatch=line1, explabels=axislabels, explegend=False, output=True
        )

    def test_binom(self):
        inputs, variables = [], []
        for n in range(3, 6):
            for i in range(1, 9):
                p = i * 0.1
                inputs.append(
                    (
                        n,
                        i * 0.1,
                    )
                )
                myvar = randomvar(
                    n * p, variance=n * p * (1 - p), vmin=0, vmax=n, isinteger=True
                )
                variables.append(myvar)
        assert check_func("binomial", inputs, variables)

    def test_error(self):
        nsamples = get("nsamples")
        pval, isi = scipy.stats.binom.pmf([0, 1, 2, 3, 4, 5], 5, 0.5), [
            False,
            False,
            False,
            False,
            False,
            False,
        ]
        myvar = randomvar(
            pval,
            dist="chi2",
            variance=pval * (1 - pval) / nsamples,
            dof=nsamples - 1,
            limit=0.9,
            isinteger=isi,
        )
        assert check_vars("error", myvar)

    def test_plot_4(self):
        nsamples = get("nsamples")
        x, e, var, bmin, bmax, isi = [], [], [], [], [], []
        for i in range(6):
            x.append(i)
            pval = scipy.stats.binom.pmf(i, 5, 0.5)
            e.append(pval)
            var.append(pval * (1 - pval) / nsamples)
            bmin.append(0)
            bmax.append(1)
            isi.append(False)

        val = randomvar(e, variance=var, vmin=bmin, vmax=bmax, isinteger=isi)
        line1 = line(x, val)
        axislabels = ["Outcome", "Fraction of occurances"]
        assert check_plot(
            [line1], exppatch=line1, explabels=axislabels, explegend=False, output=True
        )
