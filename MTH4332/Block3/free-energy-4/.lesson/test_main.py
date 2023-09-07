try:           
    from AutoFeedback.funcchecks import check_func
except:
    import subprocess
    import sys
            
    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.funcchecks import check_func
                
from AutoFeedback.plotclass import line
from AutoFeedback.plotchecks import check_plot
import numpy as np   
import unittest      
from main import *


data = np.loadtxt("magnetisations")
ddd = (maxx - minx) / nbins
xv = np.array([10, 20, 25, 100, 200, 250, 500])
yv = np.zeros(len(xv))
for k,bls in enumerate(xv) : 
    nb = int( len(data) / bls )
    fv, fv2 = np.zeros(nbins), np.zeros( nbins )
    # This loop calculates your nblocks estimates of the histogram
    for i in range(nb) :
        # Your code for calculating each of the nblocks estimate of the histogram goes here
        histo = np.zeros(nbins)
        for j in range(i*bls,(i+1)*bls) :
            mav = data[j] / (20*20)
            xbin = int( np.floor( (mav-minx) / ddd ) )
            histo[xbin] = histo[xbin] + 1
        histo = histo / bls 
        fv = fv + histo
        fv2 = fv2 + histo*histo
        
    fv = fv / nb
    fv2 = np.sqrt( (1/(nb-1))*( fv2/nb - fv*fv ) )*scipy.stats.norm.ppf(0.95)

    n = 0
    for i in range(len(fv)) : 
        if fv[i]>0 : 
           yv[k] += 5*fv2[i] / fv[i] 
           n = n + 1
    yv[k] = yv[k] / n


line1 = line( xv, yv )
axislabels = [ "Length of block", "Average error on free energy" ]

class UnitTests(unittest.TestCase) :
    def test_graph(self) :
        assert( check_plot([line1],explabels=axislabels,explegend=False,output=True) ) 
