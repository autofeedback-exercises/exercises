try:
    from AutoFeedback.plotchecks import check_plot
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.plotchecks import check_plot

from AutoFeedback.varchecks import check_vars
from AutoFeedback.plotclass import line
from AutoFeedback.funcchecks import check_func
from AutoFeedback.randomclass import randomvar
import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_dice(self) : 
        inputs, variables = [], []
        for i in range(10) :
            inputs.append(())
            myvar = randomvar( 3.5, variance=35/12, vmin=1, vmax=6, isinteger=True )
            variables.append( myvar ) 
        assert( check_func("dice_roll",inputs, variables ) ) 

    def test_histo(self) :
        inputs, variables = [], []
        for i in range(1,5) : 
            inputs.append((i*100,))
            myvar = randomvar( 1/6, variance=(1/6)*(5/6)/(i*100), vmin=0, vmax=1, isinteger=False )
            variables.append( myvar )
        assert( check_func("histo_estimate", inputs, variables, calls=["dice_roll"] ) )      

    def test_lower(self) :
        probs, isi = 1/6*np.ones(6), [False,False,False,False,False,False]
        myvar = randomvar( probs, dist="chi2", variance=probs*(1-probs)/nsamples, dof=nsamples-1, limit=0.9, isinteger=isi)
        assert( check_vars("lower", myvar) ) 

    def test_upper(self) :
        probs, isi = 1/6*np.ones(6), [False,False,False,False,False,False]
        myvar = randomvar( probs, dist="chi2", variance=probs*(1-probs)/nsamples, dof=nsamples-1, limit=0.9, isinteger=isi)
        assert( check_vars("upper", myvar) )  

    def test_plot(self) :
        probs, x, isi = 1/6*np.ones(6), np.linspace(1,6,6), [False,False,False,False,False,False]
        var = randomvar( probs, variance=probs*(1-probs)/nsamples, vmin=[0,0,0,0,0,0], vmax=[1,1,1,1,1,1], isinteger=isi )
        line1=line( x, var )
        axislabels=["Outcome", "Fraction of occurances"] 
        assert(check_plot([line1],exppatch=line1,explabels=axislabels,explegend=False,output=True))
