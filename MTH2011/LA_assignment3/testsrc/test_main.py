import AutoFeedback.varchecks as vc

import unittest
import sympy as sp

a,b,c,d=sp.symbols("a,b,c,d")
w,x,y,z=sp.symbols("w,x,y,z")

class UnitTests(unittest.TestCase) :
    def test_m0(self):
        assert(vc.check_vars('m0',sp.Matrix([[1,0],[0,1]])))

    def test_m1(self):
        assert(vc.check_vars('m1',sp.Matrix([[1,0],[0,-1]])))

    def test_m2(self):
        assert(vc.check_vars('m2',sp.Matrix([[0,1],[1,0]])))

    def test_m3(self):
        assert(vc.check_vars('m3',sp.Matrix([[0,1],[-1,0]])))

    def test_q1(self):
        assert(vc.check_vars('q1',{w: a/2 + d/2, x: a/2 - d/2, y: b/2 + c/2, z: b/2 - c/2}))

    def test_v0(self):
        assert(vc.check_vars('v0',sp.Matrix([1,2,0,0])))

    def test_v1(self):
        assert(vc.check_vars('v1',sp.Matrix([0,-1,1,1])))

    def test_v2(self):
        assert(vc.check_vars('v2',sp.Matrix([2,0,1,-1])))

    def test_q2(self):
        assert(vc.check_vars('q2',{a: 0, b: 0, c: 0}))
