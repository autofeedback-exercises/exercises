try:
    from AutoFeedback.funcchecks import check_func 
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.funcchecks import check_func

import AutoFeedback.plotchecks as pc
from AutoFeedback.randomclass import randomvar
from AutoFeedback.plotclass import line
import unittest
from main import *

xv = np.linspace( 0, (nsteps-stride)*timestep, len(vels) )
var = randomvar( 0, variance=temperature )
line1 = line( xv, var )
axislabels=["time", "velocity"]

class UnitTests(unittest.TestCase) :
   def test_potential(self) :
       inputs, outputs, xvals = [], [], np.linspace(-4,4,400)
       for x in xvals :
           inputs.append((x,))
           outputs.append((x*x/2,-x,))
       assert( check_func('potential', inputs, outputs ) )

   def test_kinetic(self) :
       inputs, outputs = [], []
       for i in range(100) :
           vel = np.random.normal()
           eng =  0.5*vel*vel
           inputs.append((vel,))
           outputs.append(eng)
       assert( check_func('kinetic', inputs, outputs ) )

   def test_trajectory(self):
       assert( pc.check_plot([line1],explabels=axislabels,explegend=False,output=True) )
   
