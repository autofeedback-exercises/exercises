try:
    from AutoFeedback.funcchecks import check_func
except:
    import subprocess
    import sys
       
    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.funcchecks import check_func
           
from AutoFeedback.randomclass import randomvar
import unittest

class UnitTests(unittest.TestCase) :
    def test_errors(self):
       inputs, var  = [], []
       for i in range(15,25) :
           inputs.append((i,))
           p = np.pi/4
           myvar1 = randomvar( p, variance=p*(1-p)/i, vmin=0, vmax=1, isinteger=False, dist="conf_lim", dof=i-1, limit=0.90 ) 
           var.append(myvar1)
       assert( check_func("area", inputs, var ) )
           
