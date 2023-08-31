try:
    from AutoFeedback.funcchecks import check_func 
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.funcchecks import check_func

import AutoFeedback.plotchecks as pc
from AutoFeedback.plotclass import line
import unittest
from main import *

filedata = np.loadtxt("md_results.txt")
tmid, cvmid = np.zeros(len(filedata)-1), np.zeros(len(filedata)-1)
for i in range(len(filedata)-1) :
    tmid[i] = (filedata[i,0] + filedata[i+1,0] ) / 2 
    cvmid[i] = (filedata[i+1,1] - filedata[i,1]) / (filedata[i+1,0] - filedata[i,0])

line1 = line( tmid, cvmid )
axislabels = ["temperature / natural units", "heat capacity / natural units"]

class UnitTests(unittest.TestCase) :
    def test_graph(self) :
        assert( pc.check_plot([line1],explabels=axislabels,explegend=False,output=True) )
