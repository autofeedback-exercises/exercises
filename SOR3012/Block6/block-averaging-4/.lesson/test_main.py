try:
    import AutoFeedback.varchecks as vc
except: 
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    import AutoFeedback.varchecks as vc

import unittest
from main import *

myeng = np.loadtxt("energies")[:,1]

class UnitTests(unittest.TestCase) :
    def test_average_correct(self) :
        myblocks, myaverage = 10*[0], 0
        for i in range(10) :
            myblocks[i] = sum( myeng[i*100:(i+1)*100] ) / 100 
            myaverage = myaverage + myblocks[i] 
        assert( vc.check_vars("average", myaverage / 10 ) )
        
    def test_error_correct(self) :
        myblocks, myaverage, mysq = 10*[0], 0, 0
        for i in range(10) :
            myblocks[i] = sum( myeng[i*100:(i+1)*100] ) / 100 
            myaverage = myaverage + myblocks[i] 
            mysq = mysq + myblocks[i]*myblocks[i]
  
        mysq, myaverage = mysq / 10, myaverage / 10
        myvar = ( 10 / 9 )*( mysq - myaverage*myaverage )
        assert( vc.check_vars("error", np.sqrt( myvar / 10 ) ) )
