import matplotlib.pyplot as plt
import scipy.stats
import numpy as np

# Read in the list of magnetisation values
mags = np.loadtxt("magnetisations")

# This is the number of bins
nbins = 50
# This is the minimum and maximum for the grid
minx, maxx = -1.1, 1.1
# This is the list of block sizes you should investigate
blocksizes = np.array([10, 20, 25, 100, 200, 250, 500])


# Your code to draw the graph described in the instructions goes here.
# I would recommend writing a function to calculate the histogram with 
# different block sizes

def get_histo_error( data, nbins, minx, maxx, blocksize ) :
    delx = ( maxx - minx ) / nbins
    nblocks = int( len(data) / blocksize )
    final_v, final_v2 = np.zeros(nbins), np.zeros( nbins )
    # This loop calculates your nblocks estimates of the histogram
    for i in range(nblocks) :
        # Your code for calculating each of the nblocks estimate of the histogram goes here
        histo = np.zeros(nbins)
        for j in range(i*blocksize,(i+1)*blocksize) :
            mav = data[j] / (20*20)
            xbin = int( np.floor( (mav-minx) / delx ) )
            histo[xbin] = histo[xbin] + 1
        histo = histo / blocksize
        final_v = final_v + histo
        final_v2 = final_v2 + histo*histo
    
    final_v = final_v / nblocks
    final_v2 = np.sqrt( (1/(nblocks-1))*( final_v2/nblocks - final_v*final_v ) )*scipy.stats.norm.ppf(0.95)
    
    errtot, n = 0, 0
    for i in range(len(final_v)) : 
        if final_v[i]>0 : 
           errtot += 5*final_v2[i] / final_v[i] 
           n = n + 1 
    return errtot / n

error = np.zeros(len(blocksizes))
for n,b in enumerate(blocksizes) : 
    error[n] = get_histo_error( mags, nbins, minx, maxx, b )

plt.plot( blocksizes, error, 'ko' )
plt.xlabel("Length of block")
plt.ylabel("Average error on free energy")
plt.savefig("error_graph.png")
