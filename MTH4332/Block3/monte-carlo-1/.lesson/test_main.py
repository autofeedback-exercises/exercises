try:           
    from AutoFeedback.plotchecks import check_plot
except:
    import subprocess
    import sys
            
    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.plotchecks import check_plot
                
from AutoFeedback.plotclass import line
from AutoFeedback.randomclass import randomvar
import numpy as np   
import unittest      
from main import *

xv = np.linspace( 1, nframes, nframes )
yv = randomvar( 0, variance=temp/2, isinteger=False )
line1 = line( xv, yv )
axislabels = [ "index", "particle position" ]

class UnitTests(unittest.TestCase) :
    def test_graph(self) :
        assert( check_plot([line1],explabels=axislabels,explegend=False,output=True) ) 
