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
    def test_rising(self) :
        inputs, variables = [], []
        for i in range(6,21) :
            for j in range(3,5) :
                inputs.append((i,j))
                spins = np.zeros(i)
                for k in range(i) : spins[k] = k%j 
                variables.append( spins )
        assert( check_func('rising_states',inputs, variables ) )         
   
    def test_lowering(self) :
        inputs, variables = [], []
        for i in range(6,21) :
            for j in range(3,5) :
                inputs.append((i,j))
                spins = np.zeros(i)
                for k in range(i) : spins[k] = j - 1 - k%j 
                variables.append( spins )
        assert( check_func('lowering_states',inputs, variables ) )
        
    def test_updown(self) :
        inputs, variables = [], []
        for i in range(6,21) :
            for j in range(3,5) :
                inputs.append((i,j))
                spins = np.zeros(i)
                for k in range(i) :
                    kb = np.floor( k / j )
                    if kb%2==0 : spins[k] = k%j
                    else : spins[k] = j - 1 - k%j 
                variables.append( spins )
        assert( check_func('updown_states',inputs, variables ) )
