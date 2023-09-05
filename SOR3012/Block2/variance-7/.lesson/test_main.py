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

x = np.linspace(2,201,200)
var = randomvar( 0.5, variance=1/12, dist="chi2", isinteger=False, meanconv=True ) 
line1=line( x, var )

axislabels=["Number of random variables", "Sample variance"]

class UnitTests(unittest.TestCase) :
    def test_variables(self) :
        assert(check_plot([line1],explabels=axislabels,explegend=False,output=True))
