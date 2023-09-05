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

class UnitTests( unittest.TestCase ): 
   def test_service_func(self):
      myvar = randomvar( 2, variance=4, nsamples=4 )
      assert( check_func( "st_func", [(0,)], [myvar] ) )
