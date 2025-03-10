from AutoFeedback check_vars
import unittest


class UnitTests(unittest.TestCase) :
    def test_q1(self):
        assert(check_vars('q1',(16888/1295)))

    def test_q2(self):
        assert(check_vars('q2',8.097694013879094))

    def test_q3(self):
        assert(check_vars('q3',0.5))

    def test_q4(self):
        assert(check_vars('q4',1.0))

    def test_q5(self):
        assert(check_vars('q5',148.4131591025766))
    
    def test_q6(self):
        assert(check_vars('q6',3.0))
