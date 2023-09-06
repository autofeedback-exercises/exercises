try:
    import AutoFeedback.varchecks as vc
except: 
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    import AutoFeedback.varchecks as vc

import unittest
#from main import *

class UnitTests( unittest.TestCase ): 
    def test_nservers(self):
        try:
            from main import qn
            edge2queue = qn.edge2queue
        except ImportError:
            assert vc.check_vars("qn", 0)
        except AttributeError:
            assert vc.check_vars("qn.edge2queue", 0)
        try:
            num_servers = edge2queue[0].num_servers
        except AttributeError:
            assert vc.check_vars("qn.edge2queue[0].num_servers", 0)

        assert vc.check_vars(num_servers, 3,
                             printname="qn.edge2queue[0].num_servers")

