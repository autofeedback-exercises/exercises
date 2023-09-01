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
    def test_mag(self) : 
        inputs, outputs = [], []
        for N in range(3,8) : 
            for h in [-2,-1,1,2] :
                for k in range(10) : 
                    spins = np.ones([N,N])
                    for i in range(N) :
                        for j in range(N) :
                            if np.random.uniform(0,1)<0.5 : spins[i,j] = -1.
                    inputs.append((spins,h))
                    outputs.append( -h*sum(sum(spins)) )
        assert( check_func("hamiltonian", inputs, outputs ) )
