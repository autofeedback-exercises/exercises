from AutoFeedback.funcchecks import check_func
from AutoFeedback.plotchecks import check_plot
from AutoFeedback.plotclass import line
from AutoFeedback.utils import get_internal as get
from AutoFeedback.randomclass import randomvar
import numpy as np
import unittest


class UnitTests(unittest.TestCase):
    def test_variables(self):
        inputs, variables = [], []
        for i in range(20):
            a, b = np.random.uniform(0, 1), np.random.uniform(0, 1)
            inputs.append(
                (
                    a,
                    b,
                )
            )
            variables.append(a * b)
        assert check_func("multiply", inputs, variables)

    def test_variables_1(self):
        inputs, variables = [], []
        for i in range(20):
            a = np.random.uniform(-1, 1)
            inputs.append((a,))
            if a < 0:
                variables.append(-a)
            else:
                variables.append(a)
        assert check_func("modulo", inputs, variables)

    def test_variables_2(self):

        x = np.linspace(1, 100, 100)
        uniform = randomvar(0.5, variance=1 / 12, vmin=0, vmax=1, isinteger=False)
        line1 = line(x, uniform)

        axislabels = ["Index", "random variable"]
        assert check_plot([line1], explabels=axislabels, explegend=False, output=True)

    def test_variables_3(self):
        inputs, variables = [], []
        for a in range(-3, 3):
            for b in range(4, 9):
                inputs.append(
                    (
                        a,
                        b,
                    )
                )
                myvar = randomvar(
                    (a + b) / 2,
                    variance=(b - a) * (b - a) / 12,
                    vmin=a,
                    vmax=b,
                    isinteger=False,
                    nsamples=100,
                )
                variables.append(myvar)
        assert check_func("uniform", inputs, variables)

    def test_mean(self):
        inputs, variables = [], []
        for i in range(1, 9):
            p = i * 0.1
            inputs.append((i * 0.1,))
            myvar = randomvar(
                p, variance=p * (1 - p), vmin=0, vmax=1, isinteger=True, nsamples=100
            )
            variables.append(myvar)
        assert check_func("bernoulli", inputs, variables)

    def test_variables_4(self):
        prob = get("prob")
        x = np.linspace(1, 100, 100)
        var = randomvar(
            prob, variance=prob * (1 - prob), vmin=0, vmax=1, isinteger=True
        )
        line1 = line(x, var)

        axislabels = ["Index", "random variable"]
        assert check_plot([line1], explabels=axislabels, explegend=False, output=True)

    def test_graph(self):
        prob = get("prob")

        x = np.linspace(1, 100, 100)
        var = randomvar(
            prob, variance=prob * (1 - prob), vmin=0, vmax=1, isinteger=True
        )
        line1 = line(x, var)

        axislabels = ["Index", "random variable"]
        assert check_plot([line1], explabels=axislabels, explegend=False, output=True)

    def test_variables_5(self):
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
                    n * p,
                    variance=n * p * (1 - p),
                    vmin=0,
                    vmax=n,
                    isinteger=True,
                    nsamples=100,
                )
                variables.append(myvar)
        assert check_func("binomial", inputs, variables, calls=["bernoulli"])

    def test_variables_6(self):

        prob = get("prob")
        num = get("num")
        x = np.linspace(1, 100, 100)
        var = randomvar(
            num * prob,
            variance=num * prob * (1 - prob),
            vmin=0,
            vmax=num,
            isinteger=True,
        )
        line1 = line(x, var)

        axislabels = ["Index", "random variable"]
        assert check_plot([line1], explabels=axislabels, explegend=False, output=True)

    def test_variables_7(self):
        inputs, variables = [], []
        for i in range(1, 9):
            p = i * 0.1
            inputs.append((p,))
            myvar = randomvar(
                1 / p, variance=(1 - p) / (p * p), vmin=1, isinteger=True, nsamples=100
            )
            variables.append(myvar)
        assert check_func("geometric", inputs, variables, calls=["bernoulli"])

    def test_variables_8(self):
        prob = get("prob")
        x = np.linspace(1, 100, 100)
        var = randomvar(
            1 / prob, variance=(1 - prob) / (prob * prob), vmin=0, isinteger=True
        )
        line1 = line(x, var)

        axislabels = ["Index", "random variable"]
        assert check_plot([line1], explabels=axislabels, explegend=False, output=True)

    def test_variables_9(self):
        inputs, variables = [], []
        for a in range(-3, 3):
            for b in range(4, 9):
                inputs.append(
                    (
                        a,
                        b,
                    )
                )
                myvar = randomvar(
                    (a + b) / 2,
                    variance=((b - a + 1) * (b - a + 1) - 1) / 12,
                    vmin=a,
                    vmax=b,
                    isinteger=True,
                )
                variables.append(myvar)
        assert check_func("uniform_discrete", inputs, variables)

    def test_variables_10(self):
        x = np.linspace(1, 100, 100)
        var = randomvar(3.5, variance=35 / 12, vmin=1, vmax=6, isinteger=True)
        line1 = line(x, var)

        axislabels = ["Index", "dice roll"]
        assert check_plot([line1], explabels=axislabels, explegend=False, output=True)
