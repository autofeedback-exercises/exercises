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
        for a in range(-3,3) :
            for b in range(4,9) :
                inputs.append((a,b,))
                myvar = randomvar( (a+b)/2, variance=(b-a)*(b-a)/12, vmin=a, vmax=b, isinteger=False, nsamples=100 )
                variables.append( myvar )
        assert( check_func('uniform', inputs, variables ) )
