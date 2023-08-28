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
        for b in range(2,11) :
            for i in range(20) :
                val = np.random.randint(0,127)
                inputs.append((val,b,))
                outval = np.zeros(7)
                for j in range(7) : 
                    ppp = b**(6-j)
                    outval[j] = int(np.floor( val / ppp ) )
                    val = val - outval[j]*ppp
                outputs.append( outval )
        assert( fc.check_func('convertToBase', inputs, outputs ) )
