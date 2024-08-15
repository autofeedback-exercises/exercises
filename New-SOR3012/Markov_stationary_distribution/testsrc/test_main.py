from AutoFeedback.funcchecks import check_func
from AutoFeedback.plotchecks import check_plot
from AutoFeedback.varchecks import check_vars
from AutoFeedback.plotclass import line
from AutoFeedback.randomclass import randomvar
from AutoFeedback.utils import get_internal as get
import numpy as np
import unittest


def get_energies():
    return np.loadtxt(
        "https://raw.githubusercontent.com/autofeedback-exercises/exercises/testpip/New-SOR3012/Markov_stationary_distribution/energies"
    )[:, 1]


def setup_block_avg():
    eng = get("eng")
    myeng = get_energies()
    xvals, yvals, k = [10, 20, 30, 40, 60, 100, 120, 200, 300, 400], np.zeros(10), 0
    for bb in xvals:
        nblocks = int(len(eng) / bb)
        myaverage, mysq = 0, 0
        for i in range(nblocks):
            myblocks = sum(myeng[i * bb : (i + 1) * bb]) / bb
            myaverage = myaverage + myblocks
            mysq = mysq + myblocks * myblocks

        mysq, myaverage = mysq / nblocks, myaverage / nblocks
        myvar = (nblocks / (nblocks - 1)) * (mysq - myaverage * myaverage)
        yvals[k] = np.sqrt(myvar / nblocks)
        k = k + 1

    return xvals, yvals, myeng


class UnitTests(unittest.TestCase):
    def test_markov_move(self):
        myp = np.array([[0.3, 0.5, 0.2], [0.3, 0.4, 0.3], [0.2, 0.5, 0.3]])
        myvars, inputs, variables = np.array([0, 1, 2]), [], []
        for j in range(3):
            exp = np.dot(myp[j, :], myvars)
            var = var = np.dot(myp[j, :], myvars * myvars) - exp * exp
            for i in range(10):
                inputs.append(
                    (
                        myp,
                        j,
                    )
                )
                myvar = randomvar(
                    exp, variance=var, vmin=0, vmax=2, isinteger=True, nsamples=100
                )
                variables.append(myvar)

        assert check_func("markov_move", inputs, variables)

    def test_endstate(self):
        myp = np.array([[0.3, 0.5, 0.2], [0.3, 0.4, 0.3], [0.2, 0.5, 0.3]])
        inputs, variables = [], []
        for i in range(2, 12):
            myprobs = np.linalg.matrix_power(myp, i)
            for s in range(3):
                for e in range(3):
                    inputs.append(
                        (
                            myp,
                            s,
                            i,
                            e,
                        )
                    )
                    p = myprobs[s, e]
                    myvar = randomvar(
                        p,
                        variance=p * (1 - p),
                        vmin=0,
                        vmax=1,
                        isinteger=True,
                        nsamples=100,
                    )
                    variables.append(myvar)
        assert check_func("is_transition", inputs, variables, calls=["markov_move"])

    def test_mean(self):
        myp = np.array([[0.3, 0.5, 0.2], [0.3, 0.4, 0.3], [0.2, 0.5, 0.3]])
        ns, inputs, variables = 100, [], []
        for i in range(2, 4):
            nsteps = i * 10
            myprobs = np.linalg.matrix_power(myp, nsteps)
            for s in range(3):
                for e in range(3):
                    inputs.append(
                        (
                            myp,
                            s,
                            nsteps,
                            e,
                            ns,
                        )
                    )
                    p = myprobs[s, e]
                    myvar = randomvar(
                        p,
                        variance=p * (1 - p) / ns,
                        dist="uncertainty",
                        dof=ns - 1,
                        limit=0.9,
                        vmin=0,
                        vmax=1,
                    )
                    variables.append(myvar)
        assert check_func("sample_mean", inputs, variables)

    def test_vals(self):
        myA = np.array([[0.3, 0.5, 0.2], [0.3, 0.4, 0.3], [0.2, 0.5, 0.3]])
        assert check_vars("A", myA)
        assert check_vars("A2", np.linalg.matrix_power(myA, 2))
        assert check_vars("A10", np.linalg.matrix_power(myA, 10))
        assert check_vars("A50", np.linalg.matrix_power(myA, 50))
        assert check_vars("A100", np.linalg.matrix_power(myA, 100))

    def test_plot(self):
        nsteps = get("nsteps")
        mya = np.array([[0.3, 0.5, 0.2], [0.3, 0.4, 0.3], [0.2, 0.5, 0.3]])
        mw, mlv = np.linalg.eig(mya.T)
        for i in range(len(mw)):
            if mw[i] > 0.9:
                myind = i
                break

        e, v, bmin, bmax, isi = mlv[:, myind] / sum(mlv[:, myind]), [], [], [], []
        for i in range(3):
            v.append(e[i] * (1 - e[i]) / nsteps)
            bmin.append(0)
            bmax.append(1)
            isi.append(False)

        rvar = randomvar(e, variance=v, vmin=bmin, vmax=bmax, isinteger=isi)
        line1 = line([1, 2, 3], rvar)
        axislabels = ["state", "probability"]

        assert check_plot(
            [], exppatch=line1, explabels=axislabels, explegend=False, output=True
        )

    def test_plot_1(self):
        mya = np.array([[0.3, 0.5, 0.2], [0.3, 0.4, 0.3], [0.2, 0.5, 0.3]])
        mw, mlv = np.linalg.eig(mya.T)
        for i in range(len(mw)):
            if mw[i] > 0.9:
                myind = i
                break

        line1 = line([1, 2, 3], mlv[:, myind] / sum(mlv[:, myind]))
        axislabels = ["State", "Probability"]

        assert check_plot(
            [], exppatch=line1, explabels=axislabels, explegend=False, output=True
        )

    def test_mean_1(self):
        mye = get_energies()
        myeng = sum(mye) / len(eng)
        assert check_vars("average", myeng)

    def test_energies(self):
        myeng = get_energies()
        xvals = np.linspace(1, 10, 10)
        yvals = np.zeros(10)
        for i in range(10):
            yvals[i] = sum(myeng[i * 100 : (i + 1) * 100]) / 100
        line1, axislabels = line(xvals, yvals), [
            "Index",
            "Average energy / natural units",
        ]
        assert check_plot([line1], explabels=axislabels, explegend=False, output=True)

    def test_graph(self):
        myeng = get_enegies()
        xvals, yvals = np.linspace(1, 10, 10), np.zeros(10)
        for i in range(10):
            thisav = sum(myeng[i * 100 : (i + 1) * 100]) / 100
            thisav2 = sum(np.power(myeng[i * 100 : (i + 1) * 100], 2)) / 100
            yvals[i] = (100 / 99) * (thisav2 - thisav * thisav)

        N = len(myeng)
        mean = sum(myeng) / N
        mean2 = sum(np.power(myeng, 2)) / N
        myvar = (N / (N - 1)) * (mean2 - mean * mean)
        line1, line2 = line(xvals, yvals), line([1, 10], [myvar, myvar])
        axislabels = ["Index", "Variance / energy^2"]
        assert check_plot(
            [line1, line2], explabels=axislabels, explegend=False, output=True
        )

    def test_average_correct(self):
        myeng = get_energies()
        myblocks, myaverage = 10 * [0], 0
        for i in range(10):
            myblocks[i] = sum(myeng[i * 100 : (i + 1) * 100]) / 100
            myaverage = myaverage + myblocks[i]
        assert check_vars("average", myaverage / 10)

    def test_error_correct(self):
        myeng = get_energies()
        myblocks, myaverage, mysq = 10 * [0], 0, 0
        for i in range(10):
            myblocks[i] = sum(myeng[i * 100 : (i + 1) * 100]) / 100
            myaverage = myaverage + myblocks[i]
            mysq = mysq + myblocks[i] * myblocks[i]

        mysq, myaverage = mysq / 10, myaverage / 10
        myvar = (10 / 9) * (mysq - myaverage * myaverage)
        assert check_vars("error", np.sqrt(myvar / 10))

    def test_blockVals(self):
        xvals, yvals, myeng = setup_block_avg()
        inputs, outputs = [], []
        for i in range(len(xvals)):
            inputs.append(
                (
                    xvals[i],
                    myeng,
                )
            )
            outputs.append(yvals[i])
        assert check_func("block_average", inputs, outputs)

    def test_plot_2(self):

        xvals, yvals, myeng = setup_block_avg()
        line1 = line(xvals, yvals)
        axislabels = ["Size of blocks", "Error"]
        assert check_plot([line1], explabels=axislabels, explegend=False, output=True)
