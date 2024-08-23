import AutoFeedback.funcchecks as fc
from AutoFeedback.randomclass import randomvar
from AutoFeedback.utils import get_internal as get

import unittest
import numpy as np


class UnitTests(unittest.TestCase):
    def test_init(self):
        try:
            epi = get("estimate_pi")
            epi(10)
            assert(type(epi(10)) is float)
        except (ImportError, TypeError, AssertionError):
            assert(fc.check_func('estimate_pi', inputs=[(1000,)],
                                 expected=['a floating point number']))

    def test_out(self):
        epi = get("estimate_pi")

        boundscount = 0
        for __ in range(20):
            lims = []
            failcount = 0
            for N in [(100, 2.52, 3.72), (1000, 2.93, 3.36)]:
                lo = 3.14159
                hi = 3.14159
                for _ in range(10):
                    val = epi(N[0])
                    lo = min(lo, val)
                    hi = max(hi, val)
                    if (N[1] > val or val > N[2]):
                        failcount += 1
                lims.append((lo, hi))

            if (failcount > 1):
                from AutoFeedback.bcolors import bcolors as b
                print(
                    f"""{b.FAIL}The function does not return the expected values for pi\n
Try executing\n
        print(estimate_pi(N))\n
with diffrent values of N and ensure the returned values are close to 3.14\n{b.ENDC}""")
                print(f"{b.WARNING}{30*'='}\n{b.ENDC}")
                assert(False)
            if (lims[0][0] > lims[1][0] or lims[0][1] < lims[1][1]):
                boundscount += 1

        if boundscount > 4:
            from AutoFeedback.bcolors import bcolors as b
            print(f"""{b.FAIL}The function does not give improved answers for larger N:
ensure you are using the input variable N to compute your estimate of pi\n{b.ENDC}""")
            print(f"{b.WARNING}{30*'='}\n{b.ENDC}")
            assert(False)
        else:
            from AutoFeedback.bcolors import bcolors as b
            print(f"{b.OKGREEN}The function works as expected!\n{b.ENDC}")
            print(f"{b.WARNING}{30*'='}\n{b.ENDC}")
            assert(True)




