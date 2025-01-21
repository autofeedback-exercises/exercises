from AutoFeedback.funcchecks import check_func
from AutoFeedback.plotchecks import check_plot
from AutoFeedback.plotclass import line
import numpy as np
import unittest


class UnitTests(unittest.TestCase):
    def test_moontemp(self):
        inputs, variables = [], []
        for t in np.linspace(7, 17):
            inputs.append((t,))
            phi = 15 * (t - 12)
            phi_rad = np.pi * phi / 180
            T4 = 1361 * (1 - 0.12) * np.cos(phi_rad) / (0.98 * 5.67e-8)
            variables.append(T4 ** (1 / 4))
        assert check_func("moon_temperature", inputs, variables)

    def test_moongraph1(self):
        times = np.linspace(7, 17, 11)
        temperatures = (
            1361
            * (1 - 0.12)
            * np.cos(15 * np.pi * (times - 12) / 180)
            / (0.98 * 5.67e-8)
        ) ** (1 / 4)
        line1, axislabels = line(times, temperatures), [
            "time of day",
            "Temperature at equator / K",
        ]
        assert check_plot([line1], explabels=axislabels, explegend=False, output=True)

    def test_moon_rotation(self):
        inputs, variables = [], []
        for t in np.linspace(0, 29.5, 360):
            inputs.append((t,))
            variables.append((t / (29.5 * 24)) * 360)
        assert check_func("moon_rotation", inputs, variables)

    def test_moongraph2(self):
        times = np.linspace(7, 17, 11)
        temperatures = (
            1361
            * (1 - 0.12)
            * np.cos(15 * np.pi * (times - 12) / 180)
            / (0.98 * 5.67e-8)
        ) ** (1 / 4)
        new_times = (times - 7) * 29.5 / 24
        line1, axislabels = line(new_times, temperatures), [
            "time / Earth days",
            "Temperature at equator / K",
        ]
        assert check_plot([line1], explabels=axislabels, explegend=False, output=True)

    def test_lunar_temperature(self):
        inputs, variables = [], []
        for t in np.linspace(0, 90, 18):
            inputs.append((t,))
            phi = 90 - t
            phi_rad = np.pi * phi / 180
            T4 = 1361 * (1 - 0.12) * np.cos(phi_rad) / (0.98 * 5.67e-8)
            variables.append(T4 ** (1 / 4) - 273)
        assert check_func("lunar_temperature", inputs, variables)
