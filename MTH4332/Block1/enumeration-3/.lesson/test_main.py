try:
    from AssCheck import funcchecks as fc
except:

    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AssCheck"])
    from AssCheck import funcchecks as fc

import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_function(self) :
        inputs, outputs = [], []  
        for n in range(4,9) :
            energies = np.zeros(2**n)
            for k in range(2**n) : 
                val = k
                for j in range(n) :
                    ppp = 2**(n-1-j)
                    coord = np.floor( val / ppp ) 
                    val = val - coord*ppp
                    if( coord==0 ) : energies[k] = energies[k] - 1
                    else :  energies[k] = energies[k] + 1
            inputs.append((n,))
            outputs.append( energies )
        assert( fc.check_func('microstate_energies', inputs, outputs ) )
