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
    def test_rdf(self) :
        nf, delx = 0, (maxx-minx) / nbins 
        histo = np.zeros([5,nbins])
        bsize = int( np.floor( len( Trajectory('trajectory.traj') ) / 5 ) )
        for atoms in Trajectory('trajectory.traj') :
            bnum = int( np.floor( nf / bsize ) )
            nf = nf + 1
            distances = atoms.get_all_distances( mic=True )
            vecs = atoms.get_all_distances( mic=True, vector=True )
            for i in range(distances.shape[0]) : 
                fcc_numer, fcc_denom = 0, 0
                for j in range(distances.shape[1]) : 
                    if i==j or distances[i,j]>1.5 : continue
                    fcc_denom += 1
                    x, y, z, r = vecs[i,j,0], vecs[i,j,1], vecs[i,j,2], distances[i,j]
                    fcc_numer += ( ( (x*y)**4 + (x*z)**4 + (y*z)**4 ) / (r**8) - ( 27*(x*y*z)**4 ) / r**12 )
    
            final = 80080/(2717+16*27)*(fcc_numer/fcc_denom) + 16*(27-143)/(2717+16*27)
            xbin = int( np.floor( (final + 0.5) / delx ) )
            if xbin<0 : raise ValueError('xbin should not be negative')
            histo[bnum,xbin] = histo[bnum,xbin] + 1
 
  	histo = histo / bsize           
        average, average2 = np.zeros(nbins), np.zeros(nbins)
        for i in range(5) : 
            average = average + histo[i,:]
            average2 = average2 + histo[i,:]*histo[i,:]
        
        gat_average = average / 5
        gat_error = np.sqrt( (1/4)*( average2 / 5 - gat_average*gat_average ) )*scipy.stats.norm.ppf(0.95)

        gat_fes, gat_fes_error = -2.0*np.log( gat_average ), gat_error
        for i in range(len(gat_average)) :
            if gat_average[i]!=0 : gat_fes_error[i] = 2*gat_error[i] / gat_average[i]

        assert vc.check_vars("fes",gat_fes)
        assert vc.check_vars("error",gat_fes_error)
