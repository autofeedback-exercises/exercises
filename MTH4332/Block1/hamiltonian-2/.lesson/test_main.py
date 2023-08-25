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
            for i in range(3**n) :
                num, spins, eng = i, np.zeros(n), 0
                for j in range(n) :
                    spins[j] = np.floor( num / 3**(n-1-j) )
                    num = num - spins[j]*3**(n-1-j)
                    if spins[j]==1 : eng = eng+2 
                    elif spins[j]==2 : eng = eng+3
                inputs.append((spins,))
                outputs.append( eng )
        assert( check_func('hamiltonian', inputs, outputs ) )   
