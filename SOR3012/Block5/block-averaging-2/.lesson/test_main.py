try:
    import AutoFeedback.plotchecks as pc
    from AutoFeedback.plotclass import line
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    import AutoFeedback.plotchecks as pc
    from AutoFeedback.plotclass import line

import unittest
from main import *

myeng = np.loadtxt("energies")[:,1]
xvals = np.linspace( 1, 10, 10 )
yvals = np.zeros(10)
for i in range(10) : yvals[i] = sum( myeng[i*100:(i+1)*100] ) / 100
line1, axislabels  = line(xvals,yvals), ["Index", "Average energy / natural units"]

class UnitTests(unittest.TestCase) :
    def test_energies(self) :
        assert( pc.check_plot([line1],explabels=axislabels,explegend=False,output=True) )
