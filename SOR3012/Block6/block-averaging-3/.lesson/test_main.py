try:
    import AutoFeedback.plotchecks as pc
    from AutoFeedback.plotclass import line
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    import AutoFeedback.plotchecks as pc
    from AutoFeedback.plotclass import line

import unittest
from main import *

myeng = np.loadtxt("energies")[:,1]
xvals, yvals = np.linspace(1,10,10), np.zeros(10)
for i in range(10) :
    thisav = sum( myeng[i*100:(i+1)*100] ) / 100
    thisav2 = sum( np.power(myeng[i*100:(i+1)*100],2) ) / 100
    yvals[i] = (100/99)*( thisav2 - thisav*thisav )

N = len( myeng )
mean = sum( myeng ) / N
mean2 = sum( np.power(myeng,2) ) / N
myvar = (N/(N-1))*( mean2 - mean*mean )
line1, line2 = line(xvals, yvals), line([1,10], [myvar,myvar])
axislabels = ["Index","Variance / energy^2"]

class UnitTests(unittest.TestCase) :
    def test_graph(self) : 
        assert( pc.check_plot([line1,line2],explabels=axislabels,explegend=False,output=True) )
