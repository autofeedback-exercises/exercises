try:
    from AutoFeedback.funcchecks import check_func
except: 
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.funcchecks import check_func

import numpy as np
import unittest
from main import *


class UnitTests(unittest.TestCase) :
    def test_kinetic(self) :
        inputs, outputs = [], []
        for i in range(3,10) : 
            for j in range(5) :
                vel, eng = np.zeros(i), 0
                for k in range(i) :  
                    vel[k] = np.random.normal()
                    eng = eng + 0.5*vel[k]*vel[k]
                inputs.append((vel,))
                outputs.append(eng)
        assert( check_func('kinetic', inputs, outputs ) )
