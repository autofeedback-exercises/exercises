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
        inputs, variables = [], []
        for i in range(1,9) :
            p = i*0.1
            inputs.append((i*0.1,))
            myvar = randomvar( p, variance=p*(1-p), vmin=0, vmax=1, isinteger=True )
            variables.append( myvar )
        assert( check_func('bernoulli',inputs, variables ) )

    def test_trials(self) : 
        inputs, variables = [], []
        for n in range(1,10) :
            nt = 10*n
            for i in range(1,9) :
                p = i*0.1
                inputs.append((nt,i*0.1,))
                myvar1 = randomvar( [nt*p,nt*(1-p)], variance=[nt*p*(1-p),nt*p*(1-p)], vmin=[0,0], vmax=[nt,nt], isinteger=[True,True] )
                variables.append(myvar1)
        assert( check_func("repeated_trials", inputs, variables ) )
