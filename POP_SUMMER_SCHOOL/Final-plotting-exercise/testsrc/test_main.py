from AutoFeedback.funcchecks import check_func
from AutoFeedback.plotchecks import check_plot
from AutoFeedback.plotclass import line
from AutoFeedback.utils import get_internal as get
import numpy as np
import unittest


def mytemp(time, lattitude) :
  phi = 15*(time - 12)
  phi_rad = phi*np.pi/180
  lamb = lattitude*np.pi/180
  T4 = (1-0.12)*1361*np.cos(lamb)*np.cos(phi_rad) / ( 0.98*5.67E-8)
  return T4**(1/4)

def my_change(initial_lattitude, start_time, duration, final_latitude ) :
  return mytemp( start_time + duration, initial_lattitude ) - mytemp( start_time, initial_lattitude )

class UnitTests(unittest.TestCase):
    def test_ex1(self):
        inputs, variables = [], []
        for l in np.linspace(0,90,10) :
            for t in np.linspace(7,17,11) :
                inputs.append((t,l,))
                phi = 15*(t- 12)
                phi_rad = phi*np.pi/180
                lamb = l*np.pi/180
                T4 = (1-0.12)*1361*np.cos(lamb)*np.cos(phi_rad) / ( 0.98*5.67E-8)
                variables.append(T4**(1/4))
        assert check_func("moon_temperature", inputs, variables)

    def test_ex2(self):
        times = np.linspace(7,17,11)
        temperatures = mytemp(times, 30)
        line1, axislabels = line(times, temperatures), ["time of day", "Temperature at lattitude of 30 degrees / K"]
        assert check_plot([line1], explabels=axislabels, explegend=False, output=True)  

    def test_ex3(self):
        latt = np.linspace(0,90,10)
        temperatures = mytemp(10, latt)
        line1, axislabels = line(latt, temperatures), ["latitude / degrees", "Temperature at 10:00 / K"]
        assert check_plot([line1], explabels=axislabels, explegend=False, output=True)

    def test_ex4(self):
        inputs, variables = [], [] 
        for t in np.linspace(7,11,10) :
            for d in np.linspace(1,4,3) : 
                for ls in np.linspace(0,90,10) :
                    for es in np.linspace(0,90,10) : 
                        inputs.append((ls, t, d, es,))
                        variables.append(my_change(ls,t,d,es))
        assert check_func("temperature_change", inputs, variables)

    def test_ex5(self):
        times = np.linspace(7,17,11)
        temperatures = mytemp(times, 25)
        line1, axislabels = line(times, temperatures), ["time / lunar hours", "temperature at latitude 25 degrees / Kelvin"]
        assert check_plot([line1], explabels=axislabels, explegend=False, output=True)

    def test_ex6(self): 
        times = np.linspace(7,17,11)
        lattitudes = np.linspace(90,35,11)
        temperatures = np.zeros(11)
        moon_temperature = get("moon_temperature")
        for i in range(11) : temperatures[i] = moon_temperature(times[i], lattitudes[i])
        line1, axislabels = line(times, temperatures), ["time / lunar hours", "temperature / K"]
        assert check_plot([line1], explabels=axislabels, explegend=False, output=True)
