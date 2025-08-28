try:
    from AutoFeedback.plotchecks import check_plot
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.plotchecks import check_plot

from AutoFeedback.plotclass import line
import unittest

class UnitTests(unittest.TestCase) :
    def test_heat_capcity2(self) :
        gatftraj = Trajectory('https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/New-MTH4332/LennardJonesII/nve-short.traj')
        gatnatoms = len( gatftraj[0].get_velocities() )
        gatvtraj = np.zeros([ 3*gatnatoms, len(gatftraj) ])
        
        k = 0
        for atoms in gatftraj :
            gatvtraj[:,k] = atoms.get_velocities().flatten()
            k = k + 1
        
        gatfftraj = np.fft.rfft(gatvtraj,axis=1)
        gatfdos = np.mean(gatfftraj*np.conjugate(gatfftraj),axis=0) / len(gatftraj)
        
        gatfreq = np.fft.rfftfreq( len(gatftraj), d=0.005 )
        line1 = line( gatfreq, gatfdos )
        axislabels = ['frequency / arbitrary units', 'vibrational density of states' ]
        assert(check_plot([line1],explabels=axislabels,explegend=False,output=True))
