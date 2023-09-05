try:
    import AutoFeedback.varchecks as vc
except:
    import subprocess
    import sys
       
    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    import AutoFeedback.varchecks as vc
    
import unittest
import inspect
from main import *

class UnitTests(unittest.TestCase) :
    def test_arrayValues(self) :
       x=np.linspace(0,70,11)
       assert( vc.check_vars( "timesTable", x ) ) 
       
    def test_loop(self) :
       assert( vc.check_vars("i",10) ) 
