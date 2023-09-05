try:
    from AutoFeedback.plotchecks import check_plot
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.plotchecks import check_plot

from AutoFeedback.plotclass import line
import unittest
from main import *

myx = np.loadtxt("data.dat")
myx.sort()
myy = range(1,len(myx)+1)
myy = [ a / len(myx) for a in myy ]
line1=line( myx, myy )

axislabels=["x", "cumulative distribution"]

class UnitTests(unittest.TestCase) :
    def test_plot(self) :
        assert(check_plot([line1],explabels=axislabels,explegend=False,output=True)) 
