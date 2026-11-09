try:
    from AutoFeedback import varchecks as vc
    from AutoFeedback import funcchecks as fc
    from AutoFeedback import plotchecks as pc
    from AutoFeedback.plotclass import line
    from AutoFeedback.utils import get_internal as get
except:

    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback[plot]"])
    from AutoFeedback import var as vc
    from AutoFeedback import funcchecks as fc
    from AutoFeedback import plotchecks as pc
    from AutoFeedback.plotclass import line
    from AutoFeedback.utils import get_internal as get

import unittest
import numpy as np
from scipy.integrate import solve_ivp


# ── Reference functions for Exercise 2 (logistic prey) and Exercise 3 (harvesting) ──

_logprey_params = {'r': 1.0, 'K': 100, 'alpha': 1.0, 'beta': 0.1, 'delta': 0.075, 'gamma': 1.5}

def logprey(t, state, params):
    x, y = state
    dxdt = params['r'] * x * (1 - x / params['K']) - params['beta'] * x * y
    dydt = params['delta'] * x * y - params['gamma'] * y
    return [dxdt, dydt]

logprey.inputs = [
    (0,   [10,  5],  _logprey_params),   # typical interior point
    (0,   [100, 0],  _logprey_params),   # no predators: pure logistic (dydt = 0)
    (0,   [0,  10],  _logprey_params),   # no prey: predators die (dxdt = 0)
    (1.5, [20, 15],  _logprey_params),   # non-zero t (should not matter)
]


_harvest_params = {'r': 1.0, 'K': 60, 'beta': 0.1, 'delta': 0.075, 'gamma': 1.5, 'H': 5.0}
_harvest_H0     = {'r': 1.0, 'K': 60, 'beta': 0.1, 'delta': 0.075, 'gamma': 1.5, 'H': 0.0}

def LV_harvest(t, state, params):
    x, y = state
    dxdt = params['r'] * x * (1 - x / params['K']) - params['beta'] * x * y - params['H']
    dydt = params['delta'] * x * y - params['gamma'] * y
    return [dxdt, dydt]

LV_harvest.inputs = [
    (0,   [20,  5],  _harvest_params),   # typical point with H > 0
    (0,   [10,  2],  _harvest_H0),        # H = 0: should match logistic prey behaviour
    (0,   [30,  8],  _harvest_params),   # different prey-rich state
    (0,   [20, 20],  _harvest_params),   # high predator density
]


# ── Reference function for Exercise 1 (logistic growth) ──

def logistic(t, N):
    r = 0.5
    K = 200
    # Logistic ODE: dN/dt = rN(1 - N/K)
    return r * N * (1 - N / K)

logistic.inputs = [(0,10), (0.1, 100), (3,300)]


class UnitTests(unittest.TestCase):
    def test_logistic(self):
        assert fc.check_func(logistic)


    def test_logprey(self):
        assert fc.check_func(logprey)

    def test_LV_harvest(self):
        assert fc.check_func(LV_harvest)

    def test_logistic_plot(self):
        lines = []
        for N0 in [5, 20, 50, 150, 250]:
            sol = solve_ivp(logistic, t_span=(0, 50), y0=[N0],
                        method='RK45')
            lines.append(line(sol.t, sol.y[0], label=f'N0={N0}'))
        assert pc.check_plot(lines, check_partial=False, output=True)

