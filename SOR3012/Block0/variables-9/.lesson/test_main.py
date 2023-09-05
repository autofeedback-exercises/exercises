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
       x=np.linspace(0,70,11)
       assert( vc.check_vars( "timesTable", x ) )

    def test_output(self) : 
       assert( vc.check_output("7\\n0.0 7.0 14.0 21.0 28.0 35.0 42.0 49.0 56.0 63.0 70.0") )
