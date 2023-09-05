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
          vv = i - np.floor( i / 600 )*600
          if vv<60 : yv.append(0.5)
          elif vv<180 : yv.append(1/6)
          elif vv<240 : yv.append(0.5)
          elif vv<360 : yv.append(1/6) 
          elif vv<420 : yv.append(0.5)
          elif vv<540 : yv.append(1/6)
          else : yv.append(0.5)
      assert( check_func( "rate", xv, yv ) )
