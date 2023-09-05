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
    def test_c3(self):
       assert( vc.check_vars("c3",4) )

    def test_e5(self):
       assert( vc.check_vars("e5",c3+5) )

    def test_b2(self):
       assert( vc.check_vars("b2",e5*c3) )

    def test_f6(self): 
       assert( vc.check_vars("f6",b2+e5) )

    def test_d4(self) :
       assert( vc.check_vars("d4",c3/f6) )

    def test_a1(self) : 
       assert( vc.check_vars("a1",( c3 + e5 ) / ( f6 + d4 ) ) )
