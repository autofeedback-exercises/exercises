import AutoFeedback.varchecks as vc
import unittest
import sympy as sy



class UnitTests(unittest.TestCase) :
    def test_A(self):
        assert(vc.check_vars('A',sy.Matrix([[1,-1,-1,],[1,3,1],[-3,1,-1]])))

    def test_Epairs(self):
        assert(vc.check_vars('Epairs',[(-2, 1, [sy.Matrix([ [sy.Rational(1,4)],
                                                           [-sy.Rational(1,4)], [   1]])]), (2, 1, [sy.Matrix([ [-1], [ 0], [ 1]])]), (3, 1, [sy.Matrix([ [-1], [ 1], [ 1]])])]))

    def test_P(self):
        assert(vc.check_vars('P',sy.Matrix([[1, -1, -1], [-1, 0, 1], [4, 1, 1]])))

    def test_D(self):
        assert(vc.check_vars('D',sy.Matrix([[-2, 0, 0], [0, 2, 0], [0, 0, 3]])))


