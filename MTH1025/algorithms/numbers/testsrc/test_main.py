try:
    import AutoFeedback.funcchecks as fc
except ModuleNotFoundError:

    import subprocess
    import sys

    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "AutoFeedback"])
    import AutoFeedback.funcchecks as fc


import unittest
import numpy as np
from math import floor


class UnitTests(unittest.TestCase):
    def test_1_thousands(self):
        inputs, outputs = [], []
        for i in range(20):
            val = np.random.randint(1, 9999)
            inputs.append((val,))
            outputs.append(floor(val / 1000))
        assert(fc.check_func('numberOfThousands', inputs, outputs))

    def test_2_hundreds(self):
        inputs, outputs = [], []
        for i in range(20) :
            val = np.random.randint(1,9999)
            inputs.append((val,))
            nthou = floor( val / 1000)
            outputs.append( floor( (val - nthou*1000) / 100 ) ) 
        assert( fc.check_func('numberOfHundreds', inputs, outputs ) )

    def test_3_tens(self):
        inputs, outputs = [], []
        for i in range(20) :
            val = np.random.randint(1,9999)
            inputs.append((val,))
            nhun = floor( val / 100)
            outputs.append( floor( (val - nhun*100) / 10 ) ) 
        assert( fc.check_func('numberOfTens', inputs, outputs ) )

    def test_4_units(self):
        inputs, outputs = [], []
        for i in range(20) :
            val = np.random.randint(1,9999)
            inputs.append((val,))
            nten = floor( val / 10)
            outputs.append( floor( (val - nten*10) ) ) 
        assert( fc.check_func('numberOfOnes', inputs, outputs ) )


    def test_decompose(self):
        inputs, outputs = [], []
        for i in range(20):
            val = np.random.randint(1, 9999)
            inputs.append((val,))
            n1000 = floor(val/1000)
            n100 = floor((val-1000*n1000)/100)
            n10 = floor((val-100*n100-1000*n1000)/10)
            n1 = floor((val-10*n10-100*n100-1000*n1000)/1)
            outputs.append([n1000, n100, n10, n1])
        assert(fc.check_func('decompose', inputs, outputs))


    def test_1_decimal1(self):
        inputs, outputs = [], []
        for i in range(20):
            val = np.random.randint(1, 9999)
            inputs.append((val, 4, 10))
            n1000 = floor(val/1000)
            n100 = floor((val-1000*n1000)/100)
            n10 = floor((val-100*n100-1000*n1000)/10)
            n1 = floor((val-10*n10-100*n100-1000*n1000)/1)
            outputs.append([n1000, n100, n10, n1])
        assert(fc.check_func('decompose', inputs, outputs))

    def test_2_decimal6(self):
        assert(fc.check_func('decompose', [(128319, 6, 10), (123, 6, 10)],
                             [[1, 2, 8, 3, 1, 9], [0, 0, 0, 1, 2, 3]]))

    def test_3_binary(self):
        assert(fc.check_func('decompose', [(255, 8, 2), (21, 6, 2)],
                             [[1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1]]))

    def test_4_arbitrary(self):
        inputs = [(277, 9, 7), (312, 4, 11), (222, 13, 3)]
        outputs = [[0, 0, 0, 0, 0, 0, 5, 4, 4],
                   [0, 2, 6, 4],
                   [0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 2, 0]]
        assert(fc.check_func('decompose', inputs, outputs))
