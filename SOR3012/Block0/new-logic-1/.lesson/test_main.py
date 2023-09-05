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
    def test_fx(self):
       tx = x 
       if x< 0 : tx *=-1 
       assert( vc.check_vars("fx",tx) )

    def test_fy(self):
       ty = y 
       if y< 0 : ty *=-1
       assert( vc.check_vars("fy",ty) )

    def test_fz(self):
       tz = z 
       if z< 0 : tz *=-1
       assert( vc.check_vars("fz",tz) )
