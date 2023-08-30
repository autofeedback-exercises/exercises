try:
    from AutoFeedback.funcchecks import check_func 
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.funcchecks import check_func

import AutoFeedback.plotchecks as pc
from AutoFeedback.plotclass import line
import unittest
from main import *

p, v, f = init_pos, init_vel, -init_pos
yvals = np.zeros(len(trajectory))
for s in range(nsteps) : 
    v = v + 0.5*timestep*f
    p = p + timestep*v
    f = -p
    v = v + 0.5*timestep*f

    if s%stride==0 : yvals[int(s/stride)] = p

xv = np.linspace( 0, (nsteps-stride)*timestep, len(yvals) )
line1 = line( xv, yvals )
axislabels=["time", "position"]

class UnitTests(unittest.TestCase) :
    def test_potential(self) :
        inputs, outputs, xvals = [], [], np.linspace(-4,4,400)
        for x in xvals :  
            inputs.append((x,))
            outputs.append((x*x/2,-x,))
        assert( check_func('potential', inputs, outputs ) )  
                
    def test_trajectory(self) :
        assert( pc.check_plot([line1],explabels=axislabels,explegend=False,output=True) )
