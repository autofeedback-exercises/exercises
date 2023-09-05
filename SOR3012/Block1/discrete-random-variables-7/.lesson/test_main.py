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
    def test_variables(self) : 
        inputs, variables = [], []
        for i in range(1,9) :
            p = i*0.1
            inputs.append((p,))
            myvar = randomvar( 1/p, variance=(1-p)/(p*p), vmin=1, isinteger=True, nsamples=100 )
            variables.append( myvar )
        assert( check_func('geometric', inputs, variables, calls=['bernoulli'] ) )
