try:
    import AutoFeedback.funcchecks as fc
except ModuleNotFoundError:

    import subprocess
    import sys

    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "AutoFeedback"])
    import AutoFeedback.funcchecks as fc

from AutoFeedback.bcolors import bcolors
import unittest
import numpy as np

def primeFactors(n):
    val, d = n, []
    for p in [x for x in range(2, n+1)
              if (all(x % i for i in range(2, int(x ** 0.5) + 1)))]:
        while (val % p == 0):
            d.append(p); val /= p
    return d


class UnitTests(unittest.TestCase):
    def test_isPrime(self):
        inputs, outputs = [(1,), (2,), (3,)], [False, True, True]
        for i in range(20):
            n = np.random.randint(3, 9999)
            inputs.append((n,))
            outputs.append(n > 1 and all(n % i for i in
                                         range(2, int(n ** 0.5) + 1)))
        assert(fc.check_func('isPrime', inputs, outputs))


    def test_primeList(self):
        inputs, outputs = [(3,), (8,)], [[2, 3], [2, 3, 5, 7]]
        for i in range(20):
            n = np.random.randint(3, 1000)
            inputs.append((n,))
            outputs.append([x for x in range(2, n+1) if
                            (all(x % i for i in range(2, int(x ** 0.5) + 1)))])
        assert(fc.check_func('primeList', inputs, outputs))


    def test_primeFactors(self):
        inputs, outputs = [(2,), (3,), (4,)], [[2], [3], [2, 2]]
        for i in range(20):
            n = np.random.randint(5, 9999)
            inputs.append((n,))
            outputs.append(primeFactors(n))
        assert(fc.check_func('primeFactors', inputs, outputs))
