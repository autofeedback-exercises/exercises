import AutoFeedback.varchecks as vc
import unittest
import sympy as sy


class UnitTests(unittest.TestCase) :
    def test_q1_T(self):
        assert(vc.check_vars('T',sy.Matrix([[1,-1,1,0],[0,0,-1,1],[0,1,-1,1]])))

    def test_q1_kerT(self):
        assert(vc.check_vars('kerT',[sy.Matrix([ [-1], [ 0], [ 1], [ 1]])]))

    def test_q1_imT(self):
        assert(vc.check_vars('imT',[sy.Matrix([ [1], [0], [0]]), sy.Matrix([ [-1], [ 0], [ 1]]), sy.Matrix([ [ 1], [-1], [-1]])]))

    def test_q1_rankT(self):
        assert(vc.check_vars('rankT',3))
    
    def test_q2_L(self):
        assert(vc.check_vars('L', sy.Matrix([[0,1,0],[1,0,1],[0,1,1]])))

    def test_q2_R(self):
        assert(vc.check_vars('R', sy.Matrix([[2,1,0],[1,2,2],[1,0,2]])))

    def test_q2_M(self):
        assert(vc.check_vars('M', sy.Matrix([[2, 3, 0], [2, 1, 0], [-1, -1, 2]])))
