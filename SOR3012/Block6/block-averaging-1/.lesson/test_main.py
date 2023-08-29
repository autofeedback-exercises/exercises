try:
    from AutoFeedback.varchecks import check_vars
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.varchecks import check_vars

import unittest
from main import *

mye = np.loadtxt("energies")[:,1]

class UnitTests(unittest.TestCase) :
    def test_mean(self) : 
        myeng = sum( mye ) / len( eng )
        assert(check_vars("average",myeng))
