try:
    from AutoFeedback.plotchecks import check_plot
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.plotchecks import check_plot

from AutoFeedback.plotclass import line
import unittest
from scipy.stats import binom
from main import *

gyvals, gdata = [], qn.get_agent_data()
for k in gdata.keys() :
    if gdata[k][0,2]>gdata[k][0,0] : gyvals.append( gdata[k][0,2] - gdata[k][0,0] )

gxvals = np.linspace( 1, len(gyvals), len(gyvals) )
line1=line( gxvals, gyvals )

axislabels=["Agent", "Time spent in system"]

class UnitTests(unittest.TestCase) :
    def test_plot(self) :
        assert(check_plot([line1],explabels=axislabels,explegend=False,output=True))
