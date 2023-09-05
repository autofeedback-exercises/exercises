try:
    from AutoFeedback.funcchecks import check_func 
except:
    import subprocess
    import sys
            
    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.funcchecks import check_func 
 
import numpy as np          
import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_variables(self) : 
        inputs, variables = [], []
        for i in range(20) :
            a = np.random.uniform(-1,1) 
            inputs.append((a,))
            if a<0 : variables.append( -a )
            else : variables.append( a )
        assert( check_func('modulo', inputs, variables ) )
