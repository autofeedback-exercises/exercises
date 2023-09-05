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

myq = np.array([[1/3,1/3,0],[0.5,0,0.5],[0.5,0,0]])
myr = np.array([[1/3,0],[0,0],[0,1/2]])
my_inv = np.linalg.inv( np.identity(3) - myq )
line1 = line( [2,3,4], np.dot( my_inv, myr )[:,1]  )
axislabels=["Initial state", "Probability of absorption in state 5"]

class UnitTests(unittest.TestCase) :
    def test_plot(self) :
        assert(check_plot([],exppatch=line1,explabels=axislabels,explegend=False,output=True))
