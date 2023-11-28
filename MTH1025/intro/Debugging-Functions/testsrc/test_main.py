import AutoFeedback.funcchecks as fc
import unittest


class UnitTests(unittest.TestCase) :
    def test_fivetimes(self):
        assert(fc.check_func('fivetimes',[(1,),(0,),(-3,)],[5,0,-15],calls=['double','triple']))

    def test_triple(self):
        assert(fc.check_func('triple',[(1,),(-7,),(0,)],[3,-21,0]))

    def test_compound(self):
        assert(fc.check_func('double',[(1,),(-4,),(0,)],[2,-8,0]))
