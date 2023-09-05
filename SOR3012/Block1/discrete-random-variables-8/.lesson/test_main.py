try:
    from AutoFeedback.plotchecks import check_plot
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.plotchecks import check_plot

from AutoFeedback.plotclass import line
from AutoFeedback.randomclass import randomvar
import unittest
from main import *

x = np.linspace(1,100,100)
var = randomvar( 1/prob, variance=(1-prob)/(prob*prob), vmin=0, isinteger=True ) 
line1=line( x, var )

axislabels=["Index", "random variable"]

class UnitTests(unittest.TestCase) :
    def test_variables(self) :
        assert(check_plot([line1],explabels=axislabels,explegend=False,output=True))
