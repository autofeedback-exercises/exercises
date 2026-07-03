try:
    from AutoFeedback import varchecks as vc
    from AutoFeedback import funcchecks as fc
    from AutoFeedback import plotchecks as pc
    from AutoFeedback.plotclass import line
    from AutoFeedback.utils import get_internal as get
except ImportError:

    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback[plot]"])
    from AutoFeedback import var as vc
    from AutoFeedback import funcchecks as fc
    from AutoFeedback import plotchecks as pc
    from AutoFeedback.plotclass import line

import unittest
import numpy as np


class UnitTests(unittest.TestCase):
    def test_df(self):
        K = get('K')
        r = get('r')
        H_val = get('H_val')
        def harvest_model(N, H=H_val):
            return r * N * (1 - N / K) - H 

        def df_harvest(x):
            h=0.01
            return (harvest_model(x+h)-harvest_model(x))/h
        df_harvest.inputs=[(1,),(20,),(99,)]
        assert fc.check_func(df_harvest)

    def test_eq1(self):
        NR_method = get('newton_raphson')
        HM_method = get('harvest_model')
        DF_method = get('df_harvest')
        eq1, _ = NR_method(HM_method, DF_method, x0=1)
        assert vc.check_vars('eq_NR1', eq1)

    def test_eq2(self):
        NR_method = get('newton_raphson')
        HM_method = get('harvest_model')
        DF_method = get('df_harvest')
        K = get('K')
        eq2, _ = NR_method(HM_method, DF_method, x0=K)
        assert vc.check_vars('eq_NR2', eq2)

    def test_double_root(self):
        def double_root(x):
            return (x-2)*(x-2)*(x+1)
        double_root.inputs = [(-3,), (-1,), (0,), (2.7,)]
        assert(fc.check_func(double_root))

    def test_df_double_root(self):
        def df_double_root(x):
            return (x - 2)**2 + (x + 1)*(2*x - 4)
        df_double_root.inputs = [(-1.1,), (0,), (2.1,)]
        assert(fc.check_func(df_double_root, tol=1e-2))

    def test_roots(self):
        NR_method = get('newton_raphson')
        DR = get('double_root')
        DF = get('df_double_root')
        r1, _ = NR_method(DR, DF, -10)
        r2, _ = NR_method(DR, DF, 10, max_iter=10000)
        assert(vc.check_vars('r1',r1))
        assert(vc.check_vars('r2',r2))

    def test_errors(self):
        hist_r1 = get('hist_r1')
        hist_r2 = get('hist_r2')
        assert (vc.check_vars('error_r1', abs(1+np.array(hist_r1))))
        assert (vc.check_vars('error_r2', abs(2-np.array(hist_r2))))

    def test_plot(self):
        error_r1 = get('error_r1')
        error_r2 = get('error_r2')
        line1 = line([x for x in range(len(error_r1))], error_r1, label='error_r1')
        line2 = line([x for x in range(len(error_r2))], error_r2, label='error_r2')
        lines = [line1, line2]
        assert pc.check_plot(lines, explegend=True, output=True, explabels=['Number of iterations', 'Error', ''])