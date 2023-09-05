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
   def test_nservers(self):
      assert( vc.check_vars("qn.edge2queue[0].num_servers",3) )
