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

S, S2, myp = 0, 0, np.array([[1,0,0,0,0],[1/3,1/3,1/3,0,0],[0,0.5,0,0.5,0],[0,0.5,0,0,0.5],[0,0,0,0,1]]) 
for i in range(100) : 
    var = nsteps_to_absorption( myp, 1 )
    S, S2 = S + var, S2 + var*var
mean = S / 100
var = (100/99)*( S2/100 - mean*mean ) 

myq = np.array([[1/3,1/3,0],[0.5,0,0.5],[0.5,0,0]])
my_inv = np.linalg.inv( np.identity(3) - myq )
rand = randomvar( np.dot( my_inv, np.array([1,1,1]) )[0], variance=var, vmin=1, isinteger=True )
line1 = line( np.linspace(1,20,20),  rand ) 
axislabels=["Index", "Number of steps till absorption"]

class UnitTests(unittest.TestCase) :
    def test_plot(self) :
        assert(check_plot([line1],explabels=axislabels,explegend=False,output=True))
