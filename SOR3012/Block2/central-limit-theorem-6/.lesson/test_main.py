try:
    from AutoFeedback.funcchecks import check_func 
except:
    import subprocess
    import sys
            
    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.funcchecks import check_func 
           
from AutoFeedback.randomclass import randomvar
import unittest
from main import *

class UnitTests(unittest.TestCase) :
   def test_function(self) : 
       inputs, var  = [], []
       for i in range(2,10) :
           inputs.append((i,))
           myvar1 = randomvar( 0.5, variance=1/12/i, dist="conf_lim", dof=i-1, limit=0.90 )
           var.append(myvar1)
       assert( check_func("mean_with_errors", inputs, var ) )
     
