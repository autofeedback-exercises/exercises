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

xvals, yvals = np.linspace(0,19,20), np.zeros(20)
for i in range(20) : yvals[i] = 0.5**i 
line1 = line(xvals,yvals)

axislabels=["Index", "Geometric series"]

class UnitTests(unittest.TestCase) :
    def test_fib(self) :
       assert( pc.check_plot([line1],explabels=axislabels,explegend=False,output=True) )    
