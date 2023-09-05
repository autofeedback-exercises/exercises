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

xvals = np.linspace(0,29,30) 
yvals = xvals*xvals
line1 = line(xvals,yvals)

axislabels=["Index", "Square"]

class UnitTests(unittest.TestCase) :
    def test_fib(self) :
       assert( pc.check_plot([line1],explabels=axislabels,explegend=False,output=True) )    
