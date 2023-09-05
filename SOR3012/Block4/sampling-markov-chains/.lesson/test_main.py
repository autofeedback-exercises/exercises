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
    def test_variable(self) : 
       inputs, variables = [], []
       
       myvars, mat1 = np.array([0,1,2]), np.array([[0.3,0.5,0.2],[0.3,0.4,0.3],[0.2,0.5,0.3]])
       for j in range(3) : 
           exp = np.dot( mat1[j,:], myvars )
           var = var = np.dot( mat1[j,:], myvars*myvars ) - exp*exp
           for i in range(10): 
               inputs.append((mat1,j,))
               myvar = randomvar( exp, variance=var, vmin=0, vmax=2, isinteger=True, nsamples=100 )
               variables.append( myvar )
       myvars, mat2 = np.array([0,1,2,3,4]), np.array([[1,0,0,0,0],[1/3,1/3,1/3,0,0],[0,0.5,0,0.5,0],[0,0.5,0,0,0.5],[0,0,0,0,1]])
       for j in range(5) : 
           exp = np.dot( mat2[j,:], myvars )
           var = var = np.dot( mat2[j,:], myvars*myvars ) - exp*exp
           for i in range(10): 
               inputs.append((mat2,j,))
               myvar = randomvar( exp, variance=var, vmin=0, vmax=4, isinteger=True, nsamples=100 )
               variables.append( myvar ) 

       assert( check_func("markov_move", inputs, variables ) )
