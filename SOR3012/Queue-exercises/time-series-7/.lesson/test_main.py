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
from scipy.stats import binom
from main import *

e, var, isi, y = [], [], [], []
for i in range(nevents) :
    e.append( (i+1)/lamd )
    var.append( (i+1)/(lamd*lamd) )
    y.append(i+1)
    isi.append(False)

var = randomvar( e, variance=var, isinteger=isi )
line1=line( var, y )

axislabels=["time", "number of events"]

class UnitTests(unittest.TestCase) :
    def test_plot(self) :
        assert(check_plot([line1],explabels=axislabels,explegend=False,output=True))
