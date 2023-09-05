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
    def test_gambler(self) : 
        inputs, variables = [], []
        for s in range(1,4) : 
            for n in range(6,9) :
                for i in range(1,5) :
                    p = i*0.2
                    rat = (1-p)/p
                    prob = ( rat**s - rat**n ) / ( 1 - rat**n )
                    inputs.append((s,n,p,))
                    myvar = randomvar( prob, variance=prob*(1-prob), vmin=0, vmax=1, isinteger=True )
                    variables.append( myvar )
        assert( check_func('gambler',inputs, variables ) )
