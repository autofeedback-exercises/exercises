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
        for n in range(2,15) :
            inputs.append((n,))
            myvar = randomvar( 0.5, variance=1/12, dist="chi2", dof=n-1, isinteger=False )
            variables.append( myvar )
        assert( check_func('variance',inputs, variables ) )
