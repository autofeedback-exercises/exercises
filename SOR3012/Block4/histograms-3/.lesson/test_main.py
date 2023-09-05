try:
    from AutoFeedback.funcchecks import check_func 
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.funcchecks import check_func

from AutoFeedback.varchecks import check_vars
from AutoFeedback.randomclass import randomvar
import unittest
from main import *

myvars = np.array([0,1,2,3,4])
exp = np.dot( probs, myvars )
var = np.dot( probs, myvars*myvars ) - exp*exp

class UnitTests(unittest.TestCase) :
    def test_probb_vector(self) : 
       check_vars("probs",[0.5,0.1,0.2,0.05,0.15])

    def test_variable(self) : 
       inputs, variables = [], []
       for i in range(10): 
           inputs.append((probs,))
           myvar = randomvar( exp, variance=var, vmin=0, vmax=4, isinteger=True, nsamples=100 )
           variables.append( myvar )

       assert( check_func("myvariable", inputs, variables ) )
