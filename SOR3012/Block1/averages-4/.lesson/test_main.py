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

x = np.linspace(1,200,200)
var = randomvar( 0.5, variance=1/12, vmin=0, vmax=1, isinteger=False, meanconv=True ) 
line1=line( x, var )
line2=line( [0,200], [0.5,0.5] )

axislabels=["Number of random variables", "Sample mean"]

class UnitTests(unittest.TestCase) :
    def test_variables(self) :
        assert(check_plot([line1,line2],explabels=axislabels,explegend=False,output=True))
