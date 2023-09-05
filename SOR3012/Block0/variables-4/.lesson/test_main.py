try:
    import AutoFeedback.varchecks as vc
except: 
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    import AutoFeedback.varchecks as vc

import unittest
from main import *

class UnitTests( unittest.TestCase ): 
   def test_a1(self):
      assert( vc.check_vars("a1",3) )
   def test_b2(self):
      assert( vc.check_vars("b2",(4+5)/2 ) )
   def test_c3(self):
      assert( vc.check_vars("c3",3*(9+4) ) )
   def test_d4(self):
      assert( vc.check_vars("d4",(7+4)*5) ) 
