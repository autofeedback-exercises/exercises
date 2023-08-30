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
    def test_energy(self) : 
        inputs, outputs, xvals = [], [], np.linspace(-4,4,400)
        for x in xvals : 
            inputs.append((x,))
            outputs.append(x*x/2)
        assert( check_func('potential', inputs, outputs ) ) 
