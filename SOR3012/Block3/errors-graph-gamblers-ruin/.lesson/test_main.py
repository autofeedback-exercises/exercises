try:
    from AutoFeedback.plotchecks import check_plot
except:
    import subprocess
    import sys
            
    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.plotchecks import check_plot
 
from AutoFeedback.varchecks import check_vars
from AutoFeedback.funcchecks import check_func          
from AutoFeedback.randomclass import randomvar
from AutoFeedback.plotclass import line
import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_plot(self) : 
        n, s = 4, 2
        x, e, var, bmin, bmax, isi  = [], [], [], [], [], []
        for sp in range(3,8) : 
            x.append( sp*0.1 )
            rat = (1-sp*0.1) / (sp*0.1)
            if( sp==5 ) : prob = ( n - s ) / n
            else : prob = ( rat**s - rat**n ) / ( 1 - rat**n ) 
            e.append( prob )
            var.append( prob*(1-prob) / 200 )
            bmin.append(0)
            bmax.append(1)
            isi.append(False)

        val = randomvar( e, variance=var, vmin=bmin, vmax=bmax, isinteger=isi )
        line1=line( x, val )
        axislabels=["Probability of winning each game", "Probability of ruin"]
        assert(check_plot([line1],explabels=axislabels,explegend=False,output=True))

    def test_errors(self) :
        n, s, prob = 4, 2, np.zeros(5)
        for sp in range(3,8) :
            rat = (1-sp*0.1) / (sp*0.1)
            if( sp==5 ) : prob[sp-3] = ( n - s ) / n
            else : prob[sp-3] = ( rat**s - rat**n ) / ( 1 - rat**n )
        myvar = randomvar( prob, variance=prob*(1-prob)/200,  dist="chi2", dof=199, limit=0.9, isinteger=[False,False,False,False,False] )
        assert( check_vars("error", myvar) )
