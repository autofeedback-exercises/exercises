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
        for i in range(20) :
            val = np.random.randint(0,63)
            inputs.append((val,))
            oval = np.zeros(6)
            for j in range(6) : 
                ppp = 2**(5-j)
                oval[j] = int(np.floor( val / ppp ) )
                val = val - oval[j]*ppp
            outputs.append( oval )
        assert( fc.check_func('getBinary', inputs, outputs ) ) 
