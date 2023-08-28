try:
    import AutoFeedback.funcchecks as fc
except:

    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    import AutoFeedback.funcchecks as fc
import unittest


class UnitTests(unittest.TestCase) :
    def test_cone(self):
        assert(fc.check_func('ispositive',[(0,),(-9,),(8,)],['zero','negative','positive']))
