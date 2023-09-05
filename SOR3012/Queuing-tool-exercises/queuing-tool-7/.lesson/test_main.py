try:
    import AutoFeedback.varchecks as vc
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    import AutoFeedback.varchecks as vc

import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_graph(self) :
        gadja_list = {0: [1], 1: [2,3]}
        gedge = {0: {1: 1}, 1: {3: 2}, 1: {2: 3}}
        g = qt.adjacency2graph(adjacency=gadja_list, edge_type=gedge)
        gqn = qt.QueueNetwork( g=g, q_classes=q_classes, q_args=q_args )
        gedge = {0: {1: 1}, 1: {2: 2}, 1: {3: 3}}
        g = qt.adjacency2graph(adjacency=gadja_list, edge_type=gedge)
        gqn2 = qt.QueueNetwork( g=g, q_classes=q_classes, q_args=q_args )
        assert( vc.check_vars("qn.g",gqn.g ) or vc.check_vars("qn.g",gqn2.g ) )
