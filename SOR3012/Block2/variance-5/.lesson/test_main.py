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

x, expect, variance, isi = np.linspace(1,50,50), np.zeros(50), np.zeros(50), []
for i in range(50) : 
    expect[i], variance[i] = 0.5, 1/12/(i+1)
    isi.append(False)

y = randomvar( expect, variance=variance, dist="chi2", dof=9, isinteger=isi )
line1=line( x, y )

axislabels=["Number of variables used to calculate mean", "Variance"]

class UnitTests(unittest.TestCase) :
    def test_variables(self) :
        assert(check_plot([line1],explabels=axislabels,explegend=False,output=True))
