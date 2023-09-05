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
    def test_zero(self):
       assert( vc.check_vars("zeroTimes",0) )

    def test_one(self):
       assert( vc.check_vars("oneTimes",13) )

    def test_two(self):
       assert( vc.check_vars("twoTimes",2*13) )

    def test_three(self):
       assert( vc.check_vars("threeTimes",3*13) )

    def test_four(self):
       assert( vc.check_vars("fourTimes",4*13) )

    def test_five(self):
       assert( vc.check_vars("fiveTimes",5*13) )

    def test_six(self):
       assert( vc.check_vars("sixTimes",6*13) )

    def test_seven(self):
       assert( vc.check_vars("sevenTimes",7*13) )

    def test_eight(self):
       assert( vc.check_vars("eightTimes",8*13) )

    def test_nine(self):
       assert( vc.check_vars("nineTimes",9*13) )

    def test_ten(self):
       assert( vc.check_vars("tenTimes",10*13) )
