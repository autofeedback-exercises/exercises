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
    def test_partition_function(self) : 
        inputs, outputs = [], []  
        for k in range(5,8) :
            pfunc1, pfunc2, pfunc3 = 0, 0, 0
            for i in range(2**k) :
                num, spins = i, np.zeros(k)
                for j in range(k) :
                    spins[j] = np.floor( num / 2**(k-1-j) )
                    num = num - spins[j]*2**(k-1-j)
                    if spins[j]==0 : spins[j] = -1
                pfunc1 = pfunc1 + np.exp( -hamiltonian( spins, 1 ) / 0.5 )
                pfunc2 = pfunc2 + np.exp( -hamiltonian( spins, 1 ) / 0.1 )
                pfunc3 = pfunc3 + np.exp( -hamiltonian( spins, 2 ) / 0.8 )
            inputs.append((k,1,0.5,))
            outputs.append( pfunc1 )
            inputs.append((k,-1,0.1,))
            outputs.append( pfunc2 )
            inputs.append((k,2,0.8,))
            outputs.append( pfunc3 )
        assert( check_func('partitionfunction', inputs, outputs ) )
            
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
