import AutoFeedback.plotchecks as pc
from AutoFeedback.plotclass import line
import unittest
import numpy as np

theta= np.linspace(0,2*np.pi,1000)
line1=line(np.cos(theta), np.sin(theta), linestyle=['-','solid'],\
colour=['k','black',(0.0,0.0,0.0,1)],label="Circle")

axislabels=["x","y",""]

class UnitTests(unittest.TestCase) :
    def test_plot(self):
        assert(pc.check_plot([line1],explabels=axislabels,output=True))

