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

ddd = (maxx - minx) / nbins
n, xv, yv = 0, np.zeros(nbins), np.zeros(nbins)
for m in np.loadtxt("magnetisations") :
    mave = m / (20*20)
    xb = int( np.floor( (mave-minx) / ddd ) )
    yv[xb] = yv[xb] + 1
    n = n + 1

yv = yv / n
xv = np.zeros(nbins)
for i in range(nbins) : xv[i] = (i+0.5)*ddd

line1 = line( xv, yv )
axislabels = [ "average magnetisation per spin", "probability density" ]

class UnitTests(unittest.TestCase) :
    def test_graph(self) :
        assert( check_plot([line1],explabels=axislabels,explegend=False,output=True) ) 
