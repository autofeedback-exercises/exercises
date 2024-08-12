try:
    from AutoFeedback.plotchecks import check_plot
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.plotchecks import check_plot

from AutoFeedback.plotclass import line
import unittest
from main import *

gatftraj = Trajectory('nve-short.traj')
gat_acf, gat_norm = np.zeros(ncorr), np.zeros(ncorr)
    
k = 0
for atoms in gatftraj :
    vel = atoms.get_velocities().flatten()
    maxn = min( len(gatftraj), k + ncorr ) - k
    for i in range(maxn) :
        veln = ftraj[k + i].get_velocities().flatten()
        gat_acf[i] = gat_acf[i] + np.dot( veln.T, vel ) / (3*len( atoms ))
        gat_norm[i] = gat_norm[i] + 1
    k = k + 1

gat_acf = gat_acf / gat_norm 

gattimes = 0.005*np.linspace(0, ncorr-1, ncorr)
line1 = line( gattimes, gat_acf )
axislabels = ['time / arbitrary units', 'velocity autoccoreation function' ]

class UnitTests(unittest.TestCase) :
    def test_heat_capcity(self) :
        assert(check_plot([line1],explabels=axislabels,explegend=False,output=True))
