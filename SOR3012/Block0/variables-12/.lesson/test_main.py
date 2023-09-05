try:
    import AutoFeedback.plotchecks as pc
    from AutoFeedback.plotclass import line
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    import AutoFeedback.plotchecks as pc
    from AutoFeedback.plotclass import line

import unittest
from main import *

xvals, fib= np.linspace(1,100,100), np.ones(100)
for i in range(2,100) : fib[i] = fib[i-2] + fib[i-1]
line1 = line(xvals,fib)

axislabels=["Index", "Fibonacci series"]

class UnitTests(unittest.TestCase) :
    def test_fib(self) :
       assert( pc.check_plot([line1],explabels=axislabels,explegend=False,output=True) )    
