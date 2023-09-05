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
    def test_r(self) :
       assert( vc.check_vars("r", (4+5)*(3+1/2)/(7*(10-4)) ) )

    def test_numerator(self) : 
       assert( vc.check_vars("numerator",4) )

    def test_denominator(self) : 
       assert( vc.check_vars("denominator",7*(10-4) ) )
