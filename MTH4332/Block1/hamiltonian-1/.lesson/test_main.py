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
    def test_eng(self) :
        inputs, outputs = [], [] 
        for n in range(3,6) : 
            for i in range(2**n) :
                num, spins = i, np.zeros(n)
                for j in range(n) :
                    spins[j] = np.floor( num / 2**(n-1-j) )
                    num = num - spins[j]*2**(n-1-j)
                    if spins[j]==0 : spins[j] = -1
                for f in range(1,4) : 
                    inputs.append((spins,f))
                    outputs.append( -f*sum(spins) )
        assert( check_func('hamiltonian', inputs, outputs ) )   
