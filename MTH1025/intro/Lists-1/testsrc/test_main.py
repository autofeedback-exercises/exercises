try:
    from AutoFeedback import funcchecks as fc
except ModuleNotFoundError:

    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip",
                           "install", "AutoFeedback"])
    from AutoFeedback import funcchecks as fc

import unittest


class UnitTests(unittest.TestCase):
    def test_remove(self):
        inputs = [(["this", "and", "that"], 1), (["this", "and", "that"], 4)]
        outputs = [["this", "and"], ["this", "and", "that"]]
        assert(fc.check_func('truncateList', inputs, outputs))

    def test_add(self):
        inputs = [(["this", "and"], "that"), ([], 1)]
        assert(fc.check_func('addToList', inputs,
                             [["this", "and", "that"], [1]]))
