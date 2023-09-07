try:
    import AutoFeedback.varchecks as vc
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    import AutoFeedback.varchecks as vc

import unittest
import queueing_tool as qt

class UnitTests(unittest.TestCase) :
    def test_graph(self) :
        try:
            from main import q_classes
        except ImportError:
            assert vc.check_vars("q_classes", 0)
        try:
            from main import q_args
        except ImportError:
            assert vc.check_vars("q_args", 0)
        try:
            from main import qn
            student_g = qn.g
        except ImportError:
            assert vc.check_vars("g", 0)
        except AttributeError:
            assert vc.check_vars("g", 0)

        gadja_list = {0: [1], 1: [2,3]}
#        gedge = {0: {1: 1}, 1: {2: 2, 3: 2}}
        gedge = {0: {1: 1}, 1: {k: 2 for k in range(2, 4)}}
        g = qt.adjacency2graph(adjacency=gadja_list, edge_type=gedge)
        gqn = qt.QueueNetwork( g=g, q_classes=q_classes, q_args=q_args )

        assert vc.check_vars(student_g, gqn.g, printname="g")
