try:
    from AutoFeedback import funcchecks as fc
except ModuleNotFoundError:

    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip",
                           "install", "AutoFeedback"])
    from AutoFeedback import funcchecks as fc

import unittest
import numpy as np


class UnitTests(unittest.TestCase):
    def test_separate(self):
        inputs, outputs = [([1, 2],)], [[[2], [1]]]
        for i in range(20):
            val = np.random.randint(1, 9999, size=np.random.randint(10, 100))
            opeven = [x for x in val if (x % 2) == 0]
            opodd = [x for x in val if (x % 2) == 1]
            inputs.append((val,))
            outputs.append([opeven, opodd])
        assert(fc.check_func('separateEvenOdd', inputs, outputs))
