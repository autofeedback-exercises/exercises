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
   def test_rate_func(self):
      xv, yv = [], [] 
      for i in range(1200) :
          xv.append((i,))
          yv.append( (1/6)*np.cos( 2*np.pi * (i-30) / 180 ) + 1/3 ) 
      assert( check_func( "rate", xv, yv ) )
