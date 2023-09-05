try:
    import AutoFeedback.varchecks as vc
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    import AutoFeedback.varchecks as vc

import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_arrayValues(self) :
       xv = np.loadtxt("mydata.dat")
       yv = (xv==5)
       assert( vc.check_vars( "yvals", yv ) )
