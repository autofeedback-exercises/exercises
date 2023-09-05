try:
    from AutoFeedback.funcchecks import check_func 
except:
    import subprocess
    import sys
            
    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.funcchecks import check_func 
           
from AutoFeedback.randomclass import randomvar
import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_mean(self) : 
        inputs, variables = [], []
        for i in range(1,9) :
            p = i*0.1
            inputs.append((i*0.1,))
            myvar = randomvar( p, variance=p*(1-p), vmin=0, vmax=1, isinteger=True, nsamples=100 )
            variables.append( myvar )
        assert( check_func('bernoulli',inputs, variables ) )
