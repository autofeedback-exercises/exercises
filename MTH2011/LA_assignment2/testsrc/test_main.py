import AutoFeedback.varchecks as vc
import unittest
import sympy as sy

a,b,c,r = sy.symbols('a,b,c,r')

class UnitTests(unittest.TestCase) :
    def test_q1_A(self):
        assert(vc.check_vars('q1_A',sy.Matrix([[1,-2,0],[2,-3,1],[1,1,5]])))

    def test_q1_L(self):
        assert(vc.check_vars('q1_L',sy.Matrix([[1,0,0],[2,1,0],[1,3,1]])))

    def test_q1_U(self):
        assert(vc.check_vars('q1_U',sy.Matrix([[1,-2,0],[0,1,1],[0,0,2]])))

    def test_q1_inv(self):
        assert(vc.check_vars('q1_inv',sy.Rational(1,2)*sy.Matrix([[-16,10,-2],[-9,5,-1],[5,-3,1]])))

    def test_q1_inv(self):
        assert(vc.check_vars('q1_inv',sy.Rational(1,2)*sy.Matrix([[-16,10,-2],[-9,5,-1],[5,-3,1]])))

    def test_q1_det(self):
        assert(vc.check_vars('q1_det',sy.sympify(2)))

    def test_q2_B(self):
        assert(vc.check_vars('q2_B',sy.Matrix([[a-b-c,2*a,2*a],[2*b,b-c-a,2*b],[2*c,2*c,c-a-b]])))

    def test_q2_det(self):
        assert(vc.check_vars('q2_det',(a+b+c)**3))

    def test_q3_C(self):
        assert(vc.check_vars('q3_C',sy.Matrix([[2,5,7],[1,4,-6],[0,0,6]])))

    def test_q3_cpoly(self):
        assert(vc.check_vars('q3_cpoly',sy.PurePoly(r**3 - 12*r**2 + 39*r - 18, r, domain='ZZ')))

