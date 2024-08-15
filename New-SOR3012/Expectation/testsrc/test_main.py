from AutoFeedback.funcchecks import check_func
from AutoFeedback.plotchecks import check_plot
import AutoFeedback.varchecks as vc
from AutoFeedback.plotclass import line
from AutoFeedback.randomclass import randomvar
import unittest
import numpy as np


class UnitTests(unittest.TestCase):
    def test_N(self):
        myx = np.loadtxt('https://raw.githubusercontent.com/autofeedback-exercises/exercises/testpip/New-SOR3012/Expectation/data.dat')
        assert vc.check_vars("N", len(myx))

    def test_L(self):
        myx = np.loadtxt('https://raw.githubusercontent.com/autofeedback-exercises/exercises/testpip/New-SOR3012/Expectation/data.dat')
        assert vc.check_vars("L", min(myx))

    def test_U(self):
        myx = np.loadtxt('https://raw.githubusercontent.com/autofeedback-exercises/exercises/testpip/New-SOR3012/Expectation/data.dat')
        assert vc.check_vars("U", max(myx))

    def test_plot(self):
        myx = np.loadtxt('https://raw.githubusercontent.com/autofeedback-exercises/exercises/testpip/New-SOR3012/Expectation/data.dat')
        myx.sort()
        myy = range(1, len(myx) + 1)
        myy = [a / len(myx) for a in myy]
        line1 = line(myx, myy)

        axislabels = ["x", "cumulative distribution"]
        assert check_plot([line1], explabels=axislabels, explegend=False, output=True)

    def test_dmin(self):
        myx = np.loadtxt('https://raw.githubusercontent.com/autofeedback-exercises/exercises/testpip/New-SOR3012/Expectation/data.dat')
        assert vc.check_vars("dmin", min(myx))

    def test_lowq(self):
        myx = np.loadtxt('https://raw.githubusercontent.com/autofeedback-exercises/exercises/testpip/New-SOR3012/Expectation/data.dat')
        assert vc.check_vars("lowq", np.percentile(myx, 25))

    def test_median(self):
        myx = np.loadtxt('https://raw.githubusercontent.com/autofeedback-exercises/exercises/testpip/New-SOR3012/Expectation/data.dat')
        assert vc.check_vars("median", np.percentile(myx, 50))

    def test_highq(self):
        myx = np.loadtxt('https://raw.githubusercontent.com/autofeedback-exercises/exercises/testpip/New-SOR3012/Expectation/data.dat')
        assert vc.check_vars("highq", np.percentile(myx, 75))

    def test_dmax(self):
        myx = np.loadtxt('https://raw.githubusercontent.com/autofeedback-exercises/exercises/testpip/New-SOR3012/Expectation/data.dat')
        assert vc.check_vars("dmax", max(myx))

    def test_bernoulli(self):
        inputs, var = [], []
        for i in range(1, 9):
            inputs.append((i * 0.1,))
            var.append(i * 0.1)
        assert check_func("bernoulli", inputs, var)

    def test_binomial(self):
        inputs, var = [], []
        for n in range(2, 7):
            for i in range(1, 9):
                inputs.append(
                    (
                        n,
                        i * 0.1,
                    )
                )
                var.append(n * i * 0.1)
        assert check_func("binomial", inputs, var)

    def test_geometric(self):
        inputs, var = [], []
        for i in range(1, 9):
            inputs.append((i * 0.1,))
            var.append(1 / (i * 0.1))
        assert check_func("geometric", inputs, var)

    def test_negative_binomial(self):
        inputs, var = [], []
        for n in range(2, 7):
            for i in range(1, 9):
                inputs.append(
                    (
                        n,
                        i * 0.1,
                    )
                )
                var.append(n / (i * 0.1))
        assert check_func("negative_binomial", inputs, var)

    def test_uniform_continuous(self):
        inputs, var = [], []
        for j in range(1, 4):
            for i in range(4, 9):
                inputs.append(
                    (
                        j,
                        i,
                    )
                )
                var.append((i + j) / 2)
        assert check_func("uniform_continuous", inputs, var)

    def test_uniform_discrete(self):
        inputs, var = [], []
        for j in range(1, 4):
            for i in range(4, 9):
                inputs.append(
                    (
                        j,
                        i,
                    )
                )
                var.append((i + j) / 2)
        assert check_func("uniform_discrete", inputs, var)

    def test_exponential(self):
        inputs, var = [], []
        for i in range(1, 9):
            inputs.append((i,))
            var.append(1 / i)
        assert check_func("exponential", inputs, var)

    def test_normal(self):
        inputs, var = [], []
        for j in range(1, 4):
            for i in range(1, 4):
                inputs.append(
                    (
                        j,
                        i,
                    )
                )
                var.append(j)
        assert check_func("normal", inputs, var)

    def test_variables(self):
        inputs, variables = [], []
        for i in range(1, 5):
            inputs.append((i * 10,))
            myvar = randomvar(
                0.5,
                variance=1 / 12 / (i * 10),
                vmin=0,
                vmax=1,
                isinteger=False,
                nsamples=100,
            )
            variables.append(myvar)
        assert check_func("average", inputs, variables)

    def test_variables_1(self):
        x = np.linspace(1, 200, 200)
        var = randomvar(
            0.5, variance=1 / 12, vmin=0, vmax=1, isinteger=False, meanconv=True
        )
        line1 = line(x, var)
        line2 = line([0, 200], [0.5, 0.5])

        axislabels = ["Number of random variables", "Sample mean"]
        assert check_plot(
            [line1, line2], explabels=axislabels, explegend=False, output=True
        )

    def test_mean(self):
        inputs, var = [], []
        for i in range(2, 10):
            inputs.append((i,))
            myvar1 = randomvar(
                0.5, variance=1 / 12 / i, vmin=0, vmax=1, isinteger=False
            )
            var.append(myvar1)
        assert check_func("sample_mean", inputs, var)

    def test_sample(self):
        inputs, var = [], []
        for i in range(15, 20):
            for j in range(5, 10):
                inputs.append((i, j))
                myvar1 = randomvar(
                    0.5, variance=1 / 12 / j, vmin=0, vmax=1, isinteger=False
                )
                var.append(myvar1)
        assert check_func("sample", inputs, var, calls=["sample_mean"])

    def test_mean_1(self):
        inputs, var = [], []
        for i in range(2, 10):
            inputs.append((i,))
            rv = randomvar(0.5, variance=1 / 12 / i, vmin=0, vmax=1, isinteger=False)
            var.append(rv)
        assert check_func("sample_mean", inputs, var)

    def test_limit(self):
        inputs, var = [], []
        for i in range(10, 12):
            for j in range(20, 21):
                inputs.append(
                    (
                        i,
                        j,
                    )
                )
                myvar1 = randomvar(
                    0.5, variance=1 / 12 / i, dist="conf_lim", dof=j - 1, limit=0.90
                )
                var.append(myvar1)
        assert check_func("limit", inputs, var)

    def test_variables_2(self):
        x, expect, variance, isi = (
            np.linspace(1, 50, 50),
            np.zeros(50),
            np.zeros(50),
            [],
        )
        for i in range(50):
            expect[i], variance[i] = 0.5, 1 / 12 / (i + 1)
            isi.append(False)

        y = randomvar(expect, variance=variance, dist="chi2", dof=9, isinteger=isi)
        line1 = line(x, y)

        axislabels = ["Number of variables used to calculate mean", "Variance"]
        assert check_plot([line1], explabels=axislabels, explegend=False, output=True)

    def test_variables_3(self):
        inputs, variables = [], []
        for n in range(2, 15):
            inputs.append((n,))
            myvar = randomvar(
                0.5, variance=1 / 12, dist="chi2", dof=n - 1, isinteger=False
            )
            variables.append(myvar)
        assert check_func("variance", inputs, variables)

    def test_variables_4(self):
        x = np.linspace(2, 201, 200)
        var = randomvar(
            0.5, variance=1 / 12, dist="chi2", isinteger=False, meanconv=True
        )
        line1 = line(x, var)

        axislabels = ["Number of random variables", "Sample variance"]
        assert check_plot([line1], explabels=axislabels, explegend=False, output=True)

    def test_function(self):
        inputs, var = [], []
        for i in range(2, 10):
            inputs.append((i,))
            myvar1 = randomvar(
                0.5, variance=1 / 12 / i, dist="conf_lim", dof=i - 1, limit=0.90
            )
            var.append(myvar1)
        assert check_func("mean_with_errors", inputs, var)
