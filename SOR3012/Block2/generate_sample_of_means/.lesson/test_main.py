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
       inputs, var = [], []
       for i in range(2,10) : 
           inputs.append((i,))
           myvar1 = randomvar( 0.5, variance=1/12/i, vmin=0, vmax=1, isinteger=False )
           var.append(myvar1)
       assert( check_func("sample_mean", inputs, var) ) 

   def test_sample(self) : 
       inputs, var = [], [] 
       for i in range(15,20) :
           for j in range(5,10) :
               inputs.append((i,j))
               myvar1 = randomvar( 0.5, variance=1/12/j, vmin=0, vmax=1, isinteger=False )
               var.append(myvar1)
       assert( check_func("sample", inputs, var, calls=["sample_mean"]) ) 
