import AutoFeedback.plotchecks as pc
from AutoFeedback.plotclass import line
import unittest

import numpy as np

theta1= np.linspace(-4,4,10)
theta2= np.linspace(-4,4,500)
line1=line(theta1, np.sin(theta1), linestyle=['-','solid'],\
colour=['r','red',(1.0,0.0,0.0,1)],\
label='coarse')

line2=line(theta2, np.sin(theta2), linestyle=['-','solid'],\
colour=['b','blue',(0.0,0.0,1.0,1)],\
label='smooth')

axislabels=["x","y",""]

class UnitTests(unittest.TestCase) :
    def test_plot(self):
        assert(pc.check_plot([line1,line2],explabels=axislabels,explegend=True,output=True))

