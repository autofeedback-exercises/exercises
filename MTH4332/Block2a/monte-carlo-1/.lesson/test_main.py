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
    def test_function(self) :
        inputs, outputs = [], []
        for i in range(100) :
           x = np.random.uniform(0,1)
           y = np.random.uniform(0,1) 
           inputs.append((x,y,))
           outputs.append( ((x*x+y*y)<1) )
        assert( check_func("incircle", inputs, outputs ) )
