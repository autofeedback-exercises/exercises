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

x, e, var, bmin, bmax, isi  = [], [], [], [], [], []
for i in range(nparam+1) :
    x.append(i)
    pval = binom.pmf(i, nparam, prob )
    e.append(pval)
    var.append(pval*(1-pval)/nsamples)
    bmin.append(0)
    bmax.append(1)
    isi.append(False)

var = randomvar( e, variance=var, vmin=bmin, vmax=bmax, isinteger=isi ) 
line1=line( x, var )

axislabels=["Random variable value", "Fraction of occurances"]

class UnitTests(unittest.TestCase) :
    def test_plot(self) :
        assert(check_plot([],exppatch=line1,explabels=axislabels,explegend=False,output=True))
