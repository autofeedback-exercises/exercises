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

mya = np.array([[0.3,0.5,0.2],[0.3,0.4,0.3],[0.2,0.5,0.3]])
mw, mlv = np.linalg.eig( mya.T )
for i in range(len(mw)) : 
    if mw[i]>0.9 : 
       myind = i
       break

line1 = line( [1,2,3], mlv[:,myind]/sum(mlv[:,myind]) )
axislabels=["State", "Probability"]

class UnitTests(unittest.TestCase) :
    def test_plot(self) :
        assert(check_plot([],exppatch=line1,explabels=axislabels,explegend=False,output=True))
