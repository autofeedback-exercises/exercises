try:
    import AutoFeedback.varchecks as vc
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    import AutoFeedback.varchecks as vc 

import unittest
from main import *

def mylj(r) : 
    r2 = r*r 
    r6 = r2*r2*r2 
    r12 = r6*r6
    eng = 4*( ( 1/r12 ) - (1/r6) )
    force = -24*( 2/r12 - 1/r6 ) / r2
    return eng, force

class UnitTests(unittest.TestCase) :
    def test_energies(self) :
        try: 
          ftraj = Trajectory("mytraj.traj")
        except:
          assert vc.check_vars("energies", 0) 

        myatoms = FaceCenteredCubic( directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]], symbol="Ar", size=(3, 3, 3), latticeconstant=2**(2/3), pbc=(1,1,1) )
        myeng = [] 
        myatoms.calc = pairwise_calculator( rc=4, pairwise_e=mylj )
        for a in ftraj : 
            myatoms.set_positions( a.get_positions() )
            myeng.append( myatoms.get_potential_energy() )

        ftraj.close()
        assert vc.check_vars( energies, myeng, printname="energies" )
            
