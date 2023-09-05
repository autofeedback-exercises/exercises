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
   def test_bernoulli(self) :
       inputs, var  = [], []
       for i in range(1,9) :
           inputs.append((i*0.1,))
           var.append(i*0.1)
       assert( check_func("bernoulli", inputs, var ) )
  
   def test_binomial(self) :
       inputs, var  = [], []
       for n in range(2,7):
           for i in range(1,9) :
               inputs.append((n, i*0.1,))
               var.append(n*i*0.1)
       assert( check_func("binomial", inputs, var ) )

   def test_geometric(self) :
       inputs, var  = [], []
       for i in range(1,9) :
           inputs.append((i*0.1,))
           var.append(1/(i*0.1))
       assert( check_func("geometric", inputs, var ) )

   def test_negative_binomial(self) :
       inputs, var  = [], []
       for n in range(2,7):
           for i in range(1,9) :
               inputs.append((n,i*0.1,))
               var.append(n/(i*0.1))
       assert( check_func("negative_binomial", inputs, var ) )

   def test_uniform_continuous(self) :
       inputs, var  = [], []
       for j in range(1,4) :
           for i in range(4,9) :
               inputs.append((j,i,))
               var.append( (i+j)/2 )
       assert( check_func("uniform_continuous", inputs, var ) )

   def test_uniform_discrete(self) :
       inputs, var  = [], []
       for j in range(1,4) :
           for i in range(4,9) :
               inputs.append((j,i,))
               var.append( (i+j)/2 )
       assert( check_func("uniform_discrete", inputs, var ) )

   def test_exponential(self) :
       inputs, var  = [], []
       for i in range(1,9) :
           inputs.append((i,))
           var.append(1/i)
       assert( check_func("exponential", inputs, var ) )

   def test_normal(self) :
       inputs, var  = [], []
       for j in range(1,4) :
           for i in range(1,4) :
               inputs.append((j,i,))
               var.append( j )
       assert( check_func("normal", inputs, var ) )

