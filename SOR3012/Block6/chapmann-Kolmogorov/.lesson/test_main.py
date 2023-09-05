try:
    from AutoFeedback.varchecks import check_vars
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.varchecks import check_vars

import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_vals(self) :
        myA = np.array([[0.3,0.5,0.2],[0.3,0.4,0.3],[0.2,0.5,0.3]])
        assert(check_vars("A",myA)) 
        assert(check_vars("A2",np.linalg.matrix_power(myA,2)))
        assert(check_vars("A10",np.linalg.matrix_power(myA,10)))
        assert(check_vars("A50",np.linalg.matrix_power(myA,50)))
        assert(check_vars("A100",np.linalg.matrix_power(myA,100)))
