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

nf, N, V = 0, 0, 0
delx, histo = maxd / nbins, np.zeros(nbins) 
for atoms in Trajectory('trajectory.traj') :
    nf, N, V = nf + 1, len(atoms), atoms.get_volume()
    distances = atoms.get_all_distances( mic=True )
    for i in range(1,distances.shape[0]) : 
        for j in range(0,i) :
            if  distances[i,j]>maxd : continue 
            xbin = int( np.floor( distances[i,j] / delx ) )
            histo[xbin] = histo[xbin] + 2

xbins = np.zeros(nbins)
for i in range(nbins) :
    if i==0 : 
        xbins[i] = 0.5*delx
        vol = (4/3)*np.pi*delx**3*(N/V)
        histo[i] = histo[i] / ( vol*nf*N )
    else :  
        xbins[i] = (i+0.5)*delx
        vol = (4/3)*np.pi*((delx*(i))**3 - (delx*(i-1))**3)*(N/V)
        histo[i] = histo[i] / ( vol*nf*N )

line1 = line( xbins, histo )
axislabels = ['r / sigma', 'g(r)' ]

class UnitTests(unittest.TestCase) :
    def test_rdf(self) :
        assert(check_plot([line1],explabels=axislabels,explegend=False,output=True))
