import AutoFeedback.varchecks as vc
import unittest
import sympy as sy

class UnitTests(unittest.TestCase) :
    def test_q1_A(self):
        assert(vc.check_vars('A', sy.Matrix([[1,0,0], [1,1,0], [1, 1, 1]])))

    def test_q1_Astar(self):
        assert(vc.check_vars('Astar', sy.Matrix([[1, 1, 1], [0, 1, 1], [0, 0, 1]])))

    def test_q1_hermitian(self):
        assert(vc.check_vars('Hermitian', False))

    def test_q1_normal(self):
        assert(vc.check_vars('normal', False))

    def test_q1_unitary(self):
        assert(vc.check_vars('unitary', False))

    def test_q2_B(self):
        assert(vc.check_vars('B', sy.Matrix([[1,2,0], [0,1,2], [2,0, 1]])))
    
    def test_q2_U(self):
        assert(vc.check_vars('U', sy.Matrix([[sy.sqrt(3)/3, sy.sqrt(3)*(-sy.Rational(1,2) - sy.sqrt(3)*sy.I/2)/3, sy.sqrt(3)*(-sy.Rational(1,2) + sy.sqrt(3)*sy.I/2)/3], [sy.sqrt(3)/3, sy.sqrt(3)*(-sy.Rational(1,2) + sy.sqrt(3)*sy.I/2)/3, sy.sqrt(3)*(-sy.Rational(1,2) - sy.sqrt(3)*sy.I/2)/3], [sy.sqrt(3)/3, sy.sqrt(3)/3, sy.sqrt(3)/3]])))

    def  test_q2_D(self):
        assert(vc.check_vars('D', sy.Matrix([[3, 0, 0], [0, -sy.sqrt(3)*sy.I, 0], [0, 0, sy.sqrt(3)*sy.I]])))


