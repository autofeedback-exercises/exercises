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
    def test_estimate(self) : 
       inputs, outputs = [], []
       myvar = randomvar( 0, variance=1, vmin=-1, vmax=1, isinteger=True )
       for j in range(3,8) :
           inputs.append((j,))
           outputs.append( myvar )
       assert( check_func('getstate',inputs, outputs ) )
