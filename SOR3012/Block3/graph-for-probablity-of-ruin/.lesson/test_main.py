try:
    from AutoFeedback.plotchecks import check_plot
except:
    import subprocess
    import sys
            
    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.plotchecks import check_plot
           
from AutoFeedback.randomclass import randomvar
from AutoFeedback.plotclass import line
import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_plot(self) : 
        n, p = 10, 0.4
        rat = (1-p)/p
        x, e, var, bmin, bmax, isi  = [], [], [], [], [], []
        for s in range(1,10) : 
            x.append( s ) 
            prob = ( rat**s - rat**n ) / ( 1 - rat**n )
            e.append( prob )
            var.append( prob*(1-prob) / 200 )
            bmin.append(0)
            bmax.append(1)
            isi.append(False)

        val = randomvar( e, variance=var, vmin=bmin, vmax=bmax, isinteger=isi )
        line1=line( x, val )
        axislabels=["start point", "probability of ruin"]
        assert(check_plot([line1],explabels=axislabels,explegend=False,output=True))
