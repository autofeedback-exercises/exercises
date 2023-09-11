try:
    from AutoFeedback.funcchecks import check_func 
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.funcchecks import check_func

import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_hamiltonian(self) : 
        inputs, outputs = [], []
        for N in range(3,8) : 
            for h in [-2,-1,1,2] :
                for k in range(10) : 
                    spins = np.ones([N,N])
                    for i in range(N) :
                        for j in range(N) :
                            if np.random.uniform(0,1)<0.5 : spins[i,j] = -1.
                    inputs.append((spins,h))
                    Ene = 0 
                    for i in range(N) :
                        for j in range(N) :
                            Ene = Ene + spins[i,j]*( spins[ (i+1)%N, j] + spins[ i, (j+1)%N] + spins[(i-1)%N, j] + spins[ i, (j-1)%N] )
                    outputs.append( - Ene / 2 - h*sum( sum( spins ) )  )
        assert( check_func("hamiltonian", inputs, outputs ) )

    def test_move(self) : 
        inputs, outputs = [], []
        for N in range(10,15) :
            for h in [-2,-1,0,1,2] :
                spins = np.ones([N,N])
                for i in range(N) :
                        for j in range(N) :
                            if np.random.uniform(0,1)<0.5 : spins[i,j] = -1.
                e = hamiltonian(spins,h)
                inputs.append((np.copy(spins),e,h,N*N,))
                spins = -1*spins
                e = hamiltonian(spins,h)
                outputs.append(e)
                for i in range(10) : 
                    rmove = int( np.floor( N*N*np.random.uniform(0,1) ) )
                    inputs.append((np.copy(spins),e,h,rmove,))
                    i, j = int( np.floor( rmove / N ) ), rmove%N
                    spins[i,j] = -1*spins[i,j]
                    e = hamiltonian(spins,h)
                    outputs.append(e)
        assert( check_func("new_energy", inputs, outputs ) )    
