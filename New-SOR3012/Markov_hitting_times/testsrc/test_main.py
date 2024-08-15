from AutoFeedback.funcchecks import check_func
from AutoFeedback.plotchecks import check_plot
from AutoFeedback.plotclass import line
from AutoFeedback.randomclass import randomvar
from AutoFeedback.varchecks import check_vars
from AutoFeedback.utils import get_internal as get
import unittest
import numpy as np


class UnitTests(unittest.TestCase):
    def test_probb_vector(self):
        check_vars("probs", [0.5, 0.1, 0.2, 0.05, 0.15])

    def test_variable(self):
        probs = get("probs")
        myvars = np.array([0, 1, 2, 3, 4])
        exp = np.dot(probs, myvars)
        var = np.dot(probs, myvars * myvars) - exp * exp
        inputs, variables = [], []
        for i in range(10):
            inputs.append((probs,))
            myvar = randomvar(
                exp, variance=var, vmin=0, vmax=4, isinteger=True, nsamples=100
            )
            variables.append(myvar)

        assert check_func("myvariable", inputs, variables)

    def test_variable_1(self):
        probs = get("probs")
        myvars = np.array([0, 1, 2, 3, 4])
        exp = np.dot(probs, myvars)
        var = np.dot(probs, myvars * myvars) - exp * exp
        inputs, variables = [], []
        for i in range(10):
            inputs.append((probs,))
            myvar = randomvar(
                exp, variance=var, vmin=0, vmax=4, isinteger=True, nsamples=100
            )
            variables.append(myvar)

        assert check_func("myvariable", inputs, variables)

    def test_variable_2(self):
        inputs, variables = [], []

        myvars, mat1 = np.array([0, 1, 2]), np.array(
            [[0.3, 0.5, 0.2], [0.3, 0.4, 0.3], [0.2, 0.5, 0.3]]
        )
        for j in range(3):
            exp = np.dot(mat1[j, :], myvars)
            var = var = np.dot(mat1[j, :], myvars * myvars) - exp * exp
            for i in range(10):
                inputs.append(
                    (
                        mat1,
                        j,
                    )
                )
                myvar = randomvar(
                    exp, variance=var, vmin=0, vmax=2, isinteger=True, nsamples=100
                )
                variables.append(myvar)
        myvars, mat2 = np.array([0, 1, 2, 3, 4]), np.array(
            [
                [1, 0, 0, 0, 0],
                [1 / 3, 1 / 3, 1 / 3, 0, 0],
                [0, 0.5, 0, 0.5, 0],
                [0, 0.5, 0, 0, 0.5],
                [0, 0, 0, 0, 1],
            ]
        )
        for j in range(5):
            exp = np.dot(mat2[j, :], myvars)
            var = var = np.dot(mat2[j, :], myvars * myvars) - exp * exp
            for i in range(10):
                inputs.append(
                    (
                        mat2,
                        j,
                    )
                )
                myvar = randomvar(
                    exp, variance=var, vmin=0, vmax=4, isinteger=True, nsamples=100
                )
                variables.append(myvar)

        assert check_func("markov_move", inputs, variables)

    def test_plot(self):
        nsteps_to_absorption = get("nsteps_to_absorption")
        S, S2, myp = (
            0,
            0,
            np.array(
                [
                    [1, 0, 0, 0, 0],
                    [1 / 3, 1 / 3, 1 / 3, 0, 0],
                    [0, 0.5, 0, 0.5, 0],
                    [0, 0.5, 0, 0, 0.5],
                    [0, 0, 0, 0, 1],
                ]
            ),
        )
        for i in range(100):
            var = nsteps_to_absorption(myp, 1)
            S, S2 = S + var, S2 + var * var
        mean = S / 100
        var = (100 / 99) * (S2 / 100 - mean * mean)

        myq = np.array([[1 / 3, 1 / 3, 0], [0.5, 0, 0.5], [0.5, 0, 0]])
        my_inv = np.linalg.inv(np.identity(3) - myq)
        rand = randomvar(
            np.dot(my_inv, np.array([1, 1, 1]))[0], variance=var, vmin=1, isinteger=True
        )
        line1 = line(np.linspace(1, 20, 20), rand)
        axislabels = ["Index", "Number of steps till absorption"]
        assert check_plot([line1], explabels=axislabels, explegend=False, output=True)

    def test_markov_move(self):
        myp = np.array(
            [
                [1, 0, 0, 0, 0],
                [1 / 3, 1 / 3, 1 / 3, 0, 0],
                [0, 0.5, 0, 0.5, 0],
                [0, 0.5, 0, 0, 0.5],
                [0, 0, 0, 0, 1],
            ]
        )
        myq, myr = np.array([[1 / 3, 1 / 3, 0], [0.5, 0, 0.5], [0.5, 0, 0]]), np.array(
            [[1 / 3, 0], [0, 0], [0, 1 / 2]]
        )
        myprobs = np.dot(np.linalg.inv(np.identity(3) - myq), myr)
        myvars, inputs, variables = np.array([0, 1, 2, 3, 4]), [], []
        for j in range(5):
            exp = np.dot(myp[j, :], myvars)
            var = var = np.dot(myp[j, :], myvars * myvars) - exp * exp
            for i in range(10):
                inputs.append(
                    (
                        myp,
                        j,
                    )
                )
                myvar = randomvar(exp, variance=var, vmin=0, vmax=4, isinteger=True)
                variables.append(myvar)

        assert check_func("markov_move", inputs, variables)

    def test_endstate(self):
        myp = np.array(
            [
                [1, 0, 0, 0, 0],
                [1 / 3, 1 / 3, 1 / 3, 0, 0],
                [0, 0.5, 0, 0.5, 0],
                [0, 0.5, 0, 0, 0.5],
                [0, 0, 0, 0, 1],
            ]
        )
        myq, myr = np.array([[1 / 3, 1 / 3, 0], [0.5, 0, 0.5], [0.5, 0, 0]]), np.array(
            [[1 / 3, 0], [0, 0], [0, 1 / 2]]
        )
        myprobs = np.dot(np.linalg.inv(np.identity(3) - myq), myr)
        inputs, variables = [], []
        for j in range(1, 4):
            for i in range(10):
                inputs.append(
                    (
                        myp,
                        j,
                    )
                )
                p = myprobs[j - 1, 1]
                myvar = randomvar(
                    p, variance=p * (1 - p), vmin=0, vmax=1, isinteger=True
                )
                variables.append(myvar)
        assert check_func("endstate", inputs, variables, calls=["markov_move"])

    def test_mean(self):
        myp = np.array(
            [
                [1, 0, 0, 0, 0],
                [1 / 3, 1 / 3, 1 / 3, 0, 0],
                [0, 0.5, 0, 0.5, 0],
                [0, 0.5, 0, 0, 0.5],
                [0, 0, 0, 0, 1],
            ]
        )
        myq, myr = np.array([[1 / 3, 1 / 3, 0], [0.5, 0, 0.5], [0.5, 0, 0]]), np.array(
            [[1 / 3, 0], [0, 0], [0, 1 / 2]]
        )
        myprobs = np.dot(np.linalg.inv(np.identity(3) - myq), myr)
        ns, inputs, variables = 100, [], []
        for j in range(1, 4):
            inputs.append(
                (
                    myp,
                    j,
                    ns,
                )
            )
            p = myprobs[j - 1, 1]
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


    def test_plot_1(self):
        myq = np.array([[1 / 3, 1 / 3, 0], [0.5, 0, 0.5], [0.5, 0, 0]])
        myr = np.array([[1 / 3, 0], [0, 0], [0, 1 / 2]])
        my_inv = np.linalg.inv(np.identity(3) - myq)
        line1 = line([2, 3, 4], np.dot(my_inv, myr)[:, 1])
        axislabels = ["Initial state", "Probability of absorption in state 5"]
        assert check_plot(
            [], exppatch=line1, explabels=axislabels, explegend=False, output=True
        )


    def test_plot_2(self):
        myq = np.array([[1 / 3, 1 / 3, 0], [0.5, 0, 0.5], [0.5, 0, 0]])
        my_inv = np.linalg.inv(np.identity(3) - myq)
        line1 = line([2, 3, 4], np.dot(my_inv, np.array([1, 1, 1])))
        axislabels = ["Initial state", "Expected number of steps till absorbtion"]
        assert check_plot(
            [], exppatch=line1, explabels=axislabels, explegend=False, output=True
        )
