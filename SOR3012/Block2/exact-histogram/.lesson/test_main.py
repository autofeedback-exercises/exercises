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

x = [0-0.05,1-0.05,2-0.05,3-0.05,4-0.05,5-0.05,6-0.05,0+0.05,1+0.05,2+0.05,3+0.05,4+0.05,5+0.05,6+0.05]
var = np.ones(14)*1/6
var[0] = 0
for i in range(7) : var[7+i] = scipy.stats.binom.pmf(i,6,0.5)
line1=line( x, var )

axislabels=["x", "P(X=x)"]

class UnitTests(unittest.TestCase) :
    def test_plot(self) :
        assert(check_plot([],exppatch=line1,explabels=axislabels,explegend=False,output=True))
