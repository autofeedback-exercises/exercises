import AutoFeedback.varchecks as vc
import unittest
import pytest
import sys

class UnitTests(unittest.TestCase) :
    def test_output(self):
        exp = """2 4 8
4 16 64
6 36 216
8 64 512
10 100 1000
"""
        if any(["kernel_launcher.py" in f for f in sys.argv]):
            assert(vc.check_vars("output", exp))
        else:
            assert(vc.check_output("2 4 8\\n4 16 64\\n6 36 216\\n8 64 512\\n10 100 1000"))
