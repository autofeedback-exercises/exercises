from AutoFeedback.funcchecks import check_func
from AutoFeedback.plotchecks import check_plot
from AutoFeedback.plotclass import line
from AutoFeedback.utils import get_internal as get
import numpy as np
import unittest


class UnitTests(unittest.TestCase):
    def test_variables(self):
        inputs, variables = [], []
        for i in range(20):
            a, b = np.random.uniform(0, 1), np.random.uniform(0, 1)
            inputs.append(
                (
                    a,
                    b,
                )
            )
            variables.append(a * b)
        assert check_func("multiply", inputs, variables)

    def test_variables_1(self):
        inputs, variables = [], []
        for i in range(20):
            a = np.random.uniform(-1, 1)
            inputs.append((a,))
            if a < 0:
                variables.append(-a)
            else:
                variables.append(a)
        assert check_func("modulo", inputs, variables)

    def test_moontemperature(self):
        inputs, variables = [], []
        for d in np.linspace(0.5,2.5,200) : 
            inputs.append((d,))
            LH = (1-0.12)*1361/(d*d) 
            T4 = LH / (0.98*5.67E-8)
            variables.append(T4**(1/4))
        assert( check_func("moon_temperature", inputs, variables ) )

    def test_planettemperature(self):
        inputs, variables = [], []
        for e in np.linspace(0.1,0.9,9) :
            for a in np.linspace(0.1,0.9,9) :
                for d in np.linspace(0.5,2.5,10) : 
                    inputs.append((e,a,d,))
                    LH = (1-a)*1361/(d*d) 
                    T4 = LH / (e*5.67E-8)
                    variables.append(T4**(1/4))
        assert( check_func("planet_temperature", inputs, variables ) )
