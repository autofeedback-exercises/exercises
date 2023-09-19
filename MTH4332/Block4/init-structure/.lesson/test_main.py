try:
    import AutoFeedback.varchecks as vc
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    import AutoFeedback.varchecks as vc

import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_ase(self) :
        myatoms = FaceCenteredCubic( directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]], symbol="Ar", size=(3, 3, 3), latticeconstant=2**(2/3), pbc=(1,1,1) )
        try:
            from main import atoms
            student_pos = atoms.get_positions()
        except ImportError:
            assert vc.check_vars("atoms",0)
        except AttributeError:
            assert vc.check_vars("atoms.positions",0) 

        assert vc.check_vars( student_pos, myatoms.get_positions(), printname="atoms.positions" )
        try: 
            student_mass = atoms.get_masses()
        except AttributeError:
            assert vc.check_vars("atoms.masses",0)

        assert vc.check_vars( student_mass, np.ones(len(atoms)), printname="atoms.masses" )
