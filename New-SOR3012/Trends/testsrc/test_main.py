from AutoFeedback.plotchecks import check_plot
from AutoFeedback.funcchecks import check_func
from AutoFeedback.plotclass import line
from AutoFeedback.randomclass import randomvar
from AutoFeedback.varchecks import check_vars
import numpy as np
import unittest


def simulate(s, n, p):
    ngoes = 0
    while s > 0 and s < n:
        ngoes = ngoes + 1
        if np.random.uniform(0, 1) < p:
            s = s + 1
        else:
            s = s - 1
    return ngoes


def get_var(s, n, p):
    myvar = simulate(s, n, p)
    S, S2 = myvar, myvar * myvar
    for i in range(1, 200):
        myvar = simulate(s, n, p)
        S, S2 = S + myvar, S2 + myvar * myvar
    mean = S / 200
    return (200 / 199) * (S2 / 200 - mean * mean)


class helper:
    def __init__(self, n, s):
        self.n, self.s = n, s

    def check_random_walk(self, val):
        return (self.n + val - self.s) / 2


class UnitTests(unittest.TestCase):
    def test_random_walk(self):
        inputs, variables, helpers = [], [], []
        for s in range(-1, 2):
            for n in range(2, 4):
                for i in range(1, 5):
                    p = i * 0.2
                    inputs.append(
                        (
                            s,
                            n,
                            p,
                        )
                    )
                    helpers.append(helper(n, s))
                    myvar = randomvar(
                        n * p,
                        variance=n * p * (1 - p),
                        vmin=0,
                        vmax=n,
                        transform=helpers[len(helpers) - 1].check_random_walk,
                        isinteger=True,
                    )
                    variables.append(myvar)
        assert check_func("random_walk", inputs, variables)

    def test_gambler(self):
        inputs, variables = [], []
        for s in range(1, 4):
            for n in range(6, 9):
                for i in range(1, 5):
                    p = i * 0.2
                    rat = (1 - p) / p
                    prob = (rat**s - rat**n) / (1 - rat**n)
                    inputs.append(
                        (
                            s,
                            n,
                            p,
                        )
                    )
                    myvar = randomvar(
                        prob, variance=prob * (1 - prob), vmin=0, vmax=1, isinteger=True
                    )
                    variables.append(myvar)
        assert check_func("gambler", inputs, variables)

    def test_gambler_1(self):
        inputs, variables = [], []
        for s in range(1, 4):
            for n in range(6, 8):
                for i in range(1, 5):
                    p = i * 0.2
                    inputs.append(
                        (
                            s,
                            n,
                            p,
                        )
                    )
                    rat = (1 - p) / p
                    exp = s / (1 - 2 * p) - (n / (1 - 2 * p)) * (1 - rat**s) / (
                        1 - rat**n
                    )
                    testvar = get_var(
                        s, n, p
                    )  # It would be nice to have an exact value here
                    myvar = randomvar(exp, variance=testvar, vmin=1, isinteger=True)
                    variables.append(myvar)
        assert check_func("nplays", inputs, variables)

    def test_random_walker(self):
        inputs, variables = [], []
        for s in range(1, 4):
            for n in range(6, 9):
                for i in range(1, 3):
                    p = i * 0.2
                    rat = (1 - p) / p
                    prob = (rat**s - rat**n) / (1 - rat**n)
                    inputs.append(
                        (
                            s,
                            n,
                            p,
                        )
                    )
                    myvar = randomvar(
                        prob, variance=prob * (1 - prob), vmin=0, vmax=1, isinteger=True
                    )
                    variables.append(myvar)
        assert check_func("random_walker", inputs, variables)

    def test_mean(self):
        inputs, variables = [], []
        for i in range(1, 3):
            p = i * 0.3
            rat = (1 - p) / p
            prob = (rat**5 - rat**10) / (1 - rat**10)
            inputs.append(
                (
                    5,
                    10,
                    p,
                    100,
                )
            )
            myvar = randomvar(
                prob,
                variance=prob * (1 - prob) / 100,
                dist="conf_lim",
                vmin=0,
                vmax=1,
                dof=99,
                limit=0.9,
            )
            variables.append(myvar)
        assert check_func("sample_mean", inputs, variables)

    def test_plot(self):
        n, p = 10, 0.4
        rat = (1 - p) / p
        x, e, var, bmin, bmax, isi = [], [], [], [], [], []
        for s in range(1, 10):
            x.append(s)
            prob = (rat**s - rat**n) / (1 - rat**n)
            e.append(prob)
            var.append(prob * (1 - prob) / 200)
            bmin.append(0)
            bmax.append(1)
            isi.append(False)

        val = randomvar(e, variance=var, vmin=bmin, vmax=bmax, isinteger=isi)
        line1 = line(x, val)
        axislabels = ["start point", "probability of ruin"]
        assert check_plot([line1], explabels=axislabels, explegend=False, output=True)

    def test_plot_1(self):
        n, s = 4, 2
        x, e, var, bmin, bmax, isi = [], [], [], [], [], []
        for sp in range(3, 8):
            x.append(sp * 0.1)
            rat = (1 - sp * 0.1) / (sp * 0.1)
            if sp == 5:
                prob = (n - s) / n
            else:
                prob = (rat**s - rat**n) / (1 - rat**n)
            e.append(prob)
            var.append(prob * (1 - prob) / 200)
            bmin.append(0)
            bmax.append(1)
            isi.append(False)

        val = randomvar(e, variance=var, vmin=bmin, vmax=bmax, isinteger=isi)
        line1 = line(x, val)
        axislabels = ["Probability of winning each game", "Probability of ruin"]
        assert check_plot([line1], explabels=axislabels, explegend=False, output=True)

    def test_errors(self):
        n, s, prob = 4, 2, np.zeros(5)
        for sp in range(3, 8):
            rat = (1 - sp * 0.1) / (sp * 0.1)
            if sp == 5:
                prob[sp - 3] = (n - s) / n
            else:
                prob[sp - 3] = (rat**s - rat**n) / (1 - rat**n)
        myvar = randomvar(
            prob,
            variance=prob * (1 - prob) / 200,
            dist="chi2",
            dof=199,
            limit=0.9,
            isinteger=[False, False, False, False, False],
        )
        assert check_vars("error", myvar)
