try:
    import AutoFeedback.varchecks as vc
    from AutoFeedback.plotclass import line
    import AutoFeedback.plotchecks as pc
except:

    import subprocess
    import sys

    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.plotclass import line
    import AutoFeedback.plotchecks as pc


import unittest
import numpy as np

theta = np.linspace(0, 2*np.pi, 100)
x = np.cos(theta)
y = np.sin(theta)
circle = line(x, y, colour=["red", "r", (1.0, 0.0, 0.0, 1)], linestyle=['-', 'solid'], label="circle")

x = [-1, 1, 1, -1, -1]
y = [-1, -1, 1, 1, -1]
square = line(x, y, colour=["blue", "b", (0.0, 0.0, 1.0, 1)], linestyle=['-', 'solid'], label="square")


class UnitTests(unittest.TestCase):

    def test_plot(self):
        assert(pc.check_plot([circle, square], output=True))

