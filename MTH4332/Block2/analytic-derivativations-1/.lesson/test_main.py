try:
    from AutoFeedback import check_vars
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback import check_vars

import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_cv( self ) :
        assert( check_vars( "CV", sy.Rational(3,4) ) ) 
