try:            
    from AutoFeedback.funcchecks import check_func
except:             
    import subprocess
    import sys
            
    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.funcchecks import check_func
                
from AutoFeedback.plotclass import line
from AutoFeedback.plotchecks import check_plot             
import numpy as np  
import unittest     
from main import *

xvals = temperatures
yvals = -8*( -np.exp(-1/xvals) - 3*np.exp(-3/xvals) )/ (1  + np.exp(-1/xvals) + np.exp(-3/xvals) )
        
line1 = line(xvals, yvals)
axislabels=["temperature","average energy"]

class UnitTests(unittest.TestCase) :
    def test_graph(self) :
        assert( check_plot( [line1], explabels=axislabels, explegend=False,output=True) )
