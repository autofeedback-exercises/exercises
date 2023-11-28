import AutoFeedback.plotchecks as pc
from AutoFeedback.plotclass import line
import unittest

import numpy as np

theta1 = np.linspace(0, 7, 500)
x = theta1
y = np.sin(x)
z = np.sin(x+np.pi/2)


line1 = line(theta1, np.sin(theta1), linestyle=['-', 'solid'],
             colour=['r', 'red', (1.0, 0.0, 0.0, 1)],
             label='phase = 0')

line2 = line(theta1, np.sin(theta1+np.pi/2), linestyle=['--', 'dashed'],
             colour=['b', 'blue', (0.0, 0.0, 1.0, 1)],
             label='phase = pi/2')

axislabels = ["Time (s)", "Amplitude (cm)",
              "Harmonic motion with differing starting phases"]


class UnitTests(unittest.TestCase):
    def test_plot(self):
        assert pc.check_plot([line1, line2], expaxes=[
            0, 2*np.pi, -1, 1], explabels=axislabels, explegend=True,
                             output=True)
