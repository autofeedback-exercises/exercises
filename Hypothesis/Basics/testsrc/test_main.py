from AutoFeedback.funcchecks import check_func
from AutoFeedback.plotchecks import check_plot
from AutoFeedback.plotclass import line
from AutoFeedback.utils import get_internal as get
from AutoFeedback.randomclass import randomvar
import numpy as np
import scipy.stats
import unittest

class UnitTests(unittest.TestCase):
    def test_ex1(self):
        inputs, output = [], []
        for mu in range(-3,3,7) :
            for sig in range(1, 4, 3 ) :   
                for n in range(10,200,19) :
                    sample = np.random.normal( mu, sig, size=n ) 
                    inputs.append((sample,) )
                    output.append( np.mean(sample) )
        assert( check_func("sample_mean",inputs,output) )

    def test_ex2(self) :
        xv = np.linspace(-1,1,100)
        yv = scipy.stats.norm.pdf( xv, 0, np.sqrt(1/200) )
        line1 = line( xv, yv )
        axislabels= ["Sample mean", "Probability density"]
        assert check_plot([line1], explabels=axislabels, explegend=False, output=True )

    def test_ex3(self) :
        inputs, output = [], []
        for mu in range(-3,3,7) :
            for sig in range(1, 4, 3 ) :
                for n in range(10,200,19) :
                    sample = np.random.normal( mu, sig, size=n )
                    inputs.append((sample, mu, sig,) )
                    output.append( (np.mean(sample)-mu) / np.sqrt(sig/n)  )
        assert( check_func("teststat",inputs,output) ) 

    def test_ex4a(self) :
        inputs, output = [], []
        for lev in np.linspace(0.05,0.95,19) :
            inputs.append((lev,))
            output.append( scipy.stats.norm.ppf(lev) )
        assert( check_func("critregH1a", inputs, output) ) 

    def test_ex4b(self) : 
        inputs, output = [], []
        for lev in np.linspace(0.05,0.95,19) :
            inputs.append((lev,))
            output.append((scipy.stats.norm.ppf(lev/2),scipy.stats.norm.ppf(1-lev/2),)) 
        assert( check_func("critregH1b", inputs, output) )

    def test_ex4c(self) :
        inputs, output = [], []
        for lev in np.linspace(0.05,0.95,19) :
            inputs.append((lev,))
            output.append( scipy.stats.norm.ppf(1-lev) ) 
        assert( check_func("critregH1c", inputs, output) )

    def test_ex5a(self) :
        inputs, output = [], []
        for mu in range(-3,3,7) :
            for sig in range(1, 4, 3 ) :
                for n in range(10,200,19) :
                    sample = np.random.normal( mu, sig, size=n )
                    inputs.append((sample, mu, sig,) )
                    teststat = (np.mean(sample)-mu) / np.sqrt(sig/n)
                    output.append( scipy.stats.norm.cdf(teststat)  )
        assert( check_func("pval_lower",inputs,output) )

    def test_ex5b(self) :
        inputs, output = [], []
        for mu in range(-3,3,7) :
            for sig in range(1, 4, 3 ) :
                for n in range(10,200,19) :
                    sample = np.random.normal( mu, sig, size=n )
                    inputs.append((sample, mu, sig,) )
                    teststat = np.abs( (np.mean(sample)-mu) / np.sqrt(sig/n) )
                    output.append( scipy.stats.norm.cdf(-teststat) + (1-scipy.stats.norm.cdf(teststat))  )
        assert( check_func("pval_not",inputs,output) )

    def test_ex5c(self) :
        inputs, output = [], []
        for mu in range(-3,3,7) :
            for sig in range(1, 4, 3 ) :
                for n in range(10,200,19) :
                    sample = np.random.normal( mu, sig, size=n )
                    inputs.append((sample, mu, sig,) )
                    teststat = (np.mean(sample)-mu) / np.sqrt(sig/n)
                    output.append( 1-scipy.stats.norm.cdf(teststat)  )
        assert( check_func("pval_lower",inputs,output) )

    def test_ex6(self) : 
        inputs, output = [], [] 
        for mu in range(-3,1) :
            signif, n = 0.05, 200
            inputs.append(( 100,n,0,mu,1.0,signif,))
            pval = scipy.stats.norm.cdf( scipy.stats.norm.ppf(signif) - mu/(1/np.sqrt(n)) ) 
            myvar = randomvar( pval, variance=pval*(1-pval)/10, vmin=0, vmax=1, isinteger=False )
            output.append(myvar)
        assert( check_func("false_neg_rate", inputs, output) )  
