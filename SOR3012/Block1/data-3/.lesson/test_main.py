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
   def test_N(self) : 
      myx = np.loadtxt("data.dat")
      assert( vc.check_vars("N",len(myx)) )

   def test_L(self) : 
      myx = np.loadtxt("data.dat")
      assert( vc.check_vars("L",min(myx)) )

   def test_U(self) : 
      myx = np.loadtxt("data.dat")
      assert( vc.check_vars("U",max(myx)) )
