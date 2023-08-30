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
    def test_vel(self) :
        inputs, outputs = [], []
        for T in [0.5,1.0,1.5,2.0,2.5] : 
            inputs.append((T,))
            r = randomvar( 0, variance=T, isinteger=False, nsamples=100 )
            outputs.append(r)
        assert( check_func('gen_vel', inputs, outputs) ) 
