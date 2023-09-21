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
        nf, N, V  = 0, 0, 0
        delx, histo = maxd / nbins, np.zeros([5,nbins])
        bsize = int( np.floor( len( Trajectory('trajectory.traj') ) / 5 ) )
        for atoms in Trajectory('trajectory.traj') :
            bnum = int( np.floor( nf / bsize ) )
            nf, N, V = nf + 1, len(atoms), atoms.get_volume()
            distances = atoms.get_all_distances( mic=True )
            for i in range(1,distances.shape[0]) : 
                for j in range(0,i) :
                    if  distances[i,j]>maxd : continue 
                    xbin = int( np.floor( distances[i,j] / delx ) )
                    histo[bnum,xbin] = histo[bnum,xbin] + 2
                
        xbins = np.zeros(nbins)
        for i in range(nbins) : 
            if i==0 : 
                xbins[i] = 0.5*delx
                vol = (4/3)*np.pi*delx**3*(N/V)
                histo[:,i] = histo[:,i] / ( vol*bsize*N )
            else :  
                xbins[i] = (i+0.5)*delx
                vol = (4/3)*np.pi*((delx*(i))**3 - (delx*(i-1))**3)*(N/V)
                histo[:,i] = histo[:,i] / ( vol*bsize*N )
            
        average, average2 = np.zeros(nbins), np.zeros(nbins)
        for i in range(5) : 
            average = average + histo[i,:]
            average2 = average2 + histo[i,:]*histo[i,:]
        
        gat_average = average / 5
        gat_error = np.sqrt( (1/4)*( average2 / 5 - gat_average*gat_average ) )*scipy.stats.norm.ppf(0.95)

        assert vc.check_vars("average",gat_average)
        assert vc.check_vars("error",gat_error)
