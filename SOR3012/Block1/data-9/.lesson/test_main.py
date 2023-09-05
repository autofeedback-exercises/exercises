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
    def test_dmin(self) : 
        myx = np.loadtxt("data.dat")
        assert( vc.check_vars("dmin",min(myx)) )

    def test_lowq(self) : 
        myx = np.loadtxt("data.dat")
        assert( vc.check_vars("lowq",np.percentile(myx,25)) )

    def test_median(self) : 
        myx = np.loadtxt("data.dat")
        assert( vc.check_vars("median",np.percentile(myx,50)) )

    def test_highq(self) : 
        myx = np.loadtxt("data.dat")
        assert( vc.check_vars("highq",np.percentile(myx,75)) )

    def test_dmax(self) : 
        myx = np.loadtxt("data.dat")
        assert( vc.check_vars("dmax",max(myx)) )
