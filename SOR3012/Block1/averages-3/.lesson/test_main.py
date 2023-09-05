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
        for i in range(1,5) :
            inputs.append((i*10,))
            myvar = randomvar( 0.5, variance=1/12/(i*10), vmin=0, vmax=1, isinteger=False, nsamples=100 )
            variables.append( myvar )
        assert( check_func('average',inputs, variables ) )
