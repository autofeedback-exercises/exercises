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
xvals = np.zeros(len(p_energy))
yvals1 = np.zeros(len(p_energy))
yvals2 = np.zeros(len(p_energy))
yvals3 = np.zeros(len(p_energy))
for s in range(nsteps) : 
    v = v + 0.5*timestep*f
    p = p + timestep*v
    f = -p    
    v = v + 0.5*timestep*f
              
    if s%stride==0 : 
       xvals[int(s/stride)] = s
       yvals1[int(s/stride)] = p*p/2
       yvals2[int(s/stride)] = v*v/2 
       yvals3[int(s/stride)] = yvals1[int(s/stride)] + yvals2[int(s/stride)]
              
line1 = line( xvals, yvals1, label='potential' )
line2 = line( xvals, yvals2, label='kinetic' )
line3 = line( xvals, yvals3, label='total' )
axislabels=["time", "energy"]

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

    def test_trajectory(self) :
       assert( pc.check_plot([line1,line2,line3],explabels=axislabels,explegend=False,output=True) )      
