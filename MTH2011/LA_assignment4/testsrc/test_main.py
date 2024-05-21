import AutoFeedback.varchecks as vc
import unittest
import sympy as sy

x,y,z,alpha = sy.symbols("x,y,z,alpha")

class UnitTests(unittest.TestCase) :
    def test_q1_M(self):
        assert(vc.check_vars('q1_M',sy.Matrix([[5,3,4,1], [1,2,2,6],[4,0,1,4]])))

    def test_q1_rref(self):
        assert(vc.check_vars('q1_rref',(sy.Matrix([ [1, 0, 0,  24], [0, 1, 0, 83], [0, 0, 1, -92]]), (0, 1, 2))))

    def test_q1_rank(self):
        assert(vc.check_vars('q1_rank',3))

    def test_q2_rref(self):
        assert(vc.check_vars('q2_rref',(sy.Matrix([ [1, 0, 0, 0, -1], [0, 1, 0, 0,  2], [0, 0, 1, 0,  1], [0, 0, 0, 1, -1]]), (0, 1, 2, 3))))

    def test_q2_rank(self):
        assert(vc.check_vars('q2_rank',4))

    def test_q3_E0(self):
        assert(vc.check_vars('q3_E0',x+y+z-2))

    def test_q3_E1(self):
        assert(vc.check_vars('q3_E1',x+alpha*y+2*alpha*z-1))

    def test_q3_E2(self):
        assert(vc.check_vars('q3_E2',x+y+alpha**2*z-alpha-3))

    def test_q3_E2(self):
        assert(vc.check_vars('q3_E2',x+y+alpha**2*z-alpha-3))

    def test_q3_1(self):
        assert(vc.check_vars('q3_1',[]))

    def test_q3_m1(self):
        assert(vc.check_vars('q3_m1',{y: sy.Rational(1,2) - 3*z/2, x: z/2 + sy.Rational(3,2)}))

    def test_q3_2(self):
        assert(vc.check_vars('q3_2',{x: 5, y: -4, z: 1}))
