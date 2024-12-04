from AutoFeedback import check_func
import unittest


class UnitTests(unittest.TestCase) :
    def test_cone(self):
        assert(check_func('cone_volume',[(0,1),(3,7),(1,0)],[0,65.97344572538566,0]))

    def test_hemi(self):
        assert(check_func('hemi_volume',[(1,),(7,),(0,)],[2.0943951023931953,718.377520120866,0]))

    def test_compound(self):
        assert(check_func('compound_volume',[(3,0),(0,1)],[56.548667764616276,0],calls=['cone_volume','hemi_volume']))

