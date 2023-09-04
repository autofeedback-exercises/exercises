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

def genSpins(N) :
    spins = np.ones([N,N])
    for i in range(N) : 
        for j in range(N) : 
            if np.random.uniform(0,1)<0.5 : spins[i,j] = -1

class UnitTests(unittest.TestCase) :
    def test_flipSpin(self) : 
        inputs, outputs = [], []
        for N in range(3,8) : 
            spins = genSpins( N )
            for j in range(30) : 
                ispin = int(np.floor( N*np.random.uniform(0,1) ) )
                jspin = int(np.floor( N*np.random.uniform(0,1) ) )
                inputs.append((spins,ispin,jspin,))
                spins[ispin,jspin] = -1*spins[ispin,jspin]
                outputs.append(spins)
        assert( check_func("flipSpin", inputs, outputs ) )

    def test_flipAllSpins(self) : 
        inputs, outputs = [], []
        for N in range(3,8) :
            for k in range(3) :
                spins = genSpins( N ) 
                for j in range(2) :
                    inputs.append((spins,))
                    spins = -1*spins
                    output.append(spins) 
        assert( check_func("flipAllSpins", inputs, outputs ) )

    def test_chooseMove(self) : 
        inputs, outputs = [], []
        for N in range(3,8) :
            spins = np.ones([N,N])
            inputs.append((spins,))
            p = 1/(1+N*N)
            myvar = randomvar( p, variance=p*(1-p), vmin=0, vmax=1, isinteger=True, nsamples=100 )
            outputs.append( myvar )
        assert( check_func("chooseMove", inputs, outputs ) )

    def test_chooseSpin(self) :
        inputs, outputs = [], []
        for N in range(3,8) :
            spins = np.ones([N,N])
            inputs.append((spins,))
            myvar = randomvar( (N-1)/2, variance=(N*N-1)/12, vmin=0, vmax=N-1, isinteger=True, nsamples=100 )
            outputs.append((myvar,myvar,))
        assert( check_func("chooseMove", inputs, outputs ) )
