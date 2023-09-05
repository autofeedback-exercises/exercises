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
from scipy.stats import binom
import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_binom(self) :
        inputs, variables = [], []
        for n in range(3,6) :
            for i in range(1,9) :
                p = i*0.1
                inputs.append((n,i*0.1,))
                myvar = randomvar( n*p, variance=n*p*(1-p), vmin=0, vmax=n, isinteger=True )
                variables.append( myvar )
        assert( check_func('binomial',inputs, variables ) ) 

    def test_error(self) :
        pval, isi = binom.pmf([0,1,2,3,4,5], 5, 0.5 ), [False,False,False,False,False,False]
        myvar = randomvar( pval, dist="chi2", variance=pval*(1-pval)/nsamples, dof=nsamples-1, limit=0.9, isinteger=isi )
        assert( check_vars("error", myvar ) )  

    def test_plot(self) :
        x, e, var, bmin, bmax, isi  = [], [], [], [], [], []
        for i in range(6) :
            x.append(i)
            pval = binom.pmf(i, 5, 0.5 )
            e.append(pval)
            var.append(pval*(1-pval)/nsamples)
            bmin.append(0)
            bmax.append(1)
            isi.append(False)
        
        val = randomvar( e, variance=var, vmin=bmin, vmax=bmax, isinteger=isi )
        line1=line( x, val )
        axislabels=["Outcome", "Fraction of occurances"] 
        assert(check_plot([line1],exppatch=line1,explabels=axislabels,explegend=False,output=True))
