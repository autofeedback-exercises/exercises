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
   def test_mean(self) :
       inputs, var  = [], []
       for i in range(2,10) :
           inputs.append((i,))
           rv = randomvar( 0.5, variance=1/12/i, vmin=0, vmax=1, isinteger=False )
           var.append(rv)
       assert( check_func("sample_mean", inputs, var ) )

   def test_limit(self) : 
       inputs, var  = [], []
       for i in range(10,12) :
           for j in range(20,21) :
               inputs.append((i,j,))
               myvar1 = randomvar( 0.5, variance=1/12/i, dist="conf_lim", dof=j-1, limit=0.90 )
               var.append(myvar1)
       assert( check_func("limit", inputs, var ) )
