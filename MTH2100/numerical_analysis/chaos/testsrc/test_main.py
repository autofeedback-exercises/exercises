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
def logistic_map(x, r):
    # your code goes here
    return r * x * (1 - x)

logistic_map.inputs = [
    (0.1,  1),
    (0.4,  2.4),
    (0.7,  3.5),
    (0.9,  3.999)
]

def iterate_map(x0, r, n_iter=100):
    # your code goes 
    x = x0
    xs = [x0]
    for _ in range(n_iter):
        x = logistic_map(x, r)
        xs.append(x)
    return xs

iterate_map.inputs = [
    (0.1,  1, 10),
    (0.4,  2.4, 5),
    (0.7,  3.5, 7),
    (0.9,  3.999, 20)
]

def double_pendulum(t, state, l1=1.0, l2=1.0, m1=1.0, m2=1.0, g=9.81):

    theta1, omega1, theta2, omega2 = state
    delta = theta2 - theta1

    denom1 = (m1 + m2) * l1 - m2 * l1 * np.cos(delta)**2
    denom2 = (l2 / l1) * denom1

    dtheta1_dt = omega1
    dtheta2_dt = omega2

    # Full nonlinear equations of motion
    domega1_dt = (
        m2 * l1 * omega1**2 * np.sin(delta) * np.cos(delta)
        + m2 * g * np.sin(theta2) * np.cos(delta)
        + m2 * l2 * omega2**2 * np.sin(delta)
        - (m1 + m2) * g * np.sin(theta1)
    ) / denom1

    domega2_dt = (
        -m2 * l2 * omega2**2 * np.sin(delta) * np.cos(delta)
        + (m1 + m2) * g * np.sin(theta1) * np.cos(delta)
        - (m1 + m2) * l1 * omega1**2 * np.sin(delta)
        - (m1 + m2) * g * np.sin(theta2)
    ) / denom2

    return [dtheta1_dt, domega1_dt, dtheta2_dt, domega2_dt]

double_pendulum.inputs = [
    (0,   [1, 1, 0, 0.1]),
    (0,   [0.3, 0.7, -0.1, 0.4]),
    (0,   [0.3, 0.7, -0.1, 0.4], 2.0, 2.0),
]

class UnitTests(unittest.TestCase):
    def test_logistic(self):
        assert fc.check_func(logistic_map)

    def test_iterate(self):
        assert fc.check_func(iterate_map)

    def test_double_pendulum(self):
        assert fc.check_func(double_pendulum)

    def test_plot(self):
        logistic_a = iterate_map(x0=0.5, r=3.9)
        logistic_b = iterate_map(x0=0.5000001, r=3.9)
        lines = [line(range(101), logistic_a, label='x0=0.5'), 
                 line(range(101), logistic_b, label='x0=0.5000001')]
        pc.check_plot(explines=lines, output=True)