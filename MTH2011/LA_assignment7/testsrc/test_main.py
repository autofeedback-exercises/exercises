import AutoFeedback.varchecks as vc
import unittest
import sympy as sy

class UnitTests(unittest.TestCase) :
    def test_V(self):
        assert(vc.check_vars('V',[sy.Matrix([1,2,1]),sy.Matrix([1,1,1])]))

    def test_basis(self):
        assert(vc.check_vars('basis',[sy.Matrix([[sy.sqrt(6)/6],[sy.sqrt(6)/3],[sy.sqrt(6)/6]]), sy.Matrix([[ sy.sqrt(3)/3],[-sy.sqrt(3)/3],[ sy.sqrt(3)/3]])]))
    
    def test_z(self):
        assert(vc.check_vars('z',sy.Matrix([2,2,2])))

    def test_coeff(self):
        a,b=sy.symbols("a,b")
        assert(vc.check_vars('coeff',{a: 4*sy.sqrt(6)/3, b: 2*sy.sqrt(3)/3}))


