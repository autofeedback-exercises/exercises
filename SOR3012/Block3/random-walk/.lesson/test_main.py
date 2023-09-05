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

class helper : 
     def __init__( self, n, s ) :
         self.n, self.s = n, s

     def check_random_walk( self, val ) :
         return (self.n + val - self.s) / 2

class UnitTests(unittest.TestCase) :
    def test_random_walk(self) : 
        inputs, variables, helpers = [], [], []
        for s in range(-1,2) : 
            for n in range(2,4) :
                for i in range(1,5) :
                    p = i*0.2
                    inputs.append((s,n,p,))
                    helpers.append( helper(n,s) )
                    myvar = randomvar( n*p, variance=n*p*(1-p), vmin=0, vmax=n, transform=helpers[len(helpers)-1].check_random_walk, isinteger=True )
                    variables.append( myvar )
        assert( check_func('random_walk',inputs, variables ) )
