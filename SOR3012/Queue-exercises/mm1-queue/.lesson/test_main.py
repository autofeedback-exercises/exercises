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
    def test_queue(self) :
        inputs, var = [], []
        for j in range(1,3) : 
           lam=0.2*j
           # Now setup the random variable 
           inputs.append((200,lam,1,))
           myvar1 = randomvar( 1/(1-lam), variance=0 )
           var.append(myvar1)
        assert( check_func("my_queue", inputs, var ) )
