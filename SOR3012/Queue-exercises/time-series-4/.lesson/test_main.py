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

delx, x, e, var, isi  = xmax/nbins, [], [], [], []
for i in range(nbins) :
    x.append( (i+0.5)*delx )
    pval = ( np.exp( -lamd*i*delx ) - np.exp( -lamd*(i+1)*delx ) )
    e.append(pval / delx )
    var.append( pval*(1-pval) / (delx*delx) )
    isi.append(False)

var = randomvar( e, variance=var, isinteger=isi )
line1=line( x, var )

axislabels=["Random variable value", "Probability"]

class UnitTests(unittest.TestCase) :
    def test_plot(self) :
        assert(check_plot([line1],explabels=axislabels,explegend=False,output=True))
