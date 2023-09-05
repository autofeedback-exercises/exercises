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
            a, b = np.random.uniform(0,1), np.random.uniform(0,1)
            inputs.append((a,b,))
            variables.append( a*b )
        assert( check_func('multiply',inputs, variables ) )
