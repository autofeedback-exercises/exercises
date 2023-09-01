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
    def test_hamiltonian(self) : 
        inputs, outputs = [], []
        for N in range(3,8) : 
            for k in range(10) : 
                spins = np.ones([N,N])
                for i in range(N) :
                    for j in range(N) :
                        if np.random.uniform(0,1)<0.5 : spins[i,j] = -1.
                inputs.append((spins,))
                Ene = 0 
                for i in range(N) :
                    for j in range(N) :
                        Ene = Ene + spins[i,j]*( spins[ (i+1)%N, j] + spins[ i, (j+1)%N] + spins[(i-1)%N, j] + spins[ i, (j-1)%N] )
                outputs.append( Ene / 2 )
        assert( check_func("hamiltonian", inputs, outputs ) )
