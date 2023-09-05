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
    def test_nlefive(self) :
       xv = np.loadtxt("mydata.dat")
       assert( vc.check_vars( "nlefive", sum(xv<=5) ) )

    def test_nmtfive(self) :
       xv = np.loadtxt("mydata.dat")
       assert( vc.check_vars( "nmefive", sum(xv>=5) ) )
