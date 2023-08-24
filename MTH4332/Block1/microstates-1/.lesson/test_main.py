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
    def test_alternating(self) :
        alt = np.ones(nspins)
        for i in range(nspins) :
            if i%2==0 : alt[i] = -1
        assert( vc.check_vars("alternating", alt ) ) 
            
    def test_spinDown(self) :
        assert( vc.check_vars("alldown", -1*np.ones(nspins) ) )
        
    def test_spinUp(self) :
        assert( vc.check_vars("allup", np.ones(nspins) ) )
