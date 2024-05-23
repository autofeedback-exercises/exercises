try:
    import AutoFeedback.varchecks as vc
except Exception:
    import subprocess
    import sys

    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "AutoFeedback"])
    import AutoFeedback.varchecks as vc

import unittest
import sympy as sy
import numpy as np

mat = [[1, 0, 0, 0], [0, 2, 0, 0], [0, 0, 3, 0],
       [0, 0, 0, 4]]
A_sym = sy.Matrix(mat)
A_num = np.array(mat)

epairs_sym = A_sym.eigenvects()
evals_num, evects_num = np.linalg.eig(A_num)


class UnitTests(unittest.TestCase):

    def test_A_sym(self):
        assert vc.check_vars('A_sym', A_sym)

    def test_A_num(self):
        assert vc.check_vars('A_num', A_num)

    def test_epairs_sym(self):
        assert vc.check_vars('epairs_sym', epairs_sym)

    def test_epairs_num(self):
        assert vc.check_vars('evals_num', evals_num)
        assert vc.check_vars('evects_num', evects_num)
