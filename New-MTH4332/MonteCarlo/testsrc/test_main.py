try:
    from AutoFeedback.funcchecks import check_func
except:
    import subprocess
    import sys
    
    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.funcchecks import check_func
                
import numpy as np
from AutoFeedback.randomclass import randomvar
import unittest     

class UnitTests(unittest.TestCase) :
    def test_function(self) :
        inputs, outputs = [], []
        for i in range(100) :
           x = np.random.uniform(0,1)
           y = np.random.uniform(0,1) 
           inputs.append((x,y,))
           outputs.append( ((x*x+y*y)<1) )
        assert( check_func("incircle", inputs, outputs ) )

    def test_estimate1(self) : 
       inputs, outputs = [], []
       for j in range(1,5) :
           p = np.pi/4 
           myvar = randomvar( p, variance=p*(1-p)/np.sqrt(j*100), vmin=0, vmax=1, isinteger=False )
           inputs.append((j*100,))
           outputs.append( myvar )
       assert( check_func('circle_estimate',inputs, outputs ) )

    def test_estimate2(self) :
       inputs, outputs = [], []
       for j in range(1,5) :
           p = np.pi/4 
           myvar = randomvar( p, variance=p*(1-p)/np.sqrt(j*100), vmin=0, vmax=1, isinteger=False )
           inputs.append((j*100,))
           outputs.append( myvar )
       assert( check_func('circle_estimate',inputs, outputs ) )

    def test_range(self) :
       inputs, var  = [], []
       for i in range(10,12) :
           for j in range(20,21) :
               inputs.append((i,j,))
               p = np.pi/4
               myvar1 = randomvar( p, variance=p*(1-p)/i, vmin=0, vmax=1, isinteger=False, dist="conf_lim", dof=j-1, limit=0.90 )
               var.append(myvar1)
       assert( check_func("myerrors", inputs, var ) ) 

    def test_errors(self):
       inputs, var  = [], []
       for i in range(15,25) :
           inputs.append((i,))
           p = np.pi/4
           myvar1 = randomvar( p, variance=p*(1-p)/i, vmin=0, vmax=1, isinteger=False, dist="conf_lim", dof=i-1, limit=0.90 ) 
           var.append(myvar1)
       assert( check_func("circle_estimate", inputs, var ) )
           
