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
    def test_lam(self) :
        inputs, var = [], []
        for j in range(1,5) : 
           lam=j
           inputs.append((lam,))
           myvar1 = randomvar( 1/lam, variance=1/(lam*lam), vmin=0, isinteger=False, nsamples=100 )
           var.append(myvar1)
        assert( check_func("exponential", inputs, var) )
