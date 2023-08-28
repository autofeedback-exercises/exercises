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
    def test_ensemble_average(self) :
        inputs, outputs = [], [] 
        for k in range(5,8) :
            Z, numer = np.zeros(9), np.zeros(9)
            for i in range(2**k) :
                num, spins = i, k*[0]
                for j in range(k) :
                   spins[j] = np.floor( num / 2**(k-1-j) )
                   num = num - spins[j]*2**(k-1-j)
                   if spins[j]==0 : spins[j] = -1
                j = 0 
                for h in range(-1,2) : 
                    eee = hamiltonian( spins, h )
                    for t in [0.5,1.0,2.0] : 
                        bweight = np.exp( -eee / t )
                        numer[j] = numer[j] + eee*bweight
                        Z[j] = Z[j] + bweight
                        j = j + 1 
            j=0
            for h in range(-1,2) : 
                for t in [0.5,1.0,2.0] :
                    inputs.append((k,h,t,)) 
                    outputs.append(numer[j]/Z[j])
                    j = j + 1
        assert( check_func('ensemble_average', inputs, outputs ) )
        
    def test_hamiltonian( self ) :
        inputs, outputs = [], []
        for k in range(5,8) :
            for i in range(2**k) :
                num, spins = i, np.zeros(k)
                for j in range(k) :
                    spins[j] = np.floor( num / 2**(k-1-j) )
                    num = num - spins[j]*2**(k-1-j)
                    if spins[j]==0 : spins[j] = -1
                sumspins = sum( spins )
                for j in range(-3,4) :
                    if j==0 : continue
                    inputs.append((spins,j,))
                    outputs.append( -j*sumspins )
        assert( check_func('hamiltonian', inputs, outputs ) )    
