from AutoFeedback.funcchecks import check_func
from AutoFeedback.plotchecks import check_plot
from AutoFeedback.plotclass import line
from AutoFeedback.utils import get_internal as get
from AutoFeedback.randomclass import randomvar
import scipy.stats
import numpy as np
import unittest

class UnitTests(unittest.TestCase):
      def test_ex1(self):
        inputs, output = [], []
        for mu in range(-3,3,7) :
            for sig in range(1, 4, 3 ) :   
                for n in range(10,200,19) :
                    sample = np.random.normal( mu, sig, size=n ) 
                    inputs.append((sample,) )
                    mean, mean2 = np.mean(sample), np.mean(sample*sample)
                    var = (n/(n-1))*( mean2 - mean*mean )
                    output.append((mean,var,) )
        assert( check_func("sample_mean_and_var",inputs,output) )

      def test_ex2(self) :
        inputs, output = [], []
        for mu in range(-3,3,7) :
            for sig in range(1, 4, 3 ) :
                for n in range(10,200,19) :
                    sample = np.random.normal( mu, sig, size=n )
                    inputs.append((sample, mu,))
                    mean, mean2 = np.mean(sample), np.mean(sample*sample)
                    var = (n/(n-1))*( mean2 - mean*mean ) 
                    output.append( (mean-mu) / np.sqrt(var/n)  )
        assert( check_func("teststat",inputs,output) )

      def test_ex3a(self) :
        inputs, output = [], []
        for mu in range(-3,3,7) :
            for sig in range(1, 4, 3 ) :
                for n in range(10,200,19) :
                    sample = np.random.normal( mu, sig, size=n )
                    inputs.append((sample, mu,))
                    mean, mean2 = np.mean(sample), np.mean(sample*sample)
                    var = (n/(n-1))*( mean2 - mean*mean )
                    teststat = (mean-mu) / np.sqrt(var/n)
                    output.append( scipy.stats.t.cdf(teststat,n-1)  )
        assert( check_func("pval_lower",inputs,output) )
        
      def test_ex3b(self) :
        inputs, output = [], [] 
        for mu in range(-3,3,7) :
            for sig in range(1, 4, 3 ) :
                for n in range(10,200,19) : 
                    sample = np.random.normal( mu, sig, size=n )
                    inputs.append((sample, mu,))
                    mean, mean2 = np.mean(sample), np.mean(sample*sample)
                    var = (n/(n-1))*( mean2 - mean*mean )
                    teststat = (mean-mu) / np.sqrt(var/n)
                    output.append( scipy.stats.t.cdf(-teststat,n-1) + (1-scipy.stats.t.cdf(teststat,n-1))  )
        assert( check_func("pval_not",inputs,output) )
        
      def test_ex3c(self) : 
        inputs, output = [], []
        for mu in range(-3,3,7) :
            for sig in range(1, 4, 3 ) :
                for n in range(10,200,19) :
                    sample = np.random.normal( mu, sig, size=n )
                    inputs.append((sample, mu,))
                    mean, mean2 = np.mean(sample), np.mean(sample*sample)
                    var = (n/(n-1))*( mean2 - mean*mean )
                    teststat = (mean-mu) / np.sqrt(var/n)
                    output.append( 1-scipy.stats.t.cdf(teststat,n-1)  )
        assert( check_func("pval_higher",inputs,output) )
