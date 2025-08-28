try:
    from AutoFeedback.funcchecks import check_func 
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.funcchecks import check_func

from AutoFeedback.randomclass import randomvar
import unittest

class UnitTests(unittest.TestCase) :
    def test_estimate1(self) : 
       inputs, outputs = [], []
       for j in range(1,5) :
           p = np.pi/4 
           myvar = randomvar( p, variance=p*(1-p)/np.sqrt(j*100), vmin=0, vmax=1, isinteger=False )
           inputs.append((j*100,))
           outputs.append( myvar )
       assert( check_func('circle_estimate',inputs, outputs ) )
