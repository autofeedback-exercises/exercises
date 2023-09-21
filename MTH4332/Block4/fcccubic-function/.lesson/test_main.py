try:
    from AutoFeedback.funcchecks import check_func 
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.funcchecks import check_func

import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_fcc(self) : 
        inputs, outputs = [], []
        for atoms in  Trajectory('.lesson/trajectory.traj') :
            inputs.append((atoms,))
            pppp = np.zeros(len(atoms))
            distances = atoms.get_all_distances( mic=True )
            vecs = atoms.get_all_distances( mic=True, vector=True )
            for i in range(distances.shape[0]) : 
                fcc_numer, fcc_denom = 0, 0
                for j in range(distances.shape[1]) : 
                    if i==j or distances[i,j]>1.5 : continue
                    fcc_denom += 1
                    x, y, z, r = vecs[i,j,0], vecs[i,j,1], vecs[i,j,2], distances[i,j]
                    fcc_numer += ( ( (x*y)**4 + (x*z)**4 + (y*z)**4 ) / (r**8) - ( 27*(x*y*z)**4 ) / r**12 )
    
                pppp[i] = 80080/(2717+16*27)*(fcc_numer/fcc_denom) + 16*(27-143)/(2717+16*27) 
            outputs.append( pppp ) 

        assert( check_func("fcc_cubic", inputs, outputs ) )
